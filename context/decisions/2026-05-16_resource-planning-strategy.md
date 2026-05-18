# Resource Planning Strategy — 6-Week Operational Plan

**Date:** 2026-05-16
**Status:** Active — runs through end of Q2 (June 30)
**Origin:** Weekly dump brainstorm, May 16. Consolidates portfolio decisions surfaced from the May 13 framework + the Tattooist/iMote portfolio shifts + Vlad pair-session findings (May 14).
**Relation to other plans:** Operational layer beneath the Q2 OKRs. Cross-references the Q2 Evidence Engineering Plan (2026-05-08). Items in this plan supersede equivalent items there only where explicitly noted.

---

## Context

Three pressures converging:

1. Manager pushing externals removal by year-end
2. Internal team at capacity (Andrey solo SE on two apps incoming; Vlad already 40/40/20 on Face AI)
3. Product side cannot supply reliable roadmap or app-investment signal — engineering must own the goalkeeper role (per David, May 12: *"we own this, not product"*)

The portfolio framework (`context/app-portfolio-framework.md`, May 13) is the instrument. This plan is the deployment.

**Two new findings since May 13:**

- **40/40/20 (pair session, May 14)** — Vlad on Face AI: 40% PO/QA info gathering, 40% bad-codebase friction, 20% feature production. First measured Phase 2 evidence point. Confirms the SE = rewrite rule with data, not principle.
- **Discovery cost** — "SE on app" is not rewrite; it's discovery + rewrite. Product context cannot be trusted to come from PMs. Discovery is SE-driven and adds ~2 weeks per app before rewrite can begin. Both AI-SE viability indicators (codebase quality + product context recoverability) belong in the framework Health column.

---

## Portfolio after Tattooist + iMote moves

