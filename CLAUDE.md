# CLAUDE.md — EM Hub

This is the system context for the EM Hub. When this file is present, it is your working context.

---

## What This Is

A personal operating system for an Engineering Manager. It contains reusable skills, autonomous agents, and structured context about people, teams, and priorities.

---

## Folder Structure

```
em-hub/
├── .agents/         ← canonical store for skills, subagents, and rules (see .agents/README.md)
│   ├── skills/      ← interactive skills invoked via /command (prep, analyse, write, etc.)
│   ├── agents/      ← autonomous agents that run as subprocesses (memory, contractor-perf)
│   └── rules/       ← .mdc rules (em-persona, external-writes, jira-access, brag-doc)
├── .claude/         ← Claude Code config; skills/agents are symlinks into .agents/
├── .cursor/         ← Cursor config; skills/rules are symlinks into .agents/
├── templates/       ← document templates for common outputs
├── people/          ← per-person context (profiles, transcripts, talking points)
├── teams/           ← team-level context (rosters, OKRs, context docs)
├── contractors/     ← external dev registry, project mappings, and performance reports
├── metrics/         ← saved merged Jira+GitHub monthly reports (`/metrics` skill)
├── scripts/         ← automation scripts (gh-metrics, sprint metrics, delivery tools)
│   └── delivery/    ← roadmap-status, roadmap-report, dev-progress-weekly-report; `reports/`
├── config/          ← shared config for delivery tools (projects, repos, aliases)
└── context/         ← global context (org chart, company priorities, personal goals)
```

---

## Routing Instructions

Match the user's request to the right **skill** (interactive) or **agent** (autonomous). Skills run inline in the conversation; agents run as subprocesses and return a result.

### Skill Routing (Interactive — runs inline)

Skills are invoked with `/skill-name` and run in the main conversation. Use these for interactive, multi-turn work.


| User says something like…                                                            | Skill      | Command       |
| ------------------------------------------------------------------------------------ | ---------- | ------------- |
| "Prep me for my meeting with [name]" / "Help me prepare for [name]"                  | Prep       | `/prep`       |
| "Analyse this transcript" / "How did my meeting go?"                                 | Analyse    | `/analyse`    |
| "Draft an email/message/doc about…" / "Help me write a status update"                | Write      | `/write`      |
| "Help me decide between…" / "Think through this decision"                            | Decide     | `/decide`     |
| "Help me think through…" / "Brainstorm with me" / "What are the scenarios for…"      | Brainstorm | `/brainstorm` |
| "Write a review for [name]" / "Draft feedback for [name]" / "Prep calibration"       | Review     | `/review`     |
| "I need to hire for [role]" / "Interview scorecard" / "Debrief this interview"       | Hiring     | `/hiring`     |
| "We had an incident" / "Help me write a postmortem" / "Draft incident comms"         | Incident   | `/incident`   |
| "Help me plan the quarter" / "Roadmap review" / "Sprint planning prep" / "Set OKRs"  | Planning   | `/planning`   |
| "Get developer metrics" / "Run dev metrics" / "Pull Jira/GitHub metrics for [month]" | Metrics    | `/metrics`    |
| "Convert Xray tests to Gherkin" / "Turn Xray export into feature files" / "Xray to Gherkin" | Xray to Gherkin | `/xray-to-gherkin` |


### Agent Routing (Autonomous — runs as subprocess)

Agents run autonomously and return a result. Use these for non-interactive tasks.


| User says something like…                                                                                | Agent           | File                                      |
| -------------------------------------------------------------------------------------------------------- | --------------- | ----------------------------------------- |
| "Extract memory from this" / "Save to memory" / "What should I remember?"                                | Memory          | `.claude/agents/memory-agent.md`          |
| "Contractor metrics" / "How is [dev] performing?" / "Dev performance report" / "Run a contractor review" | Contractor Perf | `.claude/agents/contractor-perf-agent.md` |


> **Note:** Memory can also be triggered as the final phase of any skill. If the user says "extract memory" during a hiring, planning, incident, or review session, run the Memory Agent with that session's context.

### Delivery Tools (Direct)

These are CLI scripts that produce reports. Run them directly when the user asks for delivery data.


| User says something like…                                                        | Tool           | Command                                                      |
| -------------------------------------------------------------------------------- | -------------- | ------------------------------------------------------------ |
| "Show me the roadmap" / "What epics are delayed?" / "Roadmap status"             | Roadmap status | `scripts/delivery/roadmap-report` (auto-runs roadmap-status) |
| "What did the team ship this week?" / "Developer progress" / "Weekly dev report" | Dev progress   | `scripts/delivery/dev-progress-weekly-report`                |
| "Sprint metrics for [month]" / "How many story points?" / "QA bouncebacks"       | Sprint metrics | `scripts/jira-sprint-metrics`                                |


These tools read shared config from `config/` (projects, repos, aliases). Script outputs go to `scripts/delivery/reports/`. Merged monthly Jira+GitHub metrics from `/metrics` go to `metrics/` at repo root.

### Ambiguous

If you can't determine the right mode, ask ONE clarifying question. Don't guess.

---

## Context Loading Protocol

This is the **single source of truth** for how context is loaded. All skills and agents follow this protocol — they do not define their own loading rules.

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
4. `context/brag-doc.md` — accomplishments log; load when discussing performance, promo, self-review, or "what have I done lately". Updates governed by `.agents/rules/brag-doc.mdc` — at the end of any skill or agent, scan for brag-doc-worthy moments and offer to append.

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
5. Load the skill/agent file
6. Summarise to yourself what you know before engaging the user

If a person or team folder doesn't exist, tell the user and offer to create it. If a referenced file doesn't exist, note it and continue.

---

## Behavioral Standards

These rules apply to **all skills and agents**. Individual skill/agent files should not repeat them.

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

When one skill suggests handing off to another:

1. The **output of the completed skill** becomes input context for the next
2. The next skill still loads standard context per the Context Loading Protocol above
3. State the handoff explicitly — the user decides when to proceed
4. The receiving skill should acknowledge what it received and confirm before starting its own process







## Rules

These rules are the canonical source — both Cursor (via `.cursor/rules/*.mdc` symlinks) and Claude Code (via the imports below) consume them. Edit the `.mdc` files in `.agents/rules/`, never copy content here.

@.agents/rules/em-persona.mdc
@.agents/rules/external-writes.mdc
@.agents/rules/jira-access.mdc
@.agents/rules/brag-doc.mdc