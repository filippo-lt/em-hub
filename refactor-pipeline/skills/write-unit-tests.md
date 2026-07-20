---
name: write-unit-tests
description: Generate fine-grained unit tests against the refactored feature module's public API, using the architecture doc as the testing-strategy guide. Phase 5.
---

# /write-unit-tests

Phase 5 skill. Replaces the throwaway characterisation tests with
proper unit tests against the new module's public API.

## Inputs

- Refactored feature module (phase 4 output)
- ARCH.md (testing strategy section is mandatory)
- `<feature>.feature` (Gherkin scenarios — coverage targets)
- `<feature>.spec.md` (state machine + invariants — assertion sources)
- Characterisation tests (reference; about to be deleted/migrated)

## Output

`tests/unit/<feature>/` containing:
- One test class per public type in the new module
- Tests organised by behaviour, not by method
- A short `README.md` describing test conventions used

## Goal

Every public API in the new module has tests that:
1. Cover the scenarios in `<feature>.feature` (excluding `@manual-only`)
2. Cover the invariants in `<feature>.spec.md`
3. Cover the architecture-defined contracts (per ARCH.md)
4. Are independent (no shared state)
5. Are fast (unit-level, mocked dependencies)

## Process

1. **Map scenarios to new types.** Each Gherkin scenario should map to
   1–N unit tests against specific types in the new module. Build this
   map first.
2. **Map invariants to assertions.** Every invariant in `spec.md`'s
   state-machine section becomes at least one test (e.g. "Continue
   disabled if photo unset" → test on the state-machine type, not
   the view model).
3. **Add architecture-required tests.** ARCH.md will define rules
   like "use cases must be testable in isolation", "repositories must
   be mockable" — generate tests that verify these.
4. **Generate tests in order:** domain → use cases → presentation.
   Same order as the refactor.
5. **Diff against characterisation tests.** Anything pinned by a
   characterisation test that *isn't* covered by a unit test is a gap
   — generate the missing unit test or document why it's intentionally
   integration-level.

## Test naming

Per ARCH.md if it specifies; otherwise:
```
test_<methodOrBehaviour>_<condition>_<expectedOutcome>
```
Example: `test_advanceToStep2_whenPhotoUnset_throws()`

## Coverage targets

Per type:
- Every public method has tests for happy path and key failure modes
- Every state transition in the state machine has a test
- Every invariant has a test
- Every external dependency boundary has both happy and failure tests

Coverage threshold: per ARCH.md / team standard. The skill reports
coverage; the team enforces it.

## What gets deleted

After phase 5:
- Characterisation tests that are fully replaced by unit tests → delete
- Characterisation tests that cover end-to-end flows the unit tests
  can't reach → move to `tests/integration/`
- Characterisation tests with no unit-test equivalent → review with
  team. Either gap (write the unit test) or genuinely
  integration-level (move).

## Behaviour rules

- **One assertion per test.** Or close to it. Multi-assertion tests
  hide what failed.
- **Mock at module boundary, not below.** If `GenerationUseCase`
  depends on `GenerationRepository` (an abstract boundary), mock at
  the repository. Don't mock `URLSession` directly.
- **Test behaviour, not implementation.** Don't assert "method X was
  called with Y"; assert "given X input, output is Y". Mocks are for
  *isolating*, not for *checking* call patterns.
- **Don't test the framework.** `XCTest` works; SwiftUI works; assume
  these. Test your code.
- **Reuse spec entities.** If `spec.md` defines `Palette { id,
  entitlement }`, the tests use the same shape, not a parallel
  invented type.

## Gate to mark feature complete

- All scenarios (excluding `@manual-only`) covered by ≥1 unit test
- Coverage threshold met (per team standard)
- Characterisation tests deleted or migrated to `tests/integration/`
- `<feature>.feature` updated if any scenarios were added/refined
  during testing
- Feature appears in `docs/specs/_index.md` as `phase: complete`
  (regenerate via `/trace-coverage`)

## Common failure modes

- **Testing through the UI.** SwiftUI views or VCs as test surface.
  Wrong layer; tests are slow and brittle. Push assertions down to
  the view model / use case.
- **Brittle mocks.** Mocks that capture call order or exact arguments
  break on every refactor. Only assert what the test actually cares
  about.
- **Test-as-spec drift.** Tests start asserting things not in the
  spec. Either the spec is incomplete (update it) or the test is
  wrong (fix it).
- **Skipping the boring tests.** Validation rules ("disabled if X")
  feel trivial but are exactly the bugs that hit production.
