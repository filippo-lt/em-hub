# Martech SDK — Q3 Strategy

**Owner:** Filippo (EM, Mobile App Unit)
**Audience:** David (CTO) — for review/sign-off
**Date:** 2026-06-25
**Status:** Draft for next 1:1

---

## TL;DR

MartechKit has quietly graduated from a *project* to a *platform*: multiple consuming apps, a production incident (VideoUp), a backlog of cross-team demand (#38), and a single Staff Engineer at 50% holding it up. Q3 is about putting a **platform operating model** around it — roadmap, enforcement, capacity, and visibility — so it scales without breaking.

**Good news first: OKR KR6 is essentially delivered.** MartechKit v1 + 4 integrations — Tattooist, FaceAI, ScreenMirroring (iOS) + iMote (Android, on PR merge). AI Design (via Vlad) makes a fifth.

**Three asks of you this quarter** (detail in §7):
1. Acknowledge and resource the **Victor capacity risk** (bus factor = 1).
2. Back the **Engineering Dashboard** as a named, separately-resourced initiative.
3. Close the open **H2 scope conditions** (Flutter capability, Victor cadence, Mobile SE backfill).

---

## 1. Where we are

| Platform | State |
|---|---|
| iOS | Delivered; adopted in Tattooist, FaceAI, ScreenMirroring |
| Android | Integrated in iMote; PR open, merging shortly |
| Flutter | Next in line; approach pending David Catalá confirmation |

SDK wraps RevenueCat, Amplitude, AppsFlyer (identity init + ID syncing). Victor Jalencas owns the build at 50% capacity (split with M&A app work).

**Adoption is two portfolios, not one.** Our Mobile App Unit apps are adopted and well-behaved. The Martech/Photo-Video vertical (VideoUp, Step Counter, ai-cleaner, ereasy) is **not** migrated and still hand-rolls attribution — which is where the incident happened.

---

## 2. The reframe: project → platform

The four things on the table — a messy roadmap, a need for quality gates, ad-hoc staffing, and a request for a visibility dashboard — are not separate problems. They are four symptoms of one: **a platform being run like a project.** The strategy is to install the missing platform discipline:

| Symptom | Missing discipline | Workstream |
|---|---|---|
| Roadmap long & messy (#38) | Prioritised, visible backlog | WS1 |
| VideoUp incident | Versioning + release/CI gates | WS2 |
| Victor 50%, Vlad ad-hoc | Staffing & ownership model | WS3 |
| "Where is it integrated?" | Adoption/health visibility | WS4 |

---

## 3. Q3 objectives

1. **Stabilise**: no repeat of a VideoUp-class attribution break in any app on the kit.
2. **Prioritise**: a single, agreed, visible roadmap shared with Martech.
3. **Scale safely**: enforcement + capacity that let adoption grow without raising risk.
4. **Make it visible**: ship the v0 integration dashboard; pitch the org dashboard.

---

## 4. Workstreams

### WS1 — Roadmap & prioritisation
- Move the #38 backlog into a **dedicated Eng-owned Jira project (`MTK`)**. Epics = P0 Enforcement & Adoption / P1 New SDK Surface / P2 Identity Bridges & Cleanup.
- Stand up a **prioritisation ritual** with Miguel Alvarez + David-leadtech (Martech). The demand side is engaged and specific; the gap is an agreed priority order, not a missing sponsor.
- Cross-platform rule: every contract lands iOS + Android + Flutter — no one-platform fixes.
- **Owner:** Filippo (process) + Victor (feasibility). **By:** mid-July for board + first prioritised list.

### WS2 — Enforcement & quality gates
- Defense-in-depth, MVP first:
  - `swift test` **blocks merges** on MartechKit (cheap prevention).
  - **NULL `customer_user_id` rate alert** (the safety net that would have caught VideoUp in hours).
  - Shared `verify-no-manual-martech.sh` CI script, adopted per app as it migrates.
- Mandatory Martech review is an **interim** human stopgap only — replaced by automation.
- **Owner:** Victor (kit gates) + app teams (app gates, our script) + Martech/data (alert). **By:** MVP gates live end-July.

### WS3 — Resourcing  *(the core ask)*
- **Victor at 50% is the platform's single biggest risk** — bus factor of 1 across 3 platforms + gates + roadmap.
- **Vlad** ramps by integrating MartechKit into **AI Design (iOS + Android)** — his own app (solo/async, fits his constraints), now an Invest-tier app — then supports Victor (~25%).
- Concrete capacity decision needed: either narrow Q3 scope or add capacity. **This is a dated ask, not a flag.**
- **Owner:** Filippo. **By:** decided in next 1:1.

### WS4 — Visibility
- **Dashboard v0:** auto-generated integration matrix (MartechKit/Parapet/Pipelins × app × version × health), parsed from repos. Cheap, double-demanded (you + Martech). Ships as a byproduct of the SDK work.
- **Observability layer** (NULL-rate alert + active contract verifier across RC/AppsFlyer/Amplitude): **co-built with Martech**, who own the data/API keys. A shared win, not a handoff.
- **Org dashboard (v2+):** the full EM-editable single pane of glass = the App Portfolio Framework made live. Pitched **separately** as a named, resourced initiative — not on Victor.
- **Owner:** Filippo + Vlad (v0) / Martech (data layer). **By:** v0 in Q3; org dashboard = separate pitch.

---

## 5. Scope boundary (please endorse)

> **Engineering builds and owns the rails** — the SDK, the CI gate scripts, the integration guide, the dashboard. **Each app team migrates its own app** across. Victor's 50% does not absorb a company-wide migration program.

Without this line, platform capacity silently becomes a migration service for apps we don't own.

---

## 6. Stakeholders

| Who | Role | Interest |
|---|---|---|
| **David** (CTO) | Sponsor | Visibility, stability, no exec-visible failures |
| **Victor Jalencas** | Tech lead (50%) | Clear priorities; protected focus; Flutter sign-off via Catalá |
| **Vlad Krudek** | Support (~25%) | Solo/async work; AI-SE evidence preserved |
| **David Catalá** | Flutter | Looped before Flutter work starts |
| **Miguel Alvarez + David-leadtech** | Martech demand side | Roadmap delivered; co-own observability |
| **Peer EMs** | Dashboard co-editors | Shared, low-burden status of record |
| **App teams (Photo/Video vertical)** | Migrators | Adopt the kit + gates on their own apps |

---

## 7. Asks of David

1. **Name and resource the Victor capacity risk.** Endorse either a scoped Q3 or added capacity — explicitly, with a number.
2. **Back the Engineering Dashboard** as a separately-resourced initiative (v0 ships now; v2+ needs its own owner, not Victor).
3. **Close the H2 scope conditions** (Flutter capability, Victor cadence, Mobile SE backfill) carried over from the April deal.
4. **Air cover** for the Martech prioritisation ritual and (later) PM data for the dashboard's value columns.

---

## 8. Risks

| Risk | Mitigation |
|---|---|
| Dashboard scope eats SDK delivery | v0–v1 ride along; v2+ separately resourced |
| Victor over-loaded (bus factor 1) | WS3 capacity ask; Vlad ramp; scope discipline |
| App-side gates seen as imposed on other teams | Frame as rails we provide, not rules we enforce |
| Cross-platform drift (Swift fixed, Kotlin/Flutter not) | Contract must land on all 3 stacks before "done" |
| Observability layer stalls on data access | Name the Martech/data owner; co-build |
| Roadmap re-mess in Jira without a ritual | WS1 prioritisation cadence with Martech |

---

## 9. Action points

| # | Action | Owner | By |
|---|---|---|---|
| 1 | Stand up `MTK` Jira project + migrate #38 into P0/P1/P2 epics | Filippo / Victor | Mid-July |
| 2 | First prioritisation session with Miguel + David-leadtech | Filippo | Mid-July |
| 3 | `swift test` blocks merges on MartechKit | Victor | Early-July |
| 4 | NULL-rate alert — secure data owner + build | Martech/data + Filippo | End-July |
| 5 | `verify-no-manual-martech.sh` shared script v1 | Victor / Vlad | End-July |
| 6 | Vlad integrates MartechKit into AI Design (iOS + Android) | Vlad | Q3 |
| 7 | Confirm Flutter approach with Catalá | Victor | July |
| 8 | Dashboard v0 integration matrix | Filippo / Vlad | Q3 |
| 9 | Update App Portfolio Framework (AI Design → Invest) | Filippo | Next 1:1 |
| 10 | Present this strategy + the 3 asks to David | Filippo | Next 1:1 |

---

*Open decisions still to lock: Jira project shape (dedicated `MTK` vs existing), dashboard build-vs-assemble for v0, owner of the org-dashboard v2+ initiative.*
