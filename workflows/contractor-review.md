# Workflow: Contractor Review

Generate periodic performance reports for external developers based on their GitHub and Jira activity.

---

## Routing

Activate when the user says:
- "Run a contractor review"
- "Weekly/monthly report for external devs"
- "How are the contractors performing?"
- "Performance report for [vendor/project/developer]"
- "Review [name]'s output this month"
- "External dev metrics for [timeframe]"

---

## Agents Used

1. **Contractor Performance Agent** (`agents/contractor-perf-agent.md`) — collects metrics, analyses, generates report
2. **Memory Agent** (`agents/memory-agent.md`) — optionally captures insights or patterns from the review

---

## Data Sources

- `contractors/registry.md` — developer list, skills, project assignments, usernames
- `contractors/projects.md` — project → GitHub repos → Jira boards mapping
- GitHub API via `gh` CLI — commits, PRs, reviews
- Jira API or user-provided export — story points, tickets, no-QA iterations

---

## Typical Flow

```
1. User: "Run the monthly contractor review"
   → Ask for timeframe if not provided (e.g., "February 2026")
   → Confirm scope: all devs, a specific project, or a specific developer

2. Load registry and project mappings
   → Identify which developers and repos/boards are in scope

3. Collect GitHub metrics
   → Run: scripts/gh-metrics.sh --start X --end Y [--dev/--project filters]
   → Or read existing JSON if already collected: contractors/reports/{start}_to_{end}_gh-metrics.json
   → Metrics: commits, PRs merged, PR reviews, avg PR size, avg time to merge

4. Collect Jira metrics
   → For each dev × each board: story points, stories + bugs resolved, no-QA iterations
   → If Jira API unavailable, ask user for export data

5. Analyse and flag anomalies
   → Zero-activity devs, high no-QA rates, PR size outliers, Jira/GitHub mismatches

6. Generate report
   → Default: interactive HTML saved to contractors/reports/
   → Alternative: Markdown if requested

7. Present report and offer to:
   → Dig into a specific developer's numbers
   → Compare across timeframes (if previous reports exist)
   → Extract memory for patterns worth tracking
```

---

## Scope Resolution

| User says | Scope |
|-----------|-------|
| "Run the contractor review" | All active devs, all projects |
| "Review for Tattooist" | All devs assigned to Tattooist project |
| "How is [name] doing?" | Single developer, all their projects |
| "Anadea review" | All devs from Anadea vendor |

---

## Context Loading

1. `contractors/registry.md` — **always**
2. `contractors/projects.md` — **always**
3. Previous reports in `contractors/reports/` — if comparing to prior periods
4. `teams/mobile-app-unit/roster.md` — for vendor relationship context

---

## File Outputs

| Output | Location |
|--------|----------|
| HTML report | `contractors/reports/YYYY-MM-DD_to_YYYY-MM-DD_report.html` |
| Markdown report (if requested) | `contractors/reports/YYYY-MM-DD_to_YYYY-MM-DD_report.md` |
| Memory (if extracted) | `context/memory/YYYY-MM-DD_memory.md` |
