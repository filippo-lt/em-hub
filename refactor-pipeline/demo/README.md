# Demo — Garden Design

Worked example of phase 1 output (spec generation from QA tests).

## What's here

`garden-design/` contains the three artefacts produced by `/spec-from-tests`
when run against the 21 QA tests prefixed `[Garden]` / `Garden -` /
`[Garden design]` from the source Xray export.

| File                          | Phase | Description                                    |
| ----------------------------- | ----- | ---------------------------------------------- |
| `garden-design.feature`       | 1     | Gherkin spec, 28 scenarios, tagged             |
| `garden-design.spec.md`       | 1     | Entities, state machine, dependencies          |
| `garden-design.coverage.md`   | 1     | Ambiguities, conflicts, missing scenarios      |

## What it demonstrates

- 21 source tests → 28 scenarios (bundled assertions split)
- Domain-language step text (no UI labels in the test logic)
- `Scenario Outline` + concrete `Examples:` for parametric tests
- Tag taxonomy applied (`@validation`, `@generation`, `@firebase`,
  `@manual-only`, `@i18n`, `@analytics`, etc.)
- ASCII state machine in `spec.md`
- 10 ambiguities + 4 conflicts + 20 missing scenarios in `coverage.md`

## What it does NOT demonstrate

Phase 2–5 outputs don't exist yet for Garden Design. To produce the
full picture, the audit / characterisation / refactor / unit-test
skills need to be implemented and run against the iOS codebase.

## Limitations of the demo

- No architecture doc was available when this was generated; phase 4
  artefacts can't be drafted without it.
- `coverage.md`'s "missing scenarios" list is what the LLM inferred
  from the spec; QA validation would refine it.
- Tag taxonomy is ad-hoc here. Lock the canonical list before scaling
  (see HANDOFF.md decision E).

## How to read it

Start with `garden-design.spec.md` — it gives you the domain model.
Then `garden-design.feature` — the scenarios sit on top of that model.
End with `garden-design.coverage.md` — what's missing.

This is the same reading order every reviewer should use for any
feature's phase-1 output.
