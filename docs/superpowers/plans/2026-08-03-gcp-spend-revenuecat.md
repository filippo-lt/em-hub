# GCP Spend — RevenueCat Revenue Correlation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add per-app monthly revenue from RevenueCat to the GCP spend report so it can show infra cost as a percentage of net proceeds, and surface month-over-month degradation in that ratio.

**Architecture:** A new `revenuecat.py` module in `scripts/gcp-spend/` mirrors the existing `amplitude.py` — it owns config parsing, credential lookup, HTTP, and month bucketing, degrades to `None` on every failure path, and never raises into `run.py`. `run.py` gains one field on `AppHistory` and two small pure metric helpers. The Jinja templates gain revenue-gated sections following the existing `has_amplitude` pattern.

**Tech Stack:** Python 3 stdlib (`urllib.request`, `json`, `dataclasses`, `unittest`), Jinja2 for templates. **No new pip dependencies.**

**Spec:** `docs/superpowers/specs/2026-08-03-gcp-spend-revenuecat-design.md`

## Global Constraints

- **No new pip dependencies.** `scripts/gcp-spend/requirements.txt` stays at `google-cloud-bigquery` + `jinja2`. Tests use stdlib `unittest`.
- **No RevenueCat failure may fail the run or affect spend/Amplitude data.** Every failure path degrades that one app to `None`.
- **The metric is named "infra cost as % of net proceeds"** — never "margin", never "profit". If Task 1 finds the net-proceeds selector unavailable, the name changes to "infra cost as % of gross revenue" everywhere it appears. The label must always match what was actually fetched.
- **`FRIENDLY_NAME` in `revenuecat.conf` must match `config.conf` exactly.** That string is the join key across all three data sources.
- **Secrets live only in `scripts/gcp-spend/.env`** (gitignored). Config files hold project IDs and env var *names* only.
- **Bash/Python style:** follow `AGENTS.md` — Python 3, f-strings, `subprocess.run` where shelling out. Match the surrounding file's comment density.
- **Commits:** the repo convention is that commits happen only when the user explicitly asks. Treat every "Commit" step as "stage and propose the commit" unless the user has said otherwise.

**Test command (all tasks):**

```bash
cd scripts/gcp-spend && python3 -m unittest test_revenuecat test_metrics -v
```

---

### Task 1: Probe the RevenueCat Charts API and lock down the response contract

> **COMPLETE — 2026-08-03.** All steps were executed against project `67002caa`
> (Chat Ultra). Findings are recorded in the "Verified API contract" section of
> the design spec, which is the authority for Tasks 3 and 4. Summary: Pro plan
> active; selector is `selectors={"revenue_type":"proceeds"}`; `resolution=month`
> works; `currency=EUR` is honoured; values are whole euros so `VALUE_SCALE = 1.0`;
> `incomplete` is a per-entry boolean in `values[]`; there are **three** measures
> (0 = Proceeds, 1 = Transactions, 2 = Ad Impressions). The steps below are
> retained as the reproduction record.

This task writes no production code. It resolves three unknowns that every later
task depends on. Multiple sources warn that RevenueCat's documented chart names
and selector values do not match the live API, so these must be observed, not
assumed.

**Files:**
- Modify: `docs/superpowers/specs/2026-08-03-gcp-spend-revenuecat-design.md` (append a "Verified API contract" section)

**Interfaces:**
- Consumes: nothing
- Produces: three verified constants used by Task 3 — the selector string for net proceeds, the value unit (whole currency units vs cents), and the exact field name/location of the incomplete-period flag.

- [ ] **Step 1: Confirm a Pro-plan secret key exists**

The Charts API requires RevenueCat's Pro plan. Confirm with the account owner
that the plan is active and obtain a secret key (`sk_...`).

Add it to `scripts/gcp-spend/.env` using the naming convention from
`amplitude.conf`:

```bash
echo 'REVENUECAT_CHATULTRA_KEY=sk_REPLACE_WITH_REAL_KEY' >> scripts/gcp-spend/.env
```

If no Pro plan is available, **stop here and report back** — the rest of the plan
cannot proceed.

- [ ] **Step 2: Discover the available selectors for the revenue chart**

```bash
cd scripts/gcp-spend && set -a && . ./.env && set +a && \
curl -s -H "Authorization: Bearer $REVENUECAT_CHATULTRA_KEY" \
  "https://api.revenuecat.com/v2/projects/<PROJECT_ID>/charts/revenue/options" \
  | python3 -m json.tool
```

Read the response and find the selector that means **proceeds net of taxes and
commissions** (as opposed to gross revenue, or revenue net of taxes only).
Record its exact parameter name and value.

If the endpoint 404s, the chart is not named `revenue` on this account — list
what is available and adapt.

- [ ] **Step 3: Fetch one real 12-month series and record the shape**

```bash
cd scripts/gcp-spend && set -a && . ./.env && set +a && \
curl -s -H "Authorization: Bearer $REVENUECAT_CHATULTRA_KEY" \
  "https://api.revenuecat.com/v2/projects/<PROJECT_ID>/charts/revenue?start_date=2025-08-01&end_date=2026-08-03&resolution=month&currency=EUR&<SELECTOR_FROM_STEP_2>" \
  | python3 -m json.tool
```

Record three things from the output:

1. **Units.** One source documents revenue "expressed in cents", another shows
   plain currency units. Compare a settled month's value against the RevenueCat
   dashboard for that month. If the API returns cents, the scale factor is
   `0.01`; if whole units, `1.0`.
2. **The incomplete flag.** Find where unsettled periods are marked. It may be a
   per-entry `"incomplete": true` inside `values[]`, or a separate top-level
   field. Record the exact location and name.
3. **The `measure` indices.** Confirm `measure == 0` is the revenue amount and
   `measure == 1` is the transaction count.

- [ ] **Step 4: Append the verified contract to the spec**

Add a section to the spec titled `## Verified API contract (2026-08-03)`
recording: the exact chart URL used, the selector parameter and value, the value
scale factor, the incomplete-flag field name and location, and a sample
two-entry excerpt of the `values[]` array.

This section is what Task 3 implements against. If the observed shape differs
from what Task 3's code assumes, **the observed shape wins** — update Task 3's
constants and tests to match.

- [ ] **Step 5: Commit**

```bash
git add docs/superpowers/specs/2026-08-03-gcp-spend-revenuecat-design.md
git commit -m "docs: record verified RevenueCat Charts API contract"
```

---

### Task 2: Config loading

**Files:**
- Create: `scripts/gcp-spend/revenuecat.py`
- Create: `scripts/gcp-spend/revenuecat.conf`
- Create: `scripts/gcp-spend/test_revenuecat.py`

**Interfaces:**
- Consumes: `amplitude.load_dotenv(path: Path) -> None` (existing)
- Produces:
  - `RevenueCatApp(friendly_name: str, project_id: str, api_key: str)` — frozen dataclass
  - `load_revenuecat_config(path: Path, dotenv_path: Path) -> list[RevenueCatApp]`

