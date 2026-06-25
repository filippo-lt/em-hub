#!/usr/bin/env python3
"""
cc_cost.py — Hypothetical token-based cost from local Claude Code logs.

On the Max plan you aren't billed per token, but Claude Code still records exact
token counts per turn in ~/.claude/projects/**/*.jsonl. This reads those logs and
prices them as if you were on standard token-based API pricing. No network calls.

Usage:
    cc_cost.py            Pretty-printed breakdown
    cc_cost.py --json     Machine-readable JSON (consumed by the menu bar app)

The JSON shape is the contract the Swift app decodes — keep keys stable.
"""
from __future__ import annotations

import glob
import json
import os
import sys
from collections import defaultdict
from datetime import datetime, timezone

# ---- Pricing: USD per 1,000,000 tokens, by model family --------------------
# Edit as rates / models change. Matched by substring (opus / sonnet / haiku),
# so version suffixes like claude-opus-4-8 or claude-sonnet-4-6 all resolve.
PRICING = {
    "opus":   {"input": 5.0, "output": 25.0, "cache_read": 0.50, "write_5m": 6.25, "write_1h": 10.0},
    "sonnet": {"input": 3.0, "output": 15.0, "cache_read": 0.30, "write_5m": 3.75, "write_1h": 6.0},
    "haiku":  {"input": 1.0, "output": 5.0,  "cache_read": 0.10, "write_5m": 1.25, "write_1h": 2.0},
}

LOG_GLOB = os.path.expanduser("~/.claude/projects/**/*.jsonl")


def family_for(model: str) -> str | None:
    if not model:
        return None
    for fam in PRICING:
        if fam in model:
            return fam
    return None  # "<synthetic>" or unknown — skipped


def cost_for(usage: dict, rates: dict) -> float:
    """Price the four token buckets, splitting cache writes by TTL when present."""
    inp = usage.get("input_tokens", 0) or 0
    out = usage.get("output_tokens", 0) or 0
    read = usage.get("cache_read_input_tokens", 0) or 0

    cc = usage.get("cache_creation") or {}
    w5 = cc.get("ephemeral_5m_input_tokens", 0) or 0
    w1 = cc.get("ephemeral_1h_input_tokens", 0) or 0
    if not (w5 or w1):  # older logs without the split: treat all writes as 5m
        w5 = usage.get("cache_creation_input_tokens", 0) or 0

    return (
        inp * rates["input"]
        + out * rates["output"]
        + read * rates["cache_read"]
        + w5 * rates["write_5m"]
        + w1 * rates["write_1h"]
    ) / 1_000_000


def collect() -> tuple[list[dict], int, set[str]]:
    files = glob.glob(LOG_GLOB, recursive=True)
    seen: set[str] = set()
    skipped: set[str] = set()
    entries: list[dict] = []

    for path in files:
        try:
            fh = open(path, "r", encoding="utf-8")
        except OSError:
            continue
        with fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if rec.get("type") != "assistant":
                    continue
                msg = rec.get("message") or {}
                usage = msg.get("usage")
                if not usage:
                    continue

                key = f"{rec.get('requestId','')}|{msg.get('id','')}"
                if key in seen:
                    continue
                seen.add(key)

                fam = family_for(msg.get("model", ""))
                if fam is None:
                    skipped.add(msg.get("model") or "<none>")
                    continue

                ts = None
                raw_ts = rec.get("timestamp")
                if raw_ts:
                    try:
                        ts = datetime.fromisoformat(raw_ts.replace("Z", "+00:00")).astimezone()
                    except ValueError:
                        ts = None

                entries.append({
                    "cost": cost_for(usage, PRICING[fam]),
                    "model": msg.get("model", ""),
                    "project": rec.get("cwd") or "(unknown)",
                    "session": rec.get("sessionId", "?"),
                    "ts": ts,
                    "input": usage.get("input_tokens", 0) or 0,
                    "output": usage.get("output_tokens", 0) or 0,
                    "cache_read": usage.get("cache_read_input_tokens", 0) or 0,
                    "cache_write": usage.get("cache_creation_input_tokens", 0) or 0,
                })
    return entries, len(files), skipped


