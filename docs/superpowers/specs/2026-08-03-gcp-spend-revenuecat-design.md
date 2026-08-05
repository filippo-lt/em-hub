# GCP spend report — RevenueCat revenue correlation

**Date:** 2026-08-03
**Tool:** `scripts/gcp-spend/`
**Status:** Design approved, pending implementation plan

---

## Problem

The GCP spend report answers "what do we spend, and how does it move." It cannot
answer "is infrastructure spend growing faster than the revenue it supports."
That second question is the efficiency signal — the one that tells us an app is
degrading economically before the cost line alone looks alarming.

Today the report has spend (BigQuery billing export) and usage (Amplitude MAU +
new users), which yields `$/MAU`. `$/MAU` is a usage-efficiency metric, not an
economic one: an app can have flat `$/MAU` while its revenue per user collapses.

## Goal

Add per-app monthly revenue from RevenueCat so the report can show **infra cost
as a percentage of net proceeds**, tracked over the same rolling window as
spend, and surface month-over-month degradation in that ratio.

## Non-goals

- **This is not a margin or P&L report.** Net proceeds minus GCP spend is not
  profit. It excludes user acquisition, salaries, non-GCP AI vendors, and
  RevenueCat's own fee. The metric is deliberately named "infra cost as % of net
  proceeds" so it cannot be read as margin.
- **Portfolio keep/kill decisions.** Those need full COGS. Out of scope.
- **Changing the M&A heartbeat.** See "Follow-up" below.

---

## Data source

RevenueCat Charts API v2:

```
GET https://api.revenuecat.com/v2/projects/{project_id}/charts/revenue
    ?start_date=YYYY-MM-01
    &end_date=YYYY-MM-DD
    &resolution=month
    &currency=EUR
    &selectors=<proceeds-net-of-taxes-and-commissions>
Authorization: Bearer sk_...
```

Constraints and behaviours that shape the design:

| Property | Consequence |
| --- | --- |
| Requires RevenueCat **Pro** plan | Hard prerequisite; no key, no feature |
| Rate limit **15 req/min** on the charts domain | Throttle between apps (see below) |
| Periods still settling return `incomplete: true` | Must be dropped, not plotted |
| Response `values[]` has `measure` index | Filter to `measure == 0` (primary series) |
| `cohort` is a Unix timestamp in seconds | Convert to the report's `YYYYMM` key |
| `currency` parameter accepted | Request `EUR` to match the export's `cost_eur` |
| Chart names and selector values in the docs are unreliable | Discover via the options endpoint before hardcoding |

**Resolved 2026-08-03** by probing the live API — see "Verified API contract"
below. The net-proceeds selector exists and the account has the required plan.

## Verified API contract (2026-08-03)

Probed against project `67002caa` (Chat Ultra) using
`CHATULTRA_REVENUECAT_API_KEY` from the repo-root `.env`.

**Working request:**

```
GET https://api.revenuecat.com/v2/projects/67002caa/charts/revenue
    ?start_date=2025-08-01
    &end_date=2026-08-03
    &resolution=month
    &currency=EUR
    &selectors={"revenue_type":"proceeds"}
Authorization: Bearer sk_...
```

| Question | Answer |
| --- | --- |
| Pro plan active? | **Yes** — `/charts/revenue` returns HTTP 200 |
| Net-proceeds selector | `selectors={"revenue_type":"proceeds"}`. The `revenue_type` user-selector offers `revenue`, `revenue_net_of_taxes`, `proceeds`; default is `revenue` |
| Confirmation it applied | `measures[0].display_name == "Proceeds"`, described as "total revenue after refunds, minus our estimate of revenue deducted from the stores for taxes and commission" |
| `resolution` format | Both `month` and the numeric id `2` work; the response echoes `"resolution": "month"` |
| Currency honoured? | **Yes** — response carries `"yaxis_currency": "EUR"`. Ignore `"yaxis": "$"`, which is a display glyph only |
| Value units | **Whole currency units, not cents.** `VALUE_SCALE = 1.0` |
| Incomplete flag | Per-entry boolean inside `values[]`: `{"cohort": ..., "incomplete": true, "measure": 0, "value": ...}` |
| `cohort` | Unix timestamp in seconds, UTC, at period start |
| Measures | **Three**, not two: `0` = Proceeds, `1` = Transactions, `2` = Ad Impressions. Filtering to `measure == 0` remains correct |

**Sample `values[]` excerpt:**