- [ ] **Step 1: Write the failing tests**

Create `scripts/gcp-spend/test_revenuecat.py`:

```python
import os
import tempfile
import unittest
from pathlib import Path

import revenuecat


class LoadConfigTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        self.dotenv = self.tmp / ".env"
        self.dotenv.write_text("")
        self.addCleanup(self._tmp.cleanup)

    def _conf(self, body: str) -> Path:
        p = self.tmp / "revenuecat.conf"
        p.write_text(body)
        return p

    def test_missing_file_returns_empty_list(self):
        self.assertEqual(
            revenuecat.load_revenuecat_config(self.tmp / "nope.conf", self.dotenv),
            [],
        )

    def test_parses_row_and_resolves_key_from_env(self):
        os.environ["RC_TEST_KEY"] = "sk_test_123"
        self.addCleanup(os.environ.pop, "RC_TEST_KEY", None)
        conf = self._conf("Chat Ultra | proj_abc | RC_TEST_KEY\n")

        apps = revenuecat.load_revenuecat_config(conf, self.dotenv)

        self.assertEqual(len(apps), 1)
        self.assertEqual(apps[0].friendly_name, "Chat Ultra")
        self.assertEqual(apps[0].project_id, "proj_abc")
        self.assertEqual(apps[0].api_key, "sk_test_123")

    def test_skips_comments_and_blank_lines(self):
        os.environ["RC_TEST_KEY"] = "sk_test_123"
        self.addCleanup(os.environ.pop, "RC_TEST_KEY", None)
        conf = self._conf(
            "# a comment\n"
            "\n"
            "Chat Ultra | proj_abc | RC_TEST_KEY\n"
        )

        self.assertEqual(len(revenuecat.load_revenuecat_config(conf, self.dotenv)), 1)

    def test_skips_app_with_unset_env_var(self):
        os.environ.pop("RC_ABSENT_KEY", None)
        conf = self._conf("Chat Ultra | proj_abc | RC_ABSENT_KEY\n")

        self.assertEqual(revenuecat.load_revenuecat_config(conf, self.dotenv), [])

    def test_skips_app_with_empty_project_id(self):
        os.environ["RC_TEST_KEY"] = "sk_test_123"
        self.addCleanup(os.environ.pop, "RC_TEST_KEY", None)
        conf = self._conf("Truth Seeker |  | RC_TEST_KEY\n")

        self.assertEqual(revenuecat.load_revenuecat_config(conf, self.dotenv), [])

    def test_wrong_field_count_exits(self):
        conf = self._conf("Chat Ultra | proj_abc\n")

        with self.assertRaises(SystemExit):
            revenuecat.load_revenuecat_config(conf, self.dotenv)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the tests to verify they fail**

```bash
cd scripts/gcp-spend && python3 -m unittest test_revenuecat -v
```

Expected: `ModuleNotFoundError: No module named 'revenuecat'`

- [ ] **Step 3: Write the module with config loading only**

Create `scripts/gcp-spend/revenuecat.py`:

```python
"""
RevenueCat revenue fetcher for the GCP spend dashboard.

Reads revenuecat.conf (one row per app), loads env vars from .env, and fetches
net proceeds per month per app via RevenueCat's Charts API v2.

Returned shape (consumed by run.py):
    {
      "Chat Ultra": {"202605": 41233.10, "202606": 44120.55, "202607": None},
      ...
    }

None means "not known for that month" — either unavailable, or a period
RevenueCat still considers unsettled. Apps without a row in revenuecat.conf are
absent from the dict.
"""

from __future__ import annotations

import os
import sys
from dataclasses import dataclass
from pathlib import Path

from amplitude import load_dotenv


@dataclass(frozen=True)
class RevenueCatApp:
    friendly_name: str
    project_id:    str
    api_key:       str


