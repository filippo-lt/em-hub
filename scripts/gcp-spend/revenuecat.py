"""
RevenueCat revenue fetcher for the GCP spend dashboard.

Reads revenuecat.conf (one row per app with a RevenueCat project + credential),
loads env vars from .env at the script root, and fetches net proceeds per month
per app via RevenueCat's Charts API v2.

Returned shape (consumed by run.py):
    {
      "Chat Ultra": {"202605": 192114.51, "202606": 188958.87, "202607": None},
      ...
    }

None means "not known for that month" — either unavailable, or a period
RevenueCat still considers unsettled. Apps without a row in revenuecat.conf are
absent from the dict.

The API contract this implements was verified against a live account on
2026-08-03; see docs/superpowers/specs/2026-08-03-gcp-spend-revenuecat-design.md.
"""

from __future__ import annotations

import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

from amplitude import load_dotenv


API_BASE = "https://api.revenuecat.com/v2"

# The charts domain allows 15 requests/minute. One call per app fired in a burst
# would breach that with a full portfolio, so space them out. Worst case this
# adds roughly 75s to a monthly report run.
THROTTLE_SECONDS = 4.1

REQUEST_TIMEOUT = 30

# "proceeds" is revenue after refunds, minus the stores' taxes and commission —
# the money actually received. The API default is "revenue" (gross), which would
# overstate the denominator of the cost ratio.
REVENUE_SELECTOR = '{"revenue_type":"proceeds"}'

# The API returns whole currency units, not cents.
VALUE_SCALE = 1.0

# Series index 0 is the money. 1 is transaction count, 2 is ad impressions.
PRIMARY_MEASURE = 0


@dataclass(frozen=True)
class RevenueCatApp:
    friendly_name: str
    project_id:    str
    api_key:       str


def load_revenuecat_config(path: Path, dotenv_path: Path) -> list[RevenueCatApp]:
    if not path.exists():
        return []
    load_dotenv(dotenv_path)

    apps: list[RevenueCatApp] = []
    for lineno, raw in enumerate(path.read_text().splitlines(), start=1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        parts = [p.strip() for p in line.split("|")]
        if len(parts) != 3:
            sys.exit(
                f"{path}:{lineno}: expected 3 pipe-delimited fields, got {len(parts)}\n"
                f"  line: {raw}"
            )
        name, project_id, key_env = parts
        if not project_id:
            print(f"  ⚠ {name}: no RevenueCat project id — skipping", file=sys.stderr)
            continue
        api_key = os.environ.get(key_env, "")
        if not api_key:
            print(f"  ⚠ {name}: env var {key_env} not set — skipping", file=sys.stderr)
            continue
        apps.append(RevenueCatApp(name, project_id, api_key))
    return apps


def parse_chart_response(payload: dict, months: list[str]) -> dict[str, float | None]:
    """Map a /charts/revenue response onto {yyyymm: net_proceeds | None}.

    Every requested month is present as a key so callers never have to
    distinguish "absent" from "unknown". Periods RevenueCat still considers
    unsettled are left as None: their value is real but partial, and plotting it
    would understate revenue in the freshest month — exactly where the
    cost/revenue ratio is read.
    """
    out: dict[str, float | None] = {m: None for m in months}
    for entry in payload.get("values") or []:
        if entry.get("measure") != PRIMARY_MEASURE:
            continue
        if entry.get("incomplete"):
            continue
        cohort = entry.get("cohort")
        value  = entry.get("value")
        if cohort is None or value is None:
            continue
        yyyymm = datetime.fromtimestamp(int(cohort), tz=timezone.utc).strftime("%Y%m")
        if yyyymm not in out:
            continue
        out[yyyymm] = round(float(value) * VALUE_SCALE, 2)
    return out


def _month_bounds(months: list[str]) -> tuple[str, str]:
    """('202605', ..., '202607') → ('2026-05-01', '2026-07-31')."""
    first, last = months[0], months[-1]
    start = f"{first[:4]}-{first[4:]}-01"
    y, m = int(last[:4]), int(last[4:])
    nxt = date(y + 1, 1, 1) if m == 12 else date(y, m + 1, 1)
    return start, (nxt - timedelta(days=1)).isoformat()


def _fetch_chart(app: RevenueCatApp, months: list[str]) -> dict | None:
    """One Charts API call covering the whole window. None on any failure."""
    start, end = _month_bounds(months)
    params = {
        "start_date": start,
        "end_date":   end,
        "resolution": "month",
        "currency":   "EUR",
        "selectors":  REVENUE_SELECTOR,
    }
    url = f"{API_BASE}/projects/{app.project_id}/charts/revenue?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {app.api_key}",
        "Accept":        "application/json",
    })
    try:
        with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")[:200]
        print(f"  ⚠ {app.friendly_name} revenue: HTTP {e.code} — {body}", file=sys.stderr)
        return None
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as e:
        print(f"  ⚠ {app.friendly_name} revenue: {e}", file=sys.stderr)
        return None


def fetch_all(
    rc_apps: list[RevenueCatApp],
    months: list[str],
    *,
    fetch=None,
    sleep=None,
) -> dict[str, dict[str, float | None]]:
    """Returns {friendly_name: {yyyymm: net_proceeds | None}}.

    An app whose fetch fails is still present, with all-None values — callers
    must not have to tell "failed" apart from "no revenue configured".

    `fetch` and `sleep` are injectable for tests; production omits them.
    """
    if not rc_apps or not months:
        return {}

    fetch = fetch or _fetch_chart
    sleep = sleep or time.sleep

    out: dict[str, dict[str, float | None]] = {}
    print(f"  Fetching RevenueCat data for {len(rc_apps)} app(s), "
          f"{months[0]} → {months[-1]}...", flush=True)

    for i, app in enumerate(rc_apps):
        if i > 0:
            sleep(THROTTLE_SECONDS)
        payload = fetch(app, months)
        series = (parse_chart_response(payload, months) if payload
                  else {m: None for m in months})
        out[app.friendly_name] = series
        latest = series[months[-1]]
        shown = (f"€{latest:,.2f}" if latest is not None
                 else "n/a (unsettled or unavailable)")
        print(f"    {app.friendly_name}: {months[-1]} net proceeds={shown}")
    return out
