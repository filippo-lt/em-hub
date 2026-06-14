#!/usr/bin/env python3
"""
GitHub — release tag, secret-scanning, gate bounces.

Uses the `gh` CLI (auth reused). Supplies the objective inputs for the
Release-health judgment column; it does NOT set the 🟢🟡🔴 itself.
"""

from datetime import datetime, timedelta, timezone

from .common import run


def fetch_github(app):
    """
    Returns a dict of release-governance inputs (or None if repo unreachable):
        last_release  - latest release tag, or "none"
        secret_alerts - count of OPEN secret-scanning alerts (0 = pass)
        gate_bounces  - failed gate-workflow runs in the last 14 days
    """
    repo = app.get("github_repo")
    if not repo:
        return None
    result = {}

    rel = run(["gh", "api", f"repos/{repo}/releases/latest",
               "--jq", ".tag_name"])
    result["last_release"] = rel.strip() if rel else "none"

    alerts = run(["gh", "api",
                  f"repos/{repo}/secret-scanning/alerts?state=open&per_page=100",
                  "--jq", "length"])
    result["secret_alerts"] = int(alerts.strip()) if alerts and alerts.strip().isdigit() else None

    since = (datetime.now(timezone.utc) - timedelta(days=14)).strftime("%Y-%m-%d")
    runs = run(["gh", "api",
                f"repos/{repo}/actions/runs?status=failure&created=>={since}&per_page=100",
                "--jq", ".total_count"])
    result["gate_bounces"] = int(runs.strip()) if runs and runs.strip().isdigit() else None

    return result