def load_revenuecat_config(path: Path, dotenv_path: Path) -> list[RevenueCatApp]:
    if not path.exists():
        return []
    load_dotenv(dotenv_path)

    apps: list[RevenueCatApp] = []
    for lineno, raw in enumerate(path.read_text().splitlines(), start=1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        parts = [p.strip() for p in line.split("|")]
        if len(parts) != 3:
            sys.exit(
                f"{path}:{lineno}: expected 3 pipe-delimited fields, got {len(parts)}\n"
                f"  line: {raw}"
            )
        name, project_id, key_env = parts
        if not project_id:
            print(f"  ⚠ {name}: no RevenueCat project id — skipping", file=sys.stderr)
            continue
        api_key = os.environ.get(key_env, "")
        if not api_key:
            print(f"  ⚠ {name}: env var {key_env} not set — skipping", file=sys.stderr)
            continue
        apps.append(RevenueCatApp(name, project_id, api_key))
    return apps
```

- [ ] **Step 4: Run the tests to verify they pass**

```bash
cd scripts/gcp-spend && python3 -m unittest test_revenuecat -v
```

Expected: 6 tests, all PASS.

- [ ] **Step 5: Create the config file**

Create `scripts/gcp-spend/revenuecat.conf`. Fill in real project IDs for the apps
that have them; leave the project-id field empty for apps that do not, which
makes them skip cleanly.

```
# RevenueCat revenue — app → project + credential mapping.
# Consumed by scripts/gcp-spend/revenuecat.py
#
# Format:  FRIENDLY_NAME | REVENUECAT_PROJECT_ID | API_KEY_ENV_VAR
#
# FRIENDLY_NAME must match config.conf exactly — it is the join key.
# Secrets live in .env (gitignored), never here.
# Leave PROJECT_ID empty for an app you don't have access to yet; it is skipped.

Chat Ultra       |  | REVENUECAT_CHATULTRA_KEY
PDF Editor       |  | REVENUECAT_PDFEDITOR_KEY
Music Player     |  | REVENUECAT_MUSICPLAYER_KEY
iMote            |  | REVENUECAT_IMOTE_KEY
AI Home Design   |  | REVENUECAT_AIHOME_KEY
ScreenMirroring  |  | REVENUECAT_SCREENMIRRORING_KEY
FaceAI           |  | REVENUECAT_FACEAI_KEY
Mirage           |  | REVENUECAT_MIRAGE_KEY
Goya             |  | REVENUECAT_GOYA_KEY
TraceCheck       |  | REVENUECAT_TRUTHSEEKER_KEY
```

- [ ] **Step 6: Commit**

```bash
git add scripts/gcp-spend/revenuecat.py scripts/gcp-spend/revenuecat.conf scripts/gcp-spend/test_revenuecat.py
git commit -m "feat(gcp-spend): add RevenueCat config loading"
```

---

### Task 3: Chart response parsing

This is where the `incomplete` trap is handled. Plotting an unsettled month would
depress the revenue denominator and fire a false "spend outpacing revenue" alarm
every month.

**Files:**
- Modify: `scripts/gcp-spend/revenuecat.py`
- Modify: `scripts/gcp-spend/test_revenuecat.py`

**Interfaces:**
- Consumes: the verified contract recorded in Task 1
- Produces: `parse_chart_response(payload: dict, months: list[str]) -> dict[str, float | None]`

- [ ] **Step 1: Write the failing tests**

Append to `scripts/gcp-spend/test_revenuecat.py`, above the `if __name__` block:

```python
class ParseChartResponseTest(unittest.TestCase):
    MONTHS = ["202605", "202606", "202607"]

    @staticmethod
    def _ts(year: int, month: int) -> int:
        from datetime import datetime, timezone
        return int(datetime(year, month, 1, tzinfo=timezone.utc).timestamp())

    def test_maps_cohort_timestamps_to_yyyymm(self):
        payload = {"values": [
            {"cohort": self._ts(2026, 5), "measure": 0, "value": 100.0},
            {"cohort": self._ts(2026, 6), "measure": 0, "value": 250.5},
        ]}

        out = revenuecat.parse_chart_response(payload, self.MONTHS)

        self.assertEqual(out["202605"], 100.0)
        self.assertEqual(out["202606"], 250.5)

    def test_every_requested_month_is_a_key(self):
        out = revenuecat.parse_chart_response({"values": []}, self.MONTHS)

        self.assertEqual(sorted(out), sorted(self.MONTHS))
        self.assertTrue(all(v is None for v in out.values()))

    def test_ignores_secondary_measure(self):
        payload = {"values": [
            {"cohort": self._ts(2026, 5), "measure": 0, "value": 100.0},
            {"cohort": self._ts(2026, 5), "measure": 1, "value": 42.0},
        ]}

        self.assertEqual(revenuecat.parse_chart_response(payload, self.MONTHS)["202605"], 100.0)

    def test_incomplete_period_becomes_none(self):
        payload = {"values": [
            {"cohort": self._ts(2026, 7), "measure": 0, "value": 12.0, "incomplete": True},
        ]}

        self.assertIsNone(revenuecat.parse_chart_response(payload, self.MONTHS)["202607"])

    def test_months_outside_the_window_are_dropped(self):
        payload = {"values": [
            {"cohort": self._ts(2025, 1), "measure": 0, "value": 999.0},
        ]}

        out = revenuecat.parse_chart_response(payload, self.MONTHS)

        self.assertNotIn("202501", out)
        self.assertTrue(all(v is None for v in out.values()))

    def test_null_value_becomes_none(self):
        payload = {"values": [
            {"cohort": self._ts(2026, 5), "measure": 0, "value": None},
        ]}

        self.assertIsNone(revenuecat.parse_chart_response(payload, self.MONTHS)["202605"])

    def test_empty_payload_is_safe(self):
        out = revenuecat.parse_chart_response({}, self.MONTHS)

        self.assertTrue(all(v is None for v in out.values()))
```

- [ ] **Step 2: Run the tests to verify they fail**

```bash
cd scripts/gcp-spend && python3 -m unittest test_revenuecat -v
```

Expected: FAIL with `AttributeError: module 'revenuecat' has no attribute 'parse_chart_response'`

- [ ] **Step 3: Implement the parser**

Add to the imports at the top of `revenuecat.py`:

```python
from datetime import datetime, timezone
```

Add these constants below the module docstring's imports:

```python
# Verified 2026-08-03: the API returns whole currency units, not cents.
VALUE_SCALE = 1.0

# Series index 0 is the money. 1 is transaction count, 2 is ad impressions.
PRIMARY_MEASURE = 0
```

Add the function:

```python
def parse_chart_response(payload: dict, months: list[str]) -> dict[str, float | None]:
    """Map a /charts/revenue response onto {yyyymm: net_proceeds | None}.

    Every requested month is present as a key so callers never distinguish
    "absent" from "unknown". Periods RevenueCat still considers unsettled are
    left as None: their value is real but partial, and plotting it would
    understate revenue in the freshest month — exactly where the cost/revenue
    ratio is read.
    """
    out: dict[str, float | None] = {m: None for m in months}
    for entry in payload.get("values") or []:
        if entry.get("measure") != PRIMARY_MEASURE:
            continue
        if entry.get("incomplete"):
            continue
        cohort = entry.get("cohort")
        value  = entry.get("value")
        if cohort is None or value is None:
            continue
        yyyymm = datetime.fromtimestamp(int(cohort), tz=timezone.utc).strftime("%Y%m")
        if yyyymm not in out:
            continue
        out[yyyymm] = round(float(value) * VALUE_SCALE, 2)
    return out
```

- [ ] **Step 4: Reconcile against the Task 1 findings**

Open the "Verified API contract" section of the spec. If the real response marks
incomplete periods somewhere other than a per-entry `incomplete` key, or the
values are in cents, change `VALUE_SCALE` and the `incomplete` check to match the
observed shape, and update `test_incomplete_period_becomes_none` to use the real
field. The observed shape wins over the code written in Step 3.

- [ ] **Step 5: Run the tests to verify they pass**

```bash
cd scripts/gcp-spend && python3 -m unittest test_revenuecat -v
```

Expected: 13 tests, all PASS.

- [ ] **Step 6: Commit**

```bash
git add scripts/gcp-spend/revenuecat.py scripts/gcp-spend/test_revenuecat.py
git commit -m "feat(gcp-spend): parse RevenueCat chart responses, dropping unsettled periods"
```

---

### Task 4: Fetching with throttle and failure isolation

**Files:**
- Modify: `scripts/gcp-spend/revenuecat.py`
- Modify: `scripts/gcp-spend/test_revenuecat.py`

**Interfaces:**
- Consumes: `RevenueCatApp`, `parse_chart_response` (Tasks 2 and 3)
- Produces: `fetch_all(rc_apps: list[RevenueCatApp], months: list[str], *, fetch=None, sleep=None) -> dict[str, dict[str, float | None]]`

The `fetch` and `sleep` keyword arguments exist so tests can run without network
or delay. Production callers omit both.

- [ ] **Step 1: Write the failing tests**

Append to `scripts/gcp-spend/test_revenuecat.py`, above the `if __name__` block:

```python
class FetchAllTest(unittest.TestCase):
    MONTHS = ["202605", "202606"]

    def _app(self, name="Chat Ultra"):
        return revenuecat.RevenueCatApp(name, "proj_abc", "sk_test")

    @staticmethod
    def _ts(year: int, month: int) -> int:
        from datetime import datetime, timezone
        return int(datetime(year, month, 1, tzinfo=timezone.utc).timestamp())

    def test_returns_empty_for_no_apps(self):
        self.assertEqual(revenuecat.fetch_all([], self.MONTHS), {})

    def test_returns_empty_for_no_months(self):
        self.assertEqual(revenuecat.fetch_all([self._app()], []), {})

    def test_maps_each_app_to_its_parsed_series(self):
        payload = {"values": [
            {"cohort": self._ts(2026, 5), "measure": 0, "value": 100.0},
        ]}

        out = revenuecat.fetch_all(
            [self._app()], self.MONTHS,
            fetch=lambda app, months: payload, sleep=lambda s: None,
        )

        self.assertEqual(out["Chat Ultra"]["202605"], 100.0)
        self.assertIsNone(out["Chat Ultra"]["202606"])

    def test_failed_fetch_yields_all_none_not_an_exception(self):
        out = revenuecat.fetch_all(
            [self._app()], self.MONTHS,
            fetch=lambda app, months: None, sleep=lambda s: None,
        )

        self.assertIn("Chat Ultra", out)
        self.assertTrue(all(v is None for v in out["Chat Ultra"].values()))

    def test_one_app_failing_does_not_affect_another(self):
        good = {"values": [{"cohort": self._ts(2026, 5), "measure": 0, "value": 7.0}]}

        def fetch(app, months):
            return None if app.friendly_name == "Bad App" else good

        out = revenuecat.fetch_all(
            [self._app("Bad App"), self._app("Good App")], self.MONTHS,
            fetch=fetch, sleep=lambda s: None,
        )

        self.assertIsNone(out["Bad App"]["202605"])
        self.assertEqual(out["Good App"]["202605"], 7.0)

    def test_throttles_between_apps_but_not_before_the_first(self):
        slept = []

        revenuecat.fetch_all(
            [self._app("A"), self._app("B"), self._app("C")], self.MONTHS,
            fetch=lambda app, months: {"values": []}, sleep=slept.append,
        )

        self.assertEqual(slept, [revenuecat.THROTTLE_SECONDS] * 2)
```

- [ ] **Step 2: Run the tests to verify they fail**

```bash
cd scripts/gcp-spend && python3 -m unittest test_revenuecat -v
```

Expected: FAIL with `AttributeError: module 'revenuecat' has no attribute 'fetch_all'`

- [ ] **Step 3: Implement the fetch layer**

Add to the imports at the top of `revenuecat.py`:

```python
import json
import time
import urllib.error
import urllib.parse
import urllib.request
```

Add these constants next to `VALUE_SCALE`:

```python
API_BASE = "https://api.revenuecat.com/v2"

# The charts domain allows 15 requests/minute. One call per app fired in a burst
# would breach that with a full portfolio, so space them out. Worst case this
# adds roughly 75s to a monthly report run.
THROTTLE_SECONDS = 4.1

REQUEST_TIMEOUT = 30

# Verified 2026-08-03. "proceeds" is revenue after refunds, minus the stores'
# taxes and commission — the money actually received. The default is "revenue"
# (gross), which would overstate the denominator of the cost ratio.
REVENUE_SELECTOR = {"selectors": '{"revenue_type":"proceeds"}'}
```

Add the functions:

```python
def _month_bounds(months: list[str]) -> tuple[str, str]:
    """('202605', ..., '202607') → ('2026-05-01', '2026-07-31')."""
    from datetime import date, timedelta
    first = months[0]
    last  = months[-1]
    start = f"{first[:4]}-{first[4:]}-01"
    y, m = int(last[:4]), int(last[4:])
    nxt = date(y + 1, 1, 1) if m == 12 else date(y, m + 1, 1)
    return start, (nxt - timedelta(days=1)).isoformat()


def _fetch_chart(app: RevenueCatApp, months: list[str]) -> dict | None:
    """One Charts API call covering the whole window. None on any failure."""
    start, end = _month_bounds(months)
    params = {
        "start_date": start,
        "end_date":   end,
        "resolution": "month",
        "currency":   "EUR",
        **REVENUE_SELECTOR,
    }
    url = f"{API_BASE}/projects/{app.project_id}/charts/revenue?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {app.api_key}",
        "Accept":        "application/json",
    })
    try:
        with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")[:200]
        print(f"  ⚠ {app.friendly_name} revenue: HTTP {e.code} — {body}", file=sys.stderr)
        return None
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as e:
        print(f"  ⚠ {app.friendly_name} revenue: {e}", file=sys.stderr)
        return None


