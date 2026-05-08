# M&A — Status

Last updated: 2026-05-08

## Scope

The M&A unit owns 5 acquired apps, distinct from the existing mobile app unit (Tattooist, iMote, Face AI, AI Design, Screen Mirroring).

| App | Priority | Platforms | Tech | Studio | State |
| --- | --- | --- | --- | --- | --- |
| Chatbot | P1 | iOS / Android | Flutter | Helikanon | Live, revenue-generating |
| PDF Editor | P2 | iOS / Android | Flutter | TurboCat | Live |
| Step Counter | P2 | Android | Android Native | Helikanon | Live |
| Truth Seeker | P3 | iOS / Android | Flutter | Helikanon | Pre-launch — blocked on Apple review (rejected x1) |
| Music Player | P3 | Android | Android Native | Helikanon | Live — sunset candidate (business model not proving) |

## Tech profile

- 3 Flutter, 2 Android Native, 0 iOS Native
- Flutter-heavy → intersects the unresolved Flutter expertise gap on Filippo's team

## Studios

- **Helikanon** — 4/5 apps. Dominant concentration risk.
- **TurboCat** — PDF Editor only.

The studios in `contractors/registry.md` and `contractors/projects.md` (57 Blocks, Anadea, Gilzor) are tied to the **existing** mobile app unit, not M&A. M&A studios are not yet mapped into the registry.

## Ownership

- Filippo takes Launches + M&A from Q3 (per `project_ma_expansion`).
- Victor confirmed reporting to Filippo.
- POs per app: not yet assigned in the inventory sheet.
- Tech leads / SE owners per app: not yet assigned.

## Inventory

**Source of truth:** `M&A - Apps Tech Overview` Google Sheet
https://docs.google.com/spreadsheets/d/1SwkUIHNpwIdx75FznbO9AnBHgwcDaBmG02lAKVJqLtw/edit

One overview tab + one tab per app. Per-app tabs track integrations (CI/CD, Amplitude, RevenueCat, AppsFlyer, Firebase, Crashlytics, Superwall × iOS/Android × Requested/Integrated/Tested), repos under `github.com/rosseca/`, and identity/keys placeholders.

Local working notes: `m-and-a/inventory/README.md`.

## Open questions / known gaps

- POs and SE owners not yet assigned per app
- Studios not in the contractor registry yet
- Inventory sheet missing: push notifications, CMP/consent, backend services, store URLs, credentials-location pointer
- Truth Seeker: Apple review unblocking plan
- Music Player: explicit sunset decision + capacity-reclaim plan
- Helikanon concentration risk: no mitigation plan yet
- Flutter expertise gap on Filippo's team: unresolved
