# Decision: Vlad Face AI Rebuild — Scope & Execution Plan

**Date:** 2026-03-11
**Status:** Decided — communicated to Vlad on 2026-03-11

## Context

Vlad Krudek (Software Engineer, AI-powered) is taking over Face AI as his POC project. The app shipped to the store today — scope is contained. David confirmed "Face AI rewrite" as the POC scope on 2026-03-10. The question was whether Vlad rebuilds from scratch (Option A) or modernises the existing codebase incrementally (Option B).

## Options Considered

1. **Rebuild from scratch** — Vlad creates a new app from zero, using the spec-driven workflow and Staff Engineer-provided baseline repo. Current team continues on the live app.
2. **Incremental modernisation** — Vlad takes the current codebase and improves it piece by piece alongside the current team.

## Decision

**Option 1: Rebuild from scratch.**

Reasoning:
- Aligns with the company strategy to rebuild all apps (AI replicates patterns from bad codebases — modernising perpetuates the problem)
- Produces a clean data point for David's Phase 2 narrative ("Vlad rebuilt Face AI solo in N weeks")
- Vlad already understands and bought into this approach (1-on-1, 2026-03-09)
- Staff Engineer (Sergio Durban) is providing a baseline repo with architecture rules and workflow — Vlad starts from a curated foundation, not a blank canvas

## Execution Parameters

### Scope
- Full feature parity with the store version shipping today
- No new features during the rebuild — parity first, improvements after
- Same bundle ID — rebuild ships as a future version that replaces the current app

### Current Team
- External devs stay in place and continue developing the live app
- They own bug fixes, hotfixes, and feature work until cutover
- Vlad does not take sprint work from the current backlog

### Vlad's Workload (Priority Stack)
1. **Build the app** — non-negotiable, the whole point of the POC
2. **Learn the tools** — embedded in #1 (Cursor, spec-driven workflow)
3. **Validate rules for his project** — uses Staff Engineer baseline, feeds back friction points
4. **Participate in ceremonies** — standups, refinement as observer; first thing to reduce if build velocity is threatened
5. **Shape rules for the company** — first thing to cut entirely; feed in artifacts after the build

### Rules & Architecture
- Staff Engineer provides baseline repo with architecture rules and workflow
- Vlad's role: use the baseline, validate it through real usage, feed back what's wrong or broken
- Vlad follows the baseline and logs disagreements; debrief after the build, don't deviate mid-flight
- Feedback channel to Staff Engineer needs to be defined explicitly (PRs, doc, Slack — agree upfront)

### Cutover
- Same bundle ID, future version approach
- Preserves store assets (ratings, reviews, ranking)
- Rebuild must pass QA gate before cutover — who tests (internal QA, PO acceptance) to be defined
- Old app stays available for rollback via standard App Store mechanisms

### Success Criteria
Two hypotheses being tested:

| Hypothesis | Measure | Who cares |
|---|---|---|
| **Speed** — A senior iOS dev with AI tools can rebuild an existing app significantly faster than the external team built it originally | Wall-clock time: rebuild vs original build timeline | David, Phase 2 savings narrative |
| **Model viability** — The AI-powered SE model produces production-quality, maintainable output independently | Code quality, test coverage, autonomy level, rule contribution, maintainability | Filippo, long-term scalability |

Log contributing factors during the build: tool ramp-up time, rule definition time, actual build execution time. Separate one-time costs from repeatable ones.

### Messaging to Current Team
- Lean toward transparency, framed carefully
- "Vlad is building the next-generation version. You maintain and improve the current one. Your work keeps the app running for users today."
- Exact timing and wording to be decided

### Failure Modes
| Failure | Impact | Mitigation |
|---|---|---|
| Vlad stalls/disengages | Rebuild dies. Live app unaffected. | Advisor recruitment running in parallel. Current team still in place. |
| Takes much longer than expected | Weaker headline number for David | Still useful data. First rebuild is the learning investment. Ratio to second rebuild is the real metric. |
| Quality is poor | Store rating risk at cutover | QA gate before cutover. Define who tests. |
| Current team discovers plan, disengages | Live app development slows | Manage messaging proactively. |

## Trade-offs Accepted

- Duplicating work (current team continues while Vlad rebuilds) — accepted cost
- CI/CD coordination needed (separate TestFlight track or repo) — Victor involved
- Timeline pressure is a measurement, not a promise — first rebuild is most expensive
- Vlad's product-process learning is secondary to the build if time pressure forces a choice

## What Was Communicated to Vlad (2026-03-11 Meeting)

- Rebuild Face AI from scratch — confirmed and understood
- 2–3 week timeline framed as "curiosity and wanting data," not a hard deadline
- Staff Engineer (Sergio) preparing baseline repo with rules, workflows, architecture — Vlad to use and validate
- Sergio's Friday presentation will formally introduce the spec-driven workflow
- Immediate tasks before rebuild: finish SwiftLint PR (use plan mode), get QA test account, start studying the app as a product
- Vlad grasps the spec-driven model — reframed it as "all the time for preparation, very limited time for execution"
- Backend timeline was NOT clarified — Vlad asked directly, Filippo deferred. Needs answering Friday.

## Open Items Post-Meeting

- [ ] Backend plan: iOS first, backend when? Who helps Vlad with backend?
- [ ] QA test account for Vlad to explore paywalled features
- [ ] Align with Sergio before Friday: make presentation connect to Vlad's specific task (Face AI rebuild)
- [ ] Define "done" more precisely — full feature parity with today's store version (confirm with Vlad)
- [ ] PR review model for the rebuild — who reviews Vlad's PRs? Human or AI? Specs or code?

## Review Date

- **Friday 2026-03-14:** Week 2 check-in. Short meeting (15–20 min). SwiftLint PR status, post-presentation debrief, confirm rebuild start date.
- **April 3 (SE email date):** Enough progress to justify the Phase 2 commitment?
- **End of trial (4 weeks from build start):** Full retro — what worked, what didn't, data for David

---

*Created from brainstorm session 2026-03-11. Updated after Vlad 1-on-1 same day.*