def fetch_all(
    rc_apps: list[RevenueCatApp],
    months: list[str],
    *,
    fetch=None,
    sleep=None,
) -> dict[str, dict[str, float | None]]:
    """Returns {friendly_name: {yyyymm: net_proceeds | None}}.

    The inner dict is keyed by every month in `months`. An app whose fetch fails
    is still present, with all-None values — callers must not have to tell
    "failed" apart from "no revenue configured".

    `fetch` and `sleep` are injectable for tests; production omits them.
    """
    if not rc_apps or not months:
        return {}

    fetch = fetch or _fetch_chart
    sleep = sleep or time.sleep

    out: dict[str, dict[str, float | None]] = {}
    print(f"  Fetching RevenueCat data for {len(rc_apps)} app(s), "
          f"{months[0]} → {months[-1]}...", flush=True)

    for i, app in enumerate(rc_apps):
        if i > 0:
            sleep(THROTTLE_SECONDS)
        payload = fetch(app, months)
        series = (parse_chart_response(payload, months) if payload
                  else {m: None for m in months})
        out[app.friendly_name] = series
        latest = series[months[-1]]
        shown = f"€{latest:,.2f}" if latest is not None else "n/a (unsettled or unavailable)"
        print(f"    {app.friendly_name}: {months[-1]} net proceeds={shown}")
    return out
```

- [ ] **Step 4: Run the tests to verify they pass**

```bash
cd scripts/gcp-spend && python3 -m unittest test_revenuecat -v
```

Expected: 19 tests, all PASS.

- [ ] **Step 5: Make one real call end to end**

`REVENUE_SELECTOR` is already the verified value from Task 1. Confirm the whole
module works against the live API:

```bash
cd scripts/gcp-spend && python3 -c "
import revenuecat as rc
from pathlib import Path
apps = rc.load_revenuecat_config(Path('revenuecat.conf'), Path('.env'))
print(rc.fetch_all(apps[:1], ['202605','202606','202607']))
"
```

Expected: real euro figures for settled months, `None` for the current month.

- [ ] **Step 6: Commit**

```bash
git add scripts/gcp-spend/revenuecat.py scripts/gcp-spend/test_revenuecat.py
git commit -m "feat(gcp-spend): fetch RevenueCat revenue with throttling and per-app failure isolation"
```

---

### Task 5: Wire revenue into aggregation and define the metrics

**Files:**
- Modify: `scripts/gcp-spend/run.py:216-227` (`AppHistory`)
- Modify: `scripts/gcp-spend/run.py:229-296` (`aggregate`)
- Modify: `scripts/gcp-spend/run.py:1077-1080` (`main`, fetch + aggregate wiring)
- Modify: `scripts/gcp-spend/run.py:48-64` (paths — add `RC_CONFIG_PATH`)
- Create: `scripts/gcp-spend/test_metrics.py`

**Interfaces:**
- Consumes: `revenuecat.load_revenuecat_config`, `revenuecat.fetch_all` (Tasks 2 and 4)
- Produces:
  - `AppHistory.revenue_by_month: list[float | None]`
  - `cost_ratio(spend: float, revenue: float | None) -> float | None`
  - `cost_ratio_delta_pp(cur: float | None, prev: float | None) -> float | None`

- [ ] **Step 1: Write the failing tests**

Create `scripts/gcp-spend/test_metrics.py`:

```python
import unittest

