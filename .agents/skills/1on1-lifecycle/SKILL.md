---
name: 1on1-lifecycle
description: "Run a complete 1-on-1 lifecycle end to end in one pass — pull the meeting transcript from Granola, analyse it against the prep doc, save transcript + analysis, and automatically extract memory. Use when the user says: 'run the full 1:1 with [name]', 'process my 1:1 with [name]', 'write up my 1:1', 'I just finished my 1:1 with [name]', 'debrief my 1:1'. This orchestrates /analyse and the Memory Agent so the user does not have to trigger each step manually."
user_invocable: true
metadata:
  version: 1.0.0
---

# 1:1 Lifecycle

One command that runs the whole post-1:1 workflow without stopping between steps. It exists because the pieces already exist separately (`/analyse`, the Memory Agent) but today they're chained by hand — pull transcript, run analyse, then "run memory extraction", then "yes". This collapses that into a single continuous run.

**The user has opted into full auto memory: do not pause to ask before extracting and saving memory. It is part of the run.**

---

## Reused components — do not duplicate their logic

This skill orchestrates existing skills. Follow their canonical definitions rather than restating formats here:

- Analysis format and mandatory close → `.agents/skills/analyse/SKILL.md`
- Memory taxonomy, `[YYYY-MM-DD] [tag] - content` format, and save paths → `.agents/agents/memory-agent.md`
- Context loading, naming conventions, behavioural standards → `CLAUDE.md`

If those files change, this skill inherits the change. Keep this file thin.

---

## Workflow — run in order, without pausing

### 1. Resolve the person
Map the spoken name to the canonical `people/[slug]/` folder. Known slugs: `vlad-engineer`, `andrey-direct`, `david-manager`, `victor-jalencas`, `sergio-hueso`, `ledio-bidaj`, `yevhen-holub`. Cross-check against memory and fix known mis-transcriptions (e.g. Granola renders "Sergio Hueso" as "Sergio Wetzel" — keep the established name). If the person can't be resolved to a folder, that's a valid stop — ask which report this is.

Load their Person Context per the Context Loading Protocol: `profile.md`, 3 most recent transcripts, the most recent `*_analysis.md`, the talking-points doc used for this meeting (most recent in `people/[slug]/talking-points/`), and all of `people/[slug]/memory/`.

### 2. Pull and save the transcript
Fetch the transcript from the Granola connector — default to **today's 1:1 with this person**; if ambiguous, take the latest 1:1 with them and state which meeting you used. Save it verbatim to `people/[slug]/transcripts/[YYYY-MM-DD]_transcript.md`.

If no transcript can be found in Granola, that's a valid stop — tell the user and offer to proceed from a pasted transcript instead. Never invent meeting content.

### 3. Analyse
Run the full `/analyse` process against the talking-points doc: Coverage Check, Key Outcomes, Action Items, Communication — Honest Assessment, Patterns vs. Previous Meetings, Flags for Next Meeting, Relationship Health, and the structured Carry-overs block in the exact format `/prep` expects. Save the full analysis + carry-overs to `people/[slug]/transcripts/[YYYY-MM-DD]_analysis.md`.

### 4. Extract memory — automatically, no confirmation
Immediately run the Memory Agent on this session's transcript + analysis. Apply its taxonomy (`[people]`, `[perf]`, `[planning]`, `[self]`, plus `[hiring]`/`[incident]` if relevant), its "would this change my approach in 3 months?" filter, and its max-15-entries rule. Write files per the Agent's Save Paths:

- Person entries (`[people]`, `[perf]` for this report) → `people/[slug]/memory/[YYYY-MM-DD]_memory.md`
- Self entries (`[self]`) → `context/memory/self/[YYYY-MM-DD]_[slug]-1on1_memory.md`
- Planning entries (`[planning]`) → `context/memory/planning/[YYYY-MM-DD]_[slug]-1on1_memory.md`

**Append, never overwrite** — if a dated file already exists, read it and add the new entries beneath the existing ones.

### 5. Keep source docs current
If `profile.md` has gone stale (e.g. "Current Situation" describes a now-resolved issue, or "Open Questions" were answered), update those sections to match reality. Per the brag-doc rule, if a clear win by the user surfaced, offer to append it to `context/brag-doc.md`.

### 6. Close
Present the analysis file first, then the memory files. Give a 3–4 line headline: the one-line read of the meeting, the single highest-value compounding signal, and the most important flag for next time.

Then offer — but do not auto-run — the natural next actions:
- **Commit and push to GitHub.** List exactly which files were created or updated this run (transcript, analysis, memory files, any `profile.md`/`brag-doc.md` edits), propose a commit message (e.g. `1:1 <Name> <YYYY-MM-DD>: transcript, analysis, memory`), and only run `git add` / `commit` / `push` on the user's confirmation. Pushing is an external write — never auto-push (per `.agents/rules/external-writes.mdc`).
- Draft the progress email to the org, or set a reminder for a dated commitment that surfaced.

Remind the user they can run `/prep` before the next meeting to pick up the carry-overs.

---

## Principles

- **One continuous run.** The entire point is removing the per-step prompting. The only valid stops are: person can't be resolved, or no transcript exists.
- **Single source of truth.** Don't restate the analysis or memory formats — defer to `analyse` and `memory-agent`. This prevents drift.
- **Honest, specific, kind.** The communication assessment is the highest-leverage output — name concrete moments, not vague praise.
- **Never fabricate.** No transcript → no analysis. Say so.
