# Timebox Memory — Recurring Task Estimates

Living ledger of tasks I've timeboxed before and how long they actually take. The `/timebox` skill reads this when **sizing** the day (pre-fills the box from `Typical box`) and updates it after the **end-of-day review** with real durations. The more days run, the better the estimates — this is the antidote to the planning fallacy.

This is a **ledger, not narrative memory** — edit rows in place, don't append dated entries.

---

## How matching works

When sizing a task, the skill matches the user's wording against `Match keywords` (case-insensitive, fuzzy). On a hit, it pre-fills the typical box and shows the confidence (sample count). On a miss, it asks for an estimate, then **adds a new row** so it's remembered next time.

After the review, for each task that ran:
- Append the actual minutes to `Actuals (recent)` (keep last ~6).
- Recompute `Typical box` = the box size nearest the median of recent actuals, snapped to 15/30/60.
- Bump `Samples`. Update `Last seen`.
- If actuals are drifting (e.g. consistently over the box), note it in `Notes`.

Box sizes are always one of: **15**, **30**, **60** min (break larger work into stacked boxes).

---

## Ledger

| Task | Match keywords | Typical box | Actuals (recent, min) | Samples | Last seen | Notes |
| ---- | -------------- | ----------- | --------------------- | ------- | --------- | ----- |
| Understand A/B test w/ AI Engineer | a/b test, ab test, understand test, ai engineer | 30 | — | 0 | 2026-06-17 | Completed 2026-06-17 (duration not logged). Estimate only — needs the engineer available |
| Create Jira tickets — repo transfer | jira tickets, repo transfer, transfer backend, create tickets | 30 | — | 0 | 2026-06-17 | Completed 2026-06-17 (duration not logged). Scales with number of repos |
| Request device from IT | request device, android device, hardware request | 15 | — | 0 | 2026-06-17 | Completed 2026-06-17 (duration not logged). Fire-and-forget; response is async |
| Vertex / API query | vertex, api query, google api question | 15 | — | 0 | 2026-06-17 | Completed 2026-06-17 (duration not logged). Sending the question is 15; researching is separate |
| Create documentation | documentation, write docs, document, faceai filters | 60 | — | 0 | 2026-06-17 | Completed 2026-06-17 (duration not logged). Deep work; stack boxes if past 60 |
| Tech debt spreadsheet (per app) | tech debt, tech debt spreadsheet, chatultra, pdf editor | 30 | — | 0 | 2026-06-18 | Estimate only — per-app audit + populate sheet. Two ran today (ChatUltra, PDF editor) |
| M&A pipelines update | m&a, pipelines update, portfolio tracker, m&a pipeline | 30 | — | 0 | 2026-06-18 | Estimate only — refresh the pipeline/portfolio tracker |
| Review epic (FaceAI) | review epic, faceai epic, review new epic, new epic | 30 | — | 0 | 2026-06-22 | Estimate only — scope/tickets/acceptance review of an epic |
| Review backend task | review backend task, backend task, review task, review faceai backend | 15 | — | 0 | 2026-06-22 | Estimate only — single-ticket backend review |
| PDF editor PROD setup | pdf editor prod, prod setup, production setup, pdf editor deploy | 60 | — | 0 | 2026-06-22 | Estimate only — deep/infra production deployment setup |
| Prepare 1:1 (any report) | prepare 1:1, prep 1:1, 1:1 prep, prepare weekly, prep meeting | 15 | — | 0 | 2026-06-29 | User estimate 15 min. Quick review of notes + talking points |
| Procurement tickets | procurement tickets, procurement, removing studios, m&a removal tickets | 30 | — | 0 | 2026-06-29 | User est. 20 min → boxed 30 (similar to Jira tickets in ledger). Review after actuals |
| Strategy / new structure doc | strategy, new launches, launches structure, new structure, strategic doc | 60 | — | 0 | 2026-06-29 | User est. 45 min → boxed 60 (deep strategic work, no prior record). Shippable = clear direction |

> First real rows seeded on 2026-06-17 (estimates, no actuals yet). Tonight's review will append real durations and recompute the typical box.

---

## Patterns worth remembering

Free-text space for cross-task observations the review surfaces (e.g. "focus work before 11am runs ~20% faster", "Friday afternoons consistently overrun"). The skill can read these to place boxes better, not just size them.

-
