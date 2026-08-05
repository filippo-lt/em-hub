#!/usr/bin/env python3
"""
Firebase Remote Config client fetch report (per GCP project / env).

Pulls `FetchRemoteConfig` request counts from Cloud Monitoring
(serviceruntime.googleapis.com/api/request_count), aggregates daily totals
over a rolling window, and renders an HTML table.

Auth: Application Default Credentials (Monitoring Viewer on each project).
    gcloud auth application-default login

Usage:
    python run.py
    python run.py --days 30 --publish
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import datetime, timezone, timedelta
from pathlib import Path

try:
    import google.auth
    from google.auth.transport.requests import Request
    from jinja2 import Environment, FileSystemLoader, StrictUndefined
except ImportError as exc:
    sys.stderr.write(
        f"\nMissing dependency: {exc.name}\n"
        f"Install: make setup\n\n"
    )
    sys.exit(1)

# Reuse the Amplitude MAU fetcher vendored under scripts/gcp-spend/.
# It is stdlib-only, so the import is safe; creds are loaded lazily and only
# when --with-amplitude is passed.
SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR.parent / "gcp-spend"))
try:
    import amplitude
except ImportError:  # pragma: no cover
    amplitude = None

CONFIG_PATH = SCRIPT_DIR / "config.conf"
AMP_CONFIG_PATH = SCRIPT_DIR.parent / "gcp-spend" / "amplitude.conf"
OUTPUT_DIR = SCRIPT_DIR / "reports"
TEMPLATE = "template.html.j2"
CANVAS_TEMPLATE = "canvas.tsx.j2"
CANVAS_FILENAME = "remote-config-fetches.canvas.tsx"

# Blaze plan — https://firebase.google.com/docs/remote-config/pricing
DAILY_FREE_FETCHES = 100_000
TIER2_DAILY_MAX = 10_000_000  # 100,001 … 10,000,000 requests/day
PRICE_PER_REQUEST_TIER2 = 0.000006  # $0.06 / 10K requests
PRICE_PER_REQUEST_TIER3 = 0.000001  # $0.01 / 10K requests above 10M/day
WARN_PEAK_PCT = 20.0
WATCH_AVG_PCT = 20.0  # match reference board "~60% — watch" style thresholds
DEFAULT_WINDOW_DAYS = 30  # rolling month for avg / cost projection
TREND_RECENT_DAYS = 7
TREND_PRIOR_DAYS = 7

# Firebase config.conf and Amplitude amplitude.conf use slightly different
# friendly names for the same app. Map Firebase name → Amplitude name so the
# join works without renaming either side. Apps not listed here are matched
# verbatim (e.g. "FaceAI", "iMote", "ScreenMirroring").
AMP_NAME_ALIAS = {
    "AI Design": "AI Home Design",
    "ChatUltra": "Chat Ultra",
    "Step Counter": "StepCounter",
}


def trend_kind(trend: str) -> str:
    if trend.startswith("Up"):
        return "up"
    if trend.startswith("Down"):
        return "down"
    if trend == "—":
        return "none"
    return "flat"


def compute_status(
    *,
    avg_daily: float,
    peak_pct: float,
    est_monthly_cost: float,
    env: str,
) -> tuple[str, str]:
    """Return (tier, label) — tier: billable | watch | ok | na."""
    avg_mult = avg_daily / DAILY_FREE_FETCHES
    avg_pct = avg_mult * 100.0

    if est_monthly_cost > 0 or avg_daily > DAILY_FREE_FETCHES:
        mult = max(avg_mult, peak_pct / 100.0)
        return "billable", f"Billable — {mult:.1f}× over free tier"

    if env == "prod" and max(avg_pct, peak_pct) >= WATCH_AVG_PCT:
        pct = max(avg_pct, peak_pct)
        return "watch", f"~{pct:.0f}% of free tier — watch"

    if avg_pct >= 5 or peak_pct >= 5:
        return "ok", "under free tier"

    return "ok", "under free tier"

FETCH_METHOD = (
    "google.firebase.remoteconfig.v1.RemoteConfigService.FetchRemoteConfig"
)
MONITORING_SCOPE = "https://www.googleapis.com/auth/monitoring.read"


def _find_emhub_root(start: Path) -> Path | None:
    for cand in [start, *start.parents]:
        if (cand / "CLAUDE.md").exists() and (cand / "metrics").is_dir():
            return cand
    return None


EMHUB_ROOT = _find_emhub_root(SCRIPT_DIR)
EMHUB_PUBLISH_DIR = (
    EMHUB_ROOT / "metrics" / "firebase-remoteconfig" if EMHUB_ROOT else None
)
EMHUB_SHARE_DIR = (
    EMHUB_ROOT / "outputs" / "firebase-remoteconfig" if EMHUB_ROOT else None
)
SHARE_TITLE = "Utilities — Remote Config fetch usage"


@dataclass(frozen=True)
class AppRow:
    friendly_name: str
    project_id: str
    env: str  # dev | prod
    status: str


def load_config(path: Path) -> list[AppRow]:
    if not path.exists():
        sys.exit(f"Config not found: {path}")

    rows: list[AppRow] = []
    for lineno, raw in enumerate(path.read_text().splitlines(), start=1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        parts = [p.strip() for p in line.split("|")]
        if len(parts) != 4:
            sys.exit(
                f"{path}:{lineno}: expected 4 pipe-delimited fields, got {len(parts)}"
            )
        name, project_id, env, status = parts
        if env not in ("dev", "prod"):
            sys.exit(f"{path}:{lineno}: env must be dev or prod, got '{env}'")
        if status not in ("active", "skip"):
            sys.exit(f"{path}:{lineno}: status must be active or skip, got '{status}'")
        rows.append(AppRow(name, project_id, env, status))
    return [r for r in rows if r.status == "active"]


def _get_access_token() -> str:
    creds, _ = google.auth.default(scopes=[MONITORING_SCOPE])
    creds.refresh(Request())
    return creds.token


def fetch_daily_fetches(
    project_id: str,
    token: str,
    *,
    days: int,
) -> dict[str, int]:
    end = datetime.now(timezone.utc)
    start = end - timedelta(days=days)
    filt = (
        'metric.type="serviceruntime.googleapis.com/api/request_count" '
        'AND resource.labels.service="firebaseremoteconfig.googleapis.com" '
        f'AND resource.labels.method="{FETCH_METHOD}"'
    )
    params = {
        "filter": filt,
        "interval.startTime": start.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "interval.endTime": end.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "aggregation.alignmentPeriod": "86400s",
        "aggregation.perSeriesAligner": "ALIGN_SUM",
    }
    url = (
        f"https://monitoring.googleapis.com/v3/projects/{project_id}/timeSeries?"
        + urllib.parse.urlencode(params)
    )
    req = urllib.request.Request(
        url, headers={"Authorization": f"Bearer {token}"}
    )
    last_err: urllib.error.HTTPError | None = None
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=90) as resp:
                data = json.load(resp)
            break
        except urllib.error.HTTPError as exc:
            last_err = exc
            if exc.code in (429, 500, 503) and attempt < 3:
                time.sleep(1.5 * (attempt + 1))
                continue
            raise
    else:
        assert last_err is not None
        raise last_err

    by_day: dict[str, int] = {}
    for ts in data.get("timeSeries", []):
        for pt in ts.get("points", []):
            day = pt["interval"]["startTime"][:10]
            raw = pt["value"].get("int64Value") or pt["value"].get("doubleValue") or 0
            by_day[day] = by_day.get(day, 0) + int(float(raw))
    return by_day


def compute_trend(daily: dict[str, int]) -> str:
    if not daily:
        return "—"
    days = sorted(daily.keys())
    vals = [daily[d] for d in days]
    n = len(vals)
    if n < 4:
        return "Flat"

    def pct_change(recent: float, prior: float) -> float | None:
        if prior == 0:
            return None if recent == 0 else 100.0
        return (recent - prior) / prior * 100.0

    change: float | None = None
    if n >= 14:
        recent = sum(vals[-7:]) / 7
        prior = sum(vals[-14:-7]) / 7
        change = pct_change(recent, prior)
    else:
        mid = n // 2
        if mid == 0:
            return "Flat"
        recent = sum(vals[mid:]) / (n - mid)
        prior = sum(vals[:mid]) / mid
        change = pct_change(recent, prior)

    if change is None:
        return "Flat"
    if abs(change) < 5:
        return "Flat"
    if change > 0:
        return f"Up {change:.0f}%"
    return f"Down {abs(change):.0f}%"


def blaze_daily_fetch_cost_usd(daily_fetches: float) -> float:
    """Billable USD for one day's fetch volume on the Blaze plan."""
    if daily_fetches <= DAILY_FREE_FETCHES:
        return 0.0
    cost = 0.0
    tier2_volume = min(daily_fetches, TIER2_DAILY_MAX) - DAILY_FREE_FETCHES
    cost += tier2_volume * PRICE_PER_REQUEST_TIER2
    if daily_fetches > TIER2_DAILY_MAX:
        cost += (daily_fetches - TIER2_DAILY_MAX) * PRICE_PER_REQUEST_TIER3
    return cost