def build_report(entries: list[dict]) -> dict:
    now = datetime.now().astimezone()
    today = now.date()
    wy, ww, _ = now.isocalendar()
    ym = (now.year, now.month)

    total = today_c = week_c = month_c = 0.0
    by_model = defaultdict(lambda: [0.0, 0])
    by_project = defaultdict(float)
    by_week = defaultdict(float)
    by_session: dict[str, dict] = {}
    tok = defaultdict(int)

    for e in entries:
        c = e["cost"]
        total += c
        by_model[e["model"]][0] += c
        by_model[e["model"]][1] += 1
        by_project[e["project"]] += c
        for b in ("input", "output", "cache_read", "cache_write"):
            tok[b] += e[b]

        sid = e["session"]
        s = by_session.setdefault(sid, {"cost": 0.0, "project": e["project"], "date": ""})
        s["cost"] += c

        ts = e["ts"]
        if ts:
            if ts.date() == today:
                today_c += c
            ey, ewk, _ = ts.isocalendar()
            if (ey, ewk) == (wy, ww):
                week_c += c
            if (ts.year, ts.month) == ym:
                month_c += c
            by_week[f"{ey}-W{ewk:02d}"] += c
            s["date"] = ts.date().isoformat()

    r2 = lambda x: round(x, 4)
    return {
        "total": r2(total),
        "today": r2(today_c),
        "this_week": r2(week_c),
        "this_month": r2(month_c),
        "turns": len(entries),
        "by_model": [
            {"model": m, "cost": r2(v[0]), "turns": v[1]}
            for m, v in sorted(by_model.items(), key=lambda kv: -kv[1][0])
        ],
        "by_project": [
            {"project": p, "cost": r2(c)}
            for p, c in sorted(by_project.items(), key=lambda kv: -kv[1])
        ],
        "by_week": [
            {"week": w, "cost": r2(c)} for w, c in sorted(by_week.items())
        ],
        "top_sessions": [
            {"session": sid, "date": s["date"], "project": s["project"], "cost": r2(s["cost"])}
            for sid, s in sorted(by_session.items(), key=lambda kv: -kv[1]["cost"])[:10]
        ],
        "tokens": {
            "input": tok["input"],
            "output": tok["output"],
            "cache_read": tok["cache_read"],
            "cache_write": tok["cache_write"],
        },
    }


def pretty(report: dict, files: int, skipped: set[str]) -> None:
    money = lambda x: f"${x:,.2f}"
    toks = lambda x: f"{int(x):,}"
    print("=" * 60)
    print("Claude Code — hypothetical token-based cost")
    print(f"{files} log file(s), {report['turns']} billable assistant turns")
    print("=" * 60)
    print(f"\nToday {money(report['today'])}   This week {money(report['this_week'])}"
          f"   This month {money(report['this_month'])}")
    print(f"All-time total: {money(report['total'])}")

    t = report["tokens"]
    print(f"  input {toks(t['input'])}   output {toks(t['output'])}"
          f"   cache-read {toks(t['cache_read'])}   cache-write {toks(t['cache_write'])}")

    print("\nBy model:")
    for row in report["by_model"]:
        print(f"  {row['model']:<22} {money(row['cost']):>12}  ({row['turns']} turns)")

    print("\nBy project:")
    for row in report["by_project"]:
        print(f"  {money(row['cost']):>12}  {row['project']}")

    print("\nBy week:")
    for row in report["by_week"]:
        print(f"  {row['week']}   {money(row['cost'])}")

    print("\nTop sessions by cost:")
    for row in report["top_sessions"]:
        when = row["date"] or "????-??-??"
        proj = os.path.basename(row["project"].rstrip("/")) or row["project"]
        print(f"  {money(row['cost']):>12}  {when}  {proj}  {row['session'][:8]}")

    if skipped:
        print(f"\n(skipped non-priced models: {', '.join(sorted(skipped))})")


def main() -> None:
    entries, files, skipped = collect()
    report = build_report(entries)
    if "--json" in sys.argv[1:]:
        print(json.dumps(report))
    else:
        pretty(report, files, skipped)


if __name__ == "__main__":
    main()
