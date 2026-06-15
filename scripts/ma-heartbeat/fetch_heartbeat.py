#!/usr/bin/env python3
"""
M&A Heartbeat — weekly capture + flagging.

Reads config/ma-apps.conf, pulls the time-varying numbers for each M&A app,
appends one row per app to the History store, computes deltas vs the prior
capture, and raises exception flags. It captures and flags only — it never
sets a judgment field (Posture, Release health, Next decision).

This is v2 automation behind templates/ma-portfolio-tracker.md.

Usage:
    python fetch_heartbeat.py [--config PATH] [--app NAME] [--dry-run]

    --config PATH   Path to ma-apps.conf (default: config/ma-apps.conf).
    --app NAME      Capture a single app instead of all (e.g. --app ChatUltra).
    --dry-run       Fetch + print the summary, but do NOT append to History.

Output:
    Appends rows to    m-and-a/heartbeat/history.csv   (the durable artifact)
    Writes run detail  m-and-a/heartbeat/<date>.json   (github inputs, evidence)
    Prints to stdout   the 🟡/🔴 flag summary only (green is silent).

Secrets come from env vars; CLI auth (gh, bq) is reused. See README.md.
"""

import argparse
import configparser
import csv
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import sources

REPO_ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = REPO_ROOT / "m-and-a" / "heartbeat"
HISTORY = OUT_DIR / "history.csv"
HISTORY_COLS = ["Date", "App", "Posture", "Cost", "MRR", "MAU",
                "CrashFree", "ReleaseHealth", "Flag"]


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

def load_config(path):
    if not Path(path).exists():
        sys.exit(f"config not found: {path}\n"
                 f"copy config/ma-apps.conf.example to {path} and fill it in.")
    cp = configparser.ConfigParser()
    cp.read(path)
    thresholds = {
        "crash_free_floor": cp.getfloat("thresholds", "crash_free_floor", fallback=99.0),
        "crash_free_drop_points": cp.getfloat("thresholds", "crash_free_drop_points", fallback=1.0),
        "mrr_decline_periods": cp.getint("thresholds", "mrr_decline_periods", fallback=3),
    }
    apps = []
    for section in cp.sections():
        if not section.startswith("app:"):
            continue
        app = dict(cp.items(section))
        app["name"] = section.split("app:", 1)[1].strip()
        apps.append(app)
    return thresholds, apps


# ---------------------------------------------------------------------------
# History
# ---------------------------------------------------------------------------

def read_history():
    """Return all prior rows as a list of dicts (oldest first)."""
    if not HISTORY.exists():
        return []
    with HISTORY.open(newline="") as f:
        return list(csv.DictReader(f))

def prior_rows_for(history, app_name):
    return [r for r in history if r["App"] == app_name]

