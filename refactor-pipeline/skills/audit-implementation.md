---
name: audit-implementation
description: Map every Gherkin scenario to its implementing code paths and surface diffs between spec and code. Phase 2 — highest-judgement step.
---

# /audit-implementation

Phase 2 skill. The keystone of the pipeline. Every later phase consumes
the audit output, so this skill's quality dictates the program's quality.

## Inputs

- `<feature>.feature` (Gherkin)
- `<feature>.spec.md` (domain spec)
- iOS codebase (read access)
- ARCH.md (architecture doc — for reference, not enforcement at this
  phase; the audit is against current code, not target architecture)

## Output

`<feature>.audit.md` — see structure below.

## Output structure

```markdown
# <Feature> — Implementation Audit

> Generated: <date>
> Source: <feature>.feature (rev: <git sha or date>)
> Audited against: src/ (rev: <git sha>)

## Summary

- Scenarios audited: N
- Mapped with confidence: M
- Mapped with discrepancies: P
- Unmappable / orphan scenarios: Q
- Code paths with no scenario coverage: R

## Module map

Top-level files/types implementing this feature. Build this first; the
scenario audit refers to it.

| Symbol                       | File                                | Role                          |
| ---------------------------- | ----------------------------------- | ----------------------------- |
| GardenDesignViewController   | Features/Garden/Garden…VC.swift     | UI entry, step nav            |
| GardenDesignViewModel        | Features/Garden/Garden…VM.swift     | flow state                    |
| GenerationService            | Services/GenerationService.swift    | API client                    |
| ...                          |                                     |                               |

## Scenario audit

### @ADIOSMAU-308 — Cancelling on step 3 returns to main and discards in-flow state

- **Status:** ✅ matches | ⚠️ discrepancy | ❌ not implemented | ❓ uncertain
- **Implementing code:**
    - `Features/Garden/GardenDesignVC.swift:142` — close button handler
    - `Features/Garden/GardenDesignVM.swift:89` — `reset()` method
- **Evidence:** close button calls `vm.reset()` which clears `photo`,
  `style`, `palette` fields. Navigation pops to root.
- **Notes:** state clearing happens on `viewWillDisappear`, not on
  button tap directly. Behavioural equivalent.

### @ADIOSMAU-XXX — <next scenario>
...

## Discrepancies (require resolution before phase 3)

For each ⚠️ above, repeat here with explicit decision required:

### Discrepancy D-001: <scenario key>

- **Spec says:** "the analytics event is emitted exactly once"
- **Code does:** event is emitted both on `viewDidAppear` and on button
  tap, fires twice on rapid tap
- **Likely cause:** historical, no debounce
- **Decision needed:** is the spec wrong (update Gherkin), or is the
  code wrong (file bug, fix later)?
- **Owner:** Eng lead → PM if doubt

## Orphan scenarios

Scenarios with no clear implementing code path. May be: not yet
implemented, removed, or testing a feature that moved.

- @ADIOSMAU-XXX — <reason for being unable to map>

## Orphan code (untested by spec)

Code paths in the feature module not exercised by any scenario.
Candidates for either: missing tests, or dead code.

- `GardenDesignVM.swift:215` — `prefetchPalettes()` — no scenario
  references palette prefetch.

## External dependency contracts

Confirm/deny what `<feature>.spec.md` declared:

| Declared dependency                    | Found?                       | Notes                     |
| -------------------------------------- | ---------------------------- | ------------------------- |
| Firestore: styles/styleOriginalStyle   | ✅ Services/Firestore:88     | Cached for 10 min         |
| Amplitude: start_garden                | ✅ Analytics/Events.swift:42 | No properties confirmed   |
| Amplitude: view_screen_garden          | ⚠️ found, but property name `screen_index` not `screen_number` | Spec or code wrong? |
```

## Process

1. **Build the module map first.** What files implement this feature?
   What types? What's the entry point? Without this, the per-scenario
   audit becomes a fishing expedition.
2. **Walk scenarios in spec order**, not Xray-key order. Group by
   feature area (entry, step 1, generation, etc.) so the audit reads
   coherently.
3. **For each scenario:** find the code path that would execute the
   `When` and produce the `Then`. Cite file:line. Mark confidence.
4. **Validate external dependency contracts** from `spec.md` against
   actual code. The Firebase/Amplitude/network contracts are where
   silent drift hides.
5. **Surface orphan code** by walking the feature module and checking
   each public method against scenario coverage.

## Behaviour rules

- **Cite file:line for every claim.** No "I think this is in the view
  model somewhere." If you can't cite, mark `❓ uncertain`.
- **Don't fix anything.** This skill is read-only. Discrepancies are
  *flagged*, not corrected. Phase 3 / 4 fixes them.
- **Don't trust the spec over the code.** Both can be wrong. The
  discrepancy section's job is to *raise the question*, not to answer it.
- **Report orphans honestly.** It's tempting to map every scenario to
  *something* to look complete. Better to mark ❓ than to misattribute.

## Owner

- LLM: first pass.
- Engineer: validates every ⚠️ / ❓ entry.
- PM: consulted for any discrepancy where the "correct" behaviour is
  unclear.

## Common failure modes

- **Hallucinated mappings** — LLM invents file paths or method names.
  Mitigation: every cited path must be verifiable; spot-check at least
  20% of mappings.
- **Surface-level matches** — finding a string match in the codebase
  isn't an implementation match. The mapping should follow the actual
  *control flow*.
- **Missing the indirection** — feature logic often lives 2-3 layers
  deep (VC → VM → Service). The skill needs to follow through, not stop
  at the first match.

## Gate before phase 3

All ⚠️ discrepancies have a documented decision (update spec / file bug /
intentional drift). No ❓ entries remain on critical-path scenarios.
