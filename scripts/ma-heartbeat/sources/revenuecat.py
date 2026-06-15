#!/usr/bin/env python3
"""
RevenueCat — MRR.

Env: REVENUECAT_API_KEY (v2 secret key, Bearer).
VERIFY the metrics-overview response shape against your account during the
validation window.
"""

import os

from .common import http_get_json, log


def fetch_mrr(app):
    """Monthly recurring revenue (EUR), via RevenueCat v2 metrics overview.

    Returns a float on success, or None (missing config/access/bad response).
    """
    project = app.get("revenuecat_project")
    key = os.environ.get("REVENUECAT_API_KEY")
    if not project or not key:
        return None
    url = f"https://api.revenuecat.com/v2/projects/{project}/metrics/overview"
    data = http_get_json(url, {
        "Authorization": f"Bearer {key}",
        "Accept": "application/json",
    })
    if not data:
        return None
    # The overview returns a list of metric objects; pull the one id == "mrr".
    for metric in data.get("metrics", []):
        if metric.get("id") == "mrr":
            return round(float(metric.get("value", 0)), 2)
    log(f"mrr metric not in RevenueCat overview for {app['name']}")
    return None
