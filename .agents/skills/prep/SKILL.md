---
name: prep
description: "Prepare for an upcoming 1-on-1 meeting through a full grill-me session — relentless one-at-a-time questioning, with a recommended answer for each, until every agenda topic is resolved. Use when the user says things like: 'prep for my meeting with [name]', 'help me prepare for [name]', 'get ready for my 1-on-1', 'grill me before my 1:1 with [name]'. For a non-interactive draft, use /prep-draft instead."
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

**Staleness check:** Determine the date of the most recent transcript. If it is more than 14 days ago, flag this explicitly in the Opening Statement and adjust your framing:
- Topics from the last meeting may have already resolved or escalated — ask about them with this in mind
- The person may have had significant context shifts (new priorities, team changes, personal pressures) that aren't captured in history
- Be more open-ended in Phase 3; don't assume continuity from the last transcript

---

### Phase 2 — Opening Statement

Start with a brief (3–5 bullet) summary of what you found from past context. Frame it as: *"Here's what I'm seeing going into this meeting."*

Example format:
```
Looking at your recent history with [Name]:
- [⚠️ Last meeting was X days ago — context may have shifted] (only if >14 days)
- [Open action item or carry-over from last meeting]
- [Recurring theme that hasn't been resolved]
- [Something that went well / momentum to build on]
- [A gap — something that hasn't come up in a while but probably should]
- [From memory: a pattern, commitment, or dynamic worth keeping in mind]
- [Self-awareness: a tendency of yours to watch for — listed separately from operational items]
```

If memory entries surface something the user may have forgotten (a commitment made 3 meetings ago, a self-awareness pattern), highlight it explicitly — this is where memory adds the most value.

If there's no history, say so clearly and move straight to Phase 3.

---

### Phase 3 — Grill-Me Session

Interview the user relentlessly about this meeting until you both share a clear understanding of what they want from it. This is a full grill-me session, not a light check-in.

**How it works**

1. **Build the topic tree first.** From Phase 1–2, list the candidate topics (carry-overs, open commitments, tensions, gaps, the user's own goals). Show it as a short tree, then grill one branch at a time.
2. **One question at a time.** Never batch questions. Wait for the answer before the next one.
3. **Always give your recommended answer.** Every question ends with *"My take: …"* — your best guess based on context, so the user can just confirm, correct, or push back.
4. **Answer from context before asking.** If the answer is already in transcripts, analysis files, memory, delivery reports or todos, look it up and state it instead of asking. Only ask what the files cannot tell you.
5. **Walk each branch to the bottom.** For each topic, resolve in order:
   - **Why** — why does this matter now? What happens if it is not raised?
   - **Outcome** — what exactly do you want to leave with? (decision, commitment, information, support, a changed belief)
   - **Their side** — how will they likely react? What do they want from this topic? What objections will they raise?
   - **Your position** — what is your opening line? What will you concede? What is non-negotiable?
   - **Evidence** — what concrete facts, data or examples back you up?
   - **Next step** — who does what by when if it goes well? What if it goes badly?
   Resolve dependencies between topics as you go (e.g. "if David says no to X, does topic Y still make sense?").
6. **Push on weak answers.** Vague, hedged or "I'll see how it goes" answers are not accepted. Ask: *"What specifically?"*, *"What would you actually say?"*, *"What evidence do you have?"*. If the user's reasoning has a gap, say so directly.
7. **Challenge the agenda itself.** Ask what they are avoiding, what they are over-preparing, and whether a topic belongs in this meeting at all. Cut topics that do not earn a place.

**Domains to cover** (adapt to relationship type; skip what clearly does not apply)

**MANAGER:** what you need from them (unblocking, visibility, support, decision) · what you are avoiding · your biggest pressure and whether they know it · political/org dynamics · what you want them to think about you/your team afterwards.

**DIRECT REPORT:** performance right now (concerns, standouts) · what they need but are not asking for · growth topics · tensions (people, work, expectations) · the single most important message this cycle.

**PEER / CROSS-FUNCTIONAL:** shared goal or dependency · what is blocked or misaligned · what you need from them vs. what they need from you.

**All:** follow-ups from last time · what success looks like.

**Self-awareness check:** use the `[self]` memory patterns actively. If the user is repeating a known pattern (e.g. over-reporting to a manager, avoiding a hard topic), name it in the moment.

**Imposter-syndrome check:** if the user undersells their position, apologises for asking, or frames a legitimate need as a favour, call it out and help them restate it as a clear ask backed by evidence.

**Progress tracking:** after each branch is resolved, give a one-line recap (`✅ [Topic] — outcome: …`) and show which branches remain.

**Exit criteria:** there is no question cap. Stop only when every branch in the tree is resolved (why, outcome, position, next step all clear), or when the user says they are ready. Before moving to Phase 4, show the final resolved tree and ask: *"Anything missing, or shall I write the doc?"*

---

### Phase 4 — Generate Talking Points Doc

Create a structured document using the template at `templates/talking-points.md`. Build it from the resolved branches of the grill-me session — each Priority Topic carries its agreed outcome, opening line and next step:

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

## Watch For (Operational)
- ...

## Watch For (Self — How You Tend to Show Up)
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
- If the user gives a vague answer, push: *"What specifically? What would you actually say?"* Do not move on until it is concrete.
- If a topic comes up that the user keeps avoiding or dismissing, flag it: *"You've mentioned [X] a couple of times but moved past it — is there something there worth putting on the agenda?"*
