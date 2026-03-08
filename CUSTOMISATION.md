# Customisation Guide

How to modify and improve the system over time. No coding required — everything is markdown prompts.

---

## The Mental Model

**Agents** are reusable behaviours. **Workflows** are sequences that chain agents together. **Templates** are output formats.

```
agents/          ← what the AI does (prep, analyse, write, decide, review, extract memory)
workflows/       ← when to do it (1-on-1, hiring, performance cycle, etc.)
templates/       ← how the output looks (talking points, scorecards, reviews, etc.)
```

Changing behaviour = editing markdown files. Think of them as recipes: clear steps, ordered phases, explicit rules.

---

## Common Modifications

### Add a New Person

```bash
mkdir -p people/name-role/{transcripts,talking-points,memory,context}
cp templates/context-profile.md people/name-role/profile.md
# Edit the profile
```

### Add a New Team

```bash
mkdir -p teams/team-name/context
# Create roster.md and okrs.md
```

### Change What the Prep Agent Asks

Open `agents/prep-agent.md` and find **Phase 3 — Question Loop**.

Add, remove, or reorder questions under "For meetings with a MANAGER", "For meetings with a DIRECT REPORT", or "For meetings with a PEER / CROSS-FUNCTIONAL".

Example: if you want the agent to always ask about your own energy/state before a meeting, add:
```
- How are you going into this meeting? (Energy level, state of mind — it affects how you show up)
```

### Change the Talking Points Output Format

Find **Phase 4 — Generate Talking Points Doc** in `agents/prep-agent.md`.

The template inside the code block is exactly what gets produced. Edit it to match how you naturally think. For example, if you want a "Risks to flag" section, add it there.

### Change What Analysis Covers

Open `agents/analysis-agent.md` and find **Phase 2 — Deliver Analysis**.

Each `####` heading is a section. You can:
- Remove sections you don't find useful (e.g., remove "Patterns vs. Previous Meetings" if you're just starting out)
- Add new sections (e.g., "Energy & Engagement" to track tone over time)
- Change the table format to prose or vice versa

### Add a New Workflow

1. Create `workflows/your-workflow.md` — define the phases and which agents it uses
2. Add a routing rule in `CLAUDE.md` under the workflow routing table
3. Create any new templates in `templates/` if needed

Example: a "vendor review" workflow could chain `analysis-agent` (review the vendor's performance) → `writing-agent` (draft the governance update) → `memory-agent` (capture learnings).

### Add a New Agent

1. Create `agents/your-agent.md` with the behaviour you want
2. Reference it from the relevant workflow files
3. Add a standalone routing rule in `CLAUDE.md` if it can be used outside workflows

---

## When to Update Profiles

Update `people/[name]/profile.md` whenever:
- Their priorities shift significantly
- The relationship dynamic changes
- You learn something important about their communication style
- There's a major event (promotion, reorg, project launch/failure)

Keep it honest and current — stale profiles will mislead the agents.

---

## When to Add Context Documents

Add files to `people/[name]/context/` or `teams/[team]/context/` whenever you have a document that would help an advisor understand the situation:

| Document | Why it helps |
|----------|-------------|
| Performance review | Agent knows the formal evaluation baseline |
| Roadmap or OKRs | Agent understands strategic priorities |
| Email thread export | Agent can reference specific decisions or tone |
| Your own notes after an informal chat | Agent has off-the-record context |
| Org chart or team roster | Agent understands the landscape |

---

## Improving Over Time

### After 3–5 meetings

Look at your saved prep docs and analysis files. Ask yourself:
- Are the prep questions actually surfacing things I care about?
- Is the analysis calling out the right patterns?
- What's missing?

Then edit the agent prompts accordingly.

### Signs the prep agent needs tuning

- Questions feel generic or obvious → make them more specific to the relationship type
- Too many questions → add a "stop after N topics" rule
- Not enough depth → change "4–6 topics" to a higher bar, add more follow-up probing rules

### Signs the analysis agent needs tuning

- Missing action items → add a rule: "Be aggressive about identifying implicit commitments, not just explicit ones"
- Communication feedback feels too soft → edit: "Be blunt. The user wants to improve, not be reassured"
- Too long → remove sections, or add: "Keep the full analysis under 400 words"

### Signs the writing agent needs tuning

- Too verbose → add: "Default to 3 sentences for Slack, 5 for email. Expand only if asked."
- Not matching tone → update the recipient's profile with clearer communication preferences
- Missing context → check that the relevant files are being loaded in Phase 2

---

## Prompt Engineering Tips

When editing agent prompts:

**Be specific, not general.** Instead of "ask about team health", write "ask: 'Is there anyone on the team right now who's disengaged, struggling, or creating friction?'"

**Add examples.** The agents follow examples well. If you want a certain output format, show it explicitly in the prompt.

**Use imperative language.** "Ask ONE question at a time" is more reliable than "try to ask one question at a time".

**Add negative rules for things that go wrong.** If the agent keeps doing something annoying, add: "NEVER [thing that annoys you]".

**Test iteratively.** Change one thing at a time. Run a test session. See if it improved.

---

## File Naming — Keep It Consistent

```
transcripts/    YYYY-MM-DD_transcript.md
talking-points/ YYYY-MM-DD_prep.md
memory/         YYYY-MM-DD_memory.md
context/        [descriptive-name].md
```

Consistent naming = the agents can always find "most recent" reliably.
