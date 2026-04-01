# AGENTS.md — EM Hub

Guidelines for agentic coding agents operating in this repository.

---

## Project Overview

EM Hub is a personal operating system for an Engineering Manager. It contains:
- Interactive skills (`.claude/skills/`) — invoked via `/command`
- Autonomous agents (`.claude/agents/`) — run as subprocesses
- Delivery scripts (`scripts/`) — generate reports from Jira/GitHub
- Templates (`templates/`) — reusable document structures
- Context files (`people/`, `teams/`, `context/`) — structured knowledge

This is **not** a traditional software project. Most content is markdown. Code (bash, Python) exists only in automation scripts.

---

## Available Commands

### Delivery Scripts

```bash
# Sprint metrics for a month
scripts/jira-sprint-metrics --month 2026-01 --users "Jane Smith,John Doe"

# Sprint metrics via config file
scripts/jira-sprint-metrics --config config/sprint-metrics.conf

# Roadmap status (auto-runs roadmap-status)
scripts/delivery/roadmap-report

# Weekly dev progress report
scripts/delivery/dev-progress-weekly-report

# Debug: list Jira statuses for a project
scripts/jira-sprint-metrics-debug
```

### Skills (Interactive)

Use these when the user asks for specific tasks:

| Task | Command |
|------|---------|
| Prep for meeting | `/prep` |
| Analyse transcript | `/analyse` |
| Write document | `/write` |
| Decide between options | `/decide` |
| Brainstorm | `/brainstorm` |
| Write review | `/review` |
| Hiring tasks | `/hiring` |
| Incident response | `/incident` |
| Planning | `/planning` |

### Agents (Autonomous)

| Task | Trigger |
|------|---------|
| Memory extraction | "Extract memory from this" |
| Contractor performance | "Contractor metrics" |

---

## Code Style Guidelines

### Bash Scripts

- Use `set -euo pipefail` at the top of all scripts
- Use `#!/bin/bash` shebang (not `sh`)
- Use functions for logical grouping; prefix with `_` for internal functions
- Use lower_snake_case for variables and functions
- Use `${var}` for variable expansion (not `$var`)
- Quote all variable expansions: `"$VAR"` not `$VAR`
- Use `local` for function-scoped variables
- Use `readonly` for constants
- Add usage comments at the top (see `scripts/jira-sprint-metrics` for example)
- Support `--help`, `-h` for usage information
- Use `getopt` or manual `case` parsing for arguments

Example:
```bash
#!/bin/bash
set -euo pipefail

readonly DEFAULT_CONFIG="$HOME/.config/em-hub.conf"

load_config() {
    local file="$1"
    if [[ ! -f "$file" ]]; then
        echo "Error: Config file not found: $file" >&2
        exit 1
    fi
    # ... load logic
}

main() {
    local config="${1:-}"
    if [[ -z "$config" ]]; then
        config="$DEFAULT_CONFIG"
    fi
    load_config "$config"
}

main "$@"
```

### Python (Embedded in Scripts)

- Use Python 3 syntax
- Use `subprocess.run()` for API calls
- Use `json` for parsing responses
- Use f-strings for string formatting
- Keep embedded Python minimal (prefer bash for orchestration)

### Markdown Files

- Use ATX-style headers (`#`, `##`, `###`)
- Use `-` for unordered lists
- Use `1.` for ordered lists
- Use fenced code blocks with language identifier
- Use `YYYY-MM-DD` for date-based filenames
- Use lowercase-kebab-case for file and directory names

---

## External System Access

### Jira API

Credentials are in `~/.config/jira/.env`:
- `JIRA_EMAIL`
- `JIRA_API_TOKEN`
- `JIRA_BASE_URL` (e.g., `https://yourcompany.atlassian.net`)

Call API via:
```bash
source ~/.config/jira/.env
curl -s -u "$JIRA_EMAIL:$JIRA_API_TOKEN" \
  -H "Content-Type: application/json" \
  "$JIRA_BASE_URL/rest/api/3/..."
```

For JQL searches, POST to `/rest/api/3/search/jql`.

### Write Operations — REQUIRES CONFIRMATION

Never execute write operations (PUT, POST, DELETE, PATCH) against external systems without explicit user confirmation.

Before executing:
1. Describe exactly what will change (field, value, issue key, endpoint)
2. Show before/after if applicable
3. Wait for user confirmation

**Does NOT require confirmation:**
- Read-only operations (GET, search queries)
- Local file edits in this repo

---

## Cursor Rules

The following rules are automatically loaded from `.cursor/rules/`:

1. **jira-access.mdc** — Jira API access is available; credentials in `~/.config/jira/.env`
2. **external-writes.mdc** — Require confirmation before write operations

---

## Context Loading

When working with people or teams, load context in this order:

1. Person: `people/[name]/profile.md`, transcripts, talking-points, memory
2. Team: `teams/[team]/roster.md`, `teams/[team]/okrs.md`
3. Global: `context/org-chart.md`, `context/company-priorities.md`, `context/my-goals.md`
4. Domain: `context/memory/[domain]/`, `context/decisions/`

Date-based files use `YYYY-MM-DD` format. "Most recent" = sort by date descending.

---

## Behavioral Standards

- Be concise and direct
- Ask ONE question at a time
- Load context silently before engaging
- Never fabricate content — only reference what you've read
- If a file or folder doesn't exist, tell the user and offer to create it
- When generating documents, offer to save them to the right location
