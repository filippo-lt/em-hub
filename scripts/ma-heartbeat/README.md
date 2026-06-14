# M&A Heartbeat — scripts

The data-fetch layer for the **M&A Heartbeat Agent**
(`.agents/agents/ma-heartbeat-agent.md`). The agent orchestrates and applies
judgment; these scripts do the mechanical capture, exactly as the Contractor
Performance Agent leans on `scripts/gh-metrics.sh`.

```
scripts/ma-heartbeat/
  fetch_heartbeat.py   # orchestrator: config → sources → History rows + flags
  sources/             # one module per data source, owned independently:
    common.py          #   shared HTTP/CLI helpers
    revenuecat.py      #   MRR
    crashlytics.py     #   crash-free % (via BigQuery export)
    gcp_spend.py       #   cost + MAU — read from the gcp-spend report export
    github.py          #   release tag, secret scan, gate bounces
  README.md            # this file
```

Stdlib-only Python 3 (no pip installs), matching the repo convention.

## Cost + MAU come from gcp-spend (not fetched here)

GCP cost-per-app and Amplitude MAU-per-app are already extracted by the
external `gcp-spend-report` tool (its `query.sql.j2` + `amplitude.conf`), with
the per-app attribution method and the **GCP-only `$/MAU` caveat** baked in.
The heartbeat does **not** re-query billing or Amplitude — `gcp_spend.py` reads
the tool's published export so there is a single source of truth.

**Export contract** — the `gcp-spend-report` publish step must also write, next
to its HTML, `metrics/gcp-spend/<YYYY-MM>.json`:

```json
{
  "month": "2026-06",
  "generated_at": "2026-06-14T09:00:00Z",
  "apps": {
    "chatultra": { "cost_eur": 1234.56, "mau": 45000 },
    "pdfeditor": { "cost_eur":  210.00, "mau":  8000 }
  }
}
```

Each heartbeat app maps to a report key via `gcp_spend_key` in config. The
export is monthly; the weekly run reports the latest known monthly value (flat
within a month). Until that JSON exists, cost + MAU read `n/a (no access)`.

## Setup

1. **Config (non-secret ids):** copy the example and fill it in —
   ```bash
   cp config/ma-apps.conf.example config/ma-apps.conf
   ```
   `ma-apps.conf` is gitignored. One `[app:<name>]` section per app; omit an
   id you don't have access to yet and that field reports `n/a (no access)`.

2. **Secrets (env vars, never in config):**
   ```bash
   export REVENUECAT_API_KEY=...        # RevenueCat v2 secret key
   ```
   Put this in `.env` (already gitignored) and source it. (Cost + MAU need no
   secrets here — they come from the gcp-spend export.)

3. **CLI auth reused as-is:** `gh auth login` (GitHub — releases, secret
   scanning, gate bounces) and `gcloud auth` / `bq` (BigQuery — Crashlytics
   export). Access is gated on Phase 0 of the governance model; until a login
   lands, that source returns `n/a (no access)`.

## Run

```bash
python3 scripts/ma-heartbeat/fetch_heartbeat.py            # all apps
python3 scripts/ma-heartbeat/fetch_heartbeat.py --app ChatUltra
python3 scripts/ma-heartbeat/fetch_heartbeat.py --dry-run  # fetch, don't append
```

**Output:**
- `m-and-a/heartbeat/history.csv` — append-only History (the durable artifact;
  the Tracker snapshot derives its latest values + deltas from this).
- `m-and-a/heartbeat/<date>.json` — per-run detail: flags, reasons, and the
  release-governance inputs (last release, secret alerts, gate bounces).
- stdout — the 🟡/🔴 summary only. Green is silent (exception-based, by design).

## What the script does NOT do

It **captures and flags; it never decides.** It writes the numeric fields and
the derived `Flag`. It leaves the judgment fields blank/echoed:
`ReleaseHealth` is written as `-` (Filippo sets 🟢🟡🔴 from the supplied
gate-bounce + help inputs), and `Posture` is echoed from config, never changed.

## Validate before you schedule

Per the agent's validation protocol: run manually for **2 weeks** and
reconcile every number against its source UI (RevenueCat dashboard, Crashlytics
console, gcp-spend report) before putting this on a weekly schedule. The
endpoints in `sources/` are the documented ones, but the exact RevenueCat
response shape and the Crashlytics BigQuery export schema depend on your
account — the `# VERIFY` notes mark what to confirm during that window.
Especially **crash-free %**: there is no public Crashlytics API, so it is
derived from the BigQuery export and the SQL in `fetch_crash_free` almost
certainly needs tuning to your export's user/session schema.
