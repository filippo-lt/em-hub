---
date: 2026-05-13
topic: Xray → Gherkin conversion for FAIOSMAU
status: Executed
---

# Xray → Gherkin conversion for FAIOSMAU

## Goal

Convert 203 Xray manual test cases (input: `FAIOSMAU_tests_2026-05-13.json`) into a
small set of grouped Gherkin `.feature` files. The end-state experiment: feed one
`.feature` file + the iOS source to an AI agent and get back a structured report
of where the implementation matches, diverges, or cannot be verified from code.

This conversion is implemented as a reusable em-hub skill — **`/xray-to-gherkin`**
— that any future Xray export can be fed into, not as a one-shot script for
FAIOSMAU specifically.

## Inputs

- `~/Projects/em-hub/FAIOSMAU_tests_2026-05-13.json` — 203 Xray test cases
  (manual, step-based; no existing Gherkin)
- iOS source repo at `~/Apps/FaceAI/faceai_ios` (consumed only by the downstream
  verification experiment, not by this conversion)

## Entry point

```
/xray-to-gherkin
```

Skill location: `.agents/skills/xray-to-gherkin/`
- `SKILL.md` — interactive Q&A flow (locate input → grouping → output dir → tag keywords → run → spot-check)
- `xray_to_gherkin.py` — config-driven converter (stdlib only, no third-party deps)

The skill conducts the Q&A, builds a config JSON, invokes the script, and
reports results. The script is reusable for any Xray export — routing,
output location, and tag keywords are all driven from the config.

## Output location (FAIOSMAU run)

```
~/Apps/FaceAI/faceai-docs/xray-suites/FAIOSMAU/
├── skipped.md                         # tests excluded from conversion + reason
├── source/
│   └── FAIOSMAU_tests_2026-05-13.json # snapshot of input for traceability
└── features/
    ├── onboarding.feature
    ├── home.feature
    ├── upload_photo.feature
    ├── editor.feature
    ├── face_filters_categories.feature
    ├── face_filters_behavior.feature
    ├── retouch.feature
    ├── save_export.feature
    ├── library.feature
    ├── payment.feature
    ├── paywall.feature
    ├── settings.feature
    ├── rate.feature
    ├── app_update.feature
    ├── contact_us.feature
    ├── errors.feature
    └── misc.feature
```

Rationale for top-level `xray-suites/` rather than `features/<category>/`: the
existing `features/` convention in `faceai-docs` is per-epic (each folder has an
`epic.md`), and these tests have no source epic. Keeping them separate avoids
diluting the epic convention.

## Feature grouping (FAIOSMAU run)

17 files. Semantic grouping of Xray summary prefixes, agreed with the user during
the `/xray-to-gherkin` Q&A:

| File | Merges these Xray prefixes |
|---|---|
| `onboarding.feature` | `[OnBoard]`, `[Onboard]`, `[App landing]`, `[iOS Permissions]` |
| `home.feature` | `[Home]` |
| `upload_photo.feature` | `[Upload photo]`, `[Upload Photo]`, `[Default gender]`, `[Camera]` |
| `editor.feature` | `[Editor]`, `[All Filters]`, `[All filters]`, `[Tools]` |
| `face_filters_categories.feature` | per-category "all filters apply without errors" tests for `[Hair Style]`, `[Hair Colors]`, `[Glasses]`, `[Smiles]`, `[Impression]`, `[Skin]`, `[Sizes]`, `[Age]`, `[Gender]`, `[Features]`, `[Beards]` |
| `face_filters_behavior.feature` | `[Face Filters]`, `[Makeup]`, `[Background]` |
| `retouch.feature` | `[Retouch]` |
| `save_export.feature` | `[Save/Export]` |
| `library.feature` | `[Library]`, `[Library Screen]` |
| `payment.feature` | `[Payment]`, `[Quota]`, `[PRObutton]` |
| `paywall.feature` | `[Paywall]`, `[Superwall]` |
| `settings.feature` | `[Settings]` |
| `rate.feature` | `[Rate]` |
| `app_update.feature` | `[Update]` |
| `contact_us.feature` | `[Contact Us]` |
| `errors.feature` | `[Error Handling]`, `[No internet connection]`, `[Crash]` |
| `misc.feature` | catch-all (`default_bucket`) for prefix-less or unmapped tests |

The router is the `prefix_routing` field of the config JSON the skill builds.
By default, unmapped prefixes cause the script to exit non-zero with the list
of offenders; setting `default_bucket` to a slug (e.g. `"misc"`) routes them
into a catch-all file instead.

## Per-scenario conventions

Each Xray test becomes exactly one Gherkin scenario. Conventions applied by
the script:

### Scenario name
The Xray `summary`, with the leading `[Prefix]` stripped (the containing file
already represents the feature).

