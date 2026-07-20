# M&A — Status

Last updated: 2026-06-29

> **Major shift (Q3, late June 2026):** This moved from *govern-in-place* to **exit both studios**. Helikanon and TurboCat are being offboarded, target **end of July**, aligned across David, Sergio, Kristian (CPMO). Filippo owns the procurement-driven offboarding + the ChatUltra replacement team. See `context/decisions/2026-06-29_q3-studio-exit-team-structure.md` and the plan map `context/communications/2026-06-27_q3-launches-ma-plan-combined.svg`.

## Scope

The M&A unit owns 5 acquired apps, distinct from the existing mobile app unit (Tattooist, iMote, Face AI, AI Design, Screen Mirroring).

| App | Priority | Tech | Studio | Q3 disposition |
| --- | --- | --- | --- | --- |
| ChatUltra | P1 | Flutter | Helikanon → **new external team + advisor** | **KEEP — the one critical path.** Live, revenue, heavy tech debt. Replacement Flutter team being hired (starts hiring Mon 06-29); Helikanon exits ChatUltra only once replacement is in place (KT overlap preferred; per Sergio's email, fallback is pause/alternatives — Filippo to protect a short paid handover). |
| Truth Seeker | P3 | Flutter (native) → **web** | Internal | **Web pivot, fully internal** (Andrey dev + Oscar QA from 06-29). Possible release ~early August. Native Flutter app = **dead**. |
| PDF Editor | P2 | Flutter | TurboCat | **Fix ads in July, then park/hold** until marketing numbers justify. No replacement team needed. Christian says early numbers bad (one week of ads — both agree too little; possible ad mis-implementation). |
| Step Counter | P2 | Android Native | Helikanon | **Minor fixes (days) → on hold.** Gated on the ad-monetization-model decision (tied to PDF results). No team needed now. |
| Music Player | P3 | Android Native | Helikanon | **On hold / effectively dead.** Helikanon untouched it ~2-3 months. Sergio has a reassessment plan "in a bucket" pending ad-model decision. |

> Screen Mirroring (existing unit, not M&A) also folded into the same posture: **parked**, Andrey resumes when marketing frees up.

## Studio exit (target: end of July 2026)

- **Helikanon** — exit gated **only** by ChatUltra (Music Player / Step Counter / Truth Seeker already on hold). First named exits (David, via procurement): **Mesut Güngör, Serkan Dağlıoğlu** (assumed on the on-hold apps — Filippo to confirm scope before pulling). ChatUltra devs held for handover.
- **TurboCat** — PDF only. Finalize ad fixes in July, then exit. Named exits: **Maxim Panasenko, Valeriy Knyazev**. No replacement needed.
- Commercial terms / notice period: **Sergio** owns the Michael (head of M&A) + Emilio Homedes (procurement) thread (email sent 06-27). **Filippo** owns procurement execution of the exits + the ChatUltra replacement request (Engineering → procurement, after Filippo↔David validation).

## Team structure (the 3 simultaneous launch apps)

David's ask: a structure with rollout capability across **AI Design, Truth Seeker, ChatUltra** simultaneously. Model = **launch pods** (external/internal delivery + internal lead) on a **shared rollout layer** (release gate + QA + ad-strategy launch sequencing = the fundable core; the pitch for a dedicated launches team with its own budget). David parked "final team structure based on priorities" to the week of 06-29 — Filippo to bring the proposal (own the authorship).

- **AI Design** — unchanged: Anadea (external) + advisor (advisor TBD now that Vlad moved to Face AI).
- **Truth Seeker** — internal: Andrey + Oscar (QA).
- **ChatUltra** — new external Flutter team (Anadea/Gilzor, vendor TBD) + **Vlad as lead** (frees from Face AI ~mid-July). PO on Product side open: Enrique/Carlos/Gerardo — Filippo prefers **Ruben**.
- **Face AI** — now **fully internal, Vlad as SE** (was Gilzor + advisor; Gilzor rolled off). Fix loading times → ready ~mid-July → maintenance/pause. This is what frees Vlad.

## Ownership

- Filippo owns Launches + M&A from Q3; procurement-driven studio offboarding; ChatUltra replacement team.
- Victor reports to Filippo.
- Vlad: advisor → **full SE on Face AI**; candidate **ChatUltra lead** once Face AI wraps.
- Christian pulling **Enrique (PM) + Sara** to the **Apollo** project (high revenue) — erodes the launches bench; ChatUltra PO consequently open.

The M&A studios (Helikanon, TurboCat) were never mapped into `contractors/registry.md`; given the exit, tracking the named individuals here instead.

## Inventory

**Source of truth:** `M&A - Apps Tech Overview` Google Sheet
https://docs.google.com/spreadsheets/d/1SwkUIHNpwIdx75FznbO9AnBHgwcDaBmG02lAKVJqLtw/edit

One overview tab + one tab per app. Per-app tabs track integrations (CI/CD, Amplitude, RevenueCat, AppsFlyer, Firebase, Crashlytics, Superwall × iOS/Android × Requested/Integrated/Tested), repos under `github.com/rosseca/`, and identity/keys placeholders.

Local working notes: `m-and-a/inventory/README.md`.

## Open questions / known gaps

- **ChatUltra replacement: confirm Anadea/Gilzor have Flutter bench** — the one thing that can move the end-July date. Hiring starts Mon 06-29.
- **ChatUltra PO** (Product side): Enrique / Carlos / Gerardo — Filippo prefers Ruben; ~1 month to align (with Jose).
- **Claim Vlad as ChatUltra lead** before Martech/Matellano reallocates him (he frees from Face AI ~mid-July).
- **AI Design advisor** — who, now that Vlad is on Face AI (Filippo? Andrey? vendor-only?).
- **KT/handover on ChatUltra** — Sergio's email makes the fallback "pause or alternatives"; protect a short paid Helikanon overlap so a revenue app isn't cut cold.
- Confirm Mesut/Serkan cover the on-hold apps (not ChatUltra) before pulling them.
- Step Counter / Music Player final kill-vs-park gated on the ad-model decision (tied to PDF numbers).
