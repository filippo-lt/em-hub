#!/usr/bin/env python3
"""
GCP monthly spend report.

Reads config/gcp-spend.conf, queries BigQuery billing export across all
"active" apps for the requested invoice month, and writes a self-contained
HTML report to metrics/gcp-spend/YYYY-MM.html (plus regenerates index.html).

Auth: Application Default Credentials. Run once locally:
    gcloud auth application-default login

Usage:
    python scripts/gcp-spend/run.py --month 2026-05
    python scripts/gcp-spend/run.py --month 2026-05 --billing-project imote-prod
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

try:
    from google.cloud import bigquery
    from jinja2 import Environment, FileSystemLoader, StrictUndefined
except ImportError as exc:  # pragma: no cover - friendly error
    sys.stderr.write(
        f"\nMissing dependency: {exc.name}\n"
        f"Install requirements first:\n"
        f"    pip install -r scripts/gcp-spend/requirements.txt\n\n"
    )
    sys.exit(1)


# ── Paths ─────────────────────────────────────────────────────────────────
# All files for this tool live under scripts/gcp-spend/ — config, templates,
# code, and generated reports. The repo root is only used for nicer relative
# paths in log output.
SCRIPT_DIR  = Path(__file__).resolve().parent
REPO_ROOT   = SCRIPT_DIR.parent.parent
CONFIG_PATH = SCRIPT_DIR / "config.conf"
OUTPUT_DIR  = SCRIPT_DIR / "reports"


# ── Config model ──────────────────────────────────────────────────────────
@dataclass(frozen=True)
class AppConfig:
    friendly_name: str
    project_id: str
    dataset: str
    billing_account_id: str
    status: str  # "active" | "pending"

    @property
    def table_suffix(self) -> str:
        return self.billing_account_id.replace("-", "_")


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
    invoice_month: str,
) -> list[bigquery.Row]:
    job_config = bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ScalarQueryParameter("invoice_month", "STRING", invoice_month),
        ],
    )
    print(f"  Running BigQuery job (billed to {client.project})...", flush=True)
    return list(client.query(sql, job_config=job_config).result())


# ── Aggregation ───────────────────────────────────────────────────────────
@dataclass
class ServiceRow:
    name:   str
    amount: float

@dataclass
class AppReport:
    name:       str
    project_id: str
    services:   list[ServiceRow]
    total:      float


def aggregate(rows: Iterable[bigquery.Row], active_apps: list[AppConfig]) -> tuple[list[AppReport], str]:
    """Group rows by app, compute totals, sort, attach project_id from config."""
    project_id_by_name = {a.friendly_name: a.project_id for a in active_apps}

    buckets: dict[str, list[ServiceRow]] = {}
    currencies: set[str] = set()
    for r in rows:
        buckets.setdefault(r["app"], []).append(
            ServiceRow(name=r["service"], amount=float(r["net_cost"]))
        )
        if r["currency"]:
            currencies.add(r["currency"])

    if len(currencies) > 1:
        print(f"  ⚠ multiple currencies present: {currencies}. Report assumes single currency.",
              file=sys.stderr)
    currency = next(iter(currencies)) if currencies else "USD"

    reports: list[AppReport] = []
    for name, services in buckets.items():
        services.sort(key=lambda s: s.amount, reverse=True)
        reports.append(AppReport(
            name=name,
            project_id=project_id_by_name.get(name, "?"),
            services=services,
            total=sum(s.amount for s in services),
        ))
    reports.sort(key=lambda a: a.total, reverse=True)
    return reports, currency


def to_template_context(
    reports: list[AppReport],
    pending: list[AppConfig],
    currency: str,
    month_label: str,
    active_count: int,
) -> dict:
    grand_total = sum(r.total for r in reports)
    apps_ctx = []
    for r in reports:
        max_amt = max((s.amount for s in r.services), default=0.0) or 1.0
        apps_ctx.append({
            "name":       r.name,
            "project_id": r.project_id,
            "total":      r.total,
            "services": [
                {
                    "name":   s.name,
                    "amount": s.amount,
                    "pct":    round((s.amount / max_amt) * 100.0, 1),
                }
                for s in r.services
            ],
        })
    return {
        "month_label":   month_label,
        "active_count":  active_count,
        "grand_total":   grand_total,
        "currency":      currency,
        "apps":          apps_ctx,
        "pending":       [{"friendly_name": p.friendly_name, "project_id": p.project_id} for p in pending],
        "generated_at":  datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
    }


# ── Index page ────────────────────────────────────────────────────────────
INDEX_HTML = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>GCP Spend Reports</title>
<style>
  body{{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
       max-width:640px;margin:40px auto;padding:0 24px;color:#1a1a1a;}}
  h1{{font-size:22px;margin-bottom:24px;}}
  ul{{list-style:none;padding:0;}}
  li{{padding:8px 0;border-bottom:1px solid #e6e6e6;font-size:15px;}}
  a{{color:#2563eb;text-decoration:none;}}
  a:hover{{text-decoration:underline;}}
</style></head><body>
<h1>GCP Spend Reports</h1>
<ul>
{items}
</ul>
</body></html>
"""

