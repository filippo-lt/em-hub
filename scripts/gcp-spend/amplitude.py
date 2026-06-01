"""
Amplitude MAU + new-user fetcher for the GCP spend dashboard.

Reads amplitude.conf (one row per app with Amplitude credentials), loads
env vars from .env at repo root, and fetches active+new user counts per
month per app via Amplitude's Dashboard REST API.

Returned shape (consumed by run.py):
    {
      "Tattooist": {
        "202505": {"active": 194937, "new": 12034},
        "202504": {"active": 188101, "new": 11200},
        ...
      },
      ...
    }

Apps without a row in amplitude.conf are absent from the dict.
"""

from __future__ import annotations

import base64
import json
import os
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


REGION_HOSTS = {
    "eu": "https://analytics.eu.amplitude.com",
    "us": "https://amplitude.com",
}


@dataclass(frozen=True)
class AmplitudeApp:
    friendly_name: str
    region:        str
    api_key:       str
    secret_key:    str


def load_dotenv(path: Path) -> None:
    """Minimal .env loader — no external dependency. Does not override existing env."""
    if not path.exists():
        return
    for raw in path.read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        v = v.strip().strip('"').strip("'")
        os.environ.setdefault(k.strip(), v)


def load_amplitude_config(path: Path, dotenv_path: Path) -> list[AmplitudeApp]:
    if not path.exists():
        return []
    load_dotenv(dotenv_path)

    apps: list[AmplitudeApp] = []
    for lineno, raw in enumerate(path.read_text().splitlines(), start=1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        parts = [p.strip() for p in line.split("|")]
        if len(parts) != 4:
            sys.exit(
                f"{path}:{lineno}: expected 4 pipe-delimited fields, got {len(parts)}\n"
                f"  line: {raw}"
            )
        name, region, key_env, secret_env = parts
        if region not in REGION_HOSTS:
            sys.exit(f"{path}:{lineno}: region must be 'eu' or 'us', got '{region}'")
        api_key    = os.environ.get(key_env, "")
        secret_key = os.environ.get(secret_env, "")
        if not api_key or not secret_key:
            print(f"  ⚠ {name}: env vars {key_env}/{secret_env} not set — skipping",
                  file=sys.stderr)
            continue
        apps.append(AmplitudeApp(name, region, api_key, secret_key))
    return apps


def _yyyymm_first_day(yyyymm: str) -> str:
    return f"{yyyymm}01"


def _yyyymm_last_day(yyyymm: str) -> str:
    """Return YYYYMMDD for the last day of yyyymm."""
    y, m = int(yyyymm[:4]), int(yyyymm[4:])
    if m == 12:
        next_y, next_m = y + 1, 1
    else:
        next_y, next_m = y, m + 1
    from datetime import date, timedelta
    last = date(next_y, next_m, 1) - timedelta(days=1)
    return last.strftime("%Y%m%d")


def _xvalue_to_yyyymm(xv: str) -> str:
    """Amplitude returns 'YYYY-MM-DD' for each bucket start. We bucket monthly."""
    return datetime.strptime(xv, "%Y-%m-%d").strftime("%Y%m")


def _fetch_metric(app: AmplitudeApp, metric: str, start_yyyymm: str, end_yyyymm: str) -> dict[str, int]:
    """
    metric: 'active' | 'new'
    Returns {yyyymm: count}. Empty dict on failure (logs to stderr).
    """
    host  = REGION_HOSTS[app.region]
    start = _yyyymm_first_day(start_yyyymm)
    end   = _yyyymm_last_day(end_yyyymm)
    url   = f"{host}/api/2/users?start={start}&end={end}&m={metric}&i=30"

    creds = f"{app.api_key}:{app.secret_key}".encode("utf-8")
    auth  = base64.b64encode(creds).decode("ascii")
    req   = urllib.request.Request(url, headers={"Authorization": f"Basic {auth}"})

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")[:200]
        print(f"  ⚠ {app.friendly_name} {metric}: HTTP {e.code} — {body}", file=sys.stderr)
        return {}
    except (urllib.error.URLError, TimeoutError) as e:
        print(f"  ⚠ {app.friendly_name} {metric}: {e}", file=sys.stderr)
        return {}

    data = payload.get("data") or {}
    x_values = data.get("xValues") or []
    series   = (data.get("series") or [[]])[0]
    out: dict[str, int] = {}
    for xv, count in zip(x_values, series):
        out[_xvalue_to_yyyymm(xv)] = int(count or 0)
    return out


def fetch_all(
    amp_apps: list[AmplitudeApp],
    months: list[str],
) -> dict[str, dict[str, dict[str, int]]]:
    """
    Returns: {friendly_name: {yyyymm: {"active": N, "new": N}}}

    Active users: one window-wide call (Amplitude buckets correctly per month).
    New users: one call PER MONTH so the "first-seen during query range" semantics
    collapse to "first-seen this month" — the count we actually want.
    """
    if not amp_apps or not months:
        return {}

    start_yyyymm = months[0]
    end_yyyymm   = months[-1]
    out: dict[str, dict[str, dict[str, int]]] = {}

    print(f"  Fetching Amplitude data for {len(amp_apps)} app(s), "
          f"{months[0]} → {months[-1]}...", flush=True)
    for app in amp_apps:
        active = _fetch_metric(app, "active", start_yyyymm, end_yyyymm)
        new: dict[str, int] = {}
        for m in months:
            month_new = _fetch_metric(app, "new", m, m)
            new[m] = month_new.get(m, 0)
        per_month: dict[str, dict[str, int]] = {}
        for m in months:
            per_month[m] = {"active": active.get(m, 0), "new": new.get(m, 0)}
        out[app.friendly_name] = per_month
        last = per_month[months[-1]]
        print(f"    {app.friendly_name}: {months[-1]} active={last['active']:,} new={last['new']:,}")
    return out
