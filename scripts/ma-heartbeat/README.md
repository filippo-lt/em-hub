# M&A Heartbeat — scripts

The data-fetch layer for the **M&A Heartbeat Agent**
(`.agents/agents/ma-heartbeat-agent.md`). The agent orchestrates and applies
judgment; these scripts do the mechanical capture, exactly as the Contractor
Performance Agent leans on `scripts/gh-metrics.sh`.

```
scripts/ma-heartbeat/
  fetch_heartbeat.py   # orchestrator: config → sources → History rows + flags
  sources.py           # one fetcher per data source (RevenueCat, Amplitude,
                       #   Crashlytics/BQ, GCP cost, GitHub)
  README.md            # this file
```

Stdlib-only Python 3 (no pip installs), matching the repo convention.

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
   export AMPLITUDE_API_KEY=...         # Amplitude project API key
   export AMPLITUDE_SECRET_KEY=...      # Amplitude project secret key
   export AMPLITUDE_REGION=us           # or eu
   export GCP_BILLING_TABLE=proj.dataset.gcp_billing_export_v1_XXXX
   ```
   Put these in `.env` (already gitignored) and source it.

3. **CLI auth reused as-is:** `gh auth login` (GitHub — releases, secret
   scanning, gate bounces) and `gcloud auth` / `bq` (BigQuery — Crashlytics
   export + GCP billing). Access is gated on Phase 0 of the governance model;
   until a login lands, that source returns `n/a (no access)`.

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
console, GCP billing) before putting this on a weekly schedule. The endpoints
in `sources.py` are the documented ones, but the exact RevenueCat/Amplitude
response shapes and the Crashlytics BigQuery export schema depend on your
account — the `# VERIFY` notes mark what to confirm during that window.
Especially **crash-free %**: there is no public Crashlytics API, so it is
derived from the BigQuery export and the SQL in `fetch_crash_free` almost
certainly needs tuning to your export's user/session schema.
