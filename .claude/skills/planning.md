---
name: planning
description: "Support quarterly planning, roadmap reviews, sprint planning, OKR setting, and prioritisation. Use when the user says things like: 'help me plan the quarter', 'roadmap review', 'sprint planning prep', 'help me set OKRs', 'prioritise this list'."
user_invocable: true
---

# Planning

Support quarterly planning, roadmap reviews, sprint planning, and goal-setting.

---

## Process

### Phase 1 — Load Current State

Load context per **Context Loading Protocol** in CLAUDE.md. Key files:
- `teams/[team]/okrs.md` — current goals
- `context/company-priorities.md` — what leadership cares about
- `context/my-goals.md` — personal goals
- Recent transcripts with manager — any direction given
- `context/memory/planning/` — past planning decisions and patterns
- `context/memory/self/` — self-awareness patterns in how you plan

**Delivery data (automated):**
Run `scripts/delivery/roadmap-status | scripts/delivery/roadmap-report` to get current epic status across all projects. The report surfaces delayed epics, at-risk items, recent deliveries, and warnings.

Optionally run `scripts/delivery/dev-progress-weekly-report` to see who is working on what and identify workload imbalances.

---

### Phase 2 — Review & Reflect

Ask the user ONE question at a time:
1. What worked last cycle? What didn't?
2. What's changed in the landscape (priorities, team, resources)?
3. What's the single most important thing to get right next cycle?
4. What should you stop doing?

---

### Phase 3 — Draft Goals/Plan

Depending on what's needed:
- **OKRs:** Objective + 2–3 Key Results per objective, measurable
- **Roadmap update:** What's in, what's out, what's moved
- **Sprint plan:** Priorities, capacity, risks

---

### Phase 4 — Pressure Test

Challenge the plan:
- Is this achievable with current resources?
- What are you implicitly deprioritising?
- What dependencies could derail this?
- Does this align with what leadership actually wants?

---

### Phase 5 — Memory Extraction

After the plan is finalised:
- Run the Memory Agent to extract planning decisions and strategic context using `[planning]` and `[self]` tags
- Focus: key decisions and their reasoning, what was explicitly deprioritised (and why), assumptions that need revisiting, personal patterns in how you plan

Output: Memory entries → save to `context/memory/planning/YYYY-MM-DD_memory.md`

---

## File Outputs

| Output | Location |
|--------|----------|
| OKRs / Goals | `teams/[team]/okrs.md` (updated) |
| Planning doc | `context/planning/YYYY-QN_plan.md` |
| Decision record | `context/decisions/YYYY-MM-DD_planning.md` |
| Memory | `context/memory/planning/YYYY-MM-DD_memory.md` |

---

## Behaviour Rules

Behavioral Standards from CLAUDE.md apply. Additionally:

- Ground everything in delivery data — don't plan in a vacuum.
- Push back on overcommitment. If the plan has more work than capacity, say so.
- Make deprioritisation explicit. Everything that's "in" means something else is "out".
- For OKRs: if a key result isn't measurable, it's not a key result.
- Flag when the plan contradicts signals from leadership (loaded from manager transcripts or company priorities).
