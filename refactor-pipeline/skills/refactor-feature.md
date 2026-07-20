---
name: refactor-feature
description: Migrate a feature module to the target clean architecture, using audit + spec + ARCH.md as inputs and characterisation tests as the safety net. Phase 4.
---

# /refactor-feature

Phase 4 skill. The big one. Produces a refactor plan first, then code in
stages, with characterisation tests staying green throughout.

## Inputs

- `<feature>.audit.md` (mapping + resolved discrepancies)
- `<feature>.spec.md` (entities, state machine, dependencies)
- `<feature>.feature` (Gherkin)
- ARCH.md (the target architecture doc — **load fully, this is the law**)
- Characterisation tests (must be green)
- Current iOS codebase (for reference, not as a source of truth on
  behaviour — that's the spec)

## Outputs

Two phases of output:

### Output 1: `<feature>.refactor-plan.md`

Reviewed before any code is written. Structure:

```markdown
# <Feature> — Refactor Plan

## Target module structure

src/Features/<Feature>/
├── Domain/
│   ├── <Feature>State.swift
│   ├── <Feature>UseCase.swift
│   └── ...
├── Data/
│   └── ...
├── Presentation/
│   └── ...
└── DI/
    └── <Feature>Module.swift

## Decomposition

| New type            | Replaces (legacy)                       | Responsibility                    |
| ------------------- | --------------------------------------- | --------------------------------- |
| GardenStateMachine  | GardenDesignVM (parts)                  | step-1/2/3 transitions            |
| GenerationUseCase   | GardenDesignVM.generate() + Service     | image generation orchestration    |
| ...                 |                                         |                                   |

## External dependency adapters

Per dependency in spec.md, the new boundary type:

| Dependency                  | Adapter                          | Notes                       |
| --------------------------- | -------------------------------- | --------------------------- |
| Firestore palette config    | PaletteConfigRepository          | per ARCH.md repository rule |
| Amplitude events            | GardenAnalytics                  | typed events, no strings    |
| ...                         |                                  |                             |

## Migration order

1. Domain types + state machine (no dependencies)
2. Use cases + adapters (depends on domain)
3. Presentation layer (depends on use cases)
4. DI wiring + entry-point swap

Each step: characterisation tests must stay green.

## Risks

- <risk> — <mitigation>
- ...

## Out of scope

- Cross-feature concerns (DI container itself, routing)
- Visual changes
- Behavioural changes (other than discrepancies marked as "fix" in audit)
```

### Output 2: code

Generated in the order declared in the plan. For each migration step:
1. Generate code for that step.
2. Wire it (or stub it) so the project still compiles.
3. Run characterisation tests — must stay green.
4. Commit. Move to next step.

## Process

1. **Read ARCH.md fully.** Every type, every layer, every rule. The
   architecture doc is the law for this phase. If it conflicts with
   `spec.md`, ARCH wins on *structure*; spec wins on *behaviour*.
2. **Produce the plan.** Submit for human review *before* writing code.
   The plan should be reviewable in <30 minutes.
3. **Stage migration.** Domain → use cases → presentation → DI.
4. **Run characterisation tests after each stage.** Any red is a stop
   condition.
5. **Don't change observable behaviour** unless the audit explicitly
   marked a discrepancy as "fix in refactor". Those are flagged in
   the PR description.

## Behaviour rules

- **Plan before code.** No code generation in the same call as the
  plan. Plan gets reviewed first.
- **Stage commits.** Don't generate the entire feature in one commit.
  Domain layer, use cases, presentation, DI — each is a reviewable unit.
- **Spec over current code.** When refactoring, the *spec* is what the
  new code implements. The current code is reference for *how* it works
  today, not *what* it should do tomorrow.
- **No new behaviours.** Phase 4 is migration, not feature work. New
  features happen after the refactor is complete.

## Bug fixing during refactor

If a discrepancy in audit.md is marked "code is wrong, fix in refactor":
- Implement the corrected behaviour in the new module.
- The characterisation test for that scenario *will fail* (because it
  pinned the bug).
- In the PR, explicitly call out: "Characterisation test
  `testFooEventFiresOnce` is updated; previously pinned bug
  ADIOSMAU-XXX where event fired twice."
- The new unit test in phase 5 asserts the correct behaviour.

If you find yourself "fixing" something *not* flagged in audit.md:
**stop**. Either it's an unflagged discrepancy (go back to audit) or
it's scope creep. Don't silently fix.

## Common failure modes

- **Over-engineering** — adding abstractions ARCH.md doesn't ask for.
  ARCH is the spec; don't add layers it doesn't define.
- **Direct port** — copying legacy structure into new folders without
  actually applying the architecture. The new code should look like
  ARCH says, not like the old code.
- **Big-bang** — generating the entire feature in one shot. Stage it.
- **Silent behaviour changes** — every behavioural change goes in the
  PR description, even tiny ones.
- **Dependency on legacy types** — the new feature module shouldn't
  import legacy types except via explicit adapter boundaries.

## Gate before phase 5

- All characterisation tests green (or explicitly updated for fixed
  bugs, with PR notes)
- ARCH.md adherence verified (linter / fitness function / human review)
- New module compiles in isolation (DI swap works)
- PR reviewed and merged
