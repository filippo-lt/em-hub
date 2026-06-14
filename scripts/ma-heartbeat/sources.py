#!/usr/bin/env python3
"""
M&A Heartbeat — data source fetchers.

One function per source. Every fetcher follows the same contract:

    returns a value on success, or None on any failure (missing access,
    missing config, network error, bad response). A fetcher NEVER raises out
    to the caller — a missing login for one source must not break the run.
    None is rendered downstream as `n/a (no access)`.

Secrets come from environment variables, never from config:
    REVENUECAT_API_KEY        RevenueCat v2 secret key (Bearer)
    AMPLITUDE_API_KEY         Amplitude project API key   (Basic user)
    AMPLITUDE_SECRET_KEY      Amplitude project secret key (Basic pass)
    AMPLITUDE_REGION          "us" (default) or "eu"
    GCP_BILLING_TABLE         fully-qualified BigQuery billing-export table
CLI auth is reused as-is: `gh` (GitHub) and `bq` (BigQuery) must already be
authenticated in the environment.

NOTE — verify-on-first-run: the exact RevenueCat/Amplitude response shapes and
the Crashlytics export schema depend on your account/version. The endpoints
below are the documented ones; reconcile each number against its source UI
during the 2-week validation window (see README) before scheduling.
"""

import json
import os
import subprocess
import sys
import urllib.error
import urllib.request
from base64 import b64encode
from datetime import datetime, timedelta, timezone


def _log(msg):
    """Diagnostics go to stderr so stdout stays clean for the summary."""
    print(f"[heartbeat] {msg}", file=sys.stderr)


def _http_get_json(url, headers, timeout=30):
    """GET a URL and parse JSON. Returns dict/list on success, None on any error."""
    try:
        req = urllib.request.Request(url, headers=headers, method="GET")
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        _log(f"HTTP {e.code} for {url}")
    except Exception as e:  # noqa: BLE001 - fetchers must never raise out
        _log(f"request failed for {url}: {e}")
    return None


def _run(cmd, timeout=120):
    """Run a CLI command, return stdout on success (rc 0), else None."""
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        if p.returncode != 0:
            _log(f"{cmd[0]} rc={p.returncode}: {p.stderr.strip()[:200]}")
            return None
        return p.stdout
    except FileNotFoundError:
        _log(f"{cmd[0]} not installed")
    except Exception as e:  # noqa: BLE001
        _log(f"{' '.join(cmd[:2])} failed: {e}")
    return None


# ---------------------------------------------------------------------------
# RevenueCat — MRR
# ---------------------------------------------------------------------------

def fetch_mrr(app):
    """Monthly recurring revenue (EUR), via RevenueCat v2 metrics overview."""
    project = app.get("revenuecat_project")
    key = os.environ.get("REVENUECAT_API_KEY")
    if not project or not key:
        return None
    url = f"https://api.revenuecat.com/v2/projects/{project}/metrics/overview"
    data = _http_get_json(url, {
        "Authorization": f"Bearer {key}",
        "Accept": "application/json",
    })
    if not data:
        return None
    # The overview returns a list of metric objects; pull the one id == "mrr".
    for metric in data.get("metrics", []):
        if metric.get("id") == "mrr":
            return round(float(metric.get("value", 0)), 2)
    _log(f"mrr metric not in RevenueCat overview for {app['name']}")
    return None


# ---------------------------------------------------------------------------
# Amplitude — MAU (trailing 30-day active users)
# ---------------------------------------------------------------------------

def fetch_mau(app):
    """Monthly active users, via Amplitude Dashboard REST API."""
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
    data = _http_get_json(url, {"Authorization": f"Basic {token}"})
    if not data:
        return None
    try:
        # series is a list of buckets; with i=30 we expect the trailing one.
        series = data["data"]["series"][0]
        return int(series[-1])
    except (KeyError, IndexError, TypeError):
        _log(f"unexpected Amplitude shape for {app['name']}")
        return None


# ---------------------------------------------------------------------------
# Crashlytics — crash-free % (the load-bearing metric)
# ---------------------------------------------------------------------------

def fetch_crash_free(app):
    """
    Crash-free users % over the trailing 7 days, computed from the Firebase
    Crashlytics BigQuery export.

    There is no public Crashlytics REST API — the supported path is the
    BigQuery export. crash-free % is NOT a column in the export; it is derived:
        100 * (1 - distinct_crashing_users / distinct_active_users)
    distinct_active_users is not in the crash export, so this query approximates
    against the export's own user set unless you point active-user counts at a
    DAU table. VERIFY this query against your schema during validation.
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
    out = _run(["bq", "--quiet", "--format=json", "query", "--nouse_legacy_sql", sql])
    if not out:
        return None
    try:
        rows = json.loads(out)
        return float(rows[0]["crash_free_pct"]) if rows else None
    except (json.JSONDecodeError, KeyError, IndexError, TypeError):
        _log(f"could not parse crash-free for {app['name']}")
        return None


# ---------------------------------------------------------------------------
# GCP + studio — monthly cost (EUR)
# ---------------------------------------------------------------------------

def fetch_cost(app):
    """
    Monthly cost = cloud spend (BigQuery billing export) + fixed studio
    retainer from config. Returns the studio figure alone if billing is
    unreachable, so a govern-in-place app still shows its known cost.
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
        out = _run(["bq", "--quiet", "--format=json", "query",
                    "--nouse_legacy_sql", sql])
        if out:
            try:
                rows = json.loads(out)
                if rows and rows[0].get("cost_eur") is not None:
                    cloud = float(rows[0]["cost_eur"])
            except (json.JSONDecodeError, KeyError, IndexError, TypeError):
                _log(f"could not parse GCP cost for {app['name']}")
    if cloud is None and studio_cost == 0:
        return None
    return round((cloud or 0) + studio_cost, 2)


# ---------------------------------------------------------------------------
# GitHub — release tag, secret-scanning, gate bounces
# ---------------------------------------------------------------------------

def fetch_github(app):
    """
    Returns a dict of release-governance inputs (or None if repo unreachable):
        last_release  - latest release tag, or "none"
        secret_alerts - count of OPEN secret-scanning alerts (0 = pass)
        gate_bounces  - failed gate-workflow runs in the last 14 days
    These feed Filippo's judgment on the Release-health column — the script
    supplies the objective inputs, it does NOT set the 🟢🟡🔴 itself.
    """
    repo = app.get("github_repo")
    if not repo:
        return None
    result = {}

    rel = _run(["gh", "api", f"repos/{repo}/releases/latest",
                "--jq", ".tag_name"])
    result["last_release"] = rel.strip() if rel else "none"

    alerts = _run(["gh", "api",
                   f"repos/{repo}/secret-scanning/alerts?state=open&per_page=100",
                   "--jq", "length"])
    result["secret_alerts"] = int(alerts.strip()) if alerts and alerts.strip().isdigit() else None

    since = (datetime.now(timezone.utc) - timedelta(days=14)).strftime("%Y-%m-%d")
    runs = _run(["gh", "api",
                 f"repos/{repo}/actions/runs?status=failure&created=>={since}&per_page=100",
                 "--jq", ".total_count"])
    result["gate_bounces"] = int(runs.strip()) if runs and runs.strip().isdigit() else None

    return result
