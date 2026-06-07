# M&A Portfolio Tracker

**Owner:** Filippo · **Cadence:** auto-refreshed weekly · reviewed monthly with David
**Source of truth:** `M&A - Apps Tech Overview` Google Sheet (this is the column spec + markdown mirror)
**Model:** `context/ma-governance-operating-model.md` · per-app detail: `templates/app-scorecard-template.md`

> The heartbeat. One row per app, most of it auto-filled. The monthly David review runs off this table: scan for 🔴 flags and due decision dates — pull the full scorecard only for those.

**Posture** (one per app): **Govern-in-place · Remediate · Rebuild · Sunset.** Definitions + trigger conditions live in the operating model.

---

## Tracker

| App | Posture | Studio | Cost/mo | MRR | MAU | Crash-free % | Release floor | Next decision | Flag |
|---|---|---|---|---|---|---|---|---|---|
| ChatUltra | Govern-in-place | Helikanon | €— | €— | — | —% | ✅/❌ [date] | [what · date] | 🟢 |
| PDF Editor | Govern-in-place | TurboCat | €— | €— | — | —% | ✅/❌ [date] | Business case · [date] | 🟡 |
| Step Counter | Govern-in-place | Helikanon | €— | €— | — | —% | ✅/❌ [date] | — | 🟢 |
| Truth Seeker | Sunset | Helikanon | €— | €— | — | n/a | n/a | Sunset sign-off · [date] | 🔴 |
| Music Player | Sunset | Helikanon | €— | €— | — | —% | n/a | Sunset sign-off · [date] | 🔴 |

---

## Column spec

| Column | Source | Auto? |
|---|---|---|
| **App** | — | — |
| **Posture** | judgment (rarely changes) | No |
| **Studio** | inventory (rarely changes) | No |
| **Cost/mo** | GCP (`/gcp-spend`) + studio contract | Partly |
| **MRR** | RevenueCat API | **Yes** |
| **MAU** | Amplitude API | **Yes** |
| **Crash-free %** | Crashlytics → BigQuery | **Yes** ★ |
| **Release floor** | CI release pipeline | **Yes** |
| **Next decision** | the app's scorecard trigger | No |
| **Flag** | derived from floor + decision-date proximity | Partly |

7 of 10 columns auto-fill from a weekly script (fits `scripts/` + gh-metrics). You only touch Posture, Studio, and Next decision — and those change rarely. Crash-free % (★) is the load-bearing metric: it also drives the release gate and the QA evidence.

**Flag:** 🟢 on track · 🟡 watch / decision due soon · 🔴 action needed (floor failing, trigger overdue, sunset pending).

**Build sequence:** v1 fill by hand to validate the columns → v2 automate the 7 API fields. Don't build the pipeline before the columns are proven.
