# Firebase Remote Config fetch report

Rolling **client fetch** volume per Firebase/GCP project (`FetchRemoteConfig`), pulled from Cloud Monitoring.

## Setup

```bash
cd scripts/firebase-remoteconfig
make setup
gcloud auth application-default login   # if not already done
```

Your identity needs **Monitoring Viewer** (`roles/monitoring.viewer`) on each project in `config.conf`.

## Run

```bash
make report              # writes reports/index.html + reports/latest.json
make publish             # also copies into ../../metrics/firebase-remoteconfig/
make share               # publish + dated share bundle under ../../outputs/firebase-remoteconfig/
```

Options:

```bash
python run.py --days 30 --workers 8 --publish --share
```

## Amplitude cross-reference (optional)

`--with-amplitude` joins prod rows with **monthly active users (MAU)** from Amplitude and adds two columns:

- **MAU** — latest available month in the window
- **Fetches/user/day** — `avg_daily_fetches ÷ MAU`

This is the engineering-health signal the raw fetch count can't give you: ~1.0 means each active user triggers one fetch per day (healthy, cached); values well above 1 point at over-fetching, a missing client-side cache, or a retry loop.

```bash
make report-amp          # report + MAU columns
make publish-amp         # publish + MAU columns
make share-amp           # share bundle + canvas + MAU columns
```

### Prerequisites

1. **Amplitude credentials** in `em-hub/.env` (one pair per app). See `scripts/gcp-spend/amplitude.conf` for the env-var names.
2. **An entry in `scripts/gcp-spend/amplitude.conf`** for each app you want joined. Apps without an entry show `—` in the MAU columns (the report still renders).

### Name aliasing

`config.conf` (Firebase) and `amplitude.conf` use slightly different friendly names for the same app. The alias map lives in `run.py` (`AMP_NAME_ALIAS`). Add a row there when you wire up a new app whose names differ on the two sides. Direct matches (`FaceAI`, `iMote`, `ScreenMirroring`) need no entry.

### Coverage gaps (as of 2026-07)

| Firebase app | Amplitude? |
|--------------|------------|
| AI Design    | ✓ (as "AI Home Design") |
| FaceAI       | ✓ |
| iMote        | ✓ |
| ScreenMirroring | ✓ |
| ChatUltra    | ✓ (as "Chat Ultra") |
| Music Player | ✗ (TODO in amplitude.conf) |
| Step Counter | ✗ (no Amplitude project) |
| PDF Editor   | ✗ (TODO in amplitude.conf) |

Dev rows are never joined — Amplitude MAU is prod-only.

## Sharing

`make share` writes two **standalone** files (no external deps):

- `outputs/firebase-remoteconfig/YYYY-MM-DD_remote-config-fetches.html` — attach or upload (Drive, Notion, etc.)
- `outputs/firebase-remoteconfig/YYYY-MM-DD_remote-config-fetches.md` — paste highlights into Slack/email; references the HTML filename

The HTML includes print styles (browser → Print → PDF if you need a PDF).

## Cursor dashboard

`make share` (or `python run.py --canvas`) writes **`remote-config-fetches.canvas.tsx`** to:

1. **Cursor canvases folder** for this workspace — open it from the Canvas panel beside chat.
2. **`metrics/firebase-remoteconfig/`** — commit this copy so teammates can copy it into their own `~/.cursor/projects/<workspace>/canvases/`.

Canvas data is embedded inline at generation time. Re-run `make share` locally before sharing an updated copy.

**Operator note:** `metrics/firebase-remoteconfig/` updates when you run `make publish` or `make share`.

## Config

Edit `config.conf`:

```
FRIENDLY_NAME | GCP_PROJECT_ID | dev|prod | active|skip
```

## Metric

- API: `firebaseremoteconfig.googleapis.com`
- Method: `google.firebase.remoteconfig.v1.RemoteConfigService.FetchRemoteConfig`
- Cloud Monitoring type: `serviceruntime.googleapis.com/api/request_count`

This matches the **Fetch Requests** SKU used for Remote Config quota/billing.

## Cost estimate (Blaze)

Per [Firebase Remote Config pricing](https://firebase.google.com/docs/remote-config/pricing):

| Daily fetches | Cost |
|---------------|------|
| 0 – 100,000 | $0 |
| 100,001 – 10,000,000 | $0.06 / 10K requests |
| &gt; 10,000,000 | $0.01 / 10K requests |

**Est. monthly cost (Blaze)** = average tiered daily bill over the report window × 30.
Spark-plan overage is throttled, not billed; the column is a Blaze what-if for planning.