import run


class CostRatioTest(unittest.TestCase):
    def test_computes_percentage(self):
        self.assertAlmostEqual(run.cost_ratio(250.0, 1000.0), 25.0)

    def test_none_revenue_gives_none(self):
        self.assertIsNone(run.cost_ratio(250.0, None))

    def test_zero_revenue_gives_none_not_division_error(self):
        self.assertIsNone(run.cost_ratio(250.0, 0.0))

    def test_negative_revenue_gives_none(self):
        self.assertIsNone(run.cost_ratio(250.0, -10.0))

    def test_spend_above_revenue_exceeds_one_hundred(self):
        self.assertAlmostEqual(run.cost_ratio(1500.0, 1000.0), 150.0)

    def test_zero_spend_is_zero_not_none(self):
        self.assertEqual(run.cost_ratio(0.0, 1000.0), 0.0)


class CostRatioDeltaTest(unittest.TestCase):
    def test_rising_ratio_is_positive(self):
        self.assertAlmostEqual(run.cost_ratio_delta_pp(30.0, 25.0), 5.0)

    def test_falling_ratio_is_negative(self):
        self.assertAlmostEqual(run.cost_ratio_delta_pp(20.0, 25.0), -5.0)

    def test_none_current_gives_none(self):
        self.assertIsNone(run.cost_ratio_delta_pp(None, 25.0))

    def test_none_previous_gives_none(self):
        self.assertIsNone(run.cost_ratio_delta_pp(30.0, None))


class AggregateRevenueTest(unittest.TestCase):
    MONTHS = ["202605", "202606"]

    def _apps(self):
        return [run.AppConfig("Chat Ultra", "chatai2-32311", "billing_export_data",
                              "01D6E9-4884D4-C31F38", "active")]

    def _rows(self):
        return [{"app": "Chat Ultra", "invoice_month": "202605",
                 "service": "Compute Engine", "net_cost": 100.0, "currency": "EUR"}]

    def test_revenue_is_attached_to_the_matching_app(self):
        histories, _, _ = run.aggregate(
            self._rows(), self._apps(), self.MONTHS,
            rev_data={"Chat Ultra": {"202605": 500.0, "202606": None}},
        )

        self.assertEqual(histories[0].revenue_by_month, [500.0, None])

    def test_app_without_revenue_data_gets_all_none(self):
        histories, _, _ = run.aggregate(self._rows(), self._apps(), self.MONTHS)

        self.assertEqual(histories[0].revenue_by_month, [None, None])


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the tests to verify they fail**

```bash
cd scripts/gcp-spend && python3 -m unittest test_metrics -v
```

Expected: FAIL with `AttributeError: module 'run' has no attribute 'cost_ratio'`

- [ ] **Step 3: Add the field, the parameter, and the metric helpers**

In `run.py`, add to the `AppHistory` dataclass alongside `mau_by_month`:

```python
    revenue_by_month: list[float | None] = field(default_factory=list)
```

Change the `aggregate` signature to accept revenue data:

```python
def aggregate(
    rows: Iterable[bigquery.Row],
    active_apps: list[AppConfig],
    months: list[str],
    amp_data: dict[str, dict[str, dict[str, int]]] | None = None,
    rev_data: dict[str, dict[str, float | None]] | None = None,
) -> tuple[list[AppHistory], list[dict], str]:
```

Inside `aggregate`, next to `amp_data = amp_data or {}`:

```python
    rev_data = rev_data or {}
```

and inside the per-app loop, next to the `mau_by_month` assignment:

```python
        app_rev = rev_data.get(app_name) or {}
        revenue_by_month = [app_rev.get(m) for m in months]
```

then pass `revenue_by_month=revenue_by_month` into the `AppHistory(...)` call.

Add the two helpers near `slugify`:

```python
def cost_ratio(spend: float, revenue: float | None) -> float | None:
    """Infra cost as a percentage of net proceeds.

    None when revenue is unknown or non-positive — a zero or negative
    denominator has no meaningful ratio, and returning a number there would
    read as a real signal.
    """
    if revenue is None or revenue <= 0:
        return None
    return spend / revenue * 100.0


def cost_ratio_delta_pp(cur: float | None, prev: float | None) -> float | None:
    """Month-over-month change in the cost ratio, in percentage points.
    Positive means infra is taking a growing share of revenue."""
    if cur is None or prev is None:
        return None
    return cur - prev
```

- [ ] **Step 4: Wire the fetch into `main`**

Next to `AMP_CONFIG_PATH` in the paths block:

```python
RC_CONFIG_PATH  = SCRIPT_DIR / "revenuecat.conf"
```

Next to the `import amplitude` line:

```python
import revenuecat
```

In `main`, directly after the Amplitude fetch:

```python
    rc_apps  = revenuecat.load_revenuecat_config(RC_CONFIG_PATH, DOTENV_PATH)
    rev_data = revenuecat.fetch_all(rc_apps, months) if rc_apps else {}
```

and change the aggregate call to:

```python
    histories, monthly_totals, currency = aggregate(rows, active, months, amp_data, rev_data)
```

- [ ] **Step 5: Run the tests to verify they pass**

```bash
cd scripts/gcp-spend && python3 -m unittest test_revenuecat test_metrics -v
```

Expected: 31 tests, all PASS.

- [ ] **Step 6: Commit**

```bash
git add scripts/gcp-spend/run.py scripts/gcp-spend/test_metrics.py
git commit -m "feat(gcp-spend): attach RevenueCat revenue to app history and define the cost ratio"
```

---

### Task 6: Chart builders — percentage axis and overlay series selection

**Files:**
- Modify: `scripts/gcp-spend/run.py:390-490` (`build_line_chart`)
- Modify: `scripts/gcp-spend/run.py` (new `build_overlay_series`)
- Modify: `scripts/gcp-spend/test_metrics.py`

**Interfaces:**
- Consumes: `AppHistory` with `revenue_by_month` (Task 5)
- Produces:
  - `build_line_chart(..., fmt_y="pct")` producing `"25%"`-style axis labels
  - `build_overlay_series(h: AppHistory, has_amplitude: bool) -> list[dict]`
  - `MIN_REVENUE_MONTHS_FOR_OVERLAY = 3`

- [ ] **Step 1: Write the failing tests**

Append to `scripts/gcp-spend/test_metrics.py`, above the `if __name__` block:

