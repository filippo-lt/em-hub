#!/usr/bin/env python3
"""
Amplitude — MAU (trailing 30-day active users).

Env: AMPLITUDE_API_KEY, AMPLITUDE_SECRET_KEY (HTTP Basic), AMPLITUDE_REGION
("us" default, or "eu"). VERIFY the Dashboard REST response shape against your
account during the validation window.
"""

import os
from base64 import b64encode
from datetime import datetime, timedelta, timezone

from .common import http_get_json, log


def fetch_mau(app):
    """Monthly active users, via Amplitude Dashboard REST API.

    Returns an int on success, or None (missing config/access/bad response).
    """
    api_key = os.environ.get("AMPLITUDE_API_KEY")
    secret = os.environ.get("AMPLITUDE_SECRET_KEY")
    if not app.get("amplitude_app_id") or not api_key or not secret:
        return None
    region = os.environ.get("AMPLITUDE_REGION", "us").lower()
    host = "analytics.eu.amplitude.com" if region == "eu" else "amplitude.com"
    end = datetime.now(timezone.utc).date()
    start = end - timedelta(days=30)
    url = (
        f"https://{host}/api/2/users"
        f"?start={start:%Y%m%d}&end={end:%Y%m%d}&m=active&i=30"
    )
    token = b64encode(f"{api_key}:{secret}".encode()).decode()
    data = http_get_json(url, {"Authorization": f"Basic {token}"})
    if not data:
        return None
    try:
        # series is a list of buckets; with i=30 we expect the trailing one.
        series = data["data"]["series"][0]
        return int(series[-1])
    except (KeyError, IndexError, TypeError):
        log(f"unexpected Amplitude shape for {app['name']}")
        return None
