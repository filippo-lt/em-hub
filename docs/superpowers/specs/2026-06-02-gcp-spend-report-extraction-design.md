# GCP Spend Report — Extraction & em-hub Skill

**Date:** 2026-06-02
**Status:** Design approved, ready for implementation plan

## Goal

Split the GCP spend tooling out of em-hub into its own project so it can be developed and run standalone, while keeping an em-hub skill (`/gcp-spend`) that drives it and uses the resulting report as EM context.

## Current state

- Tool lives at `em-hub/scripts/gcp-spend/` — Python project with `run.py`, Jinja templates (`app.html.j2`, `dashboard.html.j2`, `query.sql.j2`, `template.html.j2`), configs (`config.conf`, `amplitude.conf`), `requirements.txt`, `README.md`, and a `reports/` directory.
- Rendered HTML is published into `em-hub/metrics/gcp-spend/` (e.g. `2026-04.html`, `index.html`) and loaded as EM context.

## New layout

### `~/Projects/gcp-spend-report/` (new repo)

Owns the tool. Contains everything currently in `em-hub/scripts/gcp-spend/`. Runs standalone via `python run.py`. Canonical reports stay in its own `reports/` directory. After a successful run, a publish step copies the rendered HTML into `~/Projects/em-hub/metrics/gcp-spend/`.

- Sibling-path coupling: the publish step targets `../em-hub/metrics/gcp-spend/` (or the equivalent absolute path `~/Projects/em-hub/metrics/gcp-spend/`).
- If em-hub isn't present at that path, publish logs a warning and exits 0 — the run itself still succeeds.
- Publish is invoked either as `make publish` or via a `--publish` flag on `run.py` (decided in implementation).

### em-hub

- `em-hub/scripts/gcp-spend/` deleted in the same commit as the move.
- `em-hub/metrics/gcp-spend/` retained as the synced artifact destination.
- New skill `.agents/skills/gcp-spend/SKILL.md` with a symlink from `.claude/skills/gcp-spend/` (matching existing skill convention).
- Routing line added to `CLAUDE.md` under the Skill Routing table.

## Skill behaviour (`/gcp-spend`)

1. **Freshness check.** Scan `em-hub/metrics/gcp-spend/` for the newest report matching `YYYY-MM.html`. If a file for the current calendar month is present, the report is fresh. Otherwise it is stale.
2. **Refresh if stale (or `--refresh`).** Shell out to `~/Projects/gcp-spend-report/` and run the standard pipeline (`python run.py --publish` or equivalent). Wait for completion. If the external project is missing or the run fails, tell the user explicitly — do not fall back silently.
3. **Load and analyse.** Read the freshest report (post-refresh if applicable) and open the analysis conversation: cost per app, $/MAU with the GCP-only caveat from `reference_app_ai_cost_attribution.md`, attribution to AI Design / Tattooist / Chatbot, anomalies vs prior month.

The skill never assumes the external project exists silently. If it can't find `~/Projects/gcp-spend-report/`, it surfaces this and offers to skip the refresh and analyse whatever is in em-hub.

## Move mechanics

Single sequence, ideally one commit on each side:

1. Create `~/Projects/gcp-spend-report/`.
2. `git mv` the contents of `em-hub/scripts/gcp-spend/*` into the new project, preserving history if practical (otherwise copy + delete; this is acceptable for a personal tool).
3. `git init` in the new project; first commit captures the moved state.
4. In em-hub: delete `scripts/gcp-spend/` and remove any references; add the new skill files and CLAUDE.md routing line in the same commit.
5. Verify a standalone run in the new project still produces a report and that publish lands it in `em-hub/metrics/gcp-spend/`.

## Out of scope (YAGNI)

- No environment variable or em-hub config file for the tool path — hardcoded sibling (`~/Projects/gcp-spend-report/`) is fine for a one-machine personal setup.
- No backward-compatibility stub at `em-hub/scripts/gcp-spend/` — clean break.
- No scheduling, cron, or automated refresh — `/gcp-spend` is invoked on demand.
- No changes to the tool's internal behaviour (queries, templates, output format) — this is a move, not a rewrite.

## Open items for the implementation plan

- Exact mechanism for the publish step (`make publish` vs `run.py --publish` flag).
- Whether to preserve git history via `git filter-repo` or accept a fresh start in the new repo.
- Whether the skill's "refresh" call uses `python run.py --publish` directly or a wrapper script.