```python
class PctAxisTest(unittest.TestCase):
    MONTHS = ["202605", "202606", "202607"]

    def test_pct_gridline_labels_carry_a_percent_sign(self):
        chart = run.build_line_chart(
            [10.0, 20.0, 40.0], self.MONTHS, "202607", fmt_y="pct",
        )

        self.assertTrue(all(g["label"].endswith("%") for g in chart["gridlines"]))

    def test_pct_labels_are_not_abbreviated_to_thousands(self):
        chart = run.build_line_chart(
            [1500.0, 1600.0, 1700.0], self.MONTHS, "202607", fmt_y="pct",
        )

        self.assertNotIn("K", chart["gridlines"][-1]["label"])


class OverlaySeriesTest(unittest.TestCase):
    def _history(self, revenue):
        return run.AppHistory(
            name="Chat Ultra", project_id="p", color="#000",
            by_month=[1.0] * len(revenue),
            services_by_month={}, total_in_window=1.0,
            mau_by_month=[10] * len(revenue),
            new_by_month=[1] * len(revenue),
            revenue_by_month=revenue,
        )

    def test_spend_only_when_nothing_else_is_available(self):
        series = run.build_overlay_series(
            self._history([None, None, None]), has_amplitude=False,
        )

        self.assertEqual([s["name"] for s in series], ["Spend"])

    def test_amplitude_adds_mau_and_new_users(self):
        series = run.build_overlay_series(
            self._history([None, None, None]), has_amplitude=True,
        )

        self.assertEqual([s["name"] for s in series], ["Spend", "MAU", "New users"])

    def test_revenue_included_at_three_months(self):
        series = run.build_overlay_series(
            self._history([1.0, 2.0, 3.0]), has_amplitude=False,
        )

        self.assertEqual([s["name"] for s in series], ["Spend", "Revenue"])

    def test_revenue_omitted_below_three_months(self):
        series = run.build_overlay_series(
            self._history([None, 2.0, 3.0]), has_amplitude=False,
        )

        self.assertEqual([s["name"] for s in series], ["Spend"])
```

The last test encodes the rule from the spec: `build_overlay_chart` picks one
shared baseline as the max of each series' start index, so a short revenue series
would drag the baseline right and shrink the useful window for spend and MAU too.

- [ ] **Step 2: Run the tests to verify they fail**

```bash
cd scripts/gcp-spend && python3 -m unittest test_metrics -v
```

Expected: FAIL — `build_overlay_series` undefined, and the `pct` labels come back
without a `%`.

- [ ] **Step 3: Add the percentage format branch**

In `build_line_chart`, replace the gridline label block:

```python
        if fmt_y == "int":
            label = (f"{y_val/1000:,.0f}K" if y_val >= 1000 else f"{y_val:,.0f}")
        elif fmt_y == "pct":
            label = f"{y_val:,.0f}%"
        else:
            label = (f"${y_val/1000:,.1f}K" if y_val >= 1000 else f"${y_val:,.0f}")
```

Update the docstring's `fmt_y` note to `"money" | "int" | "pct"`.

- [ ] **Step 4: Add the overlay series builder**

Add near the other chart builders in `run.py`:

```python
# build_overlay_chart shares one baseline month across every series, taken as the
# latest point at which all of them have stabilised. A short revenue series would
# drag that baseline right and shrink the usable window for spend and MAU too, so
# revenue only joins once it has enough months to be worth that cost.
MIN_REVENUE_MONTHS_FOR_OVERLAY = 3


def build_overlay_series(h: AppHistory, has_amplitude: bool) -> list[dict]:
    """Series list for the indexed overlay, including only what has data."""
    series = [{"name": "Spend", "color": h.color, "values": h.by_month}]
    if has_amplitude:
        series.append({"name": "MAU",       "color": "#1e8449", "values": h.mau_by_month})
        series.append({"name": "New users", "color": "#b07aa1", "values": h.new_by_month})
    if sum(1 for v in h.revenue_by_month if v is not None) >= MIN_REVENUE_MONTHS_FOR_OVERLAY:
        series.append({"name": "Revenue",   "color": "#d97706", "values": h.revenue_by_month})
    return series
```

- [ ] **Step 5: Run the tests to verify they pass**

```bash
cd scripts/gcp-spend && python3 -m unittest test_revenuecat test_metrics -v
```

Expected: 37 tests, all PASS.

- [ ] **Step 6: Commit**

```bash
git add scripts/gcp-spend/run.py scripts/gcp-spend/test_metrics.py
git commit -m "feat(gcp-spend): add percentage axis format and overlay series selection"
```

---

### Task 7: Per-app page context and template

**Files:**
- Modify: `scripts/gcp-spend/run.py:911-1010` (`app_page_context`)
- Modify: `scripts/gcp-spend/app.html.j2:212-245` (KPI strip)
- Modify: `scripts/gcp-spend/app.html.j2:252-273` (charts section)
- Modify: `scripts/gcp-spend/app.html.j2:299-332` (table)
- Modify: `scripts/gcp-spend/app.html.j2:127` (`render_line_chart` macro, `fmt` cases)
- Modify: `scripts/gcp-spend/test_metrics.py`

**Interfaces:**
- Consumes: `cost_ratio`, `cost_ratio_delta_pp`, `build_overlay_series`, `MIN_REVENUE_MONTHS_FOR_OVERLAY` (Tasks 5 and 6)
- Produces: `app_page_context` keys `has_revenue`, `revenue`, `cost_ratio`, `cost_ratio_delta_pp`, `ratio_chart`, `show_overlay`, and per-row `revenue` + `cost_ratio` in `table_rows`

- [ ] **Step 1: Write the failing tests**

Append to `scripts/gcp-spend/test_metrics.py`, above the `if __name__` block:

```python
class AppPageContextTest(unittest.TestCase):
    MONTHS = ["202605", "202606", "202607"]

    def _history(self, revenue):
        return run.AppHistory(
            name="Chat Ultra", project_id="p", color="#000",
            by_month=[100.0, 200.0, 300.0],
            services_by_month={}, total_in_window=600.0,
            mau_by_month=[None, None, None],
            new_by_month=[None, None, None],
            revenue_by_month=revenue,
        )

    def _ctx(self, revenue):
        return run.app_page_context(
            h=self._history(revenue), months=self.MONTHS, pending=[],
            currency="EUR", target_month="202607",
        )

    def test_has_revenue_false_when_all_none(self):
        ctx = self._ctx([None, None, None])

        self.assertFalse(ctx["has_revenue"])
        self.assertIsNone(ctx["ratio_chart"])

    def test_cost_ratio_at_target_month(self):
        ctx = self._ctx([1000.0, 1000.0, 1000.0])

        self.assertAlmostEqual(ctx["cost_ratio"], 30.0)

    def test_cost_ratio_delta_is_percentage_points(self):
        ctx = self._ctx([1000.0, 1000.0, 1000.0])

        self.assertAlmostEqual(ctx["cost_ratio_delta_pp"], 10.0)

    def test_table_rows_carry_revenue_and_ratio(self):
        rows = self._ctx([1000.0, 1000.0, 1000.0])["table_rows"]

        self.assertEqual(rows[0]["revenue"], 1000.0)
        self.assertAlmostEqual(rows[0]["cost_ratio"], 10.0)

    def test_unsettled_target_month_yields_no_ratio(self):
        ctx = self._ctx([1000.0, 1000.0, None])

        self.assertIsNone(ctx["cost_ratio"])
        self.assertIsNone(ctx["cost_ratio_delta_pp"])

    def test_overlay_hidden_when_only_spend_has_data(self):
        self.assertFalse(self._ctx([None, None, None])["show_overlay"])

    def test_overlay_shown_when_revenue_qualifies(self):
        self.assertTrue(self._ctx([1000.0, 1000.0, 1000.0])["show_overlay"])
```

