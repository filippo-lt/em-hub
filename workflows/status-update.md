# Workflow: Status Update

Gather context from recent meetings, team data, and personal notes to draft a structured status update.

---

## Routing

Activate when the user says:
- "Help me write a status update"
- "Draft my weekly/fortnightly update"
- "What should I report to [name/leadership]?"

---

## Agents Used

1. **Writing Agent** (`agents/writing-agent.md`) — drafts the update
2. **Memory Agent** (`agents/memory-agent.md`) — extract memory if the drafting process surfaced new strategic insights or narrative shifts

---

## Process

### Phase 1 — Gather Context

Load context per **Context Loading Protocol** in CLAUDE.md. Key files for status updates:
- `context/my-goals.md` — what you're measured on
- `teams/[team]/okrs.md` — team-level goals and metrics
- 3 most recent transcripts from `people/*/transcripts/` — outcomes and themes
- Most recent analysis docs — key outcomes and action items
- `people/[manager]/profile.md` — what your manager cares about, how they like updates
- `context/memory/planning/` — narrative patterns from previous updates

### Phase 2 — Ask the User

One question at a time:
1. What are the top 2–3 things worth highlighting this cycle?
2. Any blockers or risks to flag?
3. Anything you want to signal without making a big deal of? (Subtle positioning)
4. Any wins from the team worth calling out?

### Phase 3 — Draft

Hand off to the **Writing Agent** (`agents/writing-agent.md`). Calibrate to the audience:
- **For a manager:** concise, outcome-focused, flag risks early
- **For leadership/skip-level:** strategic framing, numbers where possible, brief
- **For a team:** transparent, acknowledge contributions, signal direction

### Phase 4 — Iterate

> "Want to adjust emphasis, add anything, or is this ready?"

### Phase 5 — Memory Extraction (if warranted)

Not every status update produces memory-worthy insights. But if the drafting process surfaced:
- A shift in how you're framing your team's work to leadership
- A risk or blocker you hadn't previously articulated clearly
- A pattern in what you keep reporting (or avoiding reporting)

Then run the Memory Agent with `[planning]` or `[self]` tags.

---

## File Outputs

| Output | Location |
|--------|----------|
| Status update draft | Shared in chat (user decides where to send) |
| Memory (if extracted) | `context/memory/planning/YYYY-MM-DD_memory.md` |
