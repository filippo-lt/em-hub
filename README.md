# EM Hub

An AI-powered operating system for Engineering Managers. Built for Cursor IDE.

---

## How It Works

The hub has **agents** (reusable behaviours) and **workflows** (composed sequences).

```
You
 │
 ├─► CLAUDE.md (orchestrator) → routes to the right workflow
 │       │
 │       ├─► workflows/1on1.md              → prep → analysis → memory
 │       ├─► workflows/status-update.md     → gather → draft
 │       ├─► workflows/hiring.md            → scorecard → interview → debrief → decide
 │       ├─► workflows/performance-cycle.md → review → calibrate → deliver → memory
 │       ├─► workflows/incident-response.md → timeline → postmortem → comms
 │       └─► workflows/planning.md          → reflect → draft goals → pressure test
 │
 └─► agents/  (reusable across workflows)
         ├── prep-agent.md
         ├── analysis-agent.md
         ├── memory-agent.md
         ├── writing-agent.md
         ├── decision-agent.md
         └── review-agent.md
```

---

## Folder Structure

```
em-hub/
├── CLAUDE.md              ← master orchestrator (read by Cursor/.cursorrules)
├── .cursorrules            ← Cursor IDE entry point
│
├── agents/                 ← reusable agent behaviours
├── workflows/              ← composed sequences of agents
├── templates/              ← document templates
│
├── people/                 ← per-person context
│   └── [name]/
│       ├── profile.md
│       ├── transcripts/
│       ├── talking-points/
│       ├── memory/
│       └── context/
│
├── teams/                  ← team-level context
│   └── [team]/
│       ├── roster.md
│       ├── okrs.md
│       └── context/
│
└── context/                ← global context
    ├── org-chart.md
    ├── company-priorities.md
    ├── my-goals.md
    ├── decisions/
    ├── hiring/
    ├── incidents/
    └── planning/
```

---

## Quick Start

1. Open this folder in Cursor
2. Start chatting. Examples:
   - `"Prep me for my 1-on-1 with David"`
   - `"Help me write a status update"`
   - `"I need to hire a senior iOS developer"`
   - `"Draft a performance review for Andrey"`
3. Fill in the `[fill in]` placeholders in `people/`, `teams/`, and `context/` as you go

---

## Adding a New Person

```bash
mkdir -p people/firstname-role/{transcripts,talking-points,memory,context}
cp templates/context-profile.md people/firstname-role/profile.md
# Edit the profile
```

---

## Adding a New Workflow

1. Create `workflows/your-workflow.md` — define the phases and which agents it uses
2. Add a routing rule in `CLAUDE.md` under the workflow routing table
3. Create any new templates in `templates/` if needed
