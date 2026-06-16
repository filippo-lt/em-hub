#!/usr/bin/env python3
"""
RevenueCat — MRR.

Env (v2 secret key, Bearer), checked in order:
    <APP>_REVENUECAT_API_KEY   per-app key, e.g. CHATULTRA_REVENUECAT_API_KEY
    REVENUECAT_API_KEY         global fallback (one key for the whole portfolio)

Per-app keys let apps that live in separate RevenueCat accounts each carry their
own credential; the global key still works when one account covers everything.
VERIFY the metrics-overview response shape against your account during the
validation window.
"""

import os
import re

from .common import http_get_json, log


def _api_key(app):
    """Per-app env key (CHATULTRA_REVENUECAT_API_KEY) first, then the global one."""
    slug = re.sub(r"[^A-Z0-9]", "", app["name"].upper())
    return (os.environ.get(f"{slug}_REVENUECAT_API_KEY")
            or os.environ.get("REVENUECAT_API_KEY"))


def fetch_mrr(app):
    """Monthly recurring revenue (EUR), via RevenueCat v2 metrics overview.

    Returns a float on success, or None (missing config/access/bad response).
    """
    project = app.get("revenuecat_project")
    key = _api_key(app)
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
