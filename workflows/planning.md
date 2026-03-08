# Workflow: Planning

Support quarterly planning, roadmap reviews, sprint planning, and goal-setting.

---

## Routing

Activate when the user says:
- "Help me plan the quarter" / "Quarterly planning"
- "Roadmap review"
- "Sprint planning prep"
- "Help me set goals/OKRs"
- "Prioritise this list"

---

## Agents Used

1. **Decision Agent** (`agents/decision-agent.md`) — prioritisation, trade-off analysis
2. **Writing Agent** (`agents/writing-agent.md`) — draft planning docs, OKRs
3. **Prep Agent** (`agents/prep-agent.md`) — prepare for planning meetings with stakeholders
4. **Memory Agent** (`agents/memory-agent.md`) — capture planning decisions

---

## Phases

### Phase 1 — Load Current State
Read:
- `teams/[team]/okrs.md` — current goals
- `context/company-priorities.md` — what leadership cares about
- `context/my-goals.md` — personal goals
- Recent transcripts with manager — any direction given

### Phase 2 — Review & Reflect
Ask the user:
1. What worked last cycle? What didn't?
2. What's changed in the landscape (priorities, team, resources)?
3. What's the single most important thing to get right next cycle?
4. What should you stop doing?

### Phase 3 — Draft Goals/Plan
Depending on what's needed:
- **OKRs:** Objective + 2–3 Key Results per objective, measurable
- **Roadmap update:** What's in, what's out, what's moved
- **Sprint plan:** Priorities, capacity, risks

### Phase 4 — Pressure Test
Decision agent challenges the plan:
- Is this achievable with current resources?
- What are you implicitly deprioritising?
- What dependencies could derail this?
- Does this align with what leadership actually wants?

### Phase 5 — Memory Extraction
After the plan is finalised:
- Memory agent extracts planning decisions and strategic context using `[planning]` and `[self]` tags
- Focus: key decisions and their reasoning, what was explicitly deprioritised (and why), assumptions that need revisiting, personal patterns in how you plan
- Output: Memory entries → save to `context/memory/planning/YYYY-MM-DD_memory.md`

---

## File Outputs

| Output | Location |
|--------|----------|
| OKRs / Goals | `teams/[team]/okrs.md` (updated) |
| Planning doc | `context/planning/YYYY-QN_plan.md` |
| Decision record | `context/decisions/YYYY-MM-DD_planning.md` |
| Memory | `context/memory/planning/YYYY-MM-DD_memory.md` |
