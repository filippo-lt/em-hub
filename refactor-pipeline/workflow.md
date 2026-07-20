# Pipeline Workflow

5 phases per feature, with a cross-cutting traceability utility.
Each phase has: a clear input, a clear output artefact, an owner, and a
human gate before the next phase runs.

## Phase overview

```
                                ┌─────────────────────┐
                                │  /trace-coverage    │  read-only utility,
                                │   (run anytime)     │  builds the index
                                └─────────────────────┘
                                          ▲
                                          │
   ┌─────────────┐    ┌─────────────┐    ┌─┴───────────┐    ┌─────────────┐    ┌─────────────┐
   │   PHASE 1   │ →  │   PHASE 2   │ →  │   PHASE 3   │ →  │   PHASE 4   │ →  │   PHASE 5   │
   │    Spec     │    │    Audit    │    │ Characterise│    │  Refactor   │    │  Unit-test  │
   └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
        skill              skill              skill              skill              skill
   spec-from-tests   audit-impl…    write-charact…    refactor-feature   write-unit-tests
```

## Per-feature folder structure (canonical)

After all phases:

```
docs/specs/<feature-slug>/
├── <feature>.feature              ← phase 1
├── <feature>.spec.md              ← phase 1
├── <feature>.coverage.md          ← phase 1
├── <feature>.audit.md             ← phase 2
├── <feature>.refactor-plan.md     ← phase 4 (input)
└── tests/
    ├── characterisation/          ← phase 3 — throwaway-ish, pinned to current behaviour
    └── unit/                      ← phase 5 — finished, pinned to refactored code
```

Plus:
```
src/Features/<Feature>/
├── (refactored module)            ← phase 4 output
└── ...
```

## Phase contracts

### Phase 1 — Spec

| Field   | Value                                                               |
| ------- | ------------------------------------------------------------------- |
| Skill   | `/spec-from-tests`                                                  |
| Input   | Xray JSON export, feature filter (prefix or component)              |
| Output  | `<feature>.feature` + `<feature>.spec.md` + `<feature>.coverage.md` |
| Owner   | LLM drafts, Eng reviews                                             |
| Gate    | EM + QA review of `coverage.md` ambiguities and gaps                |
| Risk    | Low — read-only over QA tests                                       |

**Why it's safe to batch all features here:** no code touched, no decisions
locked. Run across all 14 features in one session, get the full
documentation tree, then pause to review.

### Phase 2 — Audit

| Field   | Value                                                                       |
| ------- | --------------------------------------------------------------------------- |
| Skill   | `/audit-implementation`                                                     |
| Input   | `<feature>.feature` + `<feature>.spec.md` + current iOS codebase + ARCH.md  |
| Output  | `<feature>.audit.md` — every scenario mapped to code paths, with diffs noted |
| Owner   | Eng leads, PM consulted on ambiguity                                        |
| Gate    | Eng confirms diffs are real (spec wrong vs code wrong); resolve before next phase |
| Risk    | Highest — every later phase depends on this being right                     |

**The audit doc structure:**
- Per scenario: implementing files/functions, evidence
- Per scenario: discrepancy ("spec says X, code does Y")
- Per code module: scenarios that touch it
- Code paths with no scenario coverage (orphan code)
- Scenarios with no code path (orphan tests — possibly testing removed features)

**Critical:** if the audit reveals "spec says X, code does Y", that's a
*decision* moment, not a "fix the code" moment. The decision: is the spec
wrong (update Gherkin), the code wrong (file a bug, fix later), or
intentional drift (document why)? Don't refactor through unresolved
discrepancies.

### Phase 3 — Characterise

| Field   | Value                                                                  |
| ------- | ---------------------------------------------------------------------- |
| Skill   | `/write-characterisation`                                              |
| Input   | `<feature>.audit.md` + current code                                    |
| Output  | Tests in `tests/characterisation/` pinning **current** behaviour       |
| Owner   | Eng + LLM                                                              |
| Gate    | All characterisation tests green against current code                  |
| Risk    | Medium — tests against legacy code can be brittle                      |

