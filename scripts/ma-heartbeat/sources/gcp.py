#!/usr/bin/env python3
"""
GCP + studio — monthly cost (EUR).

Cloud spend from the BigQuery billing export (via the `bq` CLI, auth reused)
plus the fixed studio retainer from config. Env: GCP_BILLING_TABLE.
"""

import json
import os

from .common import run, log


def fetch_cost(app):
    """
    Monthly cost = cloud spend + fixed studio retainer.

    Returns the studio figure alone if billing is unreachable (so a
    govern-in-place app still shows its known cost), or None if there is
    neither a billing result nor a studio cost.
    """
    studio_cost = float(app.get("studio_cost_eur") or 0)
    cloud = None
    billing_table = os.environ.get("GCP_BILLING_TABLE")
    billing_filter = app.get("gcp_billing_filter")
    if billing_table and billing_filter:
        sql = f"""
        SELECT ROUND(SUM(cost), 2) AS cost_eur
        FROM `{billing_table}`
        WHERE {billing_filter}
          AND usage_start_time >= TIMESTAMP_TRUNC(CURRENT_TIMESTAMP(), MONTH)
        """
        out = run(["bq", "--quiet", "--format=json", "query",
                   "--nouse_legacy_sql", sql])
        if out:
            try:
                rows = json.loads(out)
                if rows and rows[0].get("cost_eur") is not None:
                    cloud = float(rows[0]["cost_eur"])
            except (json.JSONDecodeError, KeyError, IndexError, TypeError):
                log(f"could not parse GCP cost for {app['name']}")
    if cloud is None and studio_cost == 0:
        return None
    return round((cloud or 0) + studio_cost, 2)
