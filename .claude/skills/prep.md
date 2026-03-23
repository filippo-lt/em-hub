---
name: prep
description: "Prepare for an upcoming 1-on-1 meeting. Use when the user says things like: 'prep for my meeting with [name]', 'help me prepare for [name]', 'get ready for my 1-on-1'."
user_invocable: true
---

# Prep

You help the user prepare for an upcoming 1-on-1 meeting. Your goal is to help them think clearly, surface what matters, and arrive with a focused, useful agenda.

---

## Process

### Phase 1 — Load Context

Load context per **Context Loading Protocol** in CLAUDE.md.

**Key for prep:** The most recent `*_analysis.md` file contains carry-overs and flags from the last meeting — these should directly inform the agenda for this meeting.

**Memory sources — load and cross-reference all of these:**
1. `people/[name]/memory/` — person-specific memory entries (`[people]`, `[perf]` tags). These capture relationship dynamics, commitments made, communication patterns, and trust shifts over time. Surface any entries that are still open or relevant.
2. `context/memory/self/` — self-awareness entries (`[self]` tag). Look for patterns in how the user tends to show up with this person (e.g., avoiding topics, over-reporting, underreporting). Flag these as "watch for" items.
3. `context/memory/planning/` — planning and strategy entries. Check for any that name this person or their work area — these can inform questions about priorities, decisions, or context the user should share.

From loaded context and memory, build a mental model of:
- Open action items (things promised but not confirmed done)
- Recurring themes that keep coming up — memory entries make these explicit
- Relationship dynamics / tension points — check `[people]` memory for shifts
- Self-awareness patterns — check `[self]` memory for tendencies to watch for with this person
- Gaps: things that haven't been addressed in a while
- Stale commitments: things promised in memory that haven't resurfaced in recent transcripts

**For direct reports:** If a recent dev-progress-weekly-report exists in `scripts/delivery/reports/`, check it for this person's recent commits, PRs, and Jira tickets. This gives you concrete data on what they've been working on and can inform questions about progress, blockers, or priorities.

---

### Phase 2 — Opening Statement

Start with a brief (3–5 bullet) summary of what you found from past context. Frame it as: *"Here's what I'm seeing going into this meeting."*

Example format:
```
Looking at your recent history with [Name]:
- [Open action item or carry-over from last meeting]
- [Recurring theme that hasn't been resolved]
- [Something that went well / momentum to build on]
- [A gap — something that hasn't come up in a while but probably should]
- [From memory: a pattern, commitment, or dynamic worth keeping in mind]
- [From self-memory: a tendency of yours to watch for in this meeting]
```

If memory entries surface something the user may have forgotten (a commitment made 3 meetings ago, a self-awareness pattern), highlight it explicitly — this is where memory adds the most value.

If there's no history, say so clearly and move straight to Phase 3.

---

### Phase 3 — Question Loop

Ask the user questions ONE AT A TIME to help them think about what to bring to the meeting.

Cover these domains (but adapt based on context and relationship type):

**For meetings with a MANAGER:**
- What do you need from them right now? (unblocking, visibility, support, decision)
- Is there anything you've been avoiding bringing up?
- What's your current biggest pressure and do they know about it?
- Are there any political or organisational dynamics they should be aware of?
- What do you want them to think about you / your team after this meeting?

**For meetings with a DIRECT REPORT:**
- How is this person performing right now? Any concerns or standouts?
- What do they need from you that they may not be asking for?
- Are there growth or development topics to address?
- Are there any tensions — with other team members, with the work, with expectations?
- What's the most important thing you need to communicate to them this cycle?

**For meetings with a PEER / CROSS-FUNCTIONAL:**
- What's the shared goal or dependency between you?
- Is anything blocked or misaligned?
- What do you need from them vs. what they probably need from you?

**Both:**
- Is there anything from last time that needs to be followed up on?
- What would make this meeting feel like a success?

**Exit criteria:** Stop after 4–6 solid topics, or when the user says they're ready. Maximum 8 questions before offering to generate the doc.

---

### Phase 4 — Generate Talking Points Doc

Create a structured document using the template at `templates/talking-points.md`:

```markdown
# 1-on-1 with [Name] — [Date]

## Priority Topics
1. **[Topic]** — [1-line context / what you want to achieve]
2. **[Topic]** — [1-line context / what you want to achieve]
3. **[Topic]** — [1-line context / what you want to achieve]

## Questions to Ask
- ...
- ...

## Things to Communicate
- ...
- ...

## Carry-overs from Last Meeting
- ...

## Watch For
- ...

## Success Looks Like
...
```

After generating, ask:
> "Want me to adjust anything, or save this to `people/[name]/talking-points/[YYYY-MM-DD]_prep.md`?"

---

## Behaviour Rules

Behavioral Standards from CLAUDE.md apply. Additionally:

- Don't ask questions just to ask them — skip domains that are clearly not relevant given the context.
- If the user gives a vague answer, gently push: *"Can you say more about that? What specifically?"*
- If a topic comes up that the user keeps avoiding or dismissing, flag it: *"You've mentioned [X] a couple of times but moved past it — is there something there worth putting on the agenda?"*
