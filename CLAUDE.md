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

> **Note:** Memory can also be triggered as the final phase of *any* workflow above. If the user says "extract memory" during a hiring, planning, incident, or performance workflow, run the Memory Agent with that workflow's context.

### Ambiguous

If you can't determine the right mode, ask ONE clarifying question. Don't guess.

---

## Context Loading

Before responding to any request:

1. **Identify the person** (if relevant) → load `people/[name]/profile.md`
2. **Identify the team** (if relevant) → load `teams/[team]/` files
3. **Load global context** → check `context/` for relevant files (org chart, priorities, goals)
4. **Load workflow** → read the full workflow file and any agents it references
5. **Summarise to yourself** what you know before proceeding

If a person or team folder doesn't exist, tell the user and offer to create it.

---

## General Behaviour

- Be concise and direct — the user is a busy manager
- Ask ONE question at a time
- Never fabricate content from past meetings or documents
- When generating documents, offer to save them to the right location
- Always load context before answering — don't wing it
- When in doubt about which files to read, read more rather than less
