#!/usr/bin/env python3
"""
GitHub — release tag, secret-scanning, gate bounces.

Uses the `gh` CLI (auth reused) for release tag + gate bounces, and the
`gitleaks` CLI run against a local clone for secret scanning. Local scanning
sidesteps GitHub Advanced Security (paid, often disabled on private repos)
and works uniformly across the M&A portfolio. Supplies the objective inputs
for the Release-health judgment column; does NOT set the 🟢🟡🔴 itself.
"""

import json
import os
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

from .common import run, log


def _scan_secrets(clone_path):
    """Run gitleaks against a local clone. Returns finding count, or None if
    the clone is missing or gitleaks isn't available."""
    path = Path(os.path.expanduser(clone_path)).resolve()
    if not (path / ".git").is_dir():
        log(f"gitleaks: no .git at {path} — clone the repo or fix local_clone")
        return None
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as tf:
        report = tf.name
    try:
        # exit 0 = clean, 1 = findings, anything else = tool error
        out = run([
            "gitleaks", "detect",
            "--source", str(path),
            "--report-format", "json",
            "--report-path", report,
            "--redact",
            "--no-banner",
            "--exit-code", "1",
        ])
        # `run` returns None on non-zero rc (including the 1 we want).
        # Read the report directly — its presence is the signal.
        try:
            findings = json.loads(Path(report).read_text() or "[]")
        except (json.JSONDecodeError, OSError):
            return None if out is None else 0
        return len(findings) if isinstance(findings, list) else None
    finally:
        try:
            os.unlink(report)
        except OSError:
            pass


def fetch_github(app):
    """
    Returns a dict of release-governance inputs (or None if repo unreachable):
        last_release  - latest release tag, or "none"
        secret_alerts - count of gitleaks findings on the local clone (0 = pass)
        gate_bounces  - failed gate-workflow runs in the last 14 days
    """
    repo = app.get("github_repo")
    if not repo:
        return None
    result = {}

    rel = run(["gh", "api", f"repos/{repo}/releases/latest",
               "--jq", ".tag_name"])
    result["last_release"] = rel.strip() if rel else "none"

    clone = app.get("local_clone")
    result["secret_alerts"] = _scan_secrets(clone) if clone else None

    since = (datetime.now(timezone.utc) - timedelta(days=14)).strftime("%Y-%m-%d")
    runs = run(["gh", "api",
                f"repos/{repo}/actions/runs?status=failure&created=>={since}&per_page=100",
                "--jq", ".total_count"])
    result["gate_bounces"] = int(runs.strip()) if runs and runs.strip().isdigit() else None

    return result
