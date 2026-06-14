#!/usr/bin/env python3
"""
Cost + MAU — sourced from the gcp-spend report (the single source of truth).

GCP cost-per-app and Amplitude MAU-per-app are already extracted by the
`gcp-spend-report` tool (its `query.sql.j2` + `amplitude.conf`), with the
per-app attribution method and the GCP-only `$/MAU` caveat baked in. We do NOT
re-query billing or Amplitude here — that duplicated and diverged from the
canonical numbers. Instead we read the structured export the tool publishes
next to its HTML.

Export contract (the gcp-spend-report publish step must also write this file):
    metrics/gcp-spend/<YYYY-MM>.json
    {
      "month": "2026-06",
      "generated_at": "2026-06-14T09:00:00Z",
      "apps": {
        "chatultra": { "cost_eur": 1234.56, "mau": 45000 },
        "pdfeditor": { "cost_eur":  210.00, "mau":  8000 },
        ...
      }
    }

Heartbeat apps map to a report key via `gcp_spend_key` in config. The export is
monthly; the weekly heartbeat reports the latest known monthly value (flat
within a month — accurate, just coarse-grained, which is fine for cost/MAU).
Missing file or missing key → None → `n/a (no access)`.
"""

import json
from functools import lru_cache
from pathlib import Path

from .common import log

# scripts/ma-heartbeat/sources/gcp_spend.py → parents[3] = repo root
METRICS_DIR = Path(__file__).resolve().parents[3] / "metrics" / "gcp-spend"


@lru_cache(maxsize=1)
def _latest_export():
    """Parse the newest metrics/gcp-spend/<YYYY-MM>.json. Returns {} on miss."""
    if not METRICS_DIR.exists():
        return {}
    candidates = sorted(METRICS_DIR.glob("[0-9][0-9][0-9][0-9]-[0-9][0-9].json"))
    if not candidates:
        log("no gcp-spend JSON export found — run gcp-spend with the export step")
        return {}
    try:
        return json.loads(candidates[-1].read_text()).get("apps", {})
    except (json.JSONDecodeError, OSError) as e:
        log(f"could not read gcp-spend export {candidates[-1].name}: {e}")
        return {}


def _lookup(app, field):
    key = app.get("gcp_spend_key")
    if not key:
        return None
    entry = _latest_export().get(key)
    if not entry or entry.get(field) is None:
        return None
    return entry[field]


def fetch_cost(app):
    """Monthly cost (EUR) for this app, from the gcp-spend export."""
    return _lookup(app, "cost_eur")


def fetch_mau(app):
    """Monthly active users for this app, from the gcp-spend export."""
    return _lookup(app, "mau")
