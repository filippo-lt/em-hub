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