def est_monthly_cost_usd(daily: dict[str, int]) -> float:
    """Average tiered daily cost in the window × 30 days."""
    if not daily:
        return 0.0
    daily_costs = [blaze_daily_fetch_cost_usd(v) for v in daily.values()]
    return sum(daily_costs) / len(daily_costs) * 30


def _months_overlapping_window(end: datetime, days: int) -> list[str]:
    """Return ['YYYYMM', ...] for months overlapping [end-days, end], oldest first."""
    start = end - timedelta(days=days)
    months: list[str] = []
    y, m = start.year, start.month
    while (y, m) <= (end.year, end.month):
        months.append(f"{y:04d}{m:02d}")
        m += 1
        if m > 12:
            y, m = y + 1, 1
    return months


def load_amplitude_mau(months: list[str]) -> dict[str, int]:
    """Return {amplitude_friendly_name: mau} for the latest available month.

    Returns an empty dict if Amplitude isn't configured or the module isn't
    importable. Errors per-app are logged to stderr by the fetcher.
    """
    if amplitude is None:
        sys.stderr.write(
            "  ⚠ Amplitude module unavailable — skipping MAU cross-reference.\n"
        )
        return {}
    dotenv = EMHUB_ROOT / ".env" if EMHUB_ROOT else None
    if dotenv is None or not dotenv.exists():
        sys.stderr.write(
            "  ⚠ No .env at em-hub root — skipping MAU cross-reference.\n"
        )
        return {}
    amp_apps = amplitude.load_amplitude_config(AMP_CONFIG_PATH, dotenv)
    if not amp_apps:
        sys.stderr.write(
            "  ⚠ No Amplitude apps configured in amplitude.conf — "
            "skipping MAU cross-reference.\n"
        )
        return {}
    amp_data = amplitude.fetch_all(amp_apps, months)
    latest = months[-1]
    mau_by_app: dict[str, int] = {}
    for name, per_month in amp_data.items():
        # Prefer the latest month with a non-zero active count; fall back to
        # earlier months in the window so a partial current month doesn't
        # blank out the column.
        for m in reversed(months):
            entry = per_month.get(m)
            if entry and entry.get("active"):
                mau_by_app[name] = entry["active"]
                break
    return mau_by_app


