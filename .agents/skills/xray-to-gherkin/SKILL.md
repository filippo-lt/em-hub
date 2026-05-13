---
name: xray-to-gherkin
description: "Convert an Xray manual-test JSON export into grouped Gherkin .feature files through interactive Q&A. Use when the user says things like: 'convert Xray tests to Gherkin', 'turn Xray export into feature files', 'xray to gherkin', or hands you an FAIOSMAU/XRAY/Xray JSON and asks for Gherkin."
user_invocable: true
---

# Xray → Gherkin

Interactive skill that turns an Xray manual-test JSON export into a set of grouped Gherkin `.feature` files, suitable for feeding to an AI agent that audits an implementation.

The actual conversion is done by `xray_to_gherkin.py` in this folder. The skill's job is to (a) inspect the input, (b) reach agreement with the user on grouping, output location, and tag heuristics, (c) build a config JSON, (d) invoke the script, (e) report results.

---

## State to track

Keep these in memory across the conversation:

- `input_path` — path to the Xray JSON
- `prefix_counts` — `{prefix: count}` from the input
- `prefix_routing` — `{"[Home]": "home", ...}` agreed with the user
- `feature_titles` — `{slug: "Human Title"}` (optional, defaults to title-cased slug)
- `output_dir` — absolute path where `.feature` files will be written
- `tag_keywords` — visual / firebase / external keyword lists (start from defaults below)

---

## Process

### Phase 1 — Locate and inspect the input

1. If the user supplied a path or `@file`, use it. Otherwise ask:
   > "Path to the Xray JSON export?"
2. Validate: load it with `jq`, confirm it's a list, count entries, extract prefix tag distribution.
3. Report back compactly:
   > "Loaded N tests. Distinct prefixes: M. Top 10 by count: …"

Run:
```bash
jq 'length' "$INPUT"
jq -r '.[].summary' "$INPUT" | grep -oE '^\[[^]]+\]' | sort | uniq -c | sort -rn
```

### Phase 2 — Propose grouping

1. Group prefixes into ~10–20 semantic feature files. Heuristics:
   - Merge case-variants (`[OnBoard]` + `[Onboard]`)
   - Merge near-duplicates (`[All Filters]` + `[All filters]`)
   - Merge thematically related prefixes (e.g. all per-category face-filter prefixes into one file)
   - Split files that would exceed ~30 scenarios into sub-themes
2. Present the proposed mapping as a markdown table: `file | merges these prefixes | count`.
3. Flag any judgment calls explicitly (e.g. "Settings has 45 if I keep Rate/Update/Contact Us merged — split?").
4. Wait for user confirmation. Apply any requested changes. Re-present until approved.

If a prefix is unfamiliar or ambiguous (single test, unclear meaning), **ask the user one question** rather than guessing.

### Phase 3 — Output location

Ask:
> "Where should the feature files be written? (absolute path, e.g. `~/Apps/<repo>/xray-suites/<project>/features/`)"

Confirm:
- The directory will be created if missing
- `skipped.md` will be written to the parent of `features/` (sibling, not inside)
- Existing files in the directory **will be overwritten** — call this out if the dir already contains `.feature` files

### Phase 4 — Tag keyword check (optional)

Default keyword lists:

- **visual**: `align`, `Figma`, `design`, `layout`, `position`, `appearance`, `aligned`
- **firebase**: `[Firebase]`, `Crashlytics`, `Remote Config`
- **external**: `Superwall`, `AppStore`, `Restore`, `Payment`, `NSFW`, `internet`, `Soft Update`, `Force Update`

Ask:
> "Defaults shown above for visual/firebase/external tag detection. Want to adjust any list before I run the conversion?"

If the user says "go" or "use defaults", proceed.

### Phase 5 — Build config and run

1. Write the config to a temp file next to the input (or `/tmp/xray-to-gherkin-config.json`). Schema:

```json
{
  "input_json": "/abs/path/to/xray.json",
  "output_dir": "/abs/path/to/features",
  "prefix_routing": { "[Home]": "home", "[Editor]": "editor", "...": "..." },
  "feature_titles": { "home": "Home", "editor": "Editor" },
  "visual_keywords": ["align", "Figma", "design", "layout", "position", "appearance"],
  "firebase_keywords": ["[Firebase]", "Crashlytics", "Remote Config"],
  "external_keywords": ["Superwall", "AppStore", "Restore", "Payment", "NSFW", "internet", "Soft Update", "Force Update"],
  "default_bucket": "misc"
}
```

2. Invoke the script from this skill's folder:

```bash
python3 /Users/ftosetto/Projects/em-hub/.agents/skills/xray-to-gherkin/xray_to_gherkin.py --config <config-path>
```

3. If the script exits non-zero:
   - Exit code 3 (unmapped or missing prefixes) → show the list, ask the user how to route them. Either add them to `prefix_routing` or set `default_bucket` to catch-all into a `misc` file. Update config, re-run.
   - Other errors → surface verbatim and stop

> `default_bucket` is optional. Omit it to make the script fail loud on any unmapped/prefix-less test (recommended for the first run, so you see the gaps). Set it to a slug like `"misc"` once the user has decided how to handle stragglers.

### Phase 6 — Report and verify

1. Show the script's stdout (input count, converted, skipped, file list) verbatim.
2. Pick one file at random, read the first scenario, show it to the user as a spot-check:
   > "Sample scenario from `home.feature` — does the shape look right?"
3. If `skipped.md` was written, show its contents and ask whether the user wants to address any of those tests in Xray.

---

## Output conventions (reference)

The script applies these conventions; they are documented here so the skill can answer questions about them without re-reading the script.

- **Scenario name** = Xray summary with leading `[Prefix]` stripped
- **Mandatory tags**: `@FAIOSMAU-XXX` (or `@<KEY>` from Xray), plus `@regression` if labeled
- **Heuristic tags**: `@visual`, `@firebase`, `@external` based on keyword lists
- **Step mapping**: first `action` → `When`, subsequent → `And`; first non-empty `result` → `Then`, subsequent → `And`; `data` field → comment above the step
- **Default precondition**: every scenario opens with `Given the app is launched`
- **Parameterized tests** (`${...}` placeholders): emitted as `Scenario Outline` with empty `Examples:` table and a `# TODO:` comment
- **Description context**: URLs preserved as `# ref:` comments, plain text as `# context:` comment (truncated to 200 chars)
- **Un-convertible tests** (zero steps, or all `action` fields blank): excluded and logged to `skipped.md`

---

## What this skill does NOT do

- Does not generate a `verification-agent-prompt.md` — that's a separate experiment artifact
- Does not commit the output to git — the user decides when and where
- Does not pull from Xray API — input must already be a JSON file on disk
- Does not modify the iOS/source repo being audited
