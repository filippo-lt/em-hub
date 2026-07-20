# Per-feature folder template

Copy this folder to `docs/specs/<feature-slug>/` when starting a new
feature. The skills will fill in the artefacts as they run.

```
<feature-slug>/
├── <feature>.feature           ← phase 1 — /spec-from-tests
├── <feature>.spec.md           ← phase 1
├── <feature>.coverage.md       ← phase 1
├── <feature>.audit.md          ← phase 2 — /audit-implementation
├── <feature>.refactor-plan.md  ← phase 4 — /refactor-feature (plan output)
└── tests/
    ├── characterisation/       ← phase 3 — /write-characterisation
    └── unit/                   ← phase 5 — /write-unit-tests
```

## Feature slug

Lowercase, hyphenated, single segment:
- `garden-design`
- `force-update`
- `interior-design`
- `paywall`

Match the folder name to the `Feature:` declaration inside the `.feature`
file (`@feature:garden_design` ↔ `garden-design/`).

## File naming

All artefact files use the same slug as a prefix:
- `garden-design.feature`
- `garden-design.spec.md`
- `garden-design.coverage.md`
- `garden-design.audit.md`
- `garden-design.refactor-plan.md`

This makes them greppable as a set and obvious in PRs.
