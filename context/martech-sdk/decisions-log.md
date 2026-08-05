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

## 2026-07-28 — Audit fallout

Context: three independent audits of MartechKit v2.0.1 (Vlad's `QUALITY_AUDIT_REPORT.md`, my
8-agent `AUDIT_CLAUDE.md`, and a third `QUALITY_AUDIT_VALIDATION_REPORT.md`). Seven Tier-1
blockers — crash or silent attribution data loss. Five of seven independently confirmed by 2+
audits. Four absent from the original report.

### D6 — Adoption freeze, with a version as the gate
- **New integrations are paused.** Both independent validators recommended this on their own, so it is a technical recommendation, not my judgment call.
- **Existing consumers are NOT rolled back.** They are audited against five known exposure patterns: TikTok usage, configuration started in an unstructured `Task`, events emitted before configuration completes, direct Amplitude/AppsFlyer identity mutation, RevenueCat identity changes after bootstrap.
- **Re-opens on a version, not a date: `v2.1.0` = adoption-grade.** Everything before it is pilot-grade.
- Gate contents: M0 (CI can go red), M1 (guide compiles, verified in CI), M2 (no crash on the launch path), M3 (TikTok initialises) + the verification suite green on AI Design, both platforms.
- Supersedes the implied "integrate everywhere" posture of the Q3 roadmap's priority #1 until the gate is met.

### D7 — `MARTECHKIT-FINDINGS-MERGED.md` is the system of record; A1 does not circulate
- The merged register (union of all three audits, deduped, re-cited against `main` @ `691ebfb`) supersedes all three source documents for decision-making.
- **The original report is not circulated.** Two independent reviewers found the same defect in it: it claims verification against v2.0.0 while citing files that exist only on an unmerged branch. Five of its nine claims were rejected or downgraded by consensus (folder structure, "effectively untestable", enums for every string, "AI-generated" docs, over-exposed hooks) — those are the threads that would be pulled to discredit the whole audit.
- My own audit missed the TikTok defect, the macOS platform lie, and half the identity finding. **No single report is complete or fully accurate; the union is.** This is also what makes the register nobody's personal report.

### D8 — Stop auditing; verify in production instead
- Three audits is enough. A fourth adds detection at the margin and starts to read as case-building rather than repair.
- Remaining uncertainty is empirical, not analytical. Five cheap checks:
  - TikTok event volume — predicted **zero, ever** (M3). ~10 minutes, definitive.
  - `session_start` / `session_end` in Amplitude — predicted **absent entirely** (M8, `autocapture: []` hardcoded).
  - NULL `customer_user_id` rate in AppsFlyer — the exact VideoUp alert (M6).
  - ATT prompt-shown count vs installs — a permanently unprompted cohort (M4).
  - Has any CI run ever gone red on a *test* failure? (M0).

### D9 — Settle CI before any remediation
- **M0: CI's gates may never go red.** All seven `codemagic.yaml` steps pipe `xcodebuild` through `xcsift` with no `set -o pipefail`, so the step's exit status may be the formatter's. ~1 hour to settle.
- Nothing downstream is verifiable until this returns — including every fix scheduled after it.

### D10 — Work split across Victor's leave (29 Jul – 18 Aug)
- **Vlad (3 weeks, not the cleanup crew):** CI that can fail; integration-guide snippets compiled in CI; merge `MTSDK-10-integration-confidence-pt1` (already contains the test-serialisation fix — do not redo); fix the mocks so the identity tests *can* fail; convert Tier 1 into failing tests; TikTok fix.
- **Victor on return:** the bootstrap state machine — `unconfigured → configuring(shared task) → ready | failed`, published before the first suspension, concurrent callers awaiting the same task. Closes three of the seven Tier-1 items at once.

### OPEN — ownership of `rosseca/martech-guidelines`
- ~40% of the public event API is generated by a Python generator in a repository this team does not own. Several findings (hardcoded Amplitude config, the `allowed_values` enum fix, the schema contradictions, the dead `EventComponents`/`UserProperties` symbols) are **not fixable from martech-kit**.
- Owning MartechKit means owning `martech-guidelines` too. **Ask for Matellano / David Sanchez — not a Victor task.** Target: settle before Victor's leave.

### OPEN — branch hygiene
- 16 unmerged branches; **four implement the same feature by three different authors** (Amplitude V2 identifiers → AppsFlyer customData). Process finding, not a code finding.

---
