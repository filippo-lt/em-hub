# Open Loops artifact

URL: https://claude.ai/artifact/PxP9GMu46bw5oEKBrJco71

Redeploy with the same file path in a session that has already read or
published it, or from a fresh session by passing that URL as `url` after an
`action: "read"`. Publishing without the URL creates a second artifact and
splits the data, because the db belongs to the artifact.

Publish arguments that must stay stable:

- `file_path`: `todos/dashboard.html`
- `files`: `{"logic.js": "todos/logic.js"}`
- `root`: the repo root
- `favicon`: 🧾 (first publish only, omit afterwards)
- `icon`: checklist (first publish only, omit afterwards)
- `capabilities`: `{"db": {}}` (first publish only, omit afterwards so the
  stored declaration carries forward)

Collections: `items/`, `inbox/`, `meta/sync`. Shapes are in
`docs/superpowers/specs/2026-09-16-todo-dashboard-design.md`.

## Scheduled sweep

Status: needs one manual step from Filippo.

The existing Cowork routine `trig_01VTR6GzHAFjRboFqkUG8LgE`
("Open Loops — propose items after each 1:1", daily 09:30 Europe/Rome) still
points at the previous artifact `GWpgojE8wLJx6tGwYqJ21m`. It proves a cloud
routine reaches both the Granola connector and the artifact database, so no local
launchd job is needed.

It cannot be repointed from a Claude Code session: its `job_config` is ~88KB,
including a ~77KB Cowork system prompt that a full replace would have to resend
verbatim, and whether a partial `job_config` update merges or replaces is
undocumented. Guessing wrong breaks a live routine that cannot be deleted from a
session.

To repoint it, open the routine in Cowork and replace its prompt with
`todos/routine-prompt.md`.