def append_history(rows):
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    new_file = not HISTORY.exists()
    with HISTORY.open("a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=HISTORY_COLS)
        if new_file:
            w.writeheader()
        for r in rows:
            w.writerow(r)


# ---------------------------------------------------------------------------
# Flag logic
# ---------------------------------------------------------------------------

def _num(v):
    """Parse a stored/captured value to float, or None if not numeric."""
    try:
        return float(v)
    except (TypeError, ValueError):
        return None

def compute_flag(captured, priors, thresholds):
    """
    Return (flag, reasons[]). RED beats YELLOW beats GREEN.
    captured: this run's values. priors: this app's history rows, oldest first.
    """
    reasons = []
    red = False
    yellow = False

    cf = captured.get("CrashFree")
    floor = thresholds["crash_free_floor"]
    if cf is not None:
        if cf < floor:
            red = True
            reasons.append(f"crash-free {cf}% below floor {floor}%")
        elif cf < floor + 0.5:
            yellow = True
            reasons.append(f"crash-free {cf}% nearing floor {floor}%")
        prev_cf = _num(priors[-1]["CrashFree"]) if priors else None
        if prev_cf is not None and (prev_cf - cf) >= thresholds["crash_free_drop_points"]:
            red = True
            reasons.append(f"crash-free dropped {round(prev_cf - cf, 2)}pts week-on-week")

    alerts = captured.get("_secret_alerts")
    if alerts is not None and alerts > 0:
        red = True
        reasons.append(f"{alerts} open secret-scanning alert(s)")

    # consecutive MRR decline, including this run
    mrr_series = [_num(r["MRR"]) for r in priors] + [captured.get("MRR")]
    mrr_series = [m for m in mrr_series if m is not None]
    decline = 0
    for a, b in zip(mrr_series, mrr_series[1:]):
        decline = decline + 1 if b < a else 0
    if decline >= thresholds["mrr_decline_periods"]:
        red = True
        reasons.append(f"MRR down {decline} consecutive captures")
    elif decline >= 1:
        yellow = True
        reasons.append(f"MRR down {decline} capture(s)")

    # threshold evidence for the QA wedge / Phase-5 memo
    last5 = (priors[-4:] + [{"CrashFree": cf}]) if cf is not None else priors[-5:]
    fails = sum(1 for r in last5
                if _num(r.get("CrashFree")) is not None and _num(r["CrashFree"]) < floor)
    if fails >= 2:
        reasons.append(f"{fails} of last {len(last5)} captures failed the crash-free floor")

    flag = "🔴" if red else ("🟡" if yellow else "🟢")
    return flag, reasons


# ---------------------------------------------------------------------------
# Per-app capture
# ---------------------------------------------------------------------------

def capture_app(app, priors, thresholds, run_date):
    gh = sources.fetch_github(app) or {}
    captured = {
        "MRR": sources.fetch_mrr(app),
        "MAU": sources.fetch_mau(app),
        "CrashFree": sources.fetch_crash_free(app),
        "Cost": sources.fetch_cost(app),
        "_secret_alerts": gh.get("secret_alerts"),
    }
    flag, reasons = compute_flag(captured, priors, thresholds)

    def cell(v):
        return v if v is not None else "n/a (no access)"

    row = {
        "Date": run_date,
        "App": app["name"],
        "Posture": app.get("posture", "-"),
        "Cost": cell(captured["Cost"]),
        "MRR": cell(captured["MRR"]),
        "MAU": cell(captured["MAU"]),
        "CrashFree": cell(captured["CrashFree"]),
        "ReleaseHealth": "-",  # judgment field — Filippo sets it, not the script
        "Flag": flag,
    }
    detail = {
        "app": app["name"],
        "flag": flag,
        "reasons": reasons,
        "release_inputs": gh,  # last_release, secret_alerts, gate_bounces
    }
    return row, detail


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description="M&A heartbeat capture + flagging")
    ap.add_argument("--config", default=str(REPO_ROOT / "config" / "ma-apps.conf"))
    ap.add_argument("--app")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    thresholds, apps = load_config(args.config)
    if args.app:
        apps = [a for a in apps if a["name"].lower() == args.app.lower()]
        if not apps:
            sys.exit(f"no app named {args.app!r} in config")

    history = read_history()
    run_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    rows, details = [], []
    for app in apps:
        row, detail = capture_app(app, prior_rows_for(history, app["name"]),
                                  thresholds, run_date)
        rows.append(row)
        details.append(detail)

    if not args.dry_run:
        append_history(rows)
        OUT_DIR.mkdir(parents=True, exist_ok=True)
        (OUT_DIR / f"{run_date}.json").write_text(json.dumps(details, indent=2))

    # exception-based summary: print only what needs a human
    flagged = [d for d in details if d["flag"] != "🟢"]
    print(f"M&A heartbeat — {run_date}  ({len(rows)} apps captured"
          f"{', DRY RUN — not appended' if args.dry_run else ''})")
    if not flagged:
        print("🟢 all green — nothing to look at.")
    for d in flagged:
        print(f"\n{d['flag']} {d['app']}")
        for r in d["reasons"]:
            print(f"   - {r}")


if __name__ == "__main__":
    main()
