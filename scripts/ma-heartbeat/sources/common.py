#!/usr/bin/env python3
"""
Shared helpers for the M&A heartbeat fetchers.

HTTP via stdlib urllib, CLI via subprocess. Both swallow errors and return
None so a single failing source never breaks a run.
"""

import json
import subprocess
import sys
import urllib.error
import urllib.request


def log(msg):
    """Diagnostics go to stderr so stdout stays clean for the summary."""
    print(f"[heartbeat] {msg}", file=sys.stderr)


def http_get_json(url, headers, timeout=30):
    """GET a URL and parse JSON. Returns dict/list on success, None on any error."""
    try:
        req = urllib.request.Request(url, headers=headers, method="GET")
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        log(f"HTTP {e.code} for {url}")
    except Exception as e:  # noqa: BLE001 - fetchers must never raise out
        log(f"request failed for {url}: {e}")
    return None


def run(cmd, timeout=120):
    """Run a CLI command, return stdout on success (rc 0), else None."""
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        if p.returncode != 0:
            log(f"{cmd[0]} rc={p.returncode}: {p.stderr.strip()[:200]}")
            return None
        return p.stdout
    except FileNotFoundError:
        log(f"{cmd[0]} not installed")
    except Exception as e:  # noqa: BLE001
        log(f"{' '.join(cmd[:2])} failed: {e}")
    return None
