---
name: spec-from-tests
description: Convert Xray test cases for a single feature into Gherkin spec, entity/state-machine doc, and coverage-gap doc. Phase 1 of the refactor pipeline.
---

# /spec-from-tests

Phase 1 skill. Takes a feature's QA tests from an Xray JSON export and
produces three artefacts: machine-actionable Gherkin, a domain spec doc,
and a coverage-gap doc.

## Inputs

- Xray JSON export path (default `source-data/*.json`)
- Feature filter — either:
    - prefix string in the test summary (e.g. `[Garden]`, `[Onboarding]`)
    - or explicit list of test keys
- Output directory (default `docs/specs/<feature-slug>/`)
- (optional) `tags.md` — canonical tag vocabulary if locked

## Outputs

Three files in the output directory:

### `<feature>.feature`
Gherkin file. Rules:
- One `Feature:` per file.
- `Background:` extracts shared preconditions across scenarios.
- Each Xray test → one or more `Scenario`s (split bundled assertions).
- Every scenario tagged with its source `@ADIOSMAU-xxx` key.
- Categorical tags from the canonical taxonomy (`@validation`, `@generation`,
  `@firebase`, `@analytics`, `@paywall`, `@offline`, `@i18n`,
  `@manual-only`, `@internal`, etc.).
- `Scenario Outline` + `Examples:` for any test using `${variable}`
  placeholders. Examples must be concrete values, not placeholders.
- Step text uses *domain language*, not UI labels:
    - ✅ `the user enters the Garden Design flow`
    - ❌ `the user taps on the "Garden Design" tile on the main screen`
- Single-purpose scenarios. If an Xray test bundles multiple assertions
  in different `result` fields, split into separate scenarios.

### `<feature>.spec.md`
Structured domain doc:
- **Purpose** — one paragraph.
- **Entities** — table of domain types and their fields/states.
- **State machine** — ASCII diagram of allowed flows + invariants.
- **External dependencies** — Firebase paths, analytics events, network
  contracts, paywall triggers, etc.
- **Out-of-scope assertions** — visual/quality assertions tagged
  `@manual-only`.
- **Glossary** — feature-specific terms.

Anything not directly derivable from the source tests is marked
`(inferred)` so reviewers know what to confirm.

### `<feature>.coverage.md`
Audit of the source tests themselves:
- **Ambiguous assertions** — table of unclear / non-mechanical assertions
  with suggested resolutions.
- **Internal conflicts** — inconsistent prefixes, copy-paste errors,
  cross-feature tests filed under this feature.
- **Missing scenarios** — coverage gaps grouped by feature area
  (error paths, permissions, edge cases, accessibility, analytics
  completeness, etc.).
- **Tests that should probably move** — wrong feature classification.
- **Recommended uses** — a short footer explaining how to use this doc
  (input to phase 2, conversation with QA, etc.).

## Process

1. Filter the Xray JSON to the requested feature.
2. Cluster by intent — group tests that test the same area (entry, step 1,
   generation, etc.) so the Gherkin reads as documentation, not a flat list.
3. Extract `Background:` candidates — actions/preconditions that appear in
   most tests.
4. Convert each test's steps:
    - leading "open app + enter feature" → `Background:`
    - intermediate `action` lines → `When` / `And When`
    - terminal `result` field → `Then` / `And Then`
    - `${var}` → `Scenario Outline` + concrete `Examples:`
5. Apply tags from the canonical taxonomy.
6. Build `spec.md` from cross-test patterns (entities mentioned, state
   transitions implied, dependencies referenced).
7. Build `coverage.md` by *negation* — what the spec implies should be
   tested, that the source tests don't cover.

## Worked example

See `demo/garden-design/` in this folder. 21 source tests → 28 scenarios,
plus `.spec.md` (state machine, entities, dependencies) and `.coverage.md`
(10 ambiguities, 4 conflicts, ~20 missing scenarios).

## Behaviour rules

- **Faithful, not curated.** Include debug/Firebase/internal tests, just
  tag them appropriately. Filtering is a downstream concern.
- **Mark inferences.** Anything in `spec.md` not directly stated in tests:
  `(inferred)`.
- **No silent corrections.** If a source test has a copy-paste bug
  (e.g. ADIOSMAU-315), include the scenario *as filed* and flag in
  `coverage.md`. Don't fix it silently.
- **Don't invent scenarios.** Coverage doc lists what's missing; it
  doesn't add scenarios for missing coverage to the `.feature` file
  unless an explicit `--with-inferred` flag is set (and even then, tag
  them `@inferred`).

## Common failure modes

- **Bundled assertions not split** — re-read each test's `result`
  fields; if there are multiple distinct outcomes, they're separate
  scenarios.
- **UI labels in step text** — if you wrote a string in quotes that
  looks like a button label, replace with domain action.
- **Empty `Examples:` blocks** — if you can't enumerate values, the
  test is ambiguous; flag in `coverage.md` and use a placeholder
  marked TODO.
