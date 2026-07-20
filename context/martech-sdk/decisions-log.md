# Martech SDK — Decisions Log

Confirmed decisions from the Q3 strategy brainstorm. Append-only; date each entry.

---

## 2026-06-25

### D1 — Vlad onboards via AI Design, then supports Victor
- Vlad integrates MartechKit into **AI Design (iOS + Android)** to get acquainted with the library.
- After ramping, he moves to **helping Victor push the platform forward** (~25% capacity).
- Rationale: AI Design is his own app (solo/async — fits his constraint), now an **Invest** app so the integration has real value, and it doubles as a fresh test of the integration guide + CI gate.
- Follow-ups: confirm Android integration scope; check time trade-off vs his Face AI / AI-SE evidence plan.

### D2 — Roadmap moves to a Jira board
- The roadmap (#38) is long and messy; it needs a proper home for **priorities + progress**.
- A **Jira board** will be the system of record for what we're building and in what order.
- Open (not yet decided): dedicated Eng-owned project (recommended, e.g. `MTK`) vs epics inside an existing project. Where it lives signals who owns the platform.
- Follow-ups: project creation needs Jira admin; draft epics/stories from #38 when ready.

### D3 — Separate adoption Dashboard (NOT Jira)
- A **Dashboard** shows **integration/adoption progress** — which app, which platform, which version, adopted y/n.
- Explicitly distinct from Jira: Jira = work-in-flight/intent; Dashboard = state-of-the-world/reality.
- Serves both David (visibility) and Martech (migration tracker, #38 item 9).
- Follow-ups: decide lightweight tracker (auto-parsed from repos) vs built platform.

### D5 — Engineering Dashboard: start v0, grow on top, resource v2+ separately
- The Dashboard grows into a **full Engineering Dashboard** (state of all apps/projects: what's integrated + how it performs), **editable by all EMs** — explicitly the **App Portfolio Framework made live**.
- **Design principle:** every column is either *auto-sourced* (systems, stays fresh) or *human-entered* (EM/PM, needs an owner). Maximise auto-sourced; make only genuinely EM-owned fields editable.
- **Build ladder:** v0 integration matrix (MartechKit/Parapet/Pipelins, parsed from repos) → v1 auto perf/cost (Datadog, `/metrics`, `/gcp-spend`) → v2 EM-editable multi-tenant layer → v3 real service.
- **Resourcing guardrail:** v0–v1 ride along with SDK work; **v2+ must be a separately resourced, named initiative pitched to David — NOT on Victor.** Don't let the dashboard eat the SDK.
- Index existing BI (Datadog/Tableau/Jira), don't rebuild it. Ship v0 as the wedge.

### D4 — Data/observability layer: Martech owns, built jointly
- The data/API layer behind gate #6 (NULL-rate alert) and the active contract verifier — RevenueCat + AppsFlyer + Amplitude API access — **should ideally be owned by Martech** (they hold the keys/data).
- But this is explicitly a **collaboration opportunity**: a place where Eng + Martech build something together rather than over a handoff. Strengthens the partnership and gives a "shared win" narrative.
- Direction: Eng provides the verifier/tooling design + the contract definition; Martech owns the data access + alerting home. Co-built.
- Follow-up: raise as a joint initiative with Miguel / david-leadtech; name it in the David pitch as Eng↔Martech collaboration.

---
