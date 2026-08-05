# GCP spend report — headless setup (one-time)

This is the vendored, self-contained copy of the GCP spend tool. It lives inside
em-hub so the monthly refresh job can reach and run it. Auth prefers a
**service-account key**; if the key file is absent, `run.py` falls back to
gcloud **Application Default Credentials** (`gcloud auth application-default login`),
so the tool works before the key is set up — the key just makes it durable.

You only do this once. After that, the monthly report generates itself.

---

## What's already wired

- The tool is at `em-hub/scripts/gcp-spend/` (this folder).
- `.env` here holds your Amplitude keys (copied from `~/Projects/gcp-spend-report`)
  and your RevenueCat secret keys (`<APP>_REVENUECAT_API_KEY`, e.g.
  `CHATULTRA_REVENUECAT_API_KEY`). RevenueCat is optional: apps without a key are
  skipped with a warning and the report renders without revenue for them.
  and a line `GCP_SA_KEY_FILE=secrets/gcp-sa-key.json`.
- `run.py` loads that `.env` before building the BigQuery client and resolves the
  key path to an absolute path at runtime, so the same `.env` works both on your
  Mac and inside the scheduled sandbox.
- `.env` and `secrets/` are gitignored — they never get committed or pushed.

The **only** missing piece is the key file itself. That's the step below.

---

## Step 1 — Create a service account (GCP console)

1. Go to the GCP project the BigQuery query is billed to. `run.py` bills the job
   to the **first active app** in `config.conf`, currently **`imote-prod`**.
   (You can override with `--billing-project`, but `imote-prod` is the default.)
2. IAM & Admin → **Service Accounts** → **Create service account**.
   - Name: e.g. `em-hub-gcp-spend`.
3. Grant it the roles it needs to read the billing-export tables:
   - **BigQuery Job User** (`roles/bigquery.jobUser`) on the billing project
     (`imote-prod`) — lets it run queries.
   - **BigQuery Data Viewer** (`roles/bigquery.dataViewer`) on every project whose
     `billing_export_data` dataset it reads (see `config.conf` — `imote-prod`,
     `aihomedesign-prod`, `tattooist-prod`, etc.). Granting Data Viewer at the
     **org or folder** level is the simplest way to cover all of them at once.

## Step 2 — Download a JSON key

1. Open the new service account → **Keys** → **Add key** → **Create new key** →
   **JSON** → Create. A `.json` file downloads.
2. Move it to exactly:

   ```
   em-hub/scripts/gcp-spend/secrets/gcp-sa-key.json
   ```

   (The folder is gitignored; the filename must match what `.env` points to.)

## Step 3 — Test it

From `em-hub/scripts/gcp-spend/`:

```bash
make setup                     # install deps (once per machine)
make publish MONTH=2026-06      # render + copy into ../../metrics/gcp-spend/
```

Success looks like: it prints the app tally, runs the BigQuery job, and writes
`YYYY-MM.html`, `index.html`, and `YYYY-MM.json` into `em-hub/metrics/gcp-spend/`.
If it complains the key file isn't found, the path or filename doesn't match
`GCP_SA_KEY_FILE` in `.env`.

---

## After setup

- The **local launchd job** (`com.ftosetto.emhub.gcp-spend-refresh` — plist
  versioned in this folder) runs `monthly-refresh.sh` on the **2nd of each month
  at 07:00**: builds last month's report, publishes it into
  `em-hub/metrics/gcp-spend/`, and commits + pushes the artifacts. Install once:

  ```bash
  cp scripts/gcp-spend/com.ftosetto.emhub.gcp-spend-refresh.plist ~/Library/LaunchAgents/
  launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.ftosetto.emhub.gcp-spend-refresh.plist
  ```

  Logs go to `scripts/gcp-spend/logs/refresh-YYYY-MM.log` (gitignored). If the
  Mac is asleep at 07:00, launchd runs the job on wake.
- The **"Monthly cost digest" cloud routine** (claude.ai/code/routines) runs on
  the 2nd about an hour later, clones em-hub from GitHub, reads the published
  `metrics/gcp-spend/` files, and leaves a **Gmail draft** digest (never sends).
  If the data isn't fresh it drafts an alert instead.
- The **`/gcp-spend` skill** and the **M&A heartbeat** both read the published
  `metrics/gcp-spend/` files, including the `YYYY-MM.json` export.
- The separate `~/Projects/gcp-spend-report` repo is now redundant for the
  automation — you can keep it as a scratch/dev copy or retire it. This vendored
  copy is the source of truth going forward.

## Security note

Two secrets now live in this folder (both gitignored): the Amplitude keys in
`.env` and the GCP service-account key in `secrets/`. If you'd rather not have the
Amplitude keys duplicated here, you can blank them in `.env` — the report still
runs; app cards just show "—" for MAU instead of user counts.
