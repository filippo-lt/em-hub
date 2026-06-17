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
| Understand A/B test w/ AI Engineer | a/b test, ab test, understand test, ai engineer | 30 | — | 0 | 2026-06-17 | Estimate only — needs the engineer available; confirm before boxing |
| Create Jira tickets — repo transfer | jira tickets, repo transfer, transfer backend, create tickets | 30 | — | 0 | 2026-06-17 | Estimate only — scales with number of repos; may become 2×30 |
| Request device from IT | request device, android device, hardware request | 15 | — | 0 | 2026-06-17 | Estimate only — fire-and-forget; response is async |
| Vertex / API query | vertex, api query, google api question | 15 | — | 0 | 2026-06-17 | Estimate only — sending the question is 15; researching the answer is separate |
| Create documentation | documentation, write docs, document, faceai filters | 60 | — | 0 | 2026-06-17 | Estimate only — deep work; break into stacked boxes if it runs past 60 |

> First real rows seeded on 2026-06-17 (estimates, no actuals yet). Tonight's review will append real durations and recompute the typical box.

---

## Patterns worth remembering

Free-text space for cross-task observations the review surfaces (e.g. "focus work before 11am runs ~20% faster", "Friday afternoons consistently overrun"). The skill can read these to place boxes better, not just size them.

-
