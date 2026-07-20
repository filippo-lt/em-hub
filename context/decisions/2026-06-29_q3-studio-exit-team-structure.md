# Q3 Studio Exit + Launch-Pod Team Structure

**Date:** 2026-06-29
**Status:** Active — execution starts week of 2026-06-29; target studio exit end of July 2026
**Origin:** David's Launches & M&A channel (David, Sergio, Kristian/CPMO, Filippo); Filippo↔Sergio sync 06-26; Sergio's email to Michael/Emilio 06-27; David's channel/email replies.
**Relation to other plans:** Supersedes the *govern-in-place* posture in `context/ma-governance-operating-model.md` for the studio apps. Builds on the 05-16 resource-planning strategy (the "externals out" direction) and the 06-22/06-26 Sergio alignment.
**Artifacts:** plan map `context/communications/2026-06-27_q3-launches-ma-plan-combined.svg` · agenda `people/sergio-hueso/talking-points/2026-06-26_q3-launches-ma-sync-agenda.md` · transcript+analysis `people/sergio-hueso/transcripts/2026-06-26_*`.

---

## Decision

Exit **both** external studios — **Helikanon** and **TurboCat** — target **end of July 2026**. Concentrate engineering on three apps run in parallel — **AI Design, Truth Seeker, ChatUltra** — via a **launch-pod** structure on a shared rollout layer.

## Why

The M&A portfolio dumped many half-context apps with underperforming studios. Concentrating on the few that matter (plus Face AI in maintenance) shrinks the problem, removes expensive low-value external spend, and gives a clean, fundable team shape. Both managers and the CPMO are aligned; Sergio is actively pro-concentration.

## Per-app disposition

| App | Disposition | Owner / team |
|---|---|---|
| ChatUltra | **Keep — critical path.** Replace Helikanon with new external Flutter team + internal lead. | New vendor (Anadea/Gilzor TBD) + **Vlad** (lead, frees from Face AI ~mid-Jul). PO open: Enrique/Carlos/Gerardo (Filippo prefers Ruben). |
| Truth Seeker | **Web pivot, fully internal.** Native app dead. | Andrey + Oscar (QA). Release ~early Aug. |
| AI Design | **Unchanged.** | Anadea (external) + advisor (TBD). |
| PDF Editor | **Fix ads in July, then park/hold.** No replacement. | TurboCat until exit. |
| Step Counter | **Minor fixes → hold.** Gated on ad-model decision. | None now. |
| Music Player | **On hold / effectively dead.** | None. |
| Face AI | **Fully internal (Vlad SE).** Loading-times fix → maintenance. | Vlad (frees mid-Jul). |
| Screen Mirroring | **Parked.** | Andrey, when marketing frees. |

## Studio exit execution

- **Helikanon** — gated only by ChatUltra. First named exits (procurement): Mesut Güngör, Serkan Dağlıoğlu (confirm they're on the on-hold apps, not ChatUltra). ChatUltra devs held for KT handover.
- **TurboCat** — Maxim Panasenko, Valeriy Knyazev. Exit after July ad fixes. No replacement.
- **Owners:** Sergio → Michael (head of M&A) + Emilio Homedes (commercial terms, notice period). Filippo → procurement execution of exits + ChatUltra replacement request (Engineering → procurement, after Filippo↔David validation).

## Team structure (David's "rollout-capable, 3 apps simultaneously")

**Launch pods** (per-app external/internal delivery + internal lead) sitting on a **shared rollout layer** = release gate (crash-free + smoke) + QA seal + ad-strategy launch sequencing. The shared layer is the fundable core and the case for a dedicated launches team with its own budget. Fluid: move an external team to Growth with the app (Tattooist precedent), keep internal people for the next investment. **David parked "final team structure based on priorities" to week of 06-29 — Filippo brings the proposal (own the authorship).**

## Risks / open items

- **Flutter bench** at Anadea/Gilzor unconfirmed (zero Flutter in current registry) — the one thing that can move end-July. Confirm this week.
- **KT overlap on ChatUltra** — Sergio's email reframed the fallback as "pause or alternatives" (cold cut of a revenue app). Protect a short paid Helikanon handover; raise in next week's team-structure discussion with David.
- **Vlad contention** — Face AI SE vs Martech-horizontal vs ChatUltra lead. Claim him for ChatUltra before reallocation.
- **ChatUltra PO** open (Enrique→Apollo); ~1 month to land with Jose.
- **Bench erosion** — Christian pulling Enrique + Sara to Apollo.
