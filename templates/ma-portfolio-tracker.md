# M&A Portfolio Tracker

**Owner:** Filippo · **Cadence:** History captured weekly · reviewed monthly with David
**Live file:** [M&A – Portfolio Tracker (Google Sheet)](https://docs.google.com/spreadsheets/d/1edO2XOHpxBTTqRDk9tfjegO0sZ485O4q0XORSbg4prE/edit) — Tracker · History · Trends · Column spec. Build source: `context/app-portfolio/ma-portfolio-tracker.xlsx`. This markdown is the column spec + mirror.
**Model:** `context/ma-governance-operating-model.md` · per-app detail: `templates/app-scorecard-template.md`

> The heartbeat. One row per app — the time-varying numbers pull the latest entry from the **History** sheet (single source of truth), so you only ever append to History. The monthly David review runs off this table: scan for 🔴 flags, ▼ down-arrows, and due decision dates — pull the full scorecard only for those.

**Posture** (one per app): **Govern-in-place · Remediate · Rebuild · Sunset.** Definitions + trigger conditions live in the operating model.

---

## Tracker

Numbers (Cost/MRR/MAU/Crash-free) auto-pull the latest row from History; the **Δ** columns compare to the prior period (▲ up / ▼ down, green/red).

| App | Posture | Studio | Cost/mo | MRR | Δ | MAU | Crash-free % | Δ | Release health | Next decision | Flag |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ChatUltra | Govern-in-place | Helikanon | ⟵History | ⟵History | ▲▼ | ⟵History | ⟵History | ▲▼ | 🟢 | Standing: fund takeover when ready | 🟢 |
| PDF Editor | Govern-in-place | TurboCat | ⟵History | ⟵History | ▲▼ | ⟵History | ⟵History | ▲▼ | 🟡 | Business case · [date] | 🟡 |
| Step Counter | Govern-in-place | Helikanon | ⟵History | ⟵History | ▲▼ | ⟵History | ⟵History | ▲▼ | 🟢 | — | 🟢 |
| Truth Seeker | Sunset | Helikanon | — | — | — | — | — | — | n/a | Sunset sign-off · [date] | 🔴 |
| Music Player | Sunset | Helikanon | ⟵History | ⟵History | ▲▼ | ⟵History | ⟵History | ▲▼ | n/a | Sunset sign-off · [date] | 🔴 |

---

## Column spec

| Column | Source | Auto? |
|---|---|---|
| **App** | — | — |
| **Posture** | judgment (rarely changes) | No |
| **Studio** | inventory (rarely changes) | No |
| **Cost/mo** | latest from History (GCP `/gcp-spend` + studio contract) | From History |
| **MRR** | latest from History (RevenueCat API) | From History |
| **MRR Δ** | MRR latest ÷ prior − 1 | Derived |
| **MAU** | latest from History (Amplitude API) | From History |
| **Crash-free %** | latest from History (Crashlytics → BigQuery) | From History ★ |
| **Crash-free Δ** | Crash-free latest − prior (points) | Derived |
| **Release health** | gate-bounce count (CI) + help read (studio call) | Judgment |
| **Next decision** | the app's scorecard trigger | No |
| **Flag** | derived from floor + decision-date proximity | Partly |

The numeric columns pull from the History sheet; the script appends to History, the Tracker derives. You only touch the judgment fields — Posture, Studio, Release health, Next decision, Flag — and those change rarely. Crash-free % (★) is the load-bearing metric: it also drives the release gate and the QA evidence.

**Release health** is *not* the automated CI gate. The floor (crash-free + smoke test + secret scan + consent) stays a **blocking CI gate — infrastructure, not a column** (a blocking gate is always green, so it carries no information as a metric). This column instead tracks **delivery autonomy**: 🟢 shipped clean & alone · 🟡 friction / multiple attempts · 🔴 needed heavy help to get live. Fed by CI gate-bounce count (objective) + the studio-call help read (subjective). `n/a` for pre-launch / sunsetting apps.

**Flag:** 🟢 on track · 🟡 watch / decision due soon · 🔴 action needed (floor failing, trigger overdue, sunset pending).

---

## History & trends

The Tracker is a live snapshot; **History** is the append-only memory behind it — one row per app per weekly run (Date · App · Posture · Cost · MRR · MAU · Crash-free % · Release health · Flag). Cadence: **capture weekly, review monthly.** Everything time-based reads from History:

1. **Delta on the snapshot** — the Δ columns (▲/▼ vs prior period), evolution at a glance without leaving the Tracker.
2. **Trends sheet** — line charts per metric per app (MRR, Crash-free %), to catch the multi-month slide a single delta hides.
3. **Threshold evidence** — "3 of last 5 releases failed", "MRR down 3 months" — the rule-based read that powers the QA wedge and the Phase-5 forcing memo.

**Build sequence:** v1 validate the columns → **v1.5 (current)** History store + derived snapshot + deltas + trend charts, on sample data → v2 automate: the weekly script appends a real row to History (and extends the Trends date axis). Don't build the pipeline before the columns are proven. **v2 is the `M&A Heartbeat Agent`** (`.agents/agents/ma-heartbeat-agent.md`) — it captures, appends, and flags; it never touches the judgment fields.
