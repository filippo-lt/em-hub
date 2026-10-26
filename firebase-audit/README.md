# firebase-audit

Audit of the app portfolio against **ADO-1570** — *[Firestore] Close public data plane
(anonymous Auth) on remaining Apps GCP projects*.

Screen Mirroring and ChatUltra are **created in Jira** (keys stamped at the top of each
file). The iMote set is still a draft.

## Contents

| File | What it is |
|---|---|
| [`final-report.md`](final-report.md) | Portfolio report — findings for all ten apps, cross-cutting analysis, filing plan, open questions |
| [`imote/`](imote/) | 1 Epic + 2 Stories — `IMIOSMAU` — **draft, not created** |
| [`screen-mirroring/`](screen-mirroring/) | SMIOSMAU-529 + 530, 531 — **created** |
| [`chatultra/`](chatultra/) | CBMAU-275 + 276, 277, 278, 279 — **created** |
| [`faceai/`](faceai/) | FAIOSMAU-790 — single Maintenance ticket — **created** |

## Apps with no tickets

- **AI Design** — covered by `ADIOSMAU-2259/2260/2261`
- **PDF Editor** — Cloud Storage issue, different class, own ticket recommended
- **Step Counter / Music Player** — no Firestore, no Auth
- **Goya / Mirage** — Tattooist-class credential exposure, no owner; route to IT Security

Rationale for each is in `final-report.md` §4.

## Ticket format

Epics and stories follow the house pattern established by `VUIOSMAU-2744/2745`,
`PUIOSMAU-2263/2264` and `TTIOSMAU-2570/2571`:

- **Epic** — Executive summary, exposure in plain language, a concrete attacker scenario,
  the risk a blanket block would create, Expected outcome bullets.
- **Story** — Context, provenance notice, Technical guidance, Validation, Acceptance
  criteria.

Each carries a provenance notice stating the findings came from an AI-assisted review and
must be validated by the technical owner, matching the convention in the exemplar tickets.

## Created in Jira

| Key | Type | Priority | Summary |
|---|---|---|---|
| [SMIOSMAU-529](https://leadtech.atlassian.net/browse/SMIOSMAU-529) | Epic | Major | Protect Screen Mirroring Firestore review and quota data |
| [SMIOSMAU-530](https://leadtech.atlassian.net/browse/SMIOSMAU-530) | User Story | Major | Confirm whether reviews has any consumer |
| [SMIOSMAU-531](https://leadtech.atlassian.net/browse/SMIOSMAU-531) | User Story | Major | Implement and validate least-privilege Firestore access |
| [CBMAU-275](https://leadtech.atlassian.net/browse/CBMAU-275) | Epic | Critical | Protect ChatUltra Firestore user and chat data |
| [CBMAU-276](https://leadtech.atlassian.net/browse/CBMAU-276) | User Story | Major | Export the deployed ruleset and confirm exposure |
| [CBMAU-277](https://leadtech.atlassian.net/browse/CBMAU-277) | User Story | Major | Enable App Check enforcement for Firestore |
| [CBMAU-278](https://leadtech.atlassian.net/browse/CBMAU-278) | User Story | Major | Move client-side user-record writes behind a trusted path |
| [CBMAU-279](https://leadtech.atlassian.net/browse/CBMAU-279) | User Story | Major | Implement and validate least-privilege Firestore access |
| [FAIOSMAU-790](https://leadtech.atlassian.net/browse/FAIOSMAU-790) | Maintenance | Major | Close Firestore public data plane (anonymous Auth) — Face AI |

All in `Created`, unassigned, with no link to ADO-1570.

Face AI was originally scoped as "nothing to do" because `iOSUserCredits` is dead code.
It was filed anyway to close the ~1,671 stale records holding `revenueCatId` billing
identifiers, and to cover `iOSAppRatings`, which is client-writable and absent from the
ADO-1570 probe list.

## Still open

1. **Assignees** — all 7 issues are unassigned. ChatUltra needs a decision given the
   studio off-ramp.
2. **The two investigation stories** (SMIOSMAU-530, CBMAU-276) are gated on a named person
   answering. They cannot start unassigned.
3. **iMote** — drafted but not created. Needs a call on one Epic across `IMIOSMAU` +
   `IMANDMAU` versus components on a single project.
4. **PDF Editor** — Cloud Storage issue, own ticket recommended, not yet filed.
5. **Goya / Mirage** — route to IT Security; no team to receive a ticket.
