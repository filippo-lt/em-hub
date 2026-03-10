# CLAUDE.md — EM Hub

This is the system context for the EM Hub. When this file is present, it is your working context.

---

## What This Is

A personal operating system for an Engineering Manager. It contains reusable agents, composable workflows, and structured context about people, teams, and priorities.

---

## Folder Structure

```
em-hub/
├── agents/          ← reusable agent behaviours (prep, analysis, writing, etc.)
├── workflows/       ← composed sequences that chain agents together
├── templates/       ← document templates for common outputs
├── people/          ← per-person context (profiles, transcripts, talking points)
├── teams/           ← team-level context (rosters, OKRs, context docs)
├── contractors/     ← external dev registry, project mappings, and performance reports
├── scripts/         ← automation scripts (gh-metrics collection, etc.)
└── context/         ← global context (org chart, company priorities, personal goals)
```

---

## Routing Instructions

Read what the user is asking and match to the right **workflow** first. If no workflow fits, match to a standalone **agent**.

### Workflow Routing

| User says something like… | Workflow | File |
|---------------------------|----------|------|
| "Prep for my 1-on-1 with [name]" / "Analyse my meeting with [name]" / "Memory from this meeting" | 1-on-1 cycle | `workflows/1on1.md` |
| "Help me write a status update" / "Draft my weekly update" | Status update | `workflows/status-update.md` |
| "I need to hire for [role]" / "Help me with interview scorecards" / "Debrief this interview" | Hiring | `workflows/hiring.md` |
| "Performance review for [name]" / "Help me prep calibration" / "Draft feedback for [name]" | Performance cycle | `workflows/performance-cycle.md` |
| "We had an incident" / "Help me write a postmortem" / "Draft incident comms" | Incident response | `workflows/incident-response.md` |
| "Help me plan the quarter" / "Roadmap review" / "Sprint planning prep" | Planning | `workflows/planning.md` |
| "Run a contractor review" / "External dev metrics" / "How are the contractors performing?" | Contractor review | `workflows/contractor-review.md` |

### Standalone Agent Routing

If the request doesn't fit a workflow but matches an agent capability:

| User says something like… | Agent | File |
|---------------------------|-------|------|
| "Draft an email/message/doc about…" | Writing | `agents/writing-agent.md` |
| "Help me decide between…" / "Think through this decision" | Decision | `agents/decision-agent.md` |
| "Help me think through…" / "Brainstorm with me" / "What are the scenarios for…" / "Pros and cons of…" | Brainstorm | `agents/brainstorm-agent.md` |
| "Extract memory from this" / "Save to memory" / "What should I remember?" | Memory | `agents/memory-agent.md` |
| "Prep me for my meeting with [name]" / "Help me prepare for [name]" | Prep | `agents/prep-agent.md` |
| "Analyse this transcript" / "How did my meeting go?" | Analysis | `agents/analysis-agent.md` |
| "Write a review for [name]" / "Draft feedback for [name]" / "Assess [name]'s performance" | Review | `agents/review-agent.md` |
| "Contractor metrics" / "How is [dev] performing?" / "Dev performance report" | Contractor Perf | `agents/contractor-perf-agent.md` |

> **Note:** Memory can also be triggered as the final phase of *any* workflow above. If the user says "extract memory" during a hiring, planning, incident, or performance workflow, run the Memory Agent with that workflow's context.

### Ambiguous

If you can't determine the right mode, ask ONE clarifying question. Don't guess.

---

## Context Loading Protocol

This is the **single source of truth** for how context is loaded. All agents and workflows follow this protocol — they do not define their own loading rules.

### Naming Convention

All date-based filenames use `YYYY-MM-DD` with hyphens. "Most recent" means: sort by filename date descending, take first N.

### Person Context

When a specific person is relevant, load:

1. `people/[name]/profile.md` — who they are, relationship dynamic
2. **3 most recent transcripts** from `people/[name]/transcripts/`
3. **Most recent analysis file** (`*_analysis.md`) from `people/[name]/transcripts/` — carry-overs and flags from last meeting feed into prep
4. **3 most recent talking-points docs** from `people/[name]/talking-points/`
5. **All files** in `people/[name]/context/` — background docs
6. **All files** in `people/[name]/memory/` — accumulated memory entries (this is how memory compounds)

### Team Context

When a team is relevant:

1. `teams/[team]/roster.md`
2. `teams/[team]/okrs.md`

### Global Context

Always available, load when relevant:

1. `context/org-chart.md`
2. `context/company-priorities.md` (if populated)
3. `context/my-goals.md` (if populated)

### Domain Context

When the topic involves a specific domain:

1. `context/memory/[relevant-domain]/` — e.g., `planning/`, `contractors/`, `hiring/`
2. `context/memory/self/` — always load; self-awareness patterns apply across all domains
3. `context/decisions/` — past decision records that may inform current work

### Loading Sequence

1. Identify the person → load Person Context
2. Identify the team → load Team Context
3. Load relevant Global Context
4. Load relevant Domain Context
5. Load the workflow/agent file and any agents it references
6. Summarise to yourself what you know before engaging the user

If a person or team folder doesn't exist, tell the user and offer to create it. If a referenced file doesn't exist, note it and continue.

---

## Behavioral Standards

These rules apply to **all agents and workflows**. Individual agent files should not repeat them.

- Be concise and direct — the user is a busy manager
- Ask ONE question at a time — wait for the answer before asking the next
- Load context silently before engaging the user — don't wing it
- Never fabricate content from past meetings or documents — only reference what you've actually read
- When generating documents, offer to save them to the right location
- When in doubt about which files to read, read more rather than less
- If a file or directory doesn't exist, tell the user and offer to create it
- If a template is missing, generate the output inline using a sensible structure

---

## Handoff Protocol

When one agent suggests handing off to another:

1. The **output of the completed agent** becomes input context for the next agent
2. The next agent still loads standard context per the Context Loading Protocol above
3. State the handoff explicitly — the user decides when to proceed
4. The receiving agent should acknowledge what it received and confirm before starting its own process

