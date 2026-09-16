---
name: todos
description: "Add, list or close items on the Open Loops dashboard. Use when the user says things like: 'add a todo', 'what's on my list', 'what's overdue', 'mark X done', 'what do I owe David', 'what am I waiting on'."
user_invocable: true
---

# Todos

You read and write the Open Loops dashboard, which is an artifact-backed list,
not a file in this repo.

## Before anything else

Read `todos/ARTIFACT.md` for the artifact URL. Load the `ArtifactData` tool with
`ToolSearch(query: "select:ArtifactData", max_results: 1)`.

Never create a new artifact. The list lives in one artifact's db, and publishing
a second one splits the data with no way to merge it back.

## Collections

- `items/` is the live list.
- `inbox/` is proposed items awaiting the user's decision.
- `meta/sync` holds the Granola watermark. Do not write it here; only the sweep does.

Field shapes are in `docs/superpowers/specs/2026-09-16-todo-dashboard-design.md`.

## What to do

### Listing

Read `items/` with `action: "list"`. Filter and sort in your head, then answer in
prose, shortest useful form. Lead with what is overdue. Say the count before the
detail. Do not paste the whole list when the user asked a narrow question.

"What do I owe David" means `source.person == "David"` and `owner == "me"`.
"What am I waiting on" means `owner != "me"`.

Horizon buckets follow `todos/logic.js`: overdue is `due` before today, then
today, this week (to Sunday), this month, then someday. An undated P0 counts as
today.

### Adding

Write straight to `items/`, not `inbox/`. The user asking directly is the gate.

Set `source` to `{"kind": "manual", "person": <owner if not me, else null>, "date": <today>, "meetingTitle": null, "granolaId": null}`,
`done: false`, `doneAt: null`, `verify: false`, `order: <epoch ms>`, `createdAt: <today>`.

Before writing, list `items/` and check the new wording against the open ones,
lowercased and stripped of punctuation. If it matches, say so and ask whether to
add it anyway rather than creating a near-duplicate.

Infer priority from what the user said: a date inside a week is P0, a date
further out is P1, no date is P2. State the priority you chose so they can
correct it.

### Closing

Set `done: true` and `doneAt` to the current ISO timestamp. Do not delete. The
done rows are the record of what was cleared.

### Accepting from the inbox

Same transform the page performs: copy every field except `why` and `proposedAt`,
add `done: false`, `doneAt: null`, `order: <epoch ms>`, `createdAt: <the
proposedAt date>`. Write to `items/`, then delete the `inbox/` document.

## Principles

- One write at a time per document. Await each before the next.
- Pin writes with `if_version` for any document you read first.
- Report counts honestly. If a write failed, say which one.
- The dashboard is open in the user's browser and updates live. Tell them to look
  there rather than re-listing everything you just wrote.
