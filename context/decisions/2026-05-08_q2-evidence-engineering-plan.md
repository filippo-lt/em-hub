# Decision: Q2 Evidence Engineering Plan

**Date:** 2026-05-08
**Status:** Active — runs through end of Q2 (June 30)
**Origin:** Weekly debrief, May 8 — surfaced that I don't yet *believe* my own portfolio narrative ("AI-native delivery pipeline lead"), and the 8-meeting H2-scope deferral with David is downstream of that disbelief.

> **Update — 2026-05-08 evening:** Vlad shipped a big Face AI refactor PR on the timeline he stated to me in the morning. Third instance of him delivering ahead of my read. The "stuck in a loop / codebase below AI-SE viability floor" diagnosis used to build several items below was vibe-driven, not observation-driven. Affected items annotated `[updated 2026-05-08 evening]` and superseded inline. The pair-first decision was protective (we didn't lock in a wrong strategy), but going forward: when my read is "Vlad stuck / Andre fine / X chaotic," check whether it's observation or impatience-projection BEFORE building strategy on it.

---

## Context

Portfolio is shifting fast:
- **Tattooist** may graduate to Growth — if so, I lose advisorship
- **AI Design** business-deprioritised — I take light-touch advisor for max 4 weeks
- **Face AI** AI-SE pilot — Vlad delivering on his stated timeline; ~~currently stuck in a refactor loop; hypothesis is codebase quality is below the AI-SE viability floor~~ *[updated 2026-05-08 evening: faulty premise — see update note above; codebase-floor hypothesis remains live for specific worst modules but not as the Face AI headline]*
- **Screen Mirroring** + **iMote iOS** — Andre transitioning to solo SE on both; externals (Sergey, Artiom) off-boarding May 31 / June 15
- **M&A** — 5 acquired apps inbound Q3; Flutter gap unresolved (replaced by sunset-or-rewrite-native bet, pending triage data)

There are two narratives competing for the same facts:
- **A:** "I'm losing apps and gaining chaos."
- **B:** "I'm becoming the company's AI-native delivery pipeline; Phase 2 is generating real findings."

I can pitch B only if I believe it, and I'll only believe it if the next 4–8 weeks deliver visible evidence. So the work isn't *writing* the story — it's *engineering the evidence points* that make the story true.

---

## Week 1 — by Fri May 15

| # | Item | Owner | Trigger |
|---|---|---|---|
| 1 | 90-min pair session with Vlad — **reframed** [updated 2026-05-08 evening]: not "diagnose if stuck," but "you're delivering AI-SE faster than I read it — show me how." Practitioner-to-learner posture. | Filippo | By Tue May 12 |
| 2 | Face AI 1.2.0 ships to App Store | Vlad | Mon May 11 target |
| 3 | ~~Vlad's new strategy chosen (A vs B)~~ **[shelved 2026-05-08 evening]** — current strategy is delivering. Don't pick a different one. Re-evaluate only on real signal, not impatience. | — | — |
| 4 | ~~Half-page codebase-floor finding doc~~ **[on hold 2026-05-08 evening]** — hypothesis remains live for specific worst modules (e.g. image-adjust per Vlad May 4) but is no longer the headline. Don't write doc pre-pair; revisit if pair surfaces evidence. | — | — |
| 4a | Contract reset with Vlad (experiment-to-find-boundaries vs. takeover-via-refactor) — independent of PR update, still owed | Filippo | Next 1:1 |
| 5 | Andre 1:1: open with capacity question; acknowledge release notes work; verify Codex in conversation | Filippo | Next 1:1 |
| 6 | Andre developmental feedback delivered via new mechanism (written OR dedicated 30-min off the 1:1) | Filippo | EoW May 15 — *not* deferred to next prep doc |
| 7 | AI Design light-advisor end-date written in calendar (max 4 weeks) | Filippo | Mon |
| 8 | Hiring interviews completed | Filippo | Per schedule |
| 9 | H2 scope surfaced with David — frame as partnership, not pitch | Filippo | Next David 1:1 |
| 10 | AI tokens — clarify the ask vs. the escalation before David 1:1 | Filippo | Pre-1:1 |

## Weeks 2–4 — by Sat May 31

| # | Item | Owner |
|---|---|---|
| 11 | Sergey off-boards Screen Mirroring cleanly | Andre + Filippo |
| 12 | Andre runs solo on SM for first 2 weeks — capacity check repeats | Filippo |
| 13 | Vlad delivers next named milestone on Face AI (continuation of current strategy that just shipped a refactor PR) **[updated 2026-05-08 evening]** | Vlad |
| 14 | ~~Codebase-floor finding 1-pager~~ **[on hold 2026-05-08 evening]** — write a finding only if pair session + further data surface a real boundary worth naming | — |
| 15 | If Tattooist moves to Growth: pre-frame as "advisorship worked" in David 1:1 *before* it happens | Filippo |
| 16 | Hiring offer extended (if Week 1 interviews land) | Filippo |

## Weeks 5–6 — by Mon June 15

| # | Item | Owner |
|---|---|---|
| 17 | Artiom off-boards iMote iOS | Andre + Filippo |
| 18 | Andre executes the 10-day handover window from Artiom | Andre |
| 19 | App assignments doc presented to David — 3 weeks overdue as of today | Filippo |
| 20 | Phase 2 finding shared with David formally (1-pager) — **[updated 2026-05-08 evening]** content TBD; "codebase-floor" was the working hypothesis but the actual finding may be different (e.g. AI-SE viability across legacy *given competent operator*, cross-platform validation gaps, etc.) | Filippo |
| 21 | Component library: at least 1 named output | Filippo |

## Weeks 7–8 — by Tue June 30

| # | Item | Owner |
|---|---|---|
| 22 | KR1 check: external HC -20% (Sergey + Artiom + AI Design dev = on track) | Filippo |
| 23 | AI-SE pilot has shipped Face AI 1.2.0 + at least one further refactor/feature milestone (refactor PR landed May 8 evening already counts toward this) **[updated 2026-05-08 evening]** | Vlad |
| 24 | Andre has shipped under SE on at least one app | Andre |
| 25 | H2 scope locked with David | Filippo + David |

---

## What kills the plan

| Risk | Trigger | Pre-committed action |
|---|---|---|
| Face AI 1.2.0 slips past May 15 | Vlad reports blocker | Cancel "new strategy" decision; first deal with the ship |
| Vlad pair reveals workflow gap | Pair shows fundamental AI-SE skill gap | Bring in Sergio Durban or Andrey for 2nd pair; reset timeline. **[Note 2026-05-08 evening: low-probability now — Vlad is delivering, not stuck. Pair is now learning posture, not diagnostic.]** |
| Filippo's impatience produces a wrong read on Vlad / Andre / M&A | Internal "stuck / chaotic / not progressing" feeling without observation | Pause before strategy work. Ask: what did the person actually communicate? When? Have I given the stated timeline a chance to play out? |
| Andre's capacity returns "I'm drowning" | He says or signals it | iMote iOS handover compresses; Filippo eats the gap personally for 2 weeks |
| Hiring doesn't land | Offer not extended by May 31 | AI Design light-advisor extends formally; renegotiate with David |
| AI tokens crisis worsens | Devs can't function on Sonnet-tier | Hard escalation to David — this is a Phase 2 blocker, not a tooling complaint |
| Tattooist exits without pre-frame | Sergio Hueso announces the move first | Recover with "I'd been planning to talk to you about this" — own the late framing |

---

## Self-discipline tracking (weekly review)

These are *my* failure modes, not project risks. Track them in weekly debrief:

- Talk-ratio in strategy sections with Vlad (3 sessions Filippo-heavy)
- Carry-overs led with at top of 1:1s (5 sessions skipped)
- Developmental feedback to Andre (5 sessions deferred)
- "Don't worry" count in Vlad's 1:1 (4x in 30 sec last session)
- H2 scope asked of David (8 deferrals)
- App assignments doc presented (3 weeks overdue)
- **Impatience-projection check [added 2026-05-08 evening]:** when I say someone is "stuck," "not progressing," or "chaotic," what did they actually communicate to me, and have I given the stated timeline a chance to play out? Vlad over-delivery count: 3.

---

## Review cadence

- **Weekly:** Friday debrief — check Week 1 items off; surface drift on self-discipline tracking
- **End of May:** halftime check — are evidence points landing? If not, what's the explicit reframe?
- **End of Q2:** decide whether Narrative B is true (pitchable to David and beyond) or whether the realistic frame is something different

## Decision

This plan is the operational layer beneath the Q2 OKRs. It exists because narrative belief is downstream of delivery, not upstream. Stop trying to write the story; engineer the evidence.
