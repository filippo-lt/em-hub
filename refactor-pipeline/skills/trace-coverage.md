---
name: trace-coverage
description: Walk docs/specs and build a traceability index linking Xray test keys, scenarios, tags, code paths, and phase status. Read-only. Run anytime.
---

# /trace-coverage

Cross-cutting utility skill. Builds and updates `docs/specs/_index.md`,
the single source of truth for "where is each feature in the pipeline".

## When to use

- After any phase artefact is added/updated
- Before a status review ("which features are where?")
- To answer ad-hoc queries: "which scenarios cover module X?", "which
  scenarios are `@manual-only`?", "which Xray tests are not yet in any
  Gherkin scenario?"

## Inputs

- `docs/specs/**/*.feature` — Gherkin sources
- `docs/specs/**/*.audit.md` — phase 2 outputs (when present)
- `docs/specs/**/` — directory presence indicates phase progression
- (optional) `source-data/<xray-export>.json` — to detect untracked tests

## Outputs

`docs/specs/_index.md` (regenerated, marked auto-generated):

```markdown
# Specs Index — auto-generated, do not edit

## Features

| Feature        | Scenarios | Phase    | Last updated |
| -------------- | --------- | -------- | ------------ |
| garden-design  | 28        | spec     | 2026-05-04   |
| force-update   | 6         | -        | -            |
| ...            |           |          |              |

## Scenarios by Xray key

| Key             | Feature        | Scenario                                    | Tags                  |
| --------------- | -------------- | ------------------------------------------- | --------------------- |
| ADIOSMAU-308    | garden-design  | Cancelling on step 3 returns to main…       | @cancel               |
| ADIOSMAU-1284   | garden-design  | Entering Garden Design fires start_garden…  | @analytics            |
| ...             |                |                                             |                       |

## Tag distribution

| Tag             | Count | Features                          |
| --------------- | ----- | --------------------------------- |
| @validation     | 12    | garden-design, ...                |
| @manual-only    | 4     | garden-design                     |
| ...             |       |                                   |

## Orphans

### Xray tests not yet specced
- ADIOSMAU-XXX (component=iOS_AID, prefix=[Settings])
- ...

### Scenarios with no audit mapping (phase 2 not run)
- garden-design : Cancelling on step 3 returns to main…
- ...
```

## Behaviour rules

- **Always regenerate fully** — don't try to patch incrementally; the
  index is small, regeneration is cheap.
- **Never edit other files** — read-only against `docs/specs/`.
- **Detect phase by artefact presence**, not by content:
    - `feature` exists → phase ≥ 1
    - `audit.md` exists → phase ≥ 2
    - `tests/characterisation/` non-empty → phase ≥ 3
    - new module exists per `refactor-plan.md` → phase ≥ 4
    - `tests/unit/` non-empty → phase ≥ 5
    - all of the above + characterisation tests removed → `complete`
- **Surface the orphans loudly.** The orphan section is the most useful
  output — it tells you what's missing.

## Implementation note

This is a small data-shaping job. Could be a Python script invoked via
the skill, or pure tool-call walking. Either is fine. The schema of
`_index.md` is the contract; the implementation can change.
