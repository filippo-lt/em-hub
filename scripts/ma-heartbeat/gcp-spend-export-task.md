# Task — emit a structured JSON export from gcp-spend-report

**For:** the `gcp-spend-report` project (`~/Projects/gcp-spend-report/`).
**Why:** the M&A Heartbeat consumes cost + MAU per app from this tool instead
of re-querying billing/Amplitude (single source of truth, keeps the per-app
attribution + the GCP-only `$/MAU` caveat). It needs a machine-readable export
alongside the HTML. Contract is defined in
`em-hub/scripts/ma-heartbeat/sources/gcp_spend.py`.

> Written against the documented structure (run.py, Jinja templates,
> `--publish` sibling-path copy into `../em-hub/metrics/gcp-spend/`). Adapt the
> variable names below to whatever the per-app data structure is actually
> called in `run.py`.

## What to add

After the per-app figures are computed (the same data that feeds
`app.html.j2` / the `$/MAU` rows), write a JSON file next to the rendered HTML,
then include it in the publish copy.

1. **Write `reports/<YYYY-MM>.json`** with this exact shape:

   ```json
   {
     "month": "2026-06",
     "generated_at": "2026-06-14T09:00:00Z",
     "apps": {
       "chatultra":   { "cost_eur": 1234.56, "mau": 45000 },
       "pdfeditor":   { "cost_eur":  210.00, "mau":  8000 },
       "stepcounter": { "cost_eur":   80.00, "mau": 12000 },
       "truthseeker": { "cost_eur":    0.00, "mau":     0 },
       "musicplayer": { "cost_eur":   40.00, "mau":  3000 }
     }
   }
   ```

   - `cost_eur` — the per-app cost the report already shows (same number, same
     attribution; do not recompute differently).
   - `mau` — the per-app MAU the report already pulls from Amplitude.
   - Use `null` for a field the report genuinely doesn't have for an app
     (the heartbeat renders missing values as `n/a (no access)`).
   - Extra fields are fine to add (e.g. `ai_cost_per_mau`) — the heartbeat
     ignores what it doesn't read.

2. **App keys must be stable.** Whatever string keys the report uses here are
   what the heartbeat maps to via `gcp_spend_key` in `config/ma-apps.conf`.
   Keep them lowercase and unchanging. Current heartbeat keys:
   `chatultra, pdfeditor, stepcounter, truthseeker, musicplayer`.

3. **Publish it.** The existing publish step copies the rendered HTML into
   `../em-hub/metrics/gcp-spend/`. Copy `<YYYY-MM>.json` the same way, into the
   same directory. Same sibling-path guard: if em-hub isn't present, warn and
   exit 0 (the run still succeeds).

## Acceptance

- `python -c "import json; json.load(open('reports/2026-06.json'))"` succeeds.
- After `make publish MONTH=2026-06`, the file exists at
  `em-hub/metrics/gcp-spend/2026-06.json`.
- From em-hub, the heartbeat reads it:
  ```
  python3 scripts/ma-heartbeat/fetch_heartbeat.py --app ChatUltra --dry-run
  ```
  shows a real Cost + MAU for ChatUltra instead of `n/a (no access)`.

## Optional

- Backfill the existing months (`2026-04`, `2026-05`) so the heartbeat has
  history to compute deltas against on day one.
