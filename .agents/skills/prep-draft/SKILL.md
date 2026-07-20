---
name: prep-draft
description: "Autonomously generate a talking-points draft for an upcoming 1-on-1 — no interactive question loop. Use when the user says: 'draft prep for [name]', 'auto-prep my 1:1 with [name]', 'prep-draft [name]', 'give me a first-pass agenda for [name]'. This is the non-interactive companion to /prep: it fills the whole talking-points doc from context so the user reviews and edits rather than answering questions live."
user_invocable: true
metadata:
  version: 1.0.0
---

# Prep Draft

Produces a complete first-pass talking-points doc for a 1-on-1 **from context alone**, without asking the user anything. It's the autonomous counterpart to `/prep`: run this to get a draft on the page, then optionally run `/prep` to refine it interactively before the meeting.

**Do not run the question loop. This is a one-shot draft.** The user reviews and edits afterward.

---

## Reused components — do not duplicate their logic

- Context loading, Opening Statement, and the talking-points doc format → `.agents/skills/prep/SKILL.md` (Phases 1, 2, 4) and `templates/talking-points.md`
- Carry-overs come from the most recent `*_analysis.md` in the person's `transcripts/`, in the format `/analyse` Phase 4 emits
- Naming conventions and behavioural standards → `CLAUDE.md`

Keep this file thin — it changes *how* prep runs (autonomous, whole-doc), not the format.

---

## Workflow — run in order, without asking questions

### 1. Resolve the person (scope: all 1:1s)
Map the spoken name to `people/[slug]/`. Known slugs: `vlad-engineer`, `andrey-direct`, `david-manager`, `victor-jalencas`, `sergio-hueso`, `ledio-bidaj`, `yevhen-holub`. Cross-check memory and fix known mis-transcriptions (e.g. "Sergio Hueso" not "Sergio Wetzel").

**If no folder exists, create one** — this skill preps any 1:1, including new people. Create `people/[slug]/` with subfolders `transcripts/`, `talking-points/`, `memory/`, `context/`, and a minimal `profile.md` (name, apparent role/relationship if known, "created by prep-draft — fill in"). Then continue; a thin draft is still useful.

### 2. Load context
Follow `/prep` Phase 1 exactly: `profile.md`, 3 most recent transcripts, the most recent `*_analysis.md` (its carry-overs are the backbone of this draft), 3 most recent talking-points docs, all of `people/[slug]/context/` and `people/[slug]/memory/`, plus relevant global/self/planning memory. For a direct report, also check the latest `scripts/delivery/reports/` dev-progress report for their recent commits/PRs/tickets.

Run the `/prep` **staleness check**: if the most recent transcript is >14 days old, note it at the top of the draft and keep topics more open-ended.

### 3. Fill every section from context — don't ask
Where `/prep` would ask the user a question, instead infer the best-supported answer from loaded context and write it as a **proposed** item the user can accept or cut. Never fabricate: if a section has no basis in context, write `— (nothing carried over; add live)` rather than inventing.

### 4. Generate and save the doc
Use the `templates/talking-points.md` structure:

```markdown
# 1-on-1 with [Name] — [YYYY-MM-DD]

> Draft — generated from context by /prep-draft. Review and edit before the meeting.

## Priority Topics
1. **[Topic]** — [1-line context / goal]   (sourced from: carry-over / memory / dev report)
2. ...
3. ...

## Questions to Ask
- ...

## Things to Communicate
- ...

## Carry-overs from Last Meeting
- [pulled directly from the last _analysis.md carry-overs block]

## Watch For (Operational)
- ...

## Watch For (Self — How You Tend to Show Up)
- [from context/memory/self — the [self] patterns for this relationship]

## Success Looks Like
...
```

Save to `people/[slug]/talking-points/[YYYY-MM-DD]_prep.md`. **Append/version, don't clobber** — if a `_prep.md` for that date already exists, don't overwrite; save alongside or ask which to keep.

### 5. Close
Present the saved doc. Give a 2–3 line summary: what the draft is built on (which carry-overs / signals), and the one topic you're least sure about so the user knows where to focus their edit. Offer `/prep` for an interactive refinement pass.

---

## Principles

- **No question loop.** The whole point is a ready-made draft. The only valid pause is a same-date filename collision.
- **Everything is a proposal.** Tag items by where they came from so the user can trust or cut them quickly.
- **Carry-overs are the spine.** The last analysis's open items and watch-fors should visibly drive the agenda — that's how the loop with `/1on1-lifecycle` compounds.
- **Never fabricate.** Empty section → say so, don't invent.