def join_amplitude(rows: list[dict], mau_by_app: dict[str, int]) -> list[dict]:
    """Attach `mau` and `fetches_per_user_per_day` to eligible prod rows.

    fetches/user/day = avg_daily_fetches / MAU  (each active user triggers N
    fetches per day on average). Dev rows and rows without Amplitude coverage
    keep `mau = None`.
    """
    if not mau_by_app:
        return rows
    for r in rows:
        if r.get("env") != "prod" or r.get("avg_daily") is None:
            continue
        amp_name = AMP_NAME_ALIAS.get(r["friendly_name"], r["friendly_name"])
        mau = mau_by_app.get(amp_name)
        if mau and mau > 0:
            r["mau"] = mau
            r["fetches_per_user_per_day"] = round(r["avg_daily"] / mau, 2)
        else:
            r["mau"] = None
            r["fetches_per_user_per_day"] = None
    return rows


def build_row_stats(app: AppRow, daily: dict[str, int]) -> dict:
    if not daily:
        return {
            "friendly_name": app.friendly_name,
            "project_id": app.project_id,
            "env": app.env,
            "avg_daily": None,
            "peak_daily": None,
            "peak_day": None,
            "peak_pct": None,
            "trend": "—",
            "trend_kind": "none",
            "status_tier": "na",
            "status_label": "—",
            "est_monthly_cost": None,
            "est_daily_cost_peak": None,
            "warn": False,
            "mau": None,
            "fetches_per_user_per_day": None,
            "error": None,
        }

    vals = list(daily.values())
    avg_daily = sum(vals) / len(vals)
    peak_day = max(daily, key=daily.get)
    peak_daily = daily[peak_day]
    peak_pct = peak_daily / DAILY_FREE_FETCHES * 100.0
    cost = est_monthly_cost_usd(daily)
    peak_day_cost = blaze_daily_fetch_cost_usd(peak_daily)
    warn = app.env == "prod" and peak_pct >= WARN_PEAK_PCT
    trend = compute_trend(daily)
    status_tier, status_label = compute_status(
        avg_daily=avg_daily,
        peak_pct=peak_pct,
        est_monthly_cost=cost,
        env=app.env,
    )

    return {
        "friendly_name": app.friendly_name,
        "project_id": app.project_id,
        "env": app.env,
        "avg_daily": round(avg_daily),
        "peak_daily": peak_daily,
        "peak_day": peak_day,
        "peak_pct": peak_pct,
        "trend": trend,
        "trend_kind": trend_kind(trend),
        "status_tier": status_tier,
        "status_label": status_label,
        "est_monthly_cost": cost,
        "est_daily_cost_peak": peak_day_cost,
        "warn": warn,
        "mau": None,
        "fetches_per_user_per_day": None,
        "error": None,
    }