| App | State | SE owner | Rewrite needed? |
|---|---|---|---|
| Screen Mirroring | Existing iOS native | Andrey | No (already native) |
| Face AI | Existing iOS native | Vlad | Partial (in progress) |
| AI Design | Existing iOS native, kill-trigger watch | Vlad (advisor) | Default: kill Sep 30. Rewrite only if CAC clears trigger AND Vlad takes slot. |
| Chatbot | M&A, Flutter, P1, Helikanon | New hire (rewrite #2) | Yes |
| PDF Editor | M&A, Flutter, P2, TurboCat | New hire (rewrite #1) | Yes |
| Step Counter | M&A, Android native, P2, Helikanon | TBD post-Q3 | Edge case (already native) |
| Truth Seeker | M&A, Flutter, P3, Helikanon | **Sunset candidate** | Pre-launch, Apple-blocked — easier kill than rewrite |
| Music Player | M&A, Android native, P3, Helikanon | **Sunset candidate** | Already named sunset candidate (m-and-a-status, May 8) |

Net 6 apps after both sunsets. Math against 3 SEs × 2 slots = 6 slots → "externals out by year-end" becomes achievable, conditional on:
- iMote actually moves to Català end Q3 (not confirmed — surface as dependency)
- AI Design kill trigger fires Sep 30 *or* Vlad rewrites it as his slot
- Music Player + Truth Seeker sunset by Q3

---

## Anchors

| Anchor | Date | Why it matters |
|---|---|---|
| Next David 1:1 | Tue May 19 | Framework presentation + AI Design tier sign-off + Tattooist re-frame + hire pre-offer alignment |
| Sergey off-boards Screen Mirroring | Sat May 31 | Andrey solo on SM |
| Tattooist transitions to Growth | ~Jun 13 (4 weeks from today) | Closes the advisorship bet — pre-frame opportunity expires |
| Artiom off-boards iMote iOS | ~Jun 15 | Andrey solo on iMote until Q3 handover to Català |
| End Q2 | Jun 30 | KR1 (external HC -20%) closes — framework must be operating, not designed |
| AI Design kill trigger evaluation | Sep 30 | First hard test of the framework |

---

## What the next 6 weeks must close

By Jun 28, these are *decided and visible*, not "in progress":

1. App Portfolio Framework v1 — accepted by David, operating monthly
2. AI Design — tier signed off in writing, Sep 30 kill trigger co-signed
3. Hire — offer extended, scoped against PDF Editor as first rewrite (discovery + rewrite)
4. Truth Seeker + Music Player — formal sunset decisions captured
5. Andrey — written capacity contract for solo-SE-on-two-apps period
6. FaceAI — Ruben + Vlad + Herardo running 4-week roadmap commitment
7. Tattooist — narrative locked as "advisorship worked" upward
8. iMote → Català end Q3 — dependency confirmed or contingency named
9. 40/40/20 Phase 2 finding — surfaced as one-pager to David

---

## Week 1 — May 18–24

| # | Item | Owner | Trigger / by |
|---|---|---|---|
| 1 | **Tattooist pre-frame delivered** — first 5 min of David 1:1, "advisorship worked" line | Filippo | Tue May 19 |
| 2 | **Framework presented to David** — full doc + AI Design scorecard (marketing-spend gap named if not received) | Filippo | Tue May 19 |
| 3 | **AI Design tier locked**: Wind-down, Sep 30 kill trigger, externals run to end Q3 — David signs off in 1:1 | Filippo + David | Tue May 19 |
| 4 | **Pre-offer alignment** — hire anchored to PDF Editor first, Chatbot second; SE = discovery + rewrite named explicitly | Filippo + David | Tue May 19 |
| 5 | **iMote → Català dependency surfaced explicitly** with David — confirm or name contingency | Filippo | Tue May 19 |
| 6 | **Andrey capacity contract drafted** — written, one page, what he owns / what triggers renegotiation; absorbs the deferred developmental feedback | Filippo | Sent to Andrey by Fri May 22 |
| 7 | Vlad pair session (May 14) | ✅ **Done.** Finding: **40% PO/QA, 40% bad codebase, 20% feature production.** Lead with this in framework presentation as Phase 2 evidence. | Filippo |
| 8 | **Sergio Wetzel conversation** (AI Design PM) — communicate Sep 30 kill trigger *after* David signs off | Filippo | By Fri May 22 |
| 9 | FaceAI: Ruben onboarded; Vlad + Ruben + Herardo briefed to produce a 4-week committed plan | Filippo | By Fri May 22 |
| 9b | **Marketing spend chase** — last push to AI Design PM; if not received, present scorecard with gap visible, use as the lever for David's PM air-cover ask | Filippo | By Mon May 18 |

**Decision points this week:** AI Design tier. Hire's first rewrite target. Framework v1 sign-off.

---

## Week 2 — May 25–31

| # | Item | Owner | Trigger / by |
|---|---|---|---|
| 10 | **FaceAI 4-week committed roadmap delivered** by Vlad + Ruben + Herardo | Vlad + Ruben + Herardo | Fri May 29 |
| 11 | **Sergey off-boards Screen Mirroring cleanly** | Andrey + Filippo | Sat May 31 |
| 12 | Andrey capacity contract — signed back / discussed in 1:1 | Andrey + Filippo | Mon 1:1 |
| 13 | Truth Seeker + Music Player — **sunset case drafted** (data + recommendation) | Filippo | Fri May 29 |
| 14 | **Face AI scorecard** populated in framework | Filippo | Fri May 29 |
| 15 | Hire — interviews complete, offer prepared | Filippo | Per recruiting schedule |
| 16 | **Phase 2 1-pager drafted** — "40/40/20: codebase quality + product context are binding constraints on AI-SE viability" | Filippo | Fri May 29 |

**Decision points this week:** Truth Seeker + Music Player sunset proposals to David in May 26 1:1.

---

## Week 3 — Jun 1–7

| # | Item | Owner | Trigger / by |
|---|---|---|---|
| 17 | **Truth Seeker + Music Player sunset decisions co-signed** by David | Filippo + David | Tue Jun 2 1:1 |
| 18 | Andrey solo on Screen Mirroring — Week 1 capacity check (1:1 question) | Filippo | Mon 1:1 |
| 19 | **Hire — offer extended** | Filippo | EoW Jun 5 |
| 20 | **AI Design scorecard** updated with first month of marketing/MRR data from Sergio | Filippo | Fri Jun 5 |
| 21 | M&A scorecards (Chatbot, PDF Editor) draft populated — depends on Christian/Sergio Wetzel/Listen conversations landing | Filippo | Fri Jun 5 |
| 22 | Vlad + AI Design: 1–1.5 hr/day cap holding? | Filippo | Mon 1:1 |
| 23 | **Phase 2 1-pager delivered** to David | Filippo | Tue Jun 2 1:1 |

---

## Week 4 — Jun 8–14

| # | Item | Owner | Trigger / by |
|---|---|---|---|
| 24 | **Tattooist transitions to Growth** — bet closes, captured in framework | Filippo | ~Jun 13 |
| 25 | **Hire accepts** — onboarding plan finalized: **Weeks 1–2 = discovery + 1-pager on PDF Editor (gate to rewrite start); Weeks 3–14 = rewrite. Vlad part-time advisor for discovery phase.** | Filippo | EoW Jun 12 |
| 26 | Andrey solo on SM Week 2 — capacity re-check | Filippo | Mon 1:1 |
| 27 | First **monthly portfolio review** with David — framework operating as live tool, not document | Filippo + David | Tue Jun 9 1:1 |
| 28 | M&A: Chatbot + PDF Editor scorecards — first review with David | Filippo | Tue Jun 9 1:1 |
| 29 | FaceAI — 4-week roadmap halfway check; PM/PO comms cadence sustained? | Filippo + Ruben | Fri Jun 12 |

**Decision points this week:** First operational portfolio review. This is when "framework as live tool" gets evidence.

---

## Week 5 — Jun 15–21

| # | Item | Owner | Trigger / by |
|---|---|---|---|
| 30 | **Artiom off-boards iMote iOS** | Andrey + Filippo | ~Jun 15 |
| 31 | Andrey executes Artiom handover window | Andrey | Through Jun 22 |
| 32 | **Hire start date confirmed / onboarding begins** | Filippo + new hire | Per offer |
| 33 | iMote → Català handover plan drafted (assuming confirmed in Week 1) | Filippo + Català | Fri Jun 19 |
| 34 | Screen Mirroring + iMote scorecards populated | Filippo | Fri Jun 19 |

---

## Week 6 — Jun 22–28

| # | Item | Owner | Trigger / by |
|---|---|---|---|
| 35 | **Q2 portfolio review** with David — full 6-app picture | Filippo + David | Tue Jun 23 1:1 |
| 36 | KR1 check (external HC -20%): Sergey + Artiom + AI Design externals → on track / behind / off | Filippo | Tue Jun 23 |
| 37 | Q3 plan articulated — H2 scope question with David surfaced as partnership question (per May 8 self-memory) | Filippo + David | Tue Jun 23 |
| 38 | AI Design Sep 30 kill trigger — re-confirmed publicly with Sergio Wetzel + David in writing | Filippo | Fri Jun 26 |
| 39 | Onboarding plan for new hire's PDF Editor rewrite finalized — **discovery 1-pager is the gate to rewrite start; if discovery can't produce it, that's data — escalate, don't push through** | Filippo + Vlad | Fri Jun 26 |
| 40 | Andrey developmental feedback — fully delivered via written channel (Q2 plan item, sixth-deferral compounding) | Filippo | Fri Jun 26 |

**Decision points this week:** Q3 plan locked. H2 scope partnership question deployed.

---

## What kills the plan

| Risk | Trigger | Pre-committed action |
|---|---|---|
| David doesn't sign off on framework Week 1 | Pushback on structure | Salvage AI Design tier sign-off + return with revised framework Week 2; do not let it become an indefinite re-draft |
| iMote → Català falls through | David says it's not happening | Math reverts: 6 slots / 8 apps. Find a 2nd sunset (likely Step Counter or Truth Seeker accelerated) |
| Hire offer falls through | Candidate declines | AI Design externals extend; renegotiate "no externals by year-end" with David — explicit, not silent |
| Vlad's AI Design advisor cap drifts above 1.5 hr/day | Vlad raises hand or it shows in delivery | Pull him out of AI Design advisor role; externals run pure to Sep 30 |
| Andrey signals capacity issue | His words or visible miss | iMote handover compresses or Filippo eats gap personally for 2 weeks |
| FaceAI 4-week roadmap doesn't materialize from Ruben/Herardo | No plan by May 29 | Filippo brokers it directly — Vlad has flagged he can drive it if needed |
| Marketing-spend data doesn't arrive | Not received by Mon May 18 | Present scorecard with the gap visible — gap is itself the lever for the air-cover ask |
| Discovery 1-pager doesn't materialize for first rewrite | Hire can't produce it after 2 weeks | App is not rewrite-viable. Escalate as portfolio data, don't push through |
| Filippo defers presenting framework "to gather more data" | Internal "not ready yet" signal | Read this plan. Items 2 + 3 are not optional. Present anyway. |

---

## Self-discipline tracking (continues from Q2 Evidence Engineering Plan)

- Framework presented (deadline: Tue May 19) — was the AI Design scorecard fully populated, or did it slip to structure-only?
- Tattooist pre-frame delivered in first 5 min — yes/no
- Talk ratio in 1:1s (Vlad and Andrey): one-sentence-then-pause card on desk
- Carry-overs led with: paper card mechanism
- Andrey developmental feedback: written channel locked
- Each new portfolio ask from David: name the trade-off in the moment (no silent absorption)
- Marketing-spend gap converted to air-cover ask (not absorbed silently)

---

## What's NOT in this plan (parking lot, revisit Q3)

- Replicating Vlad-advisor model on Helikanon M&A apps — too early; depends on framework operating
- Andrey rewrite-rule question (do SM/iMote count as rewrite or takeover?) — applies post-Q3, decide at Q3 boundary
- Codex per-developer cost visibility — David's ask; in flight, not blocking this plan
- Carve-out service migration list — David's recurring ask; partial > nothing — bring whatever's ready in Q3 planning
- AI Gateway investment — David accepted technical objection, parked pending Tiago

---

## End-of-6-weeks success picture

If this works, on Jun 28 you walk into the weekly debrief and write:

> *"6 apps, 3 SEs, framework is operating monthly, Sep 30 AI Design kill trigger is co-signed and public, the hire is starting on PDF Editor with a discovery 1-pager as the gate, FaceAI roadmap problems are running through Vlad/Ruben/Herardo not me, and Andrey's capacity contract is signed. 40/40/20 finding is on the table as Phase 2 evidence. No new resource decisions made under pressure this week."*

That's the artifact's success criterion.