### Tags (applied per scenario)
- `@<XRAY-KEY>` (e.g. `@FAIOSMAU-316`) — mandatory; bidirectional traceability.
- `@regression` — preserved from Xray `labels` when present.
- `@visual` — assertion is about layout / design / Figma alignment.
  Default keywords: `align`, `Figma`, `design`, `layout`, `position`, `appearance`.
- `@firebase` — depends on Firebase Remote Config or Crashlytics state.
  Default keywords: `[Firebase]`, `Crashlytics`, `Remote Config`.
- `@external` — depends on payment, App Store, network, NSFW classifier, or
  another runtime-only signal. Default keywords: `Superwall`, `AppStore`,
  `Restore`, `Payment`, `NSFW`, `internet`, `Soft Update`, `Force Update`.

Keyword lists are config-driven. Detection is intentionally over-inclusive —
better to mark a behavioral test `@visual` than to miss one.

### Step mapping
Xray steps have `action`, `data`, `result`. Gherkin shape:

- Every scenario opens with `Given the app is launched` as a safe default
- First `action` → `When <action>`, subsequent `action` fields → `And <action>`
- First non-empty `result` → `Then <result>`, subsequent → `And <result>`
- Non-empty `data` field → `# data: <value>` comment under the step

### Parameterized tests
Tests containing `${...}` placeholders are emitted as `Scenario Outline`:
- Step text rewritten with `<param>` in place of `${param}`
- An empty `Examples:` table with placeholder column headers
- A `# TODO: fill from Xray <KEY> — placeholders were not expanded in source` comment above the scenario

### Context preservation
- URLs from `description` (Figma, Drive, etc.) → `# ref: <url>` comments above the scenario
- Plain-text description content (non-trivial, not a duplicate of the summary) → `# context: <text>` comment, truncated to 200 chars

### Un-convertible tests
A test is excluded (and logged to `skipped.md`) when:
- The test has zero steps, OR
- All `action` fields are empty

`skipped.md` lists each excluded test as `- <KEY> — <summary> — reason: <reason>`.

## Conversion script

`.agents/skills/xray-to-gherkin/xray_to_gherkin.py`

Responsibilities:
1. Load the Xray JSON (path from config)
2. For each test:
   - Route by prefix to a feature file via `prefix_routing` (or `default_bucket` if set)
   - Determine tags via keyword heuristics
   - Detect placeholders → choose `Scenario` vs `Scenario Outline`
   - Build the Gherkin scenario block
   - If un-convertible: append to skip list instead
3. Group scenarios by feature file; write each with a `Feature:` header
   (title from config `feature_titles`, falling back to title-cased slug)
4. Write `skipped.md` to the parent of the output dir
5. Exit non-zero if converted + skipped ≠ input count

Idempotency: running the script twice produces byte-identical output (stable
ordering by Xray key within each file).

Dependencies: Python 3 stdlib only.

Exit codes:
- `0` — success
- `2` — malformed input JSON
- `3` — unmapped prefixes (and `default_bucket` not set)
- `4` — accounting mismatch (would indicate a bug; should never fire)

## Verification agent prompt (future work)

The next experiment — feeding feature files to an agent that audits the iOS
implementation — needs a `verification-agent-prompt.md` defining outcome
classes (`PASS` / `FAIL` / `CANNOT_VERIFY` / `NOT_APPLICABLE`), tag-based
branching rules, findings classification (`Missing` / `Divergent` / `Dead` /
`Ambiguous`), an output table format, and anti-hallucination clauses
(file:line citations required for any `PASS`/`FAIL`).

This is intentionally **not** generated by the `/xray-to-gherkin` skill — it's
a separate artifact tied to the audit experiment, not to the conversion.
Author it ad-hoc when running the experiment.

## Out of scope

- No edits to existing `features/<category>/<epic-slug>/` content in `faceai-docs`
- No reconciliation between Xray tests and the existing epic-level Gherkin in `features/filters/`
- No automated Xray re-pull — the input is the dated JSON snapshot
- No execution of the verification agent — that is the experiment to be run separately
- No changes to the iOS repo

## Execution outcome (2026-05-13)

Smoke-tested end-to-end against `FAIOSMAU_tests_2026-05-13.json`:

- **203 input** = **198 converted** + **5 skipped** (zero-step tests; see `skipped.md`)
- **16 feature files** + 1 `misc.feature` (FAIOSMAU-299, prefix-less)
- Tags, Scenario Outlines, context comments, and traceability all render correctly on spot-check
- Output written to `/tmp/xray-smoketest/` during validation; not yet committed to `faceai-docs`

## Open follow-ups

- Commit the conversion output to `~/Apps/FaceAI/faceai-docs/xray-suites/FAIOSMAU/`
  (or run `/xray-to-gherkin` again pointing directly at that location)
- Author `verification-agent-prompt.md` and run the audit experiment against one feature
- Decide whether `xray-suites/` lives on `main` in `faceai-docs` or on a long-lived experiment branch
- Periodic re-export from Xray (cadence TBD)