def process_app(app: AppRow, token: str, days: int) -> dict:
    try:
        daily = fetch_daily_fetches(app.project_id, token, days=days)
        return build_row_stats(app, daily)
    except urllib.error.HTTPError as exc:
        return {
            "friendly_name": app.friendly_name,
            "project_id": app.project_id,
            "env": app.env,
            "avg_daily": None,
            "peak_daily": None,
            "peak_day": None,
            "peak_pct": None,
            "trend": "—",
            "trend_kind": "none",
            "status_tier": "na",
            "status_label": "—",
            "est_monthly_cost": None,
            "warn": False,
            "mau": None,
            "fetches_per_user_per_day": None,
            "error": f"HTTP {exc.code}",
        }
    except Exception as exc:  # pragma: no cover
        return {
            "friendly_name": app.friendly_name,
            "project_id": app.project_id,
            "env": app.env,
            "avg_daily": None,
            "peak_daily": None,
            "peak_day": None,
            "peak_pct": None,
            "trend": "—",
            "trend_kind": "none",
            "status_tier": "na",
            "status_label": "—",
            "est_monthly_cost": None,
            "warn": False,
            "mau": None,
            "fetches_per_user_per_day": None,
            "error": str(exc)[:80],
        }


def sort_rows(rows: list[dict]) -> list[dict]:
    def key(r: dict) -> tuple:
        avg = r.get("avg_daily")
        # Errors / no data sink to the bottom.
        avg_sort = -(avg if avg is not None else -1)
        env_order = 0 if r["env"] == "dev" else 1
        return (avg_sort, r["friendly_name"].lower(), env_order)

    return sorted(rows, key=key)


def cursor_canvas_dir(emhub_root: Path) -> Path:
    """Cursor IDE canvas folder for this workspace (see canvas skill)."""
    slug = emhub_root.as_posix().lstrip("/").replace("/", "-")
    return Path.home() / ".cursor" / "projects" / slug / "canvases"


def render_canvas_tsx(
    rows: list[dict],
    *,
    days: int,
    generated_at: datetime,
    has_amplitude: bool = False,
) -> str:
    env = Environment(
        loader=FileSystemLoader(SCRIPT_DIR),
        undefined=StrictUndefined,
        autoescape=False,
    )
    tpl = env.get_template(CANVAS_TEMPLATE)
    snapshot = {
        "share_title": SHARE_TITLE,
        "generated_at": generated_at.isoformat(),
        "days": days,
        "trend_label": f"{TREND_RECENT_DAYS}d vs prior {TREND_PRIOR_DAYS}d",
        "daily_free": DAILY_FREE_FETCHES,
        "has_amplitude": has_amplitude,
        "rows": rows,
    }
    return tpl.render(snapshot_json=json.dumps(snapshot, indent=2))


