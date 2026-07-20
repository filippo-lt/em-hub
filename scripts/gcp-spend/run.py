#!/usr/bin/env python3
"""
GCP monthly spend report + historical dashboard.

Reads config.conf, runs a single BigQuery job covering N months of history
(default 12) ending at --month, and writes:

  reports/YYYY-MM.html   ← focused detail view for --month (tabs by app)
  reports/index.html     ← dashboard: stacked bars + sparklines + table

Both files come from the same query result — the dashboard query covers
the whole window; the monthly report just slices to one month.

Auth: Application Default Credentials. Run once locally:
    gcloud auth application-default login

Usage:
    python scripts/gcp-spend/run.py --month 2026-04
    python scripts/gcp-spend/run.py --month 2026-04 --history-months 6
    python scripts/gcp-spend/run.py --month 2026-04 --billing-project imote-prod
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

try:
    from google.cloud import bigquery
    from jinja2 import Environment, FileSystemLoader, StrictUndefined
except ImportError as exc:  # pragma: no cover
    sys.stderr.write(
        f"\nMissing dependency: {exc.name}\n"
        f"Install requirements first:\n"
        f"    make gcp-spend-setup\n\n"
    )
    sys.exit(1)

import amplitude


# ── Paths ─────────────────────────────────────────────────────────────────
SCRIPT_DIR  = Path(__file__).resolve().parent
REPO_ROOT   = SCRIPT_DIR
CONFIG_PATH = SCRIPT_DIR / "config.conf"
AMP_CONFIG_PATH = SCRIPT_DIR / "amplitude.conf"
DOTENV_PATH = REPO_ROOT / ".env"
OUTPUT_DIR  = SCRIPT_DIR / "reports"
# Vendored inside em-hub (scripts/gcp-spend/). Walk up to the em-hub root
# (marked by CLAUDE.md + metrics/) so publish works regardless of nesting
# depth and of differing absolute mount paths (Mac vs scheduled sandbox).
def _find_emhub_root(start: Path):
    for cand in [start, *start.parents]:
        if (cand / "CLAUDE.md").exists() and (cand / "metrics").is_dir():
            return cand
    return None
EMHUB_ROOT = _find_emhub_root(SCRIPT_DIR)
EMHUB_PUBLISH_DIR = (EMHUB_ROOT / "metrics" / "gcp-spend") if EMHUB_ROOT else None


# ── Color palette (Tableau-10 ish, 12 hand-picked categorical hues) ───────
# Used consistently across the hero stacked bars and per-app sparklines so
# a user can recognise an app by colour at a glance.
PALETTE = [
    "#4E79A7", "#F28E2B", "#E15759", "#76B7B2", "#59A14F",
    "#EDC948", "#B07AA1", "#FF9DA7", "#9C755F", "#BAB0AC",
    "#D37295", "#2C7BB6",
]


# ── Config model ──────────────────────────────────────────────────────────
@dataclass(frozen=True)
class AppConfig:
    friendly_name: str
    project_id: str
    dataset: str
    billing_account_id: str
    status: str  # "active" | "pending"


def load_config(path: Path) -> list[AppConfig]:
    if not path.exists():
        sys.exit(f"Config not found: {path}")

    apps: list[AppConfig] = []
    for lineno, raw in enumerate(path.read_text().splitlines(), start=1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        parts = [p.strip() for p in line.split("|")]
        if len(parts) != 5:
            sys.exit(
                f"{path}:{lineno}: expected 5 pipe-delimited fields, got {len(parts)}\n"
                f"  line: {raw}"
            )
        name, project, dataset, billing_acct, status = parts
        if status not in ("active", "pending"):
            sys.exit(f"{path}:{lineno}: status must be 'active' or 'pending', got '{status}'")
        apps.append(AppConfig(name, project, dataset, billing_acct, status))
    return apps


# ── Month helpers ─────────────────────────────────────────────────────────
def parse_month(s: str) -> tuple[str, str, str, datetime]:
    """'2026-04' → ('2026-04', '202604', 'April 2026', dt)."""
    try:
        dt = datetime.strptime(s, "%Y-%m")
    except ValueError:
        sys.exit(f"--month must be YYYY-MM (e.g. 2026-05); got '{s}'")
    return s, dt.strftime("%Y%m"), dt.strftime("%B %Y"), dt


def months_window(end_month_yyyymm: str, n: int) -> list[str]:
    """Return n YYYYMM strings ending at end_month_yyyymm inclusive."""
    end_dt = datetime.strptime(end_month_yyyymm, "%Y%m")
    out: list[str] = []
    y, m = end_dt.year, end_dt.month
    for _ in range(n):
        out.append(f"{y:04d}{m:02d}")
        m -= 1
        if m == 0:
            m, y = 12, y - 1
    return list(reversed(out))


def fmt_month_short(yyyymm: str) -> str:
    return datetime.strptime(yyyymm, "%Y%m").strftime("%b")


def fmt_month_full(yyyymm: str) -> str:
    return datetime.strptime(yyyymm, "%Y%m").strftime("%B %Y")


def fmt_month_iso(yyyymm: str) -> str:
    """'202604' → '2026-04'."""
    return f"{yyyymm[:4]}-{yyyymm[4:]}"


def current_yyyymm() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m")


# ── Query ─────────────────────────────────────────────────────────────────
def render_query(active_apps: list[AppConfig], jinja_env: Environment) -> str:
    tmpl = jinja_env.get_template("query.sql.j2")
    return tmpl.render(
        apps=[
            {
                "friendly_name":      a.friendly_name,
                "project_id":         a.project_id,
                "dataset":            a.dataset,
                "billing_account_id": a.billing_account_id,
            }
            for a in active_apps
        ]
    )


def run_query(
    client: bigquery.Client,
    sql: str,
    invoice_months: list[str],
) -> list[bigquery.Row]:
    job_config = bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ArrayQueryParameter("invoice_months", "STRING", invoice_months),
        ],
    )
    print(f"  Running BigQuery job ({len(invoice_months)} months, billed to {client.project})...",
          flush=True)
    return list(client.query(sql, job_config=job_config).result())


# ── Aggregation ───────────────────────────────────────────────────────────
@dataclass
class ServiceRow:
    name:   str
    amount: float

@dataclass
class AppHistory:
    name:        str
    project_id:  str
    color:       str
    by_month:    list[float]                       # one float per month in window
    services_by_month: dict[str, list[ServiceRow]] # invoice_month -> services
    total_in_window: float
    # Amplitude — None means no creds configured for this app
    mau_by_month: list[int | None] = field(default_factory=list)
    new_by_month: list[int | None] = field(default_factory=list)


def aggregate(
    rows: Iterable[bigquery.Row],
    active_apps: list[AppConfig],
    months: list[str],
    amp_data: dict[str, dict[str, dict[str, int]]] | None = None,
) -> tuple[list[AppHistory], list[dict], str]:
    """
    Return:
      - per-app history (sorted by total spend in window, descending)
      - per-month totals across all apps
      - dominant currency
    """
    project_by_name = {a.friendly_name: a.project_id for a in active_apps}

    spend:    dict[str, dict[str, float]]            = {}
    services: dict[str, dict[str, list[ServiceRow]]] = {}
    currencies: set[str] = set()

    for r in rows:
        app, mo, svc, amt = r["app"], r["invoice_month"], r["service"], float(r["net_cost"])
        spend.setdefault(app, {}).setdefault(mo, 0.0)
        spend[app][mo] += amt
        services.setdefault(app, {}).setdefault(mo, []).append(ServiceRow(name=svc, amount=amt))
        if r["currency"]:
            currencies.add(r["currency"])

    if len(currencies) > 1:
        print(f"  ⚠ multiple currencies present: {currencies}. Report assumes single currency.",
              file=sys.stderr)
    currency = next(iter(currencies)) if currencies else "USD"

    totals = {a: sum(spend[a].get(m, 0.0) for m in months) for a in spend}
    ranked = sorted(totals.items(), key=lambda kv: kv[1], reverse=True)

    amp_data = amp_data or {}
    histories: list[AppHistory] = []
    for idx, (app_name, total) in enumerate(ranked):
        # services within each month: sort by amount desc
        svc_by_month = {
            m: sorted(svcs, key=lambda s: s.amount, reverse=True)
            for m, svcs in services.get(app_name, {}).items()
        }
        app_amp = amp_data.get(app_name)
        if app_amp:
            mau_by_month = [app_amp.get(m, {}).get("active") for m in months]
            new_by_month = [app_amp.get(m, {}).get("new")    for m in months]
        else:
            mau_by_month = [None] * len(months)
            new_by_month = [None] * len(months)
        histories.append(AppHistory(
            name=app_name,
            project_id=project_by_name.get(app_name, "?"),
            color=PALETTE[idx % len(PALETTE)],
            by_month=[spend.get(app_name, {}).get(m, 0.0) for m in months],
            services_by_month=svc_by_month,
            total_in_window=total,
            mau_by_month=mau_by_month,
            new_by_month=new_by_month,
        ))

    monthly_totals = [
        {"month": m, "total": sum(spend.get(a, {}).get(m, 0.0) for a in spend)}
        for m in months
    ]
    return histories, monthly_totals, currency


# ── SVG geometry ──────────────────────────────────────────────────────────
def build_hero_svg(
    histories: list[AppHistory],
    monthly_totals: list[dict],
    current_month: str,
    width: int = 820,
    height: int = 260,
    pad_top: int = 16,
    pad_bottom: int = 28,
    pad_left: int = 56,
) -> dict:
    """Return the data needed to render the stacked-bar hero chart in the template."""
    n = len(monthly_totals)
    max_total = max((mt["total"] for mt in monthly_totals), default=1.0) or 1.0
    chart_area_w = width - pad_left
    step = chart_area_w / max(n, 1)
    bar_w = step * 0.72

    bars = []
    for i, mt in enumerate(monthly_totals):
        m = mt["month"]
        x = pad_left + i * step + (step - bar_w) / 2
        y_acc = height - pad_bottom
        for h in histories:
            v = h.by_month[i]
            if v <= 0:
                continue
            seg_h = (v / max_total) * (height - pad_top - pad_bottom)
            y_acc -= seg_h
            bars.append({
                "x": round(x, 1),
                "y": round(y_acc, 1),
                "w": round(bar_w, 1),
                "h": round(seg_h, 1),
                "color": h.color,
                "app": h.name,
                "value": v,
                "month": m,
                "is_current": m == current_month,
            })

    labels = []
    for i, mt in enumerate(monthly_totals):
        m = mt["month"]
        labels.append({
            "x": round(pad_left + i * step + step / 2, 1),
            "y": height - 8,
            "text": fmt_month_short(m),
            "month": m,
            "iso": fmt_month_iso(m),
            "is_current": m == current_month,
            "total": mt["total"],
        })

    # 4 gridlines + axis
    nlines = 4
    gridlines = []
    for i in range(nlines + 1):
        y_val = max_total * i / nlines
        y_px = (height - pad_bottom) - (i / nlines) * (height - pad_top - pad_bottom)
        label = (f"${y_val/1000:,.1f}K" if y_val >= 1000
                 else f"${y_val:,.0f}")
        gridlines.append({
            "y": round(y_px, 1),
            "x_label": pad_left - 6,
            "x_line_start": pad_left,
            "x_line_end": width,
            "label": label,
        })

    return {
        "width":     width,
        "height":    height,
        "bars":      bars,
        "labels":    labels,
        "gridlines": gridlines,
    }


def slugify(name: str) -> str:
    """'AI Home Design' → 'ai-home-design'."""
    out = []
    prev_dash = False
    for ch in name.lower():
        if ch.isalnum():
            out.append(ch); prev_dash = False
        elif not prev_dash:
            out.append("-"); prev_dash = True
    return "".join(out).strip("-")


def build_line_chart(
    values: list[float | int | None],
    months: list[str],
    target_month: str,
    *,
    width: int = 820,
    height: int = 220,
    pad_top: int = 18,
    pad_bottom: int = 30,
    pad_left: int = 64,
    pad_right: int = 12,
    fmt_y: str = "money",     # "money" | "int"
    color: str = "#2563eb",
) -> dict:
    """
    Build the data for a single-series line chart with axis + gridlines.
    None values are skipped (line breaks across gaps).
    """
    plot_w = width - pad_left - pad_right
    plot_h = height - pad_top - pad_bottom
    n = len(values)

    numeric = [v for v in values if v is not None]
    max_v = max(numeric) if numeric else 1.0
    if max_v == 0:
        max_v = 1.0

    def x_at(i: int) -> float:
        return pad_left + (plot_w * (i / max(n - 1, 1)))

    def y_at(v: float) -> float:
        return (height - pad_bottom) - (v / max_v) * plot_h

    # Build segments — break the polyline whenever we hit None
    segments: list[list[tuple[float, float]]] = []
    current: list[tuple[float, float]] = []
    for i, v in enumerate(values):
        if v is None:
            if current:
                segments.append(current); current = []
        else:
            current.append((x_at(i), y_at(float(v))))
    if current:
        segments.append(current)

    # Dots — only on non-None points
    dots = []
    for i, v in enumerate(values):
        if v is None:
            continue
        dots.append({
            "cx": round(x_at(i), 1),
            "cy": round(y_at(float(v)), 1),
            "value": float(v),
            "month": months[i],
            "is_target": months[i] == target_month,
        })

    # Gridlines (4 + axis)
    nlines = 4
    gridlines = []
    for i in range(nlines + 1):
        y_val = max_v * i / nlines
        y_px  = (height - pad_bottom) - (i / nlines) * plot_h
        if fmt_y == "int":
            label = (f"{y_val/1000:,.0f}K" if y_val >= 1000 else f"{y_val:,.0f}")
        else:
            label = (f"${y_val/1000:,.1f}K" if y_val >= 1000 else f"${y_val:,.0f}")
        gridlines.append({
            "y": round(y_px, 1),
            "x_label": pad_left - 6,
            "x_line_start": pad_left,
            "x_line_end": width - pad_right,
            "label": label,
        })

    # x-axis labels — one per month
    x_labels = []
    for i, m in enumerate(months):
        x_labels.append({
            "x": round(x_at(i), 1),
            "y": height - 10,
            "text": fmt_month_short(m),
            "is_target": m == target_month,
        })

    polylines = [
        " ".join(f"{p[0]:.1f},{p[1]:.1f}" for p in seg)
        for seg in segments
    ]

    return {
        "width":     width,
        "height":    height,
        "polylines": polylines,
        "dots":      dots,
        "gridlines": gridlines,
        "x_labels":  x_labels,
        "color":     color,
        "has_data":  bool(numeric),
    }


def build_overlay_chart(
    series: list[dict],
    months: list[str],
    target_month: str,
    *,
    width: int = 820,
    height: int = 240,
    pad_top: int = 18,
    pad_bottom: int = 30,
    pad_left: int = 64,
    pad_right: int = 12,
) -> dict:
    """
    Multi-series indexed line chart. Each series is normalised to 100
    at the first month with a non-None value, so wildly different
    scales (spend vs MAU) become directly comparable trends.

    series: [{"name": "Spend", "color": "#...", "values": [...]}, ...]
    Values can include None for gaps.
    """
    plot_w = width - pad_left - pad_right
    plot_h = height - pad_top - pad_bottom
    n = len(months)

    # Pick a SHARED baseline month: the first index where every series has
    # stabilised (>=10% of its own max in the window). Indexing against a
    # near-zero launch month produces astronomical, meaningless numbers.
    per_series_start: list[int] = []
    for s in series:
        numeric_vals = [v for v in s["values"] if v is not None]
        if not numeric_vals:
            per_series_start.append(n)  # never starts
            continue
        s_max = max(numeric_vals)
        threshold = max(s_max * 0.10, 1e-9)
        first = next(
            (i for i, v in enumerate(s["values"])
             if v is not None and v >= threshold),
            n,
        )
        per_series_start.append(first)
    baseline_idx = max(per_series_start) if per_series_start else 0
    baseline_idx = min(baseline_idx, n - 1)

    baseline_month = months[baseline_idx] if baseline_idx < n else None

    # Normalise each series to 100 at baseline_idx; mask earlier months
    normalised: list[dict] = []
    for s in series:
        baseline = s["values"][baseline_idx] if baseline_idx < n else None
        if not baseline:
            norm = [None] * n
        else:
            norm = []
            for i, v in enumerate(s["values"]):
                if i < baseline_idx or v is None:
                    norm.append(None)
                else:
                    norm.append(100.0 * v / baseline)
        normalised.append({"name": s["name"], "color": s["color"],
                           "raw": s["values"], "norm": norm})

    # Y range: span across all normalised values
    all_norm = [v for s in normalised for v in s["norm"] if v is not None]
    if not all_norm:
        max_v, min_v = 200.0, 0.0
    else:
        max_v = max(all_norm + [100.0])
        min_v = min(all_norm + [100.0])
    # Pad the range 10% so the line doesn't kiss the top
    span = max(max_v - min_v, 1.0)
    max_v += span * 0.1
    min_v -= span * 0.05
    if min_v < 0:
        min_v = 0

    def x_at(i: int) -> float:
        return pad_left + plot_w * (i / max(n - 1, 1))

    def y_at(v: float) -> float:
        return (height - pad_bottom) - ((v - min_v) / (max_v - min_v)) * plot_h

    # Build segments + dots per series
    rendered_series = []
    for s in normalised:
        segments: list[list[tuple[float, float]]] = []
        current: list[tuple[float, float]] = []
        dots = []
        for i, v in enumerate(s["norm"]):
            if v is None:
                if current:
                    segments.append(current); current = []
                continue
            current.append((x_at(i), y_at(v)))
            dots.append({
                "cx": round(x_at(i), 1),
                "cy": round(y_at(v), 1),
                "index": v,
                "raw":   s["raw"][i],
                "month": months[i],
                "is_target": months[i] == target_month,
            })
        if current:
            segments.append(current)
        polylines = [
            " ".join(f"{p[0]:.1f},{p[1]:.1f}" for p in seg)
            for seg in segments
        ]
        rendered_series.append({
            "name":      s["name"],
            "color":     s["color"],
            "polylines": polylines,
            "dots":      dots,
            "has_data":  any(v is not None for v in s["norm"]),
        })

    # Gridlines
    nlines = 4
    gridlines = []
    for i in range(nlines + 1):
        y_val = min_v + (max_v - min_v) * i / nlines
        y_px  = (height - pad_bottom) - (i / nlines) * plot_h
        gridlines.append({
            "y": round(y_px, 1),
            "x_label": pad_left - 6,
            "x_line_start": pad_left,
            "x_line_end": width - pad_right,
            "label": f"{y_val:,.0f}",
        })

    # Baseline marker at 100
    baseline_y = round(y_at(100.0), 1)

    x_labels = []
    for i, m in enumerate(months):
        x_labels.append({
            "x": round(x_at(i), 1),
            "y": height - 10,
            "text": fmt_month_short(m),
            "is_target": m == target_month,
        })

    return {
        "width":       width,
        "height":      height,
        "gridlines":   gridlines,
        "x_labels":    x_labels,
        "series":      rendered_series,
        "baseline_y":  baseline_y,
        "baseline_x_start": pad_left,
        "baseline_x_end":   width - pad_right,
        "baseline_month_label": fmt_month_full(baseline_month) if baseline_month else None,
    }


def build_services_stacked(
    h: "AppHistory",
    months: list[str],
    target_month: str,
    palette: list[str],
    *,
    width: int = 820,
    height: int = 240,
    pad_top: int = 16,
    pad_bottom: int = 30,
    pad_left: int = 64,
    pad_right: int = 12,
    top_n: int = 6,
) -> dict:
    """
    Stacked-bar chart of per-service cost over time for ONE app.
    Top N services by total spend in window get their own colour; rest folded into "Other".
    """
    # Aggregate per-service totals across the window
    totals_by_service: dict[str, float] = {}
    for m in months:
        for s in h.services_by_month.get(m, []):
            totals_by_service[s.name] = totals_by_service.get(s.name, 0.0) + s.amount

    ranked = sorted(totals_by_service.items(), key=lambda kv: kv[1], reverse=True)
    top_services = [name for name, _ in ranked[:top_n]]
    others_exist = len(ranked) > top_n

    service_order = top_services + (["Other"] if others_exist else [])
    color_map = {name: palette[i % len(palette)] for i, name in enumerate(service_order)}

    plot_w = width - pad_left - pad_right
    plot_h = height - pad_top - pad_bottom
    n = len(months)
    step = plot_w / max(n, 1)
    bar_w = step * 0.72

    # Monthly stack values per service
    stacks: list[dict] = []
    for i, m in enumerate(months):
        per_service: dict[str, float] = {s: 0.0 for s in service_order}
        for s in h.services_by_month.get(m, []):
            if s.name in top_services:
                per_service[s.name] += s.amount
            elif others_exist:
                per_service["Other"] += s.amount
        stacks.append({"month": m, "values": per_service,
                       "total": sum(per_service.values())})

    max_total = max((s["total"] for s in stacks), default=1.0) or 1.0

    bars = []
    for i, stk in enumerate(stacks):
        x = pad_left + i * step + (step - bar_w) / 2
        y_acc = height - pad_bottom
        for svc in service_order:
            v = stk["values"][svc]
            if v <= 0:
                continue
            seg_h = (v / max_total) * plot_h
            y_acc -= seg_h
            bars.append({
                "x":     round(x, 1),
                "y":     round(y_acc, 1),
                "w":     round(bar_w, 1),
                "h":     round(seg_h, 1),
                "color": color_map[svc],
                "svc":   svc,
                "value": v,
                "month": stk["month"],
                "is_target": stk["month"] == target_month,
            })

    nlines = 4
    gridlines = []
    for i in range(nlines + 1):
        y_val = max_total * i / nlines
        y_px  = (height - pad_bottom) - (i / nlines) * plot_h
        label = (f"${y_val/1000:,.1f}K" if y_val >= 1000 else f"${y_val:,.0f}")
        gridlines.append({
            "y": round(y_px, 1),
            "x_label": pad_left - 6,
            "x_line_start": pad_left,
            "x_line_end": width - pad_right,
            "label": label,
        })

    x_labels = []
    for i, m in enumerate(months):
        x_labels.append({
            "x": round(pad_left + i * step + step / 2, 1),
            "y": height - 10,
            "text": fmt_month_short(m),
            "is_target": m == target_month,
        })

    legend = [{"name": s, "color": color_map[s]} for s in service_order]

    return {
        "width":     width,
        "height":    height,
        "bars":      bars,
        "gridlines": gridlines,
        "x_labels":  x_labels,
        "legend":    legend,
    }


def sparkline_polyline(values: list[float], width: int = 160, height: int = 32, pad: int = 3) -> str:
    if not values:
        return ""
    n = len(values)
    max_v = max(values) or 1.0
    if n == 1:
        return f"{pad},{height - pad - (values[0] / max_v) * (height - 2*pad):.1f}"
    return " ".join(
        f"{pad + i * (width - 2*pad) / (n - 1):.1f},"
        f"{height - pad - (v / max_v) * (height - 2*pad):.1f}"
        for i, v in enumerate(values)
    )


# ── Build template contexts ───────────────────────────────────────────────
def monthly_report_context(
    histories: list[AppHistory],
    pending: list[AppConfig],
    currency: str,
    target_month: str,
    target_month_label: str,
    active_count: int,
) -> dict:
    """Per-app slice for the focused monthly report (existing template.html.j2)."""
    apps_ctx = []
    grand_total = 0.0
    for h in histories:
        services = h.services_by_month.get(target_month, [])
        total = sum(s.amount for s in services)
        if total == 0 and not services:
            continue  # no data this month for this app — omit
        grand_total += total
        max_amt = max((s.amount for s in services), default=0.0) or 1.0
        apps_ctx.append({
            "name":       h.name,
            "project_id": h.project_id,
            "total":      total,
            "services": [
                {
                    "name":   s.name,
                    "amount": s.amount,
                    "pct":    round((s.amount / max_amt) * 100.0, 1),
                }
                for s in services
            ],
        })
    apps_ctx.sort(key=lambda a: a["total"], reverse=True)
    return {
        "month_label":  target_month_label,
        "active_count": active_count,
        "grand_total":  grand_total,
        "currency":     currency,
        "apps":         apps_ctx,
        "pending":      [{"friendly_name": p.friendly_name, "project_id": p.project_id} for p in pending],
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
    }


def dashboard_context(
    histories: list[AppHistory],
    monthly_totals: list[dict],
    months: list[str],
    pending: list[AppConfig],
    currency: str,
    target_month: str,
) -> dict:
    """Full multi-month dashboard view."""
    current_running_month = current_yyyymm()

    months_meta = []
    for mt in monthly_totals:
        m = mt["month"]
        months_meta.append({
            "month":      m,
            "iso":        fmt_month_iso(m),
            "label":      fmt_month_short(m),
            "full_label": fmt_month_full(m),
            "total":      mt["total"],
            "is_current_calendar": m == current_running_month,
            "is_target":  m == target_month,
        })

    target_total = next((mt["total"] for mt in monthly_totals if mt["month"] == target_month), 0.0)
    prev_idx = next((i for i, mt in enumerate(monthly_totals) if mt["month"] == target_month), 0) - 1
    prev_total = monthly_totals[prev_idx]["total"] if prev_idx >= 0 else None
    overall_mom = ((target_total - prev_total) / prev_total * 100.0) if prev_total else None

    hero = build_hero_svg(histories, monthly_totals, current_month=target_month)

    # Per-app cards
    apps_ctx = []
    for h in histories:
        cur_idx  = months.index(target_month) if target_month in months else len(months) - 1
        prev     = h.by_month[cur_idx - 1] if cur_idx > 0 else None
        cur      = h.by_month[cur_idx]
        mom      = ((cur - prev) / prev * 100.0) if prev else None
        avg      = sum(h.by_month) / max(len(h.by_month), 1)
        mau_cur  = h.mau_by_month[cur_idx] if cur_idx < len(h.mau_by_month) else None
        new_cur  = h.new_by_month[cur_idx] if cur_idx < len(h.new_by_month) else None
        cost_per_mau = (cur / mau_cur) if (mau_cur and mau_cur > 0) else None
        apps_ctx.append({
            "name":         h.name,
            "slug":         slugify(h.name),
            "project_id":   h.project_id,
            "color":        h.color,
            "current":      cur,
            "previous":     prev,
            "mom_pct":      mom,
            "average":      avg,
            "sparkline":    sparkline_polyline(h.by_month),
            "by_month":     [round(v, 2) for v in h.by_month],
            "total_in_window": h.total_in_window,
            "mau":          mau_cur,
            "new_users":    new_cur,
            "cost_per_mau": cost_per_mau,
        })

    # Table: show last 6 months + average + delta vs prior
    table_months = months[-6:]
    table_rows = []
    for h in histories:
        # map full by_month to last 6
        idx_start = len(months) - len(table_months)
        last6 = h.by_month[idx_start:]
        # delta = last vs second-to-last in the same 6-month slice
        delta = ((last6[-1] - last6[-2]) / last6[-2] * 100.0) if (len(last6) >= 2 and last6[-2]) else None
        table_rows.append({
            "name":             h.name,
            "color":            h.color,
            "monthly_amounts":  last6,
            "avg":              sum(h.by_month) / max(len(h.by_month), 1),
            "delta":            delta,
        })
    table_months_meta = [
        {"label": fmt_month_short(m), "iso": fmt_month_iso(m),
         "is_target": m == target_month, "is_current_calendar": m == current_running_month}
        for m in table_months
    ]

    return {
        "target_month":        target_month,
        "target_month_iso":    fmt_month_iso(target_month),
        "target_month_label":  fmt_month_full(target_month),
        "target_total":        target_total,
        "overall_mom_pct":     overall_mom,
        "currency":            currency,
        "window_count":        len(months),
        "months":              months_meta,
        "hero":                hero,
        "apps":                apps_ctx,
        "table_months":        table_months_meta,
        "table_rows":          table_rows,
        "pending":             [{"friendly_name": p.friendly_name, "project_id": p.project_id} for p in pending],
        "generated_at":        datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
    }


def app_page_context(
    h: AppHistory,
    months: list[str],
    pending: list[AppConfig],
    currency: str,
    target_month: str,
) -> dict:
    """Self-contained per-app page context."""
    cur_idx = months.index(target_month) if target_month in months else len(months) - 1
    cur     = h.by_month[cur_idx]
    prev    = h.by_month[cur_idx - 1] if cur_idx > 0 else None
    mom     = ((cur - prev) / prev * 100.0) if prev else None
    avg     = sum(h.by_month) / max(len(h.by_month), 1)

    mau_cur = h.mau_by_month[cur_idx] if cur_idx < len(h.mau_by_month) else None
    new_cur = h.new_by_month[cur_idx] if cur_idx < len(h.new_by_month) else None
    mau_prev = h.mau_by_month[cur_idx - 1] if (cur_idx > 0 and cur_idx - 1 < len(h.mau_by_month)) else None
    mau_mom = ((mau_cur - mau_prev) / mau_prev * 100.0) if (mau_cur is not None and mau_prev) else None
    cost_per_mau = (cur / mau_cur) if (mau_cur and mau_cur > 0) else None

    # Charts
    spend_chart = build_line_chart(
        [round(v, 2) for v in h.by_month], months, target_month,
        fmt_y="money", color=h.color,
    )
    has_amplitude = any(v is not None for v in h.mau_by_month)
    mau_chart = build_line_chart(
        h.mau_by_month, months, target_month, fmt_y="int", color="#1e8449",
    ) if has_amplitude else None
    new_chart = build_line_chart(
        h.new_by_month, months, target_month, fmt_y="int", color="#b07aa1",
    ) if has_amplitude else None

    # $/MAU per month
    cpm_series: list[float | None] = []
    for spend_v, mau_v in zip(h.by_month, h.mau_by_month):
        cpm_series.append(spend_v / mau_v if (mau_v and mau_v > 0) else None)
    cpm_chart = build_line_chart(
        cpm_series, months, target_month, fmt_y="money", color="#2563eb",
    ) if has_amplitude else None

    # Indexed overlay: spend + MAU + new users on a single normalised axis
    overlay_chart = build_overlay_chart(
        series=[
            {"name": "Spend",     "color": h.color,    "values": h.by_month},
            {"name": "MAU",       "color": "#1e8449",  "values": h.mau_by_month},
            {"name": "New users", "color": "#b07aa1",  "values": h.new_by_month},
        ],
        months=months,
        target_month=target_month,
    ) if has_amplitude else None

    services_chart = build_services_stacked(h, months, target_month, PALETTE)

    # Table rows: per month, spend + MAU + new + $/MAU
    table_rows = []
    for i, m in enumerate(months):
        mau = h.mau_by_month[i] if i < len(h.mau_by_month) else None
        new = h.new_by_month[i] if i < len(h.new_by_month) else None
        spend_v = h.by_month[i]
        table_rows.append({
            "month":      m,
            "label":      fmt_month_short(m),
            "full_label": fmt_month_full(m),
            "iso":        fmt_month_iso(m),
            "spend":      spend_v,
            "mau":        mau,
            "new":        new,
            "cost_per_mau": (spend_v / mau) if (mau and mau > 0) else None,
            "is_target":  m == target_month,
        })

    return {
        "name":             h.name,
        "project_id":       h.project_id,
        "color":            h.color,
        "currency":         currency,
        "target_month":     target_month,
        "target_month_iso": fmt_month_iso(target_month),
        "target_month_label": fmt_month_full(target_month),
        "current":          cur,
        "previous":         prev,
        "mom_pct":          mom,
        "average":          avg,
        "total_in_window":  h.total_in_window,
        "window_count":     len(months),
        "mau":              mau_cur,
        "new_users":        new_cur,
        "mau_mom_pct":      mau_mom,
        "cost_per_mau":     cost_per_mau,
        "has_amplitude":    has_amplitude,
        "spend_chart":      spend_chart,
        "mau_chart":        mau_chart,
        "new_chart":        new_chart,
        "cpm_chart":        cpm_chart,
        "overlay_chart":    overlay_chart,
        "services_chart":   services_chart,
        "table_rows":       table_rows,
        "generated_at":     datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
    }


# ── Rendering ─────────────────────────────────────────────────────────────
def render_html(jinja_env: Environment, template_name: str, context: dict) -> str:
    return jinja_env.get_template(template_name).render(**context)


# ── Main ──────────────────────────────────────────────────────────────────
def main() -> int:
    ap = argparse.ArgumentParser(
        description="Generate the monthly GCP spend HTML report + multi-month dashboard."
    )
    ap.add_argument("--month", required=True, help="Focal month in YYYY-MM format.")
    ap.add_argument(
        "--history-months", type=int, default=12,
        help="Months of history to include in the dashboard (default: 12).",
    )
    ap.add_argument(
        "--billing-project",
        help="GCP project to bill the BigQuery query to. Defaults to the first active app's project.",
    )
    ap.add_argument(
        "--publish", action="store_true",
        help="After rendering, copy the focal monthly report and index.html into the sibling em-hub/metrics/gcp-spend/ directory.",
    )
    args = ap.parse_args()

    file_slug, target_yyyymm, month_label, _ = parse_month(args.month)
    history_n = max(1, args.history_months)

    print(f"GCP spend → {month_label} (target invoice.month={target_yyyymm}), "
          f"window {history_n} months")

    apps = load_config(CONFIG_PATH)
    active  = [a for a in apps if a.status == "active"]
    pending = [a for a in apps if a.status == "pending"]
    if not active:
        sys.exit("No active apps in config — nothing to report.")
    print(f"  {len(active)} active apps, {len(pending)} pending")

    months = months_window(target_yyyymm, history_n)
    print(f"  months: {months[0]} → {months[-1]}")

    billing_project = args.billing_project or active[0].project_id

    sql_env = Environment(
        loader=FileSystemLoader(str(SCRIPT_DIR)),
        undefined=StrictUndefined,
        autoescape=False,
    )
    sql = render_query(active, sql_env)
    # Headless auth: load .env before building the BigQuery client so the
    # service-account credential is in the environment in time. A repo-relative
    # GCP_SA_KEY_FILE is resolved to an absolute path so the same .env works on
    # the Mac and in the scheduled sandbox (different absolute mount roots).
    amplitude.load_dotenv(DOTENV_PATH)
    _sa_rel = os.environ.get("GCP_SA_KEY_FILE")
    if _sa_rel and not os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str((SCRIPT_DIR / _sa_rel).resolve())
    client = bigquery.Client(project=billing_project)
    rows = run_query(client, sql, months)
    print(f"  {len(rows)} rows returned")

    amp_apps = amplitude.load_amplitude_config(AMP_CONFIG_PATH, DOTENV_PATH)
    amp_data = amplitude.fetch_all(amp_apps, months) if amp_apps else {}

    histories, monthly_totals, currency = aggregate(rows, active, months, amp_data)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    html_env = Environment(
        loader=FileSystemLoader(str(SCRIPT_DIR)),
        undefined=StrictUndefined,
        autoescape=True,
    )

    # 1) Focused monthly report
    monthly_ctx = monthly_report_context(
        histories=histories,
        pending=pending,
        currency=currency,
        target_month=target_yyyymm,
        target_month_label=month_label,
        active_count=len(active),
    )
    monthly_path = OUTPUT_DIR / f"{file_slug}.html"
    monthly_path.write_text(render_html(html_env, "template.html.j2", monthly_ctx))
    print(f"  ✓ wrote {monthly_path.relative_to(REPO_ROOT)}  "
          f"(total ${monthly_ctx['grand_total']:,.2f} {currency})")

    # 2) Dashboard (replaces the old simple link-list index.html)
    dash_ctx = dashboard_context(
        histories=histories,
        monthly_totals=monthly_totals,
        months=months,
        pending=pending,
        currency=currency,
        target_month=target_yyyymm,
    )
    dash_path = OUTPUT_DIR / "index.html"
    dash_path.write_text(render_html(html_env, "dashboard.html.j2", dash_ctx))
    print(f"  ✓ wrote {dash_path.relative_to(REPO_ROOT)}  "
          f"(dashboard, last {history_n} months)")

    # 3) Per-app pages
    apps_dir = OUTPUT_DIR / "apps"
    apps_dir.mkdir(parents=True, exist_ok=True)
    for h in histories:
        app_ctx = app_page_context(
            h=h, months=months, pending=pending,
            currency=currency, target_month=target_yyyymm,
        )
        slug = slugify(h.name)
        out = apps_dir / f"{slug}.html"
        out.write_text(render_html(html_env, "app.html.j2", app_ctx))
    print(f"  ✓ wrote {len(histories)} app pages under "
          f"{apps_dir.relative_to(REPO_ROOT)}/")

    export_path = write_export_json(OUTPUT_DIR, file_slug, target_yyyymm, histories, months)
    print(f"  ✓ wrote {export_path.relative_to(REPO_ROOT)}  "
          f"(heartbeat export, {len(histories)} apps)")

    if args.publish:
        publish_to_emhub(monthly_path, dash_path, export_path)

    return 0


def _export_key(name: str) -> str:
    """Stable lowercase-alphanumeric key for the M&A heartbeat consumer.
    'Chat Ultra' → 'chatultra', 'PDF Editor' → 'pdfeditor'."""
    return slugify(name).replace("-", "")


def write_export_json(
    output_dir: Path,
    file_slug: str,
    target_yyyymm: str,
    histories: list[AppHistory],
    months: list[str],
) -> Path:
    """Write reports/<YYYY-MM>.json with per-app cost + MAU for the focal month.
    Contract is consumed by em-hub's M&A heartbeat (gcp_spend.py)."""
    try:
        cur_idx = months.index(target_yyyymm)
    except ValueError:
        cur_idx = len(months) - 1
    apps = {}
    for h in histories:
        cost = h.by_month[cur_idx] if cur_idx < len(h.by_month) else None
        mau  = h.mau_by_month[cur_idx] if cur_idx < len(h.mau_by_month) else None
        apps[_export_key(h.name)] = {
            "cost_eur": round(float(cost), 2) if cost is not None else None,
            "mau":      int(mau) if mau is not None else None,
        }
    payload = {
        "month": file_slug,
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "apps": apps,
    }
    out = output_dir / f"{file_slug}.json"
    out.write_text(json.dumps(payload, indent=2) + "\n")
    return out


def publish_to_emhub(monthly_path: Path, dash_path: Path, export_path: Path) -> None:
    """Copy the focal monthly report, dashboard, and the heartbeat JSON export
    into the sibling em-hub metrics directory. No-op with a warning if em-hub
    isn't a sibling."""
    import shutil
    if EMHUB_PUBLISH_DIR is None:
        print("  ⚠ publish skipped: em-hub root not found (need CLAUDE.md + metrics/ above this script)")
        return
    EMHUB_PUBLISH_DIR.mkdir(parents=True, exist_ok=True)
    for src in (monthly_path, dash_path, export_path):
        dst = EMHUB_PUBLISH_DIR / src.name
        shutil.copy2(src, dst)
        print(f"  ✓ published {src.name} → {dst}")


if __name__ == "__main__":
    sys.exit(main())
