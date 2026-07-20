# Brag Doc — Filippo

**Last updated:** 2026-07-06
**Current period:** 2026 H1

> Cadence: 5–10 min every Friday. Monthly roll-up on the last Friday. Quarterly close = pre-built self-review input.
> Rule: outcomes over tasks. If you can't say what changed, don't write it down.

---

## Period highlights
- Q2 OKR architecture in place: 3 objectives, 11 KRs, mapped to EBITDA / predictability / AI transformation.
- Built em-hub: a structured manager OS (skills, agents, weekly self-debrief loop). Compounding leverage tool.
- Caught a near-miss developmental feedback to Vlad that observation showed was objectively wrong. Judgment > reflex.

---

## Shipped — team outcomes I drove

- **2026-05-20 — MartechKit v1.0 (iOS) shipped — portfolio-wide martech unification** — Role: framed, sponsored, and announced to product + engineering + C-levels. What shipped: single iOS library unifying Amplitude, RevenueCat, AppsFlyer and other martech vendors; validated in 3 pilot apps; built end-to-end by Victor Yalenkas. Why it matters: historically our slowest portfolio-wide workflow (per-app tickets for every martech change) collapses to a version bump — directly hits the Q2 OKR deliverable for MartechKit and unlocks parallel Android/Flutter tracks. Evidence: `context/communications/2026-05-20-martechkit-v1-announcement.md`.

- **2026-04-09 — Q2 2026 OKRs locked across the org** — Role: framed and decided. 3 objectives (EBITDA via efficiency, Launches predictability, AI transformation), 11 KRs, each tied to a measurable cut-line (20% external HC reduction, 6→4d cycle time, ≥75% on-time delivery, Parapet/AI Observability/TVFoundationKit/MartechKit shipped). Evidence: `context/okrs-q2-2026.md`.

---

## People & leverage

- **2026-05-08 — Near-miss on Vlad feedback** — Context: I was holding "be more proactive" feedback to deliver. Action: ran a `/analyse` debrief, then checked the actual delivery record. Outcome: Vlad had shipped a major refactor on the timeline he stated — third time he'd delivered ahead of my read. Recognised the feedback would have been objectively wrong; root cause was my impatience under low-trust, not his behaviour. Held it. Evidence: `context/memory/self/2026-05-08_vlad-pr-update_memory.md`.

- **2026-07-03 — Broke the retreat-to-coding pattern by delegating instead of absorbing** — Context: was slipping back into IC work (coding + jumping onto the TraceCheck UI) as apps closed and manager scope felt ambiguous. Action: negotiated a clean-state sprint for FaceAI then parking, and delegated the *entire* backend/AI-generation investigation to Vlad with a report deliverable — ran only the high-level Langfuse pass myself to frame it, then handed the rest. Outcome: Vlad engaged, got hands into backend, and volunteered web-dev interest (new growth signal). Named the underlying pattern (avoidance-via-competence — same shape as built-but-not-presented) so it's catchable next time. Evidence: `context/memory/self/2026-07-03_em-disconnect-brainstorm_memory.md`.

---

## Process & systems

- **2026-05-08 — Em-hub manager OS in active use** — Before: 1-on-1 notes scattered, decisions un-recorded, self-patterns invisible across weeks. After: per-person context folders, weekly `/analyse` debrief, self-memory accumulating, skills routable via slash commands. Why it sticks: it's the system I actually use, not a system I designed and abandoned. First compounding evidence: cross-week patterns now caught in days, not quarters (Vlad-impatience read, M&A vague-placeholder loop).

- **2026-07-03 — Designed the MartechKit platform operating model + M&A transition-readiness checklist** — Before: MTSDK board had 5 epics/13 tasks all at Minor/unranked, no cadence, and visibility depended on me pinging Victor (who reports to Matellano, not me). After: a ranked P0/P1/P2 backlog, WIP-limited columns with auto stale-flags, and a 15-min weekly folded into the Victor 1:1 — visibility comes from the artifact, not shadow-management. Also built a reusable transition-readiness checklist across all six M&A apps (keep/park/wind-down), surfacing the real exit risk: committed secrets (ChatUltra Firebase keys, PDF hardcoded keys) that must be rotated before the studios lose access end-July. Designed and being stood up (build-to-completion discipline). Evidence: `context/martech-sdk/board-operating-model.md`, `m-and-a/transition-readiness-checklist.md`.

---

## Strategy & influence

- **2026-05-08 — Reframed Tattooist graduation as success, not loss** — Stakes: app likely moving from my org to Growth; my reflex read it as "I'm gonna lose it" (Narrative A — empire). Position I took: "advisorship worked, app graduated — that's the job" (Narrative B — AI-native delivery). Where it landed: pre-frame the exit before someone else describes it first; treat graduation as a portfolio proof point for the H2 scope conversation with David.

- **2026-05-08 — Inverted my approach to the H2 narrative** — Stakes: I'd deferred the H2 scope conversation with David 8 times because I didn't believe Narrative B (AI-native delivery pipeline). Position I took: belief in a strategic narrative is *downstream* of delivery, not upstream — stop trying to write the story, engineer the evidence points that make it true. Where it landed: decoupled "surface H2 scope as a partnership question" from "pitch Narrative B" — the former doesn't require the latter to be true yet. Removes the deferral block.