def write_canvas_artifact(
    tsx: str,
    generated_at: datetime,
) -> list[Path]:
    if EMHUB_ROOT is None:
        sys.exit("Could not locate em-hub root for canvas export")
    paths: list[Path] = []

    cursor_dir = cursor_canvas_dir(EMHUB_ROOT)
    cursor_dir.mkdir(parents=True, exist_ok=True)
    cursor_path = cursor_dir / CANVAS_FILENAME
    cursor_path.write_text(tsx, encoding="utf-8")
    paths.append(cursor_path)

    if EMHUB_PUBLISH_DIR is not None:
        EMHUB_PUBLISH_DIR.mkdir(parents=True, exist_ok=True)
        tracked = EMHUB_PUBLISH_DIR / CANVAS_FILENAME
        tracked.write_text(tsx, encoding="utf-8")
        paths.append(tracked)

    return paths


def render_html(
    rows: list[dict], *, days: int, generated_at: datetime,
    has_amplitude: bool = False,
) -> str:
    env = Environment(
        loader=FileSystemLoader(SCRIPT_DIR),
        undefined=StrictUndefined,
        autoescape=True,
    )
    tpl = env.get_template(TEMPLATE)
    return tpl.render(
        rows=rows,
        days=days,
        share_title=SHARE_TITLE,
        generated_at=generated_at.strftime("%Y-%m-%d %H:%M UTC"),
        daily_free=DAILY_FREE_FETCHES,
        price_tier2=PRICE_PER_REQUEST_TIER2,
        price_tier3=PRICE_PER_REQUEST_TIER3,
        warn_peak_pct=WARN_PEAK_PCT,
        has_amplitude=has_amplitude,
        total_monthly=sum(
            (r.get("est_monthly_cost") or 0) for r in rows if r.get("env") == "prod"
        ),
        billable_count=sum(
            1 for r in rows if r.get("env") == "prod" and r.get("status_tier") == "billable"
        ),
        trend_label=f"{TREND_RECENT_DAYS}d vs prior {TREND_PRIOR_DAYS}d",
    )