```json
{"cohort": 1754006400, "incomplete": false, "measure": 0, "value": 1365.36}
{"cohort": 1785542400, "incomplete": true,  "measure": 0, "value": 14151.67}
```

**The incomplete trap, observed live.** At the time of probing, Chat Ultra's
July 2026 proceeds were €176,151.01 (settled) and August 2026 read €14,151.67
with `incomplete: true` — a partial month two days in. Plotted as a real value
that is a 92% apparent revenue collapse, which would drive the cost ratio up by
more than a factor of twelve and fire the degradation alarm every single month.
Dropping incomplete periods is not a nicety; it is the difference between a
working signal and a permanently false one.

### Why `incomplete` matters more than it looks

RevenueCat builds these charts from live receipt streams, so the most recent
period is partially settled. The report's target month is normally the freshest
month. Plotting an incomplete revenue figure would depress the denominator and
inflate the cost ratio — firing the exact "spend outpacing revenue" alarm this
feature exists to detect, every month, falsely. Incomplete periods therefore
become `None`, rendering as a gap.

---

## Architecture

### New module: `scripts/gcp-spend/revenuecat.py`

A structural sibling of `amplitude.py`. It owns config parsing, credential
lookup, HTTP, and month bucketing. It never raises into `run.py`.

Public surface, mirroring `amplitude.py`:

```python
@dataclass(frozen=True)
class RevenueCatApp:
    friendly_name: str
    project_id:    str
    api_key:       str

def load_revenuecat_config(path: Path, dotenv_path: Path) -> list[RevenueCatApp]: ...

def fetch_all(
    rc_apps: list[RevenueCatApp],
    months: list[str],
) -> dict[str, dict[str, float | None]]:
    """Returns {friendly_name: {yyyymm: net_proceeds_eur_or_None}}

    The inner dict is keyed by every month in `months`, so callers never have
    to distinguish "month missing" from "month known to be unavailable".
    """
```

One call per app covers the whole window, since `resolution=month` returns the
full range in a single response. Months absent from the response, or flagged
incomplete, map to `None`.

**Throttle:** the charts domain allows 15 requests/minute. With up to 18 apps
configured, a burst would exceed it. Sleep `4.1s` between app calls. Worst case
adds roughly 75 seconds to a run that already takes minutes, which is acceptable
for a monthly report.

`amplitude.py` already owns `load_dotenv`; `revenuecat.py` imports it rather
than duplicating it.

### Config: `scripts/gcp-spend/revenuecat.conf`

Pipe-delimited, matching `amplitude.conf`'s established style:

```
# FRIENDLY_NAME | REVENUECAT_PROJECT_ID | API_KEY_ENV_VAR
Chat Ultra      | projXXXXXXXX          | REVENUECAT_CHATULTRA_KEY
PDF Editor      | projYYYYYYYY          | REVENUECAT_PDFEDITOR_KEY
```

`FRIENDLY_NAME` must match `config.conf` exactly — that string is the join key
across all three data sources.

The file is committed (it holds project IDs and env var *names*, no secrets),
consistent with `amplitude.conf` and `config.conf`. Secret keys live in the
existing gitignored `scripts/gcp-spend/.env`.

Apps missing from the conf, or present with an unset env var, are skipped with a
warning to stderr — identical to Amplitude's behaviour today.

### Aggregation

`AppHistory` gains one field:

```python
revenue_by_month: list[float | None] = field(default_factory=list)
```

`aggregate()` gains a `rev_data` parameter alongside the existing `amp_data`,
populated the same way: present apps get their per-month values, absent apps get
`[None] * len(months)`.

---

## Metric definitions

For each month `m` in the window:

- **`net_proceeds[m]`** — EUR, net of taxes and store commissions. `None` when
  unavailable or incomplete.
- **`cost_ratio[m]`** — `spend[m] / net_proceeds[m] * 100`, expressed as a
  percentage. `None` when `net_proceeds[m]` is `None` or `<= 0`.
- **`cost_ratio_delta_pp`** — `cost_ratio[target] - cost_ratio[target-1]`, in
  percentage points. Positive means infra is consuming a growing share of
  revenue; this is the degradation signal. `None` if either month is `None`.

A single derived ratio and its delta is deliberately the whole metric set. A
separate "spend growth minus revenue growth" figure would express the same idea
in a second unit and give the reader two numbers to reconcile.

---

## Rendering

