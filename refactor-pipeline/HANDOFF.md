# Handoff — iOS Refactor Pipeline

> Use this doc to resurface the pipeline conversation in the iOS repo.
> It captures: where the thinking landed, what's already decided, what's
> still open, and what to do next.

## Origin context

Filippo + Claude designed this pipeline in em-hub on 2026-05-04, starting
from a question: **can we use Xray test exports to generate Gherkin
documentation of the AID app?**

The conversation evolved into something larger:

> Generate Gherkin → audit current implementation → refactor to clean
> architecture → add the unit tests we don't currently have.

The full conversation produced:
- A **prototype** (Garden Design feature, three files in `demo/`)
- A **5-phase pipeline** (`workflow.md`)
- **Six skill briefs** (`skills/`)
- This handoff doc

---

## Decisions made (don't relitigate)

1. **Workflow is 5 phases, not 4.**
   Refactoring without tests is unsafe. Characterisation tests come *before*
   the refactor, not after. See `workflow.md` for the full pipeline.

2. **Three artefacts per feature in phase 1**, not just a `.feature` file.
   `.feature` (Gherkin) + `.spec.md` (entities, state machine, deps) + `.coverage.md`
   (gaps, ambiguities). The coverage doc surfaces what QA tests *don't* cover —
   often more valuable than what they do.

3. **Faithful test mirror, not curated user-spec.** Every QA test becomes a
   scenario, including debug/Firebase/internal paths. Tags (`@internal`,
   `@manual-only`, `@firebase`, etc.) let downstream prompts filter for context.

4. **One skill per phase**, plus a cross-cutting `/trace-coverage` utility.
   Six skills total. Briefs in `skills/`, not yet implemented.

5. **Pipeline tooling lives in the iOS repo, not em-hub.**
   em-hub keeps initiative-level artefacts (progress, retros, decisions).
   The skills, prompts, and per-feature spec folders belong with the code
   they operate on.

6. **Audit ownership: Engineering first pass, PM if doubts.**
   Phase 2 (the Gherkin ↔ code mapping) is highest-judgement and not
   delegable to LLM alone.

7. **There are zero features in the new architecture today.**
   No mixed-state migration pain to manage. Sequencing decisions are
   purely about pilot selection and priority.

---

## Decisions still open (resolve before scaling)

### A. Pilot feature

Garden Design is fine for the spec prototype, but as the **first end-to-end
pilot** (all 5 phases) it's mid-sized and touches Firebase + paywall +
analytics. Risk: when the pipeline misbehaves, you can't tell whether the
problem is the skill or the feature complexity.

Candidates for a smaller pilot:
- `[Force Update]` (4 tests) — likely simplest
- `[Onboarding]` (6 tests)
- `[Credits]` (6 tests)

**Decision needed:** which feature is pilot #1? Recommend smallest →
prove the pipeline → then Garden Design as pilot #2.

### B. Priority order for the remaining 12+ features

Once the pipeline is proven, what dictates order? Options:
- Regression rate / bug count (data-driven)
- Change frequency in git
- Strategic value (revenue-critical features first)
- Developer pain (where engineers complain most)

**Decision needed:** which signal drives priority. Recommend pulling the
data once and deciding once, not feature-by-feature.

### C. Architecture doc location and linkage

You mentioned the architecture doc is ready. The pipeline needs it as a
*hard input* to phases 4 (refactor) and 5 (unit tests). Before phase 4 can
run on any feature:

- Architecture doc lives at a stable path in the iOS repo
- Skills reference it by relative path
- Doc covers: pattern (MVVM-C? TCA? VIPER?), module boundaries, DI strategy,
  testing strategy, lint/architectural fitness rules

**Decision needed:** confirm the doc's path and that it covers the above.

### D. Skill home — global vs project

iOS repo's `.claude/skills/` directory will hold the six skills. But:
- Will multiple engineers run them, or just one?
- Should they be version-controlled, or per-developer?

**Decision needed:** check in to repo (recommended — shared improvement loop).

### E. Tag taxonomy

The Garden prototype introduced ~10 ad-hoc tags (`@validation`, `@generation`,
`@firebase`, `@manual-only`, `@internal`, `@i18n`, `@analytics`, `@paywall`,
`@offline`, `@persistence`, `@first-run`, `@edge-case`, `@palette`, `@camera`,
`@cancel`, `@ui`, `@template`, `@entitlement`, `@platform:ios`,
`@feature:garden_design`).

Useful as filters but will drift across features without a canonical list.

**Decision needed:** before phase 1 runs on the next feature, lock the tag
vocabulary. Recommend a small tag glossary as part of the architecture doc
or as `tags.md` inside the spec folder root.