- **2026-06-07 — Reframed an unfunded M&A mandate into a zero-resource governance model** — Stakes: David asked me to "establish control" over the 5 M&A apps but wouldn't fund the takeover (≈1 month of delayed ChatUltra externals) — a textbook responsibility-without-authority trap. Position I took: separated *control* (visibility, gates, decision rhythm — deliverable now, zero new resources) from *takeover* (funded execution, gated on business case + resourcing). Where it landed: a full operating model where governance alone shrinks the portfolio 5→3 (two sunsets, one business-case gate), the resource ask flips from expensive-and-denied (externals) to cheap-and-unrefusable (logins/data), and a 3-tier QA strategy mandates quality without fighting the "studios are independent" politics. Designed and saved; deliberately holding presentation to David until it's set up and running (build-to-completion discipline). Evidence: `context/ma-governance-operating-model.md`.

- **2026-06-22 — Ran a privileged-information alignment without leaking the cut, and got full strategic buy-in anyway** — Stakes: Matellano signalled a Q3 scope cut (8 apps → 2: AI Design + TruthSeeker web; sunset the M&A studios) before Sergio's manager (Kristian) had briefed him. Sharing the magnitude myself would have front-run Kristian, put Sergio in an awkward spot, and made me the owner of a decision that isn't mine. Position I took: don't reveal the cut — reach the same destination (concentration) through engineering logic I'm allowed to own (finite capacity, externals underperforming, one-team-per-app unsustainable), then let Sergio rank priorities himself. Where it landed: held the cut through multiple natural openings, and Sergio self-corrected live from "launch everything as soon as ready" to "we need to prioritize or we're not arriving anywhere." Came out with his full Q3 launch calendar, ChatUltra clarified (live/operational, not killed), a co-designed "dedicated launches team + budget" resourcing vehicle to pitch upward, and the coalition intact — all without spending Kristian's news. Best-executed 1:1 in the series; clean reversal of prior-meeting passivity. Evidence: `people/sergio-hueso/transcripts/2026-06-22_analysis.md`.

- **2026-06-29 — Drove the Q3 Launches+M&A studio-exit plan and claimed ownership of it** — Stakes: leadership aligned (David, Sergio, Kristian/CPMO) to exit both external studios (Helikanon + TurboCat) by end of July and concentrate on AI Design / Truth Seeker / ChatUltra — a takeover-grade execution against a control-era resource base. Two of my recurring patterns (built-but-not-presented; fold-on-resource / "out of my hands") were the live risks. What I did: brought the roadmap visual into the Sergio sync and drove a nine-app realignment off it (broke built-but-not-presented), then claimed clear ownership in the leadership channel — "I'll drive the TurboCat + Helikanon offboarding with Procurement, and I have a proposal for the new ChatUltra team I'll discuss with David." Reduced the whole plan to one critical path (ChatUltra replacement Flutter team) and put hiring in motion. Where it landed: procurement ownership now on record across David + Kristian; per-app dispositions decided; authorship of the team structure planted against David's "we'll analyze it next week" drift. Evidence: `context/decisions/2026-06-29_q3-studio-exit-team-structure.md`, `context/communications/2026-06-27_q3-launches-ma-plan-combined.svg`.

- **2026-07-06 — Converted the Martech dotted-line into an owned EM mandate, in the room** — Stakes: MartechKit had stalled (backlog open since April, Android PR stuck 3 weeks, video-app blocked on a Victor feature since early June) with visibility depending on me pinging Victor, who reports to Matellano, not me. My recurring risk here is fold-on-resource / accept-and-receive. What I did: rather than passively receiving David's "maybe move Victor to you" float, I claimed the mandate outright — "get me on top of it, officially the EM on Martech" — and backed it with a concrete mechanism (ranked Jira board, twice-weekly standups from tomorrow, Vlad added to clear the backlog once Sat AI frees him) plus a roadmap deliverable for next week (features track + app-integration track). Where it landed: David endorsed me as the official Martech EM and attached a daily Victor cadence behind it; the line-management transfer (Victor: David→me) is on the table for end-of-month, contingent on the cadence working — proposed, not yet decided. First clear shaping move in several 1:1s — the offensive version of the delegation muscle. Evidence: `people/david-manager/transcripts/2026-07-06_analysis.md`, `context/memory/self/2026-07-06_david-1on1_memory.md`.

---

## Growth & learning

- **2026-05-08 — Named the "vague verbal placeholder" pattern in my own decision-making** — Trigger: noticed "live with it," "stuck in a loop," "make it work," "few more weeks" all functioning as fake decisions across M&A Flutter, Vlad pilot, Phase 2. Shift: every time I catch this phrasing in my own mouth, force the concrete shape (which strategy? what date? what's the trigger?). Test it survived: applied successfully in the same debrief to M&A April-1 conditions — exposed the load-without-the-deal pattern that had been silent for 4 weeks.

---

## Recognition

-

---

## Stretch / didn't land

-