def regenerate_index(output_dir: Path) -> None:
    months = sorted(
        (p for p in output_dir.glob("[0-9][0-9][0-9][0-9]-[0-9][0-9].html")),
        key=lambda p: p.stem, reverse=True,
    )
    items = "\n".join(
        f'  <li><a href="{p.name}">{p.stem}</a></li>' for p in months
    ) or '  <li><em>no reports yet</em></li>'
    (output_dir / "index.html").write_text(INDEX_HTML.format(items=items))


# ── Main ──────────────────────────────────────────────────────────────────
def parse_month(s: str) -> tuple[str, str, str]:
    """'2026-05' → ('2026-05', '202605', 'May 2026')."""
    try:
        dt = datetime.strptime(s, "%Y-%m")
    except ValueError:
        sys.exit(f"--month must be YYYY-MM (e.g. 2026-05); got '{s}'")
    return s, dt.strftime("%Y%m"), dt.strftime("%B %Y")


def main() -> int:
    ap = argparse.ArgumentParser(description="Generate the monthly GCP spend HTML report.")
    ap.add_argument("--month", required=True, help="Report month in YYYY-MM format (e.g. 2026-05).")
    ap.add_argument(
        "--billing-project",
        help="GCP project to bill the BigQuery query to. Defaults to the first active app's project.",
    )
    args = ap.parse_args()

    file_slug, invoice_month, month_label = parse_month(args.month)

    print(f"GCP spend report → {month_label} (invoice.month={invoice_month})")

    apps = load_config(CONFIG_PATH)
    active  = [a for a in apps if a.status == "active"]
    pending = [a for a in apps if a.status == "pending"]
    if not active:
        sys.exit("No active apps in config — nothing to report.")
    print(f"  {len(active)} active apps, {len(pending)} pending")

    billing_project = args.billing_project or active[0].project_id

    jinja_env = Environment(
        loader=FileSystemLoader(str(SCRIPT_DIR)),
        undefined=StrictUndefined,
        trim_blocks=False,
        lstrip_blocks=False,
        autoescape=False,  # SQL & inline HTML; values are controlled
    )

    sql = render_query(active, jinja_env)
    client = bigquery.Client(project=billing_project)
    rows = run_query(client, sql, invoice_month)

    if not rows:
        print(f"  ⚠ no rows returned for invoice.month={invoice_month}. "
              f"Generating empty report.", file=sys.stderr)

    reports, currency = aggregate(rows, active)
    context = to_template_context(
        reports=reports,
        pending=pending,
        currency=currency,
        month_label=month_label,
        active_count=len(active),
    )

    # html template uses autoescape=True on its own env (defensive — user-visible)
    html_env = Environment(
        loader=FileSystemLoader(str(SCRIPT_DIR)),
        undefined=StrictUndefined,
        autoescape=True,
    )
    html = html_env.get_template("template.html.j2").render(**context)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUTPUT_DIR / f"{file_slug}.html"
    out_path.write_text(html)
    regenerate_index(OUTPUT_DIR)

    grand = context["grand_total"]
    print(f"  ✓ wrote {out_path.relative_to(REPO_ROOT)}  "
          f"(total ${grand:,.2f} {currency})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
