# GCP Spend Report

Generates self-contained HTML reports of monthly GCP spend across all your
apps. Two artefacts per run:

1. **`reports/YYYY-MM.html`** — Focused detail of the requested month, with one
   tab per app and a per-service breakdown.
2. **`reports/index.html`** — Multi-month dashboard with:
   - Stacked-bar hero showing the last N months of total spend, coloured by app
     (clickable: each bar links to that month's detail report)
   - Per-app cards with 12-month sparkline, current total, and MoM %
   - Wide table of the last 6 months with column totals + per-row average + Δ

Everything lives under `scripts/gcp-spend/`.

## Folder layout

```
scripts/gcp-spend/
├── run.py              ← entrypoint
├── config.conf         ← app → BigQuery dataset mapping
├── query.sql.j2        ← BigQuery query (Jinja2 template)
├── template.html.j2    ← monthly detail HTML
├── dashboard.html.j2   ← multi-month dashboard HTML
├── requirements.txt
├── README.md           ← this file
└── reports/            ← generated output
    ├── 2026-04.html
    ├── 2026-05.html
    └── index.html      ← the dashboard
```

## How it works

```
config.conf       ──┐
                    ├──►  run.py  ──►  BigQuery  ─┬─►  reports/YYYY-MM.html   (focused)
template.html.j2  ──┤    (one job,                │
dashboard.html.j2 ──┤     N months)               └─►  reports/index.html     (dashboard)
query.sql.j2      ──┘
```

- One row per app in `config.conf` (pipe-delimited).
- A single BigQuery job fetches N months of history (default 12); the same rows
  feed both the monthly report and the dashboard.
- All charts are server-side inline SVG — no JavaScript anywhere.
- "Net cost" = `cost + SUM(credits)`. Credits are stored as negative values, so this
  matches what hits the invoice.
- Filter is on `invoice.month` (YYYYMM), the canonical "billed this month" partition.

## One-time setup

```bash
make gcp-spend-setup
```

Installs deps and runs `gcloud auth application-default login`.

Your ADC identity needs `bigquery.dataViewer` + `bigquery.jobUser` on every
project listed in `config.conf` (status=active). If you can `bq ls`
each project's `billing_export_data` dataset, you already have what's needed.

## Run

```bash
make gcp-spend                    # last completed calendar month
make gcp-spend MONTH=2026-04      # specific focal month
make gcp-spend-open               # open the dashboard (reports/index.html)
```

Each run regenerates both the focal month's detail report and the dashboard.
The dashboard always shows N months of history ending at `MONTH`.

Direct CLI for the extra flags:

```bash
python scripts/gcp-spend/run.py --month 2026-04
python scripts/gcp-spend/run.py --month 2026-04 --history-months 6
python scripts/gcp-spend/run.py --month 2026-04 --billing-project imote-prod
```

Query cost is well under the 1 TB / month free tier regardless of which project
it bills to.

## Adding a new app

When billing export is enabled on a project, flip its status in
`config.conf` from `pending` to `active` and add the billing
account ID:

```diff
-Chat Ultra | chat-ultra-appbot | billing_export_data | TBD                  | pending
+Chat Ultra | chat-ultra-appbot | billing_export_data | XXXXXX-XXXXXX-XXXXXX | active
```

Next run will include the app automatically.

To find a project's billing account ID:

```bash
gcloud billing projects describe <PROJECT_ID> --format="value(billingAccountName)"
```

## Notes & caveats

- **No backfill.** Data only exists from the moment billing export was first enabled.
  Months before that will show 0 (or be missing) for that app.
- **Up to 24h lag.** A report run for "this month so far" may miss the last day's data.
  Running for *completed* months is recommended.
- **Detailed (resource-level) export** is assumed (table prefix `gcp_billing_export_resource_v1_`).
  If you ever switch to standard export, update the prefix in `query.sql.j2`.
- **Currency.** Report assumes a single currency across all billing accounts. A warning
  is printed if more than one is detected.
- **Free-tier safe.** Querying ~12 tables for one month stays well under the 1 TB/month
  free BigQuery quota.
