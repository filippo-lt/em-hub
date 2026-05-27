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


# ── Paths ─────────────────────────────────────────────────────────────────
SCRIPT_DIR  = Path(__file__).resolve().parent
REPO_ROOT   = SCRIPT_DIR.parent.parent
CONFIG_PATH = SCRIPT_DIR / "config.conf"
OUTPUT_DIR  = SCRIPT_DIR / "reports"


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


def aggregate(
    rows: Iterable[bigquery.Row],
    active_apps: list[AppConfig],
    months: list[str],
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

    histories: list[AppHistory] = []
    for idx, (app_name, total) in enumerate(ranked):
        # services within each month: sort by amount desc
        svc_by_month = {
            m: sorted(svcs, key=lambda s: s.amount, reverse=True)
            for m, svcs in services.get(app_name, {}).items()
        }
        histories.append(AppHistory(
            name=app_name,
            project_id=project_by_name.get(app_name, "?"),
            color=PALETTE[idx % len(PALETTE)],
            by_month=[spend.get(app_name, {}).get(m, 0.0) for m in months],
            services_by_month=svc_by_month,
            total_in_window=total,
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
        apps_ctx.append({
            "name":         h.name,
            "project_id":   h.project_id,
            "color":        h.color,
            "current":      cur,
            "previous":     prev,
            "mom_pct":      mom,
            "average":      avg,
            "sparkline":    sparkline_polyline(h.by_month),
            "by_month":     [round(v, 2) for v in h.by_month],
            "total_in_window": h.total_in_window,
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
    client = bigquery.Client(project=billing_project)
    rows = run_query(client, sql, months)
    print(f"  {len(rows)} rows returned")

    histories, monthly_totals, currency = aggregate(rows, active, months)

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

    return 0


if __name__ == "__main__":
    sys.exit(main())