A per-app `has_revenue` flag (any non-`None` value in `revenue_by_month`) gates
every addition, exactly as `has_amplitude` does today.

### Per-app page (`app.html.j2`)

**KPI strip** — one new tile after `$/MAU`, gated on `has_revenue`:
label `Cost / revenue`, value `cost_ratio` as a percentage, with the existing
`mom up` / `mom down` / `mom flat` treatment driven by `cost_ratio_delta_pp`.
Rising is bad for both spend and this ratio, so the existing colour semantics
carry over unchanged.

**Indexed overlay** — revenue joins as a fourth series in `build_overlay_chart`,
colour `#d97706` (amber; distinct from spend's per-app colour, MAU `#1e8449`,
and new users `#b07aa1`). This chart is where divergence is visible at a glance.

Two changes to how the overlay is gated and built:

1. `build_overlay_chart` picks a *shared* baseline as the max of each series'
   start index. A revenue series that begins late (recently monetised app) would
   drag the baseline right and shrink the useful window for every series. **Rule:
   if revenue has fewer than 3 non-`None` months in the window, omit it from the
   overlay** — it still appears in its own chart and the table.
2. The section is currently inside `{% if has_amplitude %}`. Gating moves to the
   series list itself: build the list conditionally (Spend always; MAU and new
   users if `has_amplitude`; revenue if it survived rule 1), and render the
   section only when **two or more** series remain. A one-series indexed chart is
   a flat line at 100 and carries no information. The heading becomes "Trend
   overlap · indexed to 100".

**New chart** — "Infra cost as % of net proceeds", via `build_line_chart` with a
new `fmt_y="pct"` branch producing `f"{y_val:,.0f}%"` axis labels. The
`render_line_chart` macro gains a matching `fmt="pct"` case for its tooltips.

**Monthly figures table** — two columns gated on `has_revenue`: `Revenue`
(EUR, thousands-separated, no decimals) and `Cost %`. Both render `—` for `None`
months, following the existing empty-cell pattern.

**No-data message** — when `has_revenue` is false, the pattern already used for
Amplitude: a short note pointing at `revenuecat.conf` and the required env var.

### Dashboard (`dashboard.html.j2`)

`dashboard_context` adds `cost_ratio` and `cost_ratio_delta_pp` to each entry in
`apps_ctx`, computed at the target-month index the same way `mom_pct` already is.

Each app card gains a single line below the existing `.row-mau` block, gated on
`app.cost_ratio is not none`: the current cost ratio and its percentage-point
delta. One number per card keeps the dashboard scannable; the per-app page holds
the detail.

---

## Error handling

Every new field is `None`-safe from fetch through to template. Specifically:

- **No `revenuecat.conf`** — `load_revenuecat_config` returns `[]`, the fetch is
  skipped entirely, all apps render as they do today.
- **App not in the conf** — `revenue_by_month` is all `None`, `has_revenue` is
  false, no revenue UI renders for that app.
- **Missing env var** — warning to stderr, app skipped, same as above.
- **HTTP error, timeout, or unparseable response** — warning to stderr, that
  app's data is `{}`, same as above.
- **Zero or negative net proceeds** — `cost_ratio` is `None` rather than a
  division error or an infinite ratio.

No RevenueCat failure can fail the run or affect the spend and Amplitude data.
This matches the existing per-app resilience in `run_queries_per_app`, where a
missing billing export degrades one app rather than the report.

---

## Verification

Following the validation protocol in `scripts/ma-heartbeat/README.md`:

1. Probe `/charts/revenue/options` for one project to confirm the real selector
   and chart name before writing the fetch.
2. Reconcile a full 12-month series for one app against the RevenueCat dashboard
   by eye. Currency, magnitude, and month alignment all have to match.
3. Confirm the target month is dropped when RevenueCat marks it incomplete, and
   appears once it settles.
4. Run against an app with no RevenueCat config and confirm the page is byte-wise
   unchanged from the current output.

---

## Follow-up (out of scope)

`scripts/ma-heartbeat/sources/revenuecat.py` fetches current-snapshot MRR
independently. Once gcp-spend owns historical revenue, the natural next step is
to add `revenue_eur` to the export JSON written by `write_export_json` and have
the heartbeat read it the way it already reads `cost_eur` and `mau`, deleting its
own RevenueCat module. That restores the single-source-of-truth principle stated
in the heartbeat README, which this change otherwise weakens by creating a second
RevenueCat consumer. Worth doing, but as its own change with its own validation.