def render_markdown_brief(
    rows: list[dict],
    *,
    days: int,
    generated_at: datetime,
    html_filename: str,
    has_amplitude: bool = False,
) -> str:
    """Slack/email-friendly summary; attach the paired HTML for the full table."""
    date_label = generated_at.strftime("%Y-%m-%d")
    lines = [
        f"# {SHARE_TITLE}",
        "",
        f"**As of:** {generated_at.strftime('%Y-%m-%d %H:%M UTC')} · "
        f"**Window:** {days} days · "
        f"**Pricing:** [Firebase Remote Config (Blaze)](https://firebase.google.com/docs/remote-config/pricing)",
        "",
        f"Full interactive table: `{html_filename}` (self-contained HTML — attach or upload to Drive).",
        "",
        "## Prod highlights",
        "",
    ]

    prod_rows = [r for r in rows if r["env"] == "prod" and r.get("avg_daily") is not None]
    prod_rows.sort(key=lambda r: r.get("est_monthly_cost") or 0, reverse=True)

    billed = [r for r in prod_rows if (r.get("est_monthly_cost") or 0) > 0]
    if billed:
        lines.append("**Estimated Blaze overage (monthly):**")
        for r in billed:
            lines.append(
                f"- **{r['friendly_name']}** — ~${r['est_monthly_cost']:.2f}/mo "
                f"(avg {r['avg_daily']:,} fetches/day, peak {r['peak_daily']:,} on {r['peak_day']})"
            )
        lines.append("")
    else:
        lines.append("- No prod project exceeds the 100k/day free tier on average (Blaze bill = $0).")
        lines.append("")

    warn_rows = [r for r in prod_rows if r.get("warn")]
    if warn_rows:
        lines.append("**Peak day ≥ 20% of free tier (100k/day):**")
        for r in warn_rows:
            lines.append(
                f"- **{r['friendly_name']}** — peak {r['peak_pct']:.1f}% "
                f"({r['peak_daily']:,} on {r['peak_day']})"
            )
        lines.append("")

    if has_amplitude:
        fpu_rows = [
            r for r in prod_rows
            if r.get("fetches_per_user_per_day") is not None
        ]
        fpu_rows.sort(
            key=lambda r: r["fetches_per_user_per_day"], reverse=True
        )
        if fpu_rows:
            lines.append("**Fetches per active user per day** (avg/day ÷ MAU):")
            for r in fpu_rows:
                lines.append(
                    f"- **{r['friendly_name']}** — {r['fetches_per_user_per_day']:.2f} "
                    f"fetches/user/day (avg {r['avg_daily']:,}/day, MAU {r['mau']:,})"
                )
            lines.append(
                "_~1.0 = healthy (one fetch per active user per day); "
                "≫1 suggests over-fetching, no client-side cache, or a retry loop._"
            )
            lines.append("")

    lines.extend(["## All environments", ""])
    if has_amplitude:
        lines.append(
            "| App | Env | Avg/day | Peak/day | Peak day | % free tier | Trend | Est. $/mo (Blaze) | MAU | Fetches/user/day |"
        )
        lines.append("|-----|-----|--------:|---------:|----------|------------:|-------|------------------:|----:|-----------------:|")
    else:
        lines.append(
            "| App | Env | Avg/day | Peak/day | Peak day | % free tier | Trend | Est. $/mo (Blaze) |"
        )
        lines.append("|-----|-----|--------:|---------:|----------|------------:|-------|------------------:|")

    for r in rows:
        if r.get("error"):
            err_row = (
                f"| {r['friendly_name']} | {r['env']} | — | — | — | — | {r['error']} | — |"
            )
            if has_amplitude:
                err_row += " — | — |"
            lines.append(err_row)
            continue
        if r.get("avg_daily") is None:
            nd_row = f"| {r['friendly_name']} | {r['env']} | — | — | — | — | no data | — |"
            if has_amplitude:
                nd_row += " — | — |"
            lines.append(nd_row)
            continue
        cost = r.get("est_monthly_cost") or 0
        base = (
            f"| {r['friendly_name']} | {r['env']} | {r['avg_daily']:,} | {r['peak_daily']:,} | "
            f"{r['peak_day']} | {r['peak_pct']:.1f}% | {r['trend']} | ${cost:.2f} |"
        )
        if has_amplitude:
            mau = r.get("mau")
            fpu = r.get("fetches_per_user_per_day")
            mau_str = f"{mau:,}" if mau is not None else "—"
            fpu_str = f"{fpu:.2f}" if fpu is not None else "—"
            base += f" {mau_str} | {fpu_str} |"
        lines.append(base)

    lines.extend(
        [
            "",
            "---",
            f"_Generated by `scripts/firebase-remoteconfig` on {date_label}._",
        ]
    )
    return "\n".join(lines) + "\n"


