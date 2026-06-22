---
name: new-project
description: Interview-driven skill for documenting a greenfield project at kickoff. Produces 8 typed Markdown files (brief, scope, architecture, conventions, runbook, ownership, README, CLAUDE.md) plus an empty `decisions/` folder, ready to hand off to an implementation agent. Use when the user says 'new project', 'document a new project', 'kick off a project', 'set up project docs', or '/new-project'.
---

# New Project

You run a focused interview that produces a complete kickoff doc set for a greenfield project. The output is a typed Markdown doc tree an implementation agent can load and act on without guesswork.

---

## What you produce

Eight files plus a `decisions/` folder at the project root:

1. `README.md` — `type: index` (generated)
2. `CLAUDE.md` — `type: index` (generated)
3. `product-brief.md` — `type: brief`, `status: frozen`
4. `scope.md` — `type: scope`, `status: living`
5. `architecture.md` — `type: architecture`, `status: living`
6. `ownership.md` — `type: reference`, `status: living`
7. `engineering-conventions.md` — `type: convention`, `status: living`
8. `getting-started.md` — `type: runbook`, `status: living`
9. `decisions/` — empty folder, fills as decisions get made

Every doc has the same frontmatter shape:

```yaml
---
type: <one of: brief|scope|architecture|reference|convention|runbook|decision|index|note>
status: <living|frozen|draft>
summary: <one sentence>
---
```

Body conventions: first line after frontmatter is an H1 matching the doc's purpose. `## Summary` H2 at the top, 3–5 lines. Everything else freeform.

---

## Process

### Phase 1 — Confirm scope and target

Ask in this order, one at a time:

1. **"Where should the docs land?"** — get the absolute path of the project root.
2. **"One-paragraph pitch: what is this project?"** — seeds everything that follows. If the answer is thin, ask one follow-up; don't proceed on vague input.

If the project root doesn't exist yet, offer to create it. If it exists and already has any of the 8 files, **stop and ask** — never overwrite without confirmation.

---

### Phase 2 — Walk the doc types in dependency order

Order is fixed: **brief → scope → architecture → ownership → convention → runbook → indexes (generated)**.

For each doc:
1. Ask the questions for that doc (lists below), one at a time.
2. Write the file with locked frontmatter.
3. Show the user the file, ask "good as-is? edits? move on?"
4. Only proceed to the next doc when confirmed.

If the user can't answer a question:
- Accept "skip" → leave the section out
- Accept "draft" → set `status: draft` on that doc and write a `> TODO:` line in the section
- Never stall the interview

---

### Phase 3 — Question lists per doc

#### `product-brief.md` — 5 questions
1. What problem does this solve, and who has it?
2. Who specifically is the target user? (one persona, not "everyone")
3. What's the bet — what do we believe will be true if this works?
4. What single metric tells us it worked, and what threshold?
5. Name 2–3 things this explicitly is **not** for.

Output sections: Problem, User, Hypothesis, Success criteria, Non-goals.

#### `scope.md` — 3 questions
1. What must ship in v1? List the capabilities.
2. What's been considered and explicitly rejected? (one-line why each)
3. What's plausible v2+ — worth remembering but not building?

Output sections: In scope, Out of scope, Deferred.

#### `architecture.md` — 4 questions
1. What are the major moving pieces? (services, apps, jobs, data stores)
2. How does data flow between them? (one paragraph, or a simple mermaid)
3. What's the tech stack, and what are 1–2 decisions worth recording **why**?
4. What external dependencies does this rely on?

Output sections: Components, Data flow, Tech stack, External dependencies, Key constraints.

**Side effect:** Q3's "why" answers become the first ADRs. After writing `architecture.md`, create `decisions/0001-<slug>.md` (and `0002-…` if a second) automatically. ADR sections: Context, Decision, Consequences. `status: frozen`.

#### `ownership.md` — 2 questions
1. Name one person for each role: EM, PM/PO, tech lead, on-call.
2. Who approves: scope changes, architecture changes, releases?

Output sections: Roles, Decision rights, External stakeholders (only if mentioned).

#### `engineering-conventions.md` — 4 questions
1. Language + version + framework?
2. Lint/format tooling and config source? (or "org default")
3. Branch / PR / commit rules? (or "org default")
4. Test expectations: what must be tested, coverage target, what's deliberately not tested?

Output sections: Stack, Tooling, Workflow, Testing, Project-specific notes.

#### `getting-started.md` — 5 questions
1. What tools/versions must be installed first?
2. What commands set it up, in order?
3. How do you run it locally?
4. How do you verify it's working?
5. What 1–2 things bite first-timers?

Output sections: Prerequisites, Setup, Run, Verify, Gotchas.

---

### Phase 4 — Generate the indexes

`README.md` and `CLAUDE.md` are **not interviewed**. Compose them from the docs already written:

**`README.md` body:**
- H1 = project name (from pitch)
- One-paragraph project description (pulled from `product-brief.md` summary)
- `## Documentation` — bulleted list of every doc with its `summary` frontmatter as the description
- `## Quick start` — link to `getting-started.md`

**`CLAUDE.md` body** — drop in this exact snippet, plus any project-specific agent rules the user mentions:

```markdown
## Project Documentation

This project is documented in a small set of typed Markdown files at the repo root. Every doc has frontmatter with three fields: `type`, `status`, `summary`. Types are: `brief` (why we're building it), `scope` (in/out/deferred), `architecture` (system shape), `reference` (data model, glossary, ownership), `convention` (rules we follow), `runbook` (how to do X), `decision` (one ADR per file in `decisions/`, frozen, superseded not edited), `index` (`README.md`, this file). Status is `living`, `frozen`, or `draft` — never edit a `frozen` doc, write a new one that supersedes it. Before implementing anything, load `brief`, `scope`, and `architecture`; load `convention` before writing code; load `runbook` only when doing the task it covers; treat `reference` as lookup. Significant decisions become new numbered files in `decisions/`.
```

Ask: "Any project-specific agent rules to add to CLAUDE.md?" — if no, ship as-is.

---

### Phase 5 — Handoff

Show the user:

1. **File tree** of what was created.
2. **Draft status report** — list any docs with `status: draft` and the gaps they call out.
3. **Handoff prompt** they can paste into an implementation agent, verbatim:

   > Here's the project documentation. Load `README.md`, then `CLAUDE.md`, then proceed with the first implementation task per `scope.md`.

End the session.

---

## Behaviour rules

- **One question at a time.** Never batch.
- **Show every file before moving on.** User must confirm.
- **Never overwrite without explicit confirmation.** If the file exists, stop and ask.
- **No mandatory sections beyond `## Summary`.** If a question's answer is "n/a," skip the section.
- **Tech-choice rationale goes in `decisions/`, not in `architecture.md`.** `architecture.md` says *what*, ADRs say *why*.
- **No "TBD" sections.** Either the section has content or it doesn't exist. `status: draft` covers "not ready" at the doc level.
- **Be ruthlessly concise.** Docs are read by agents; verbosity hurts them.

---

## Out of scope for this skill

- M&A / inherited codebases (use a separate `/inherit-project` skill when built)
- Scaffolding code, CI, or repo init — this skill produces docs only
- Generating Jira tickets, roadmaps, or plans — those live in planning tooling
- Updating existing docs — this is kickoff-only
