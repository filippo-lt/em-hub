# M&A Portfolio Tracker

**Owner:** Filippo · **Cadence:** live (auto-refreshed weekly) · reviewed monthly with David
**Source of truth:** `M&A - Apps Tech Overview` Google Sheet (this is the column spec + markdown mirror)
**Related:** `context/ma-governance-operating-model.md` · per-app detail in `templates/app-scorecard-template.md`

> The heartbeat. One row per app, most of it auto-filled. The monthly David review is run off this table: scan for 🔴 flags and due decision dates — pull the full scorecard only for those.

---

## The four-verb decision vocabulary

Every artifact uses these. **Posture** is where an app sits now; a scorecard **recommends** a move between them.

| Verb | Meaning | Trigger condition |
|---|---|---|
| **Govern-in-place** | Studio keeps delivery; we govern via gates + visibility | Acceptable + has value |
| **Remediate** | Time-boxed internal SE fix campaign | Bad but savable + worth it |
| **Rebuild** | Greenfield / new-app track, internal SE | Worth it, not savable as-is |
| **Sunset** | Wind down, reclaim capacity | Not worth it |

---

## Tracker

| App | Posture | Tier | Studio | Cost/mo | MRR | MAU | Crash-free % | Release floor | Next decision | Flag |
|---|---|---|---|---|---|---|---|---|---|---|
| ChatUltra | Govern-in-place | Maintain | Helikanon | €— | €— | — | —% | ✅/❌ [date] | [what · date] | 🟢 |
| PDF Editor | Govern-in-place | Wind-down | TurboCat | €— | €— | — | —% | ✅/❌ [date] | Business case · [date] | 🟡 |
| Step Counter | Govern-in-place | Maintain | Helikanon | €— | €— | — | —% | ✅/❌ [date] | [what · date] | 🟢 |
| Truth Seeker | Sunset | Sunset | Helikanon | €— | €— | — | n/a | n/a | Sunset sign-off · [date] | 🔴 |
| Music Player | Sunset | Sunset | Helikanon | €— | €— | — | —% | n/a | Sunset sign-off · [date] | 🔴 |

---

## Column spec

| Column | Source | Auto? | Notes |
|---|---|---|---|
| **App** | — | — | |
| **Posture** | judgment | No | One of the four verbs |
| **Tier** | scorecard | No | Build · Scale · Maintain · Wind-down · Sunset |
| **Studio** | inventory | No | Delivery owner (≠ governance owner, who is always Filippo) |
| **Cost/mo** | GCP + contract | Partly | `/gcp-spend` for infra/AI; studio cost manual |
| **MRR** | RevenueCat API | **Yes** | |
| **MAU** | Amplitude API | **Yes** | |
| **Crash-free %** | Crashlytics → BigQuery | **Yes** | ★ load-bearing — feeds health, release gate, QA evidence |
| **Release floor** | CI / release pipeline | **Yes** | Last automated floor result: crash-free + smoke + secret scan + consent |
| **Next decision** | scorecard | No | The dated trigger from the app's scorecard |
| **Flag** | derived | Partly | 🟢 on track · 🟡 watch / decision due soon · 🔴 action needed (floor failing, trigger overdue, sunset pending) |

7 of 11 columns are API-pullable. Hand-maintained: Posture, Tier, Studio, Next decision. A scheduled script (fits `scripts/` + gh-metrics) writes the auto columns weekly; Flag derives from floor result + decision-date proximity.

**Build sequence:** v1 fill by hand to validate the columns → v2 automate the 7 API fields. Don't build the pipeline before the columns are proven right.
