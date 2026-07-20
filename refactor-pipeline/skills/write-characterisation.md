---
name: write-characterisation
description: Generate characterisation tests pinning the current behaviour of a feature, against the legacy code, before refactoring. Phase 3.
---

# /write-characterisation

Phase 3 skill. Writes throwaway-ish integration tests that lock in the
*current* behaviour of a feature so the phase 4 refactor can't silently
break things.

## Inputs

- `<feature>.audit.md` (mapping of scenarios to code paths)
- `<feature>.feature` (Gherkin scenarios)
- Current iOS codebase
- Test infrastructure conventions (how tests are run, mocked, etc.)

## Output

`tests/characterisation/<feature>/` containing:
- One test class/file per major scenario group
- A `README.md` documenting why these tests exist and when to delete them

## Goal & non-goals

**Goal:** every audited scenario (excluding `@manual-only`) has at least
one characterisation test that fails if the scenario's behaviour changes.

**Non-goals:**
- Pretty test code. These will be deleted.
- Unit-level granularity. Test at the seam available, not the seam you
  wish you had.
- Fixing bugs. If the current code has a bug, the test pins the bug.

## Test level

Use the *highest* level of seam that lets you write the test:
1. **Pure unit** if the code happens to be testable that way (rare in
   legacy)
2. **View-model / use-case test** with mocked dependencies
3. **Integration test** with real or in-memory dependencies
4. **UI test** as last resort (slow, brittle, but sometimes the only
   option for legacy code)

The characterisation test layer is whatever level makes the test
*possible*. Phase 5 fills in the unit-test layer properly.

## Process

1. Walk scenarios in `<feature>.feature` in audit-cited order.
2. For each, identify the smallest testable seam from `audit.md`
   (the implementing files/methods).
3. Write a test that:
    - Sets up the preconditions (`Given`)
    - Exercises the action (`When`)
    - Asserts the outcome (`Then`)
4. If the seam doesn't exist, *don't* refactor the legacy code to add
   one — write at the next-higher level. The legacy code is being
   replaced anyway.
5. Tag tests with the source `@ADIOSMAU-xxx` and `@characterisation`
   so they can be filtered.

## Bug-pinning

Some characterisation tests will pin known-buggy behaviour. Mark these
with a comment:

```swift
// CHARACTERISATION: pins current bug — tap-fires-event-twice.
// Phase 4 may intentionally break this; if so, replace with corrected
// assertion in tests/unit/ and remove this test.
```

## Skip rules

Skip generation for:
- `@manual-only` scenarios (visual / quality assertions)
- `@firebase` / `@internal` scenarios where the precondition requires
  real Firestore writes (test-doubles probably won't capture the
  behaviour faithfully — flag for QA-level coverage instead)
- Scenarios marked `❓ uncertain` in the audit (don't pin behaviour
  you don't understand)

## Output README template

```markdown
# Characterisation tests — <Feature>

These tests are scaffolding for the <Feature> refactor. They pin the
**current** behaviour, including bugs, so phase 4 can refactor safely.

## When to delete

After phase 5, when:
- All scenarios have proper unit tests in tests/unit/<Feature>/
- Any integration paths still needed are moved to tests/integration/

Tests still tagged @characterisation after phase 5 should be reviewed
case-by-case.

## Known bug-pins

- <test name>: pins ADIOSMAU-XXX bug — <description>
```

## Behaviour rules

- **Coverage over quality.** Better an ugly test that runs than a
  clean test that doesn't.
- **No refactoring for testability.** If the legacy code resists
  testing, write at a higher level. Don't change the code under test.
- **Fail loudly, not informatively.** A failing test in phase 4 should
  obviously point at the changed scenario; doesn't need to debug
  itself.

## Common failure modes

- **Over-mocking** — pinning the implementation rather than the
  behaviour. If the test fails because a mock wasn't called in the
  exact order, you've over-mocked.
- **Under-asserting** — checking only that a method ran, not what it
  produced. Tests should fail if behaviour changes, not just if code
  paths change.
- **Skipping the messy scenarios** — those are the ones you most need
  pinned. If a scenario is hard to test, that's information about why
  the refactor is needed.

## Gate before phase 4

- All non-skipped scenarios have at least one characterisation test
- All tests are green against current code (committed)
- README is filled in with bug-pins listed