**These tests are scaffolding.** They exist to fail loudly during the
refactor. They will be deleted or replaced in phase 5. Do not over-invest
in their quality — invest in their *coverage of audited scenarios*.

Test level: integration / acceptance, not unit. The legacy code may not
be testable at unit level — that's the whole point of refactoring it.

### Phase 4 — Refactor

| Field   | Value                                                                |
| ------- | -------------------------------------------------------------------- |
| Skill   | `/refactor-feature`                                                  |
| Input   | `<feature>.audit.md` + ARCH.md + characterisation tests (must be green) |
| Output  | New feature module in target architecture                            |
| Owner   | Eng + LLM (heavy human review)                                       |
| Gate    | All characterisation tests still green; PR review                    |
| Risk    | High — large code change                                             |

**Process:**
1. Skill produces `<feature>.refactor-plan.md` first — module decomposition,
   file plan, ordering. Review *before* code.
2. Skill produces code in stages — domain layer first, then UI bindings.
3. Each stage: run characterisation tests, must stay green.
4. PR is reviewed end-to-end, not by phase.

**Bug-vs-behaviour:** characterisation tests pin current behaviour,
including bugs. If a bug is intentionally fixed in the refactor, the
corresponding test changes — and that change is called out explicitly
in the PR description.

### Phase 5 — Unit-test

| Field   | Value                                                              |
| ------- | ------------------------------------------------------------------ |
| Skill   | `/write-unit-tests`                                                |
| Input   | Refactored module + ARCH.md                                        |
| Output  | Tests in `tests/unit/` against the new module's public API         |
| Owner   | Eng + LLM                                                          |
| Gate    | Coverage threshold (define per-team); LLM-audit "no untested public API" |
| Risk    | Low-medium — well-bounded by the new architecture                  |

**After phase 5:** characterisation tests can be deleted where they
duplicate unit tests. Some may stay as integration/regression tests if
they cover end-to-end flows the unit tests don't.

## Cross-cutting — `/trace-coverage`

Read-only utility. Walks `docs/specs/**/*.feature`, builds an index:

- Test key → scenario(s)
- Scenario → tags
- Tag → scenarios
- Feature → scenarios → audit-status (from `audit.md`)
- Feature → phase-status (which artefacts exist)

Used to answer:
- "Which scenarios cover module X?"
- "Which features are in which phase?"
- "Which tests have no characterisation test?"
- "Which scenarios are tagged `@manual-only` and should be excluded from CI?"

Run on demand. Output: `docs/specs/_index.md` (regenerated, do not edit by hand).

## Gates summary

| Gate       | Who              | Looks for                                                       |
| ---------- | ---------------- | --------------------------------------------------------------- |
| End P1     | EM + QA          | Coverage gaps. New tests filed back to QA where appropriate.    |
| End P2     | Eng lead         | Spec-vs-code diffs resolved. No "we'll figure it out in P4."    |
| End P3     | Eng + CI         | Char tests green. Cover all `@validation`, `@generation`, etc.  |
| End P4     | Eng review + CI  | Char tests still green. Architecture doc adhered to.            |
| End P5     | Eng + CI         | Coverage threshold. Public API fully tested.                    |

## What "done" looks like per feature

A feature is migrated when:
1. All five phase artefacts exist in `docs/specs/<feature>/`
2. The feature's source lives in `src/Features/<Feature>/` per the new architecture
3. CI runs the unit tests; characterisation tests are deleted or moved to integration
4. Manual-only scenarios are listed for QA in `<feature>.coverage.md`
5. The feature appears in `docs/specs/_index.md` as `phase: complete`

## What it does NOT mean

- Does not mean the feature has zero bugs.
- Does not mean QA can stop manual testing.
- Does not mean cross-feature flows are tested (that's a separate stream).
