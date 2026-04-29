---
name: metrics
description: "Run developer delivery metrics from Jira and/or GitHub for a given month. Use when the user says things like: 'get developer metrics', 'run dev metrics', 'pull metrics for [month]', 'jira/github metrics', 'sprint metrics', 'delivery metrics', 'monthly metrics', 'story points delivered', 'QA bouncebacks', 'QA rejections', 'No QA pass', 'items delivered', 'tickets completed', or any question about a developer's delivery output over a time period."
user_invocable: true
---

# Metrics

You run the developer delivery metrics scripts located at `/Users/ftosetto/Projects/metrics` and present the results back to the user.

By default, run **both Jira and GitHub** metrics. Only run a single source if the user explicitly asks for it (e.g. "just Jira", "GitHub only").

---

## Process

### Phase 1 — Determine the month

Ask the user **one** question:

> "Which month should I pull metrics for? (format: `YYYY-MM`, e.g. `2026-03`. Press enter to use the previous month.)"

- If the user provides `YYYY-MM`, use it.
- If the user says "previous month", "last month", or presses enter, omit `MONTH=` and let the Makefile default kick in (previous month).
- If the user gives a relative reference ("March", "this month"), convert it to `YYYY-MM` using today's date from the system context. Confirm the resolved value before running.

Also confirm scope if ambiguous:
- Default: both Jira and GitHub
- "Just Jira" / "Jira only" → run Jira target only
- "Just GitHub" / "GitHub only" → run GitHub target only

### Phase 2 — Run the scripts

Working directory: `/Users/ftosetto/Projects/metrics`

| Scope  | Specific month                                  | Previous month (default) |
| ------ | ----------------------------------------------- | ------------------------ |
| Jira   | `make dev-metrics-month MONTH=YYYY-MM`          | `make dev-metrics`       |
| GitHub | `make github-metrics-month MONTH=YYYY-MM`       | `make github-metrics`    |

Run them sequentially (Jira first, then GitHub) so the output is grouped clearly. Use the Bash tool with `cd /Users/ftosetto/Projects/metrics && <command>`.

If a command fails:
- Credential errors (`~/.config/jira/.env` or `~/.config/github/.env` missing) → tell the user which env file is missing and stop.
- Other errors → surface the error verbatim and ask the user how to proceed. Do not retry blindly.

### Phase 3 — Present results

Show the raw tables from each script's output. Then add a short summary (3–6 bullets) covering:
- Top contributors by score (GitHub) and delivered story points (Jira)
- Anyone with notably low or zero activity
- NO QA / bounceback flags from Jira if present
- Any vendor-import warnings from GitHub

Keep it terse — the user will dig into details themselves.

### Phase 4 — Offer follow-ups

Offer (don't auto-run):
- Save the combined output to `metrics/metrics-YYYY-MM.md` in em-hub (repo root)
- Run `/analyse` style follow-up for a specific developer
- Hand off to the **Contractor Perf** agent for deeper review of a contractor

---

## Notes

- These scripts are **read-only** against Jira and GitHub APIs — no confirmation needed before running.
- Config files live at `/Users/ftosetto/Projects/metrics/config/` (`dev-metrics.conf`, `github-dev-metrics.conf`). If the user asks to add/remove a developer, edit those configs directly and confirm before saving.
- The Jira target uses `--delivered-status "PO REVIEW"` and `--noqa-status "No Pass, No QA Pass"`. Don't override unless the user asks.

---

## Alternative: in-repo Jira sprint script

em-hub also ships a self-contained Jira sprint metrics script (independent of the `/Users/ftosetto/Projects/metrics` project). Use this only if the user explicitly asks for it or the main scripts above are unavailable.

**Location:** `scripts/jira-sprint-metrics` (em-hub workspace)
**Config:** `config/sprint-metrics.conf` — populates `MONTH`, `USERS`, status names, etc.
**Debug helper:** `scripts/jira-sprint-metrics-debug` — lists Jira statuses and field IDs.

Usage:

```bash
# From config (preferred)
scripts/jira-sprint-metrics

# With explicit flags
scripts/jira-sprint-metrics --month YYYY-MM --users "Name1,Name2"
scripts/jira-sprint-metrics --json    # raw JSON output
```

Optional flags: `--config FILE`, `--delivered-status NAME`, `--qa-from-status NAME`, `--qa-to-status NAMES`, `--sp-field FIELD_ID`, `--issue-types "T1,T2"`.

Requires `~/.config/jira/.env` with `JIRA_BASE_URL`, `JIRA_EMAIL`, `JIRA_API_TOKEN`.

What it measures: items delivered (status transitions to delivered status), story points delivered (sum of SP field), QA bouncebacks (transitions from QA review back to in-progress, counted via the changelog API).
