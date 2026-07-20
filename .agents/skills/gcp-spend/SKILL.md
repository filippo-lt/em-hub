---
name: gcp-spend
description: "Show or refresh the GCP monthly spend report and analyse it. Use when the user says things like: 'GCP spend', 'show the GCP report', 'cloud cost report', 'how much are we spending on GCP', 'monthly cloud spend', 'cost per app', 'AI cost per MAU', 'refresh the GCP report'."
user_invocable: true
---

# GCP Spend

You run and analyse the monthly GCP spend report. The tool itself lives in a separate project at `/Users/ftosetto/Projects/gcp-spend-report/`; the rendered HTML is published into `em-hub/metrics/gcp-spend/` and is what you load as EM context.

---

## Process

### Phase 1 — Freshness check

Scan `metrics/gcp-spend/` for files matching `YYYY-MM.html`. Find the newest by filename date.

- **Fresh:** a file matching the **current calendar month** (use the date from system context) is present → skip to Phase 3.
- **Stale or missing:** no file for the current month → go to Phase 2.
- **`--refresh` passed:** always refresh, regardless of freshness.

### Phase 2 — Refresh

The tool is vendored inside em-hub at `scripts/gcp-spend/`. Run the publish target from there:

  ```
  cd scripts/gcp-spend && make setup && make publish MONTH=YYYY-MM
  ```

  Where `YYYY-MM` is the target month (default: last completed month). `make setup` installs Python deps; skip it if already installed. Surface the command output. Auth is non-interactive via a service-account key at `scripts/gcp-spend/secrets/gcp-sa-key.json` (one-time setup in `scripts/gcp-spend/SETUP-HEADLESS.md`). If it fails because the key is missing/invalid, tell the user verbatim and stop — do not fabricate numbers.

### Phase 3 — Load and analyse

Load the freshest `metrics/gcp-spend/YYYY-MM.html` and `metrics/gcp-spend/index.html`. Open the analysis conversation. Cover:

- Total spend for the month vs prior months (anomalies, trend)
- Cost per app — biggest movers, what shipped that month that might explain them
- AI cost attribution — flag the `$/MAU` caveat from `reference_app_ai_cost_attribution.md`: GCP dashboard $/MAU is GCP-only, so Tattooist routes AI through GCP but AI Home Design uses a separate provider; do not compare $/MAU across apps without this caveat
- Pending apps not yet active

Ask the user what they want to dig into rather than dumping everything.

---

## The tool

Vendored and self-contained inside em-hub at `scripts/gcp-spend/`:

- `make publish MONTH=YYYY-MM` — render the focal month + dashboard and copy them (plus the `YYYY-MM.json` heartbeat export) into `metrics/gcp-spend/`
- `make report MONTH=YYYY-MM` — render only, no publish
- `make setup` — install Python deps (one-time per environment; no interactive login)
- Auth: service-account key at `secrets/gcp-sa-key.json`, pointed to by `GCP_SA_KEY_FILE` in `.env`. One-time setup in `SETUP-HEADLESS.md`.

Automation: a local launchd job (`com.ftosetto.emhub.gcp-spend-refresh`) runs `monthly-refresh.sh` on the 2nd of each month — publish + commit + push — and the "Monthly cost digest" cloud routine then drafts a Gmail digest from the published files. If the service-account key is absent, `run.py` falls back to gcloud ADC. The older `~/Projects/gcp-spend-report` repo is now redundant for automation — this copy is canonical.