- [ ] **Step 2: Run the tests to verify they fail**

```bash
cd scripts/gcp-spend && python3 -m unittest test_metrics -v
```

Expected: FAIL with `KeyError: 'has_revenue'`

- [ ] **Step 3: Extend `app_page_context`**

In `app_page_context`, after the `has_amplitude` line:

```python
    has_revenue = any(v is not None for v in h.revenue_by_month)
    rev_cur  = h.revenue_by_month[cur_idx] if cur_idx < len(h.revenue_by_month) else None
    rev_prev = h.revenue_by_month[cur_idx - 1] if cur_idx > 0 else None
    ratio_cur  = cost_ratio(cur, rev_cur)
    ratio_prev = cost_ratio(prev, rev_prev) if prev is not None else None
    ratio_delta = cost_ratio_delta_pp(ratio_cur, ratio_prev)

    ratio_series = [cost_ratio(s, r) for s, r in zip(h.by_month, h.revenue_by_month)]
    ratio_chart = build_line_chart(
        ratio_series, months, target_month, fmt_y="pct", color="#d97706",
    ) if has_revenue else None
```

Replace the `overlay_chart` block with:

```python
    overlay_series = build_overlay_series(h, has_amplitude)
    show_overlay   = len(overlay_series) >= 2
    overlay_chart  = build_overlay_chart(
        series=overlay_series, months=months, target_month=target_month,
    ) if show_overlay else None
```

In the `table_rows` loop, add the revenue lookup next to the existing `mau` and
`new` lookups:

```python
        rev = h.revenue_by_month[i] if i < len(h.revenue_by_month) else None
```

and add two keys to the appended row dict:

```python
            "revenue":    rev,
            "cost_ratio": cost_ratio(spend_v, rev),
```

Add to the returned dict:

```python
        "has_revenue":         has_revenue,
        "revenue":             rev_cur,
        "cost_ratio":          ratio_cur,
        "cost_ratio_delta_pp": ratio_delta,
        "ratio_chart":         ratio_chart,
        "show_overlay":        show_overlay,
```

- [ ] **Step 4: Run the tests to verify they pass**

```bash
cd scripts/gcp-spend && python3 -m unittest test_revenuecat test_metrics -v
```

Expected: 44 tests, all PASS.

- [ ] **Step 5: Update `app.html.j2`**

Add a `pct` case to the `render_line_chart` macro's `fmt` handling, formatting
tooltip values as `{{ "%.1f"|format(d.value) }}%`.

Add a KPI tile after the `$/MAU` tile, outside the `has_amplitude` block:

```jinja
{% if has_revenue %}
<div class="kpi">
  <span class="label">Cost / revenue</span>
  <span class="val small">{% if cost_ratio is not none %}{{ "%.1f"|format(cost_ratio) }}%{% else %}—{% endif %}</span>
  {% if cost_ratio_delta_pp is not none %}
    {% if cost_ratio_delta_pp > 0.5 %}<span class="mom up">▲ {{ "%.1f"|format(cost_ratio_delta_pp) }}pp</span>
    {% elif cost_ratio_delta_pp < -0.5 %}<span class="mom down">▼ {{ "%.1f"|format(-cost_ratio_delta_pp) }}pp</span>
    {% else %}<span class="mom flat">— flat</span>{% endif %}
  {% endif %}
</div>
{% endif %}
```

Move the overlay section out of the `has_amplitude` block and gate it on
`show_overlay`, with the heading `Trend overlap · indexed to 100`.

Add the ratio chart section, gated on `has_revenue`:

```jinja
<h2 class="section">Infra cost as % of net proceeds</h2>
{{ render_line_chart(ratio_chart, fmt="pct") }}
<p class="caveat">GCP infrastructure only. Excludes user acquisition, salaries,
non-GCP AI vendors, and RevenueCat fees — this is not margin.</p>
```

Add a `.caveat` rule to the stylesheet matching the existing `.no-data` muted
treatment.

When `has_revenue` is false, render the existing `no-data` pattern pointing at
`revenuecat.conf` and the required env var:

```jinja
{% else %}
<h2 class="section">Revenue</h2>
<div class="no-data">No RevenueCat data configured for this app. Add a row to <code>revenuecat.conf</code> + env vars to enable revenue and cost-ratio charts.</div>
{% endif %}
```

Add two table columns gated on `has_revenue`. In `<thead>`, after the `$/MAU`
block:

```jinja
{% if has_revenue %}
<th>Revenue</th>
<th>Cost %</th>
{% endif %}
```

and the matching cells in `<tbody>`, after the Amplitude block:

```jinja
{% if has_revenue %}
  {% if r.revenue is not none %}
    <td>€{{ "{:,.0f}".format(r.revenue) }}</td>
    <td>{% if r.cost_ratio is not none %}{{ "%.1f"|format(r.cost_ratio) }}%{% else %}—{% endif %}</td>
  {% else %}
    <td class="empty">—</td><td class="empty">—</td>
  {% endif %}
{% endif %}
```

- [ ] **Step 6: Render and eyeball**

```bash
cd scripts/gcp-spend && python3 run.py --month 2026-07 && open reports/apps/chat-ultra.html
```

Check: KPI tile present with a plausible percentage; ratio chart axis reads
`0%`–`N%`; the caveat line is visible; table columns line up; an app with no
RevenueCat config renders its no-data message rather than breaking.

- [ ] **Step 7: Commit**

```bash
git add scripts/gcp-spend/run.py scripts/gcp-spend/app.html.j2 scripts/gcp-spend/test_metrics.py
git commit -m "feat(gcp-spend): show cost-to-revenue ratio on the per-app page"
```

---

### Task 8: Dashboard card

**Files:**
- Modify: `scripts/gcp-spend/run.py:812-908` (`dashboard_context`)
- Modify: `scripts/gcp-spend/dashboard.html.j2:101-110` (styles)
- Modify: `scripts/gcp-spend/dashboard.html.j2:262-275` (card rows)
- Modify: `scripts/gcp-spend/test_metrics.py`

**Interfaces:**
- Consumes: `cost_ratio`, `cost_ratio_delta_pp` (Task 5)
- Produces: `cost_ratio` and `cost_ratio_delta_pp` on each entry of `dashboard_context`'s `apps` list