def write_share_artifacts(
    html: str,
    markdown: str,
    generated_at: datetime,
) -> tuple[Path, Path]:
    if EMHUB_SHARE_DIR is None:
        sys.exit("Could not locate em-hub root for --share")
    EMHUB_SHARE_DIR.mkdir(parents=True, exist_ok=True)
    stamp = generated_at.strftime("%Y-%m-%d")
    html_name = f"{stamp}_remote-config-fetches.html"
    md_name = f"{stamp}_remote-config-fetches.md"
    html_path = EMHUB_SHARE_DIR / html_name
    md_path = EMHUB_SHARE_DIR / md_name
    html_path.write_text(html, encoding="utf-8")
    md_path.write_text(markdown, encoding="utf-8")
    return html_path, md_path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--days",
        type=int,
        default=DEFAULT_WINDOW_DAYS,
        help=f"Rolling window for avg fetches and cost (default: {DEFAULT_WINDOW_DAYS})",
    )
    parser.add_argument(
        "--publish",
        action="store_true",
        help="Copy index.html into em-hub/metrics/firebase-remoteconfig/",
    )
    parser.add_argument(
        "--canvas",
        action="store_true",
        help="Write Cursor dashboard (.canvas.tsx) to Cursor canvases/ + metrics/",
    )
    parser.add_argument(
        "--share",
        action="store_true",
        help="Write dated HTML + Markdown brief to em-hub/outputs/firebase-remoteconfig/",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=4,
        help="Parallel project queries (default: 4; lower if you see HTTP 503)",
    )
    parser.add_argument(
        "--with-amplitude",
        action="store_true",
        help="Cross-reference prod rows with Amplitude MAU (adds MAU + "
             "fetches/user/day columns). Requires Amplitude creds in em-hub/.env "
             "and an entry in scripts/gcp-spend/amplitude.conf.",
    )
    args = parser.parse_args()

    apps = load_config(CONFIG_PATH)
    token = _get_access_token()

    print(f"Querying Remote Config fetches for {len(apps)} projects ({args.days}d window)…")

    results: list[dict] = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {
            pool.submit(process_app, app, token, args.days): app for app in apps
        }
        for fut in as_completed(futures):
            app = futures[fut]
            row = fut.result()
            results.append(row)
            label = f"{app.friendly_name} ({app.env})"
            if row.get("error"):
                print(f"  ✗ {label}: {row['error']}")
            elif row["avg_daily"] is None:
                print(f"  · {label}: no fetch data")
            else:
                print(
                    f"  ✓ {label}: avg {row['avg_daily']:,}/day, "
                    f"peak {row['peak_daily']:,} ({row['peak_pct']:.1f}% of free tier)"
                )

    results = sort_rows(results)

    has_amplitude = False
    if args.with_amplitude:
        months = _months_overlapping_window(datetime.now(timezone.utc), args.days)
        print(f"Fetching Amplitude MAU for {len(months)} month(s) "
              f"({months[0]}→{months[-1]})…")
        mau_by_app = load_amplitude_mau(months)
        if mau_by_app:
            results = join_amplitude(results, mau_by_app)
            has_amplitude = any(r.get("mau") is not None for r in results)
            joined = sum(1 for r in results if r.get("mau") is not None)
            print(f"  ✓ Joined MAU for {joined} prod app(s).")
        else:
            print("  · No Amplitude data — continuing without MAU columns.")

    generated_at = datetime.now(timezone.utc)
    html = render_html(
        results, days=args.days, generated_at=generated_at,
        has_amplitude=has_amplitude,
    )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUTPUT_DIR / "index.html"
    out_path.write_text(html, encoding="utf-8")
    print(f"\nWrote {out_path}")

    json_path = OUTPUT_DIR / "latest.json"
    json_path.write_text(
        json.dumps(
            {
                "generated_at": generated_at.isoformat(),
                "days": args.days,
                "rows": results,
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    if args.publish:
        if EMHUB_PUBLISH_DIR is None:
            sys.exit("Could not locate em-hub root for --publish")
        EMHUB_PUBLISH_DIR.mkdir(parents=True, exist_ok=True)
        shutil.copy2(out_path, EMHUB_PUBLISH_DIR / "index.html")
        shutil.copy2(json_path, EMHUB_PUBLISH_DIR / "latest.json")
        print(f"Published → {EMHUB_PUBLISH_DIR}")

    if args.share:
        stamp = generated_at.strftime("%Y-%m-%d")
        html_name = f"{stamp}_remote-config-fetches.html"
        md = render_markdown_brief(
            results,
            days=args.days,
            generated_at=generated_at,
            html_filename=html_name,
            has_amplitude=has_amplitude,
        )
        html_path, md_path = write_share_artifacts(html, md, generated_at)
        print(f"Shareable HTML → {html_path}")
        print(f"Shareable brief → {md_path}")

    if args.canvas or args.share:
        tsx = render_canvas_tsx(
            results, days=args.days, generated_at=generated_at,
            has_amplitude=has_amplitude,
        )
        canvas_paths = write_canvas_artifact(tsx, generated_at)
        for p in canvas_paths:
            print(f"Cursor dashboard → {p}")


if __name__ == "__main__":
    main()
