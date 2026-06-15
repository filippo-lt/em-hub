#!/usr/bin/env python3
"""
Crashlytics — crash-free % (the load-bearing metric).

No public Crashlytics REST API exists; the supported path is the Firebase
Crashlytics BigQuery export, queried via the `bq` CLI (auth reused).
"""

import json

from .common import run, log


def fetch_crash_free(app):
    """
    Crash-free users % over the trailing 7 days, from the Crashlytics export.

    crash-free % is NOT a column in the export; it is derived:
        100 * (1 - distinct_crashing_users / distinct_active_users)
    distinct_active_users is not in the crash export, so this query approximates
    against the export's own user set unless you point active-user counts at a
    DAU table. VERIFY this query against your schema during validation.

    Returns a float on success, or None (no table configured / bq unavailable).
    """
    table = app.get("crashlytics_bq_table")
    if not table:
        return None
    sql = f"""
    SELECT ROUND(100 * (1 - SAFE_DIVIDE(
             COUNT(DISTINCT IF(event_name = 'crash', user.id, NULL)),
             COUNT(DISTINCT user.id))), 2) AS crash_free_pct
    FROM `{table}`
    WHERE event_timestamp >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 7 DAY)
    """
    out = run(["bq", "--quiet", "--format=json", "query", "--nouse_legacy_sql", sql])
    if not out:
        return None
    try:
        rows = json.loads(out)
        return float(rows[0]["crash_free_pct"]) if rows else None
    except (json.JSONDecodeError, KeyError, IndexError, TypeError):
        log(f"could not parse crash-free for {app['name']}")
        return None
