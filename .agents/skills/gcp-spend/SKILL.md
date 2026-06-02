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

Check that `/Users/ftosetto/Projects/gcp-spend-report/` exists.

- **Missing:** tell the user the external project isn't at the expected path. Offer to analyse the most recent stale report instead. Do not invent a path or fall back silently.
- **Present:** run the publish target. Working directory: `/Users/ftosetto/Projects/gcp-spend-report`.

  ```
  cd /Users/ftosetto/Projects/gcp-spend-report && make publish MONTH=YYYY-MM
  ```

  Where `YYYY-MM` is the current month. Surface the command output. If it fails on auth (`gcloud auth application-default login` not done) or env vars, tell the user verbatim and stop.

### Phase 3 — Load and analyse

Load the freshest `metrics/gcp-spend/YYYY-MM.html` and `metrics/gcp-spend/index.html`. Open the analysis conversation. Cover:

- Total spend for the month vs prior months (anomalies, trend)
- Cost per app — biggest movers, what shipped that month that might explain them
- AI cost attribution — flag the `$/MAU` caveat from `reference_app_ai_cost_attribution.md`: GCP dashboard $/MAU is GCP-only, so Tattooist routes AI through GCP but AI Home Design uses a separate provider; do not compare $/MAU across apps without this caveat
- Pending apps not yet active

Ask the user what they want to dig into rather than dumping everything.

---

## External project

The tool is self-contained at `/Users/ftosetto/Projects/gcp-spend-report/`:

- `python run.py --month YYYY-MM [--publish]` — render the focal month and dashboard; `--publish` also copies them into `em-hub/metrics/gcp-spend/`
- `make report` / `make publish` — same, with the previous month as default
- `make setup` — install requirements and run ADC login (one-time)

The sibling path coupling is hardcoded. If you ever move either project, publish will warn and exit 0 — the report still renders, it just doesn't reach em-hub.
