# M&A — Status

Last updated: 2026-08-26

> **Historical record** — this doc captures the Q3 2026 studio exit plan as of late June 2026.
> For the current app list (posture, studio, source ids), see `config/ma-apps.conf`
> (example: `config/ma-apps.conf.example`); for the live numbers, see `templates/ma-portfolio-tracker.md`.
> For repos by project, see `docs/repos-by-project.md`.
> For current team structure and launch status, see `status-updates/`.

## Summary (June 2026 snapshot)

Q3 major shift: exit both studios (Helikanon + TurboCat), target **end of July 2026**.
Filippo owned procurement-driven offboarding + the ChatUltra replacement team.
See `context/decisions/2026-06-29_q3-studio-exit-team-structure.md` and plan map
`context/communications/2026-06-27_q3-launches-ma-plan-combined.svg`.

## Original Scope (June 2026)

The M&A unit owned 5 acquired apps, distinct from the existing mobile app unit
(AI Design, iMote, Face AI, Screen Mirroring).

| App | Priority | Tech | Studio | Q3 disposition |
| --- | --- | --- | --- | --- |
| ChatUltra | P1 | Flutter | Helikanon → new external team + advisor | KEEP — critical path. Live, revenue, heavy tech debt. |
| Truth Seeker | P3 | Flutter (native) → **web** | Internal | Web pivot. Native Flutter app = dead. |
| PDF Editor | P2 | Flutter | TurboCat | Fix ads in July, then park until numbers justify. |
| Step Counter | P2 | Android Native | Helikanon | Minor fixes → on hold. |
| Music Player | P3 | Android Native | Helikanon | On hold / effectively dead. |

> Screen Mirroring (existing unit, not M&A) was parked; Andrey resumes when marketing frees up.

## Studio Exit (target: end of July 2026)

- **Helikanon** — exit gated only by ChatUltra. ChatUltra devs held for handover.
- **TurboCat** — PDF only. Finalize ad fixes in July, then exit.

## Ownership (June 2026)

- Filippo owned Launches + M&A from Q3.
- Victor reported to Filippo.
- Vlad: advisor → full SE on Face AI; candidate ChatUltra lead.