- [ ] **Step 1: Write the failing tests**

Append to `scripts/gcp-spend/test_metrics.py`, above the `if __name__` block:

```python
class DashboardContextTest(unittest.TestCase):
    MONTHS = ["202605", "202606", "202607"]

    def _history(self, revenue):
        return run.AppHistory(
            name="Chat Ultra", project_id="p", color="#000",
            by_month=[100.0, 200.0, 300.0],
            services_by_month={}, total_in_window=600.0,
            mau_by_month=[None, None, None],
            new_by_month=[None, None, None],
            revenue_by_month=revenue,
        )

    def _apps(self, revenue):
        ctx = run.dashboard_context(
            histories=[self._history(revenue)],
            monthly_totals=[{"month": m, "total": 1.0} for m in self.MONTHS],
            months=self.MONTHS, pending=[], currency="EUR", target_month="202607",
        )
        return ctx["apps"]

    def test_card_carries_cost_ratio_and_delta(self):
        app = self._apps([1000.0, 1000.0, 1000.0])[0]

        self.assertAlmostEqual(app["cost_ratio"], 30.0)
        self.assertAlmostEqual(app["cost_ratio_delta_pp"], 10.0)

    def test_card_ratio_is_none_without_revenue(self):
        app = self._apps([None, None, None])[0]

        self.assertIsNone(app["cost_ratio"])
        self.assertIsNone(app["cost_ratio_delta_pp"])
```

- [ ] **Step 2: Run the tests to verify they fail**

```bash
cd scripts/gcp-spend && python3 -m unittest test_metrics -v
```

Expected: FAIL with `KeyError: 'cost_ratio'`

- [ ] **Step 3: Extend `dashboard_context`**

Inside the per-app loop, alongside the existing `cost_per_mau` computation:

```python
        rev_cur  = h.revenue_by_month[cur_idx] if cur_idx < len(h.revenue_by_month) else None
        rev_prev = h.revenue_by_month[cur_idx - 1] if cur_idx > 0 else None
        ratio_cur = cost_ratio(cur, rev_cur)
        ratio_delta = cost_ratio_delta_pp(
            ratio_cur, cost_ratio(prev, rev_prev) if prev is not None else None,
        )
```

and add to the appended dict:

```python
            "cost_ratio":          ratio_cur,
            "cost_ratio_delta_pp": ratio_delta,
```

- [ ] **Step 4: Run the tests to verify they pass**

```bash
cd scripts/gcp-spend && python3 -m unittest test_revenuecat test_metrics -v
```

Expected: 46 tests, all PASS.

- [ ] **Step 5: Update `dashboard.html.j2`**

Add a `.row-rev` style block mirroring `.row-mau` (same font size, muted label,
tabular numerals, accent colour for the ratio).

Add below the `.row-mau` block inside the card:

```jinja
{% if app.cost_ratio is not none %}
<div class="row-rev">
  <span><span class="label">cost / rev</span> <span class="val">{{ "%.1f"|format(app.cost_ratio) }}%</span></span>
  {% if app.cost_ratio_delta_pp is not none %}
    {% if app.cost_ratio_delta_pp > 0.5 %}<span class="mom up">▲ {{ "%.1f"|format(app.cost_ratio_delta_pp) }}pp</span>
    {% elif app.cost_ratio_delta_pp < -0.5 %}<span class="mom down">▼ {{ "%.1f"|format(-app.cost_ratio_delta_pp) }}pp</span>
    {% endif %}
  {% endif %}
</div>
{% endif %}
```

- [ ] **Step 6: Render and eyeball**

```bash
cd scripts/gcp-spend && python3 run.py --month 2026-07 && open reports/index.html
```

Check: cards with revenue show the ratio line; cards without are visually
unchanged; the grid does not reflow awkwardly with a mix of both.

- [ ] **Step 7: Commit**

```bash
git add scripts/gcp-spend/run.py scripts/gcp-spend/dashboard.html.j2 scripts/gcp-spend/test_metrics.py
git commit -m "feat(gcp-spend): show cost-to-revenue ratio on dashboard cards"
```

---

### Task 9: End-to-end verification and documentation

**Files:**
- Modify: `scripts/gcp-spend/README.md`
- Modify: `scripts/gcp-spend/SETUP-HEADLESS.md`

**Interfaces:**
- Consumes: everything above
- Produces: nothing consumed by later tasks

- [ ] **Step 1: Full run against real credentials**

```bash
cd scripts/gcp-spend && python3 run.py --month 2026-07 --history-months 12
```

Expected: completes without error; RevenueCat lines appear in stdout for
configured apps; unconfigured apps produce no RevenueCat output at all.

- [ ] **Step 2: Reconcile one app against the RevenueCat dashboard**

Pick the app with the largest revenue. Open its page in `reports/apps/`. Compare
every month in the `Revenue` column against the RevenueCat dashboard for the same
project, same currency, same net-proceeds selector.

All settled months must match. If they are off by a constant factor of 100, the
`VALUE_SCALE` constant from Task 3 is wrong — fix it and re-run.

- [ ] **Step 3: Confirm the unsettled month is dropped**

The current calendar month should show `—` in the `Revenue` column and no cost
ratio, rather than a small number. If it shows a value, the incomplete check from
Task 3 is not matching the real field name — go back and fix it against the Task 1
findings.

This is the single most important check in the plan: an unsettled month plotted
as real would fire a false efficiency alarm every month.

- [ ] **Step 4: Confirm graceful degradation**

Temporarily rename the config and re-run:

```bash
cd scripts/gcp-spend && mv revenuecat.conf revenuecat.conf.bak && \
python3 run.py --month 2026-07 && mv revenuecat.conf.bak revenuecat.conf
```

Expected: the run succeeds, and every page renders as it did before this feature.

- [ ] **Step 5: Document the new source**

Add a RevenueCat section to `scripts/gcp-spend/README.md` covering: what the
metric is and explicitly what it is not (not margin), the `revenuecat.conf`
format, the env var naming convention, the Pro-plan requirement, and the
throttling behaviour with its effect on run time.

Add the `REVENUECAT_*` env vars to `SETUP-HEADLESS.md` alongside the existing
Amplitude and GCP credential documentation.

- [ ] **Step 6: Commit**

```bash
git add scripts/gcp-spend/README.md scripts/gcp-spend/SETUP-HEADLESS.md
git commit -m "docs(gcp-spend): document the RevenueCat revenue source"
```

---

## Deferred (explicitly not in this plan)

Adding `revenue_eur` to `write_export_json` and deleting
`scripts/ma-heartbeat/sources/revenuecat.py` so the heartbeat reads revenue from
the gcp-spend export, as it already reads `cost_eur` and `mau`. This restores the
single-source-of-truth principle stated in the heartbeat README, which the
present change weakens by creating a second RevenueCat consumer. It needs its own
validation against the heartbeat's history CSV and belongs in its own plan.
