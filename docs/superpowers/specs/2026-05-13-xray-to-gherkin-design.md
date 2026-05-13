---
date: 2026-05-13
topic: Xray → Gherkin conversion for FAIOSMAU
status: Approved
---

# Xray → Gherkin conversion for FAIOSMAU

## Goal

Convert 203 Xray manual test cases (input: `FAIOSMAU_tests_2026-05-13.json`) into a
small set of grouped Gherkin `.feature` files, plus a ready-to-use agent prompt that
an AI agent can follow to audit the iOS implementation against those scenarios.

The end-state experiment: feed one `.feature` file + the iOS source to an agent and
get back a structured report of where the implementation matches, diverges, or
cannot be verified from code alone.

## Inputs

- `~/Projects/em-hub/FAIOSMAU_tests_2026-05-13.json` — 203 Xray test cases
  (manual, step-based; no existing Gherkin)
- iOS source repo at `~/Apps/FaceAI/faceai_ios` (consumed only by the verification
  agent, not by the conversion pipeline)

## Output location

```
~/Apps/FaceAI/faceai-docs/xray-suites/FAIOSMAU/
├── README.md                          # conventions, tag glossary, usage
├── verification-agent-prompt.md       # ready-to-use audit prompt
├── skipped.md                         # tests excluded from conversion + reason
├── source/
│   └── FAIOSMAU_tests_2026-05-13.json # snapshot of input for traceability
├── scripts/
│   └── xray_to_gherkin.py             # idempotent converter (Python)
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
    └── errors.feature
```

Rationale for top-level `xray-suites/` rather than `features/<category>/`: the
existing `features/` convention in `faceai-docs` is per-epic (each folder has an
`epic.md`), and these tests have no source epic. Keeping them separate avoids
diluting the epic convention.

## Feature grouping

16 files, derived by semantic grouping of Xray summary prefixes:

| File | Merges these Xray prefixes |
|---|---|
| `onboarding.feature` | `[OnBoard]`, `[Onboard]`, `[App landing]`, `[iOS Permissions]` |
| `home.feature` | `[Home]` |
| `upload_photo.feature` | `[Upload photo]`, `[Upload Photo]`, `[Default gender]`, `[Camera]` |
| `editor.feature` | `[Editor]`, `[All Filters]`, `[All filters]`, `[Tools]` |
| `face_filters_categories.feature` | per-category "all filters apply without errors" tests for `[Hair Style]`, `[Hair Colors]`, `[Glasses]`, `[Smiles]`, `[Impression]`, `[Skin]`, `[Sizes]`, `[Age]`, `[Gender]`, `[Features]`, `[Beards]` |
| `face_filters_behavior.feature` | `[Face Filters]`, `[Makeup]`, `[Background]` (selection, intensity, credits, multi-select) |
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

The router lives in `scripts/xray_to_gherkin.py` as an explicit `prefix → file`
mapping. Unmapped prefixes cause the script to exit with an error rather than
silently dropping tests.

## Per-scenario conventions

Each Xray test becomes exactly one Gherkin scenario. Conventions:

### Scenario name
The Xray `summary`, with the leading `[Prefix]` stripped (the containing file
already represents the feature).

### Tags (applied per scenario)
- `@FAIOSMAU-XXX` — Xray key. Mandatory. Bidirectional traceability.
- `@regression` — preserved from Xray `labels` when present.
- `@visual` — assertion is about layout / design / Figma alignment.
  Detected from keywords: `align`, `Figma`, `design`, `layout`, `position`, `appearance`.
- `@firebase` — depends on Firebase Remote Config or Crashlytics state.
  Detected from: `[Firebase]` in summary, `Crashlytics`, `Remote Config`.
- `@external` — depends on payment, App Store, network, NSFW classifier, or
  another runtime-only signal. Detected from: `Superwall`, `AppStore`, `Restore`,
  `Payment`, `NSFW`, `internet`, `Soft Update`, `Force Update`.

Multiple tags can apply to one scenario. Detection is keyword-based and
intentionally over-inclusive — better to mark a behavioral test `@visual` than
to miss one.

### Step mapping
Xray steps have `action`, `data`, `result`. Gherkin shape:

- First step's setup context → `Given` (when ambiguous, emit `Given the app is launched`
  as a safe default and leave a `# TODO:` comment)
- Each `action` → `When <action>` (or `And` after the first `When`)
- Each non-empty `result` → `Then <result>` (or `And` after the first `Then`)
- `data` field, if non-empty → appended as `# data: <value>` comment above the step

