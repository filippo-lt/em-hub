# iOS Refactor Pipeline

A repeatable, skill-driven pipeline for taking a feature from **QA test cases**
→ **Gherkin spec** → **implementation audit** → **characterisation tests**
→ **clean-architecture refactor** → **unit tests**.

Built initially for the AID iOS app, but the pipeline shape is platform-agnostic.

## Why this exists

The iOS codebase has:
- 354 manual QA tests in Xray (Jira), well-structured but human-prose
- No unit tests
- Plans to migrate to a new clean architecture (architecture doc maintained separately)
- ~14 user-facing features, all currently in legacy architecture

We want a workflow that lets engineers (with LLM assistance) move features
through to the new architecture without losing behaviour, with tests as the
safety net rather than the afterthought.

## Folder map

```
refactor-pipeline/
├── README.md             ← you are here
├── HANDOFF.md            ← decisions made, decisions still open, next steps
├── workflow.md           ← the 5-phase pipeline, per-phase contracts
├── skills/               ← skill drafts to install in .claude/skills/
│   ├── trace-coverage.md
│   ├── spec-from-tests.md
│   ├── audit-implementation.md
│   ├── write-characterisation.md
│   ├── refactor-feature.md
│   └── write-unit-tests.md
├── demo/
│   └── garden-design/    ← worked example: Garden Design (21 tests → spec)
│       ├── garden-design.feature
│       ├── garden-design.spec.md
│       └── garden-design.coverage.md
├── source-data/
│   └── ADIOSMAU_tests_combined_2026-05-04.json   ← Xray export, all 354 tests
└── templates/
    └── feature/          ← per-feature folder skeleton (copy when starting a new feature)
```

## Quick start

1. Read **HANDOFF.md** first — open decisions to make before scaling.
2. Read **workflow.md** for the 5-phase pipeline.
3. Browse **demo/garden-design/** for what phase-1 output looks like.
4. Browse **skills/** for the prompt-level contracts of each skill.

## Status

- ✅ Phase 1 (spec) prototyped on Garden Design — see demo
- ⬜ Skills not yet implemented as installable `.claude/skills/`
- ⬜ Architecture doc not yet linked into this folder
- ⬜ Pilot feature not yet selected
- ⬜ Phases 2–5 not yet attempted on any feature

See HANDOFF.md for what to decide before starting.