### F. Cross-feature tests

`coverage.md` flagged that ADIOSMAU-313 (no-internet) and ADIOSMAU-1284
(analytics) are arguably cross-cutting, not Garden-specific. The spec
folders are per-feature; cross-cutting concerns need a home.

**Decision needed:** add a `docs/specs/_cross-cutting/` folder, or leave
duplicated per feature. Recommend the former.

### G. Coverage gaps surfaced in `coverage.md` — who closes them?

The Garden coverage doc flagged ~20 missing test scenarios (server errors,
permission denials, accessibility, etc.). These are gaps in QA test
coverage, not in the pipeline.

**Decision needed:** are these flagged back to QA (suggested), generated
as new scenarios in the .feature (and asked to QA to backfill), or
deliberately ignored for now?

---

## Risks worth naming

1. **The audit phase is where reality bites.** Every skill before it (phase 1)
   produces clean artefacts; every skill after it (phases 3–5) operates on
   what audit produces. If the audit is sloppy, the rest is downstream of
   bad input. Budget more review time for phase 2 than feels necessary.

2. **"LLM-driven refactor" is not yet a one-shot operation.** Expect phase 4
   to be heavily guided. The skill output is a *first draft*, not finished
   code.

3. **Characterisation tests are throwaway-ish.** They pin current behaviour
   including current bugs. If the refactor intentionally fixes a bug, the
   characterisation test for that bug must be updated, not "made green".
   Easy to lose the distinction under pressure — be explicit in PRs.

4. **Multi-feature program means multi-quarter.** 14 features × 5 phases
   each with engineer review at every gate = months. Decide what "good
   enough" looks like at each gate; perfection per feature kills throughput.

5. **The Gherkin → unit-test gap is real.** Gherkin is acceptance-level;
   unit tests are finer-grained. Phase 5's skill needs to *invent* test
   targets below the Gherkin scenarios using the architecture doc as guide.
   This is the skill most likely to need iteration.

---

## Recommended next steps (in order)

| #   | Step                                                                                | Owner         | Outcome                                |
| --- | ----------------------------------------------------------------------------------- | ------------- | -------------------------------------- |
| 1   | Move this folder to AID iOS repo under e.g. `docs/refactor-pipeline/`               | Filippo       | Pipeline lives next to code            |
| 2   | Resolve open decisions A–G in this doc                                              | Filippo + Eng | Inputs locked                          |
| 3   | Link architecture doc into pipeline (decision C)                                    | Filippo       | Phase 4 unblocked                      |
| 4   | Implement `/trace-coverage` skill first (read-only, low risk)                       | Eng + LLM     | Index format proven                    |
| 5   | Implement `/spec-from-tests` skill, run on **all 14 features** in batch             | Eng + LLM     | Complete `docs/specs/` tree            |
| 6   | EM + QA review all `coverage.md` files — surface QA gaps                            | Filippo + QA  | Coverage program separate from refactor |
| 7   | Pick pilot feature (decision A); implement `/audit-implementation` skill against it | Eng + LLM     | Audit output validated                 |
| 8   | Walk pilot through phases 3 → 4 → 5 with heavy review                               | Eng + LLM     | One feature in new architecture        |
| 9   | Pilot retro: what worked, what didn't, refine skills                                | Filippo + Eng | Pipeline production-ready              |
| 10  | Roll to remaining 13 features in priority order (decision B)                        | Eng + LLM     | Migration complete                     |

Steps 4–6 are cheap, deliver value before any refactor starts (you get
documentation of the whole app even if you stop there), and don't depend
on the architecture doc.

---

## What's NOT in scope of this pipeline

Be explicit about what this *doesn't* do, so it doesn't get stretched:

- **It doesn't replace QA.** The pipeline documents what QA tests; it
  doesn't validate that the tests are correct or sufficient.
- **It doesn't generate UI tests.** Gherkin → unit tests is the contract.
  XCUITest / snapshot tests are a separate stream.
- **It doesn't refactor cross-feature concerns** (DI container, networking,
  routing). Those need to be in the architecture doc *before* phase 4 runs
  on any feature.
- **It doesn't migrate Firebase / analytics / paywall** as a stream. Those
  are external dependencies that the refactored code consumes; the
  contracts shouldn't change.

---

## Pointers

- Worked example: `demo/garden-design/`
- Pipeline phases: `workflow.md`
- Skill briefs: `skills/`
- Source Xray export: `source-data/ADIOSMAU_tests_combined_2026-05-04.json`
- Original prototype location (em-hub): `gherkin-prototype/` — can be deleted
  after this folder is moved.