### Parameterized tests
Tests containing `${...}` placeholders are emitted as `Scenario Outline` with:
- Step text rewritten with `<param>` in place of `${param}`
- An empty `Examples:` table containing the column headers only
- A `# TODO: fill from Xray FAIOSMAU-XXX — placeholders were not expanded in source` comment

### Context preservation
- Figma / Drive / Confluence URLs from `description` → `# ref: <url>` comments above the scenario
- Plain-text description content (non-trivial, not a duplicate of the summary) → `# context: <text>` comment above the scenario

### Un-convertible tests
A test is excluded (and logged to `skipped.md`) when:
- All `action` fields are empty, OR
- The test has zero steps and the summary alone gives no actionable behavior

`skipped.md` lists each excluded test as `- FAIOSMAU-XXX — <summary> — reason: <reason>`.

## Conversion pipeline

A single Python script: `scripts/xray_to_gherkin.py`.

Responsibilities:
1. Load the Xray JSON from `source/` (path is a CLI arg, defaults to the snapshot)
2. For each test:
   - Route by prefix to a feature file (fail loudly on unmapped prefix)
   - Determine tags via keyword heuristics
   - Detect placeholders → choose `Scenario` vs `Scenario Outline`
   - Build the Gherkin scenario block
   - If un-convertible: append to skip list instead
3. Group scenarios by feature file; write each file with a `Feature:` header
   derived from the file slug
4. Write `skipped.md`
5. Exit non-zero if any test was lost (i.e. converted + skipped != input count)

Idempotency: running the script twice produces byte-identical output (stable
ordering by Xray key within each file).

Dependencies: standard library only. No third-party packages.

## `verification-agent-prompt.md`

The audit protocol given to the verification agent. Defines:

### Inputs the agent receives
- One `.feature` file from `features/`
- The iOS repo at `~/Apps/FaceAI/faceai_ios`

### Per-scenario outcome (exactly one of)
- `PASS` — implementation matches; must cite `file:line` as evidence
- `FAIL` — implementation diverges or is missing; must cite `file:line` and describe the gap
- `CANNOT_VERIFY` — cannot be determined from code alone (visual, runtime-only, external service)
- `NOT_APPLICABLE` — scenario references something that no longer exists in the product (e.g. removed feature)

### Tag-based branching rules
- `@visual` → default to `CANNOT_VERIFY` for the layout assertion itself, but the
  agent must still check that the referenced view/asset exists in code and report
  `FAIL` if it doesn't
- `@firebase` → `CANNOT_VERIFY` unless Remote Config defaults or Crashlytics
  setup are visible in the repo
- `@external` → `CANNOT_VERIFY` unless mocks/stubs in the codebase let the
  behavior be inferred

### Findings classification
Each `FAIL` is classified as one of:
- **Missing**: the behavior has no corresponding code
- **Divergent**: code exists but behaves differently from the scenario
- **Dead**: code path exists but appears unreachable
- **Ambiguous**: scenario is open to multiple interpretations; agent picks the most likely and flags it

### Output format
A single Markdown table per run:

```
| Xray key | Scenario | Outcome | Evidence | Classification | Notes |
|----------|----------|---------|----------|----------------|-------|
| FAIOSMAU-316 | … | FAIL | OnboardingViewController.swift:142 | Missing | … |
```

### Anti-hallucination clauses
- Every `PASS` or `FAIL` requires a concrete `file:line` citation
- If no citation is possible, the outcome must be `CANNOT_VERIFY`
- The agent must never invent Xray keys, file paths, or step text

## Out of scope

- No edits to existing `features/<category>/<epic-slug>/` content in `faceai-docs`
- No reconciliation between Xray tests and the existing epic-level Gherkin in `features/filters/`
- No automated Xray re-pull — the input is the dated JSON snapshot
- No execution of the verification agent — that is the experiment to be run separately
- No changes to the iOS repo

## Success criteria

- `scripts/xray_to_gherkin.py` runs to completion and reports 203 input tests = (converted + skipped)
- 16 `.feature` files produced; each parses as valid Gherkin (gherkin-official Python lib check, run manually)
- Every scenario carries a `@FAIOSMAU-XXX` tag
- A spot-check of 10 scenarios across 5 files confirms: tags assigned sensibly,
  step mapping readable, parameterized cases use Scenario Outline correctly
- `verification-agent-prompt.md` is self-contained — a fresh agent given the prompt + one feature file produces a usable audit table

## Open follow-ups (not in this spec)

- Running the verification experiment end-to-end against one feature
- Deciding whether to commit `xray-suites/` to the `faceai-docs` main branch or
  keep it on a long-lived experiment branch
- Periodic re-export from Xray (cadence TBD)
