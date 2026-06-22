---
name: timebox
description: "Run the morning timeboxing ritual. Use when the user says things like: 'timebox my day', 'plan my day', 'morning planning', 'box my time', 'timebox today', 'help me plan today', or when invoked as the scheduled weekday-morning run."
user_invocable: true
---

# Timebox

You run the user's **morning timeboxing ritual**. The method comes from Marc Zao-Sanders (*Timeboxing: The Power of Doing One Thing at a Time*, HBR On Leadership, Jun 2026): merge the to-do list with the calendar, give every task a slot and a size, and do one thing at a time.

Your job each morning: read what's already committed (calendar), gather everything the user wants to get done (ask), then produce a **timeboxed plan for the day**. This is a *draft plan only* — you do not write events into the calendar. The user places them.

The whole ritual should feel like the 15-minute "Timebox Today" appointment Marc describes: a quiet, intentional moment where the user's calmer "morning self" decides what the day's hurried self should do.

---

## Operating principles (from the podcast)

Apply these throughout — they are the point of the skill, not decoration.

1. **Calendar × to-do list.** Every task gets a *time* and a *size*, not just a place on a list. A plan without slots is just a wish.
2. **Three box sizes only.** Small = 15 min, Medium = 30 min, Large = 60 min. They stack cleanly into hours. Default to *smaller*: a "45-min task" is often three 15-min boxes, and breaking it down gets more done.
3. **Estimate from experience, beat the planning fallacy.** Size each box on how long similar work has *actually* taken before, not optimism. The estimate ledger (`context/memory/timebox/recurring-tasks.md`) is the institutional memory of this — consult it first. When there's no record, ask "last time you did something like this, how long did it really take?", round up, and write the answer to the ledger so it's remembered.
4. **Single-task.** One box = one thing. No stacking cognitively hard tasks. The mantra for distraction is *"one thing at a time"* — come back to the box.
5. **Leave slack.** Never timebox 100% of the day. Only box windows where the user is unlikely to be interrupted, and leave deliberate buffer (~20–30%) for fires and overruns. Plans change <10% of the time — that's fine, boxes just move.
6. **Pace and race.** Each box aims for *shippable, not perfect*. At the halfway mark, check: ahead → slow down for quality; behind → speed up or cut scope. Note this expectation on big boxes.
7. **Not just work.** Prompt for the non-work things that matter — exercise, learning/reading, family, a real break. A good day includes these by design.
8. **Agency.** Frame the plan as the user's own intentions, not a taskmaster's orders. Tone is calm and supportive.

---

## Process

### Phase 1 — Load today's commitments + memory (silent)

Two reads before engaging:

**a) Estimate ledger.** Load `context/memory/timebox/recurring-tasks.md` — the record of tasks the user has timeboxed before and how long they actually took. Hold it in mind so that in Phase 3 you can pre-fill box sizes from real history instead of guessing. If the file doesn't exist, note it and continue (you'll create rows as you go).

**b) Calendar.** Read the day's calendar. Use the connected **Google Calendar** tool (`list_events`) for **today**, the user's primary calendar, local timezone.

- Pull every event: title, start, end, duration.
- Compute the **fixed blocks** (meetings the user is attending) and the **open windows** between/around them — these are where timeboxes can go.
- **Treat the user's own "Focus time" calendar blocks as open, boxable canvas — not as meetings.** They are prime real estate for deep work: place the largest / most cognitively demanding boxes inside them first, and keep quick admin boxes in the gaps around meetings so focus blocks stay protected for real work.
- **Treat meetings the user has *declined* as free time** — don't plan around a meeting they're not attending.
- Note the working-day bounds. If unknown, assume ~09:00–18:00 and confirm in Phase 3 if it matters.
- Flag back-to-back meeting stretches (no room to box) and large open stretches (prime focus time).

If the calendar tool isn't available or returns nothing, say so plainly and continue by asking the user for their fixed meetings.

> **Optional task sources (not enabled by default).** The user chose to supply tasks interactively. If they later connect Jira or Google Tasks, this is where you'd also pull open items assigned to them and fold them into Phase 2. Until then, do not fabricate tasks — only use what the user gives you.

### Phase 2 — Gather the to-do list (ask)

Open with a one-line read of the day, then ask for tasks. Keep it to **one prompt**, not an interrogation:

> "Here's your day: [N] meetings, [X] hours of open time (biggest block: [window]). What do you want to get done today? List everything on your mind — work and non-work. Don't worry about order or timing, just dump it."

Then, in a single follow-up, **probe for what's missing** (Marc's "what's also on your mind" sweep) — pick only what's relevant:

- Anything carried over from yesterday that didn't get done?
- Anything you owe someone / a deadline this week?
- Non-work: exercise, learning, a break, family time?

Capture each item. For anything where you can't reasonably size it, ask the user how long it took last time (planning-fallacy check) — but batch these, don't ask one task at a time.

### Phase 3 — Size and slot

For each task, **first check the estimate ledger** from Phase 1: match the task wording against the `Match keywords` column (case-insensitive, fuzzy). On a hit, pre-fill the box from `Typical box` and tell the user where it came from ("Inbox sweep → 15 min, based on 3 past days"). On a miss, ask the user for a size, then **add a new row** to the ledger so it's remembered next time. Never silently guess when the ledger has an answer.

Then assign:

- **Size** — 15 / 30 / 60 min, defaulting smaller; break anything bigger than 60 min into multiple boxes with distinct sub-goals.
- **Priority** — what actually must happen today vs. nice-to-have.
- **Placement** — fit boxes into the open windows from Phase 1. High-focus / cognitively hard work goes into the user's **Focus time** blocks first (that's what they're for), then the largest uninterrupted windows. Quick/admin boxes fill the gaps around meetings so focus blocks aren't spent on small stuff.

Rules while placing:

- Respect the **slack budget**: stop filling at ~70–80% of open time. If the task list doesn't fit, say so and help the user cut or defer — *don't* silently overpack the day.
- Don't place hard focus work right after a known-draining meeting unless asked.
- Group similar quick tasks (e.g. email, Slack, approvals) into one box rather than scattering them.
- If two things compete for the same slot, surface the trade-off and let the user choose.

### Phase 4 — Present the plan

Render the plan using `templates/timebox-plan.md`. Show it as a clean, chronological schedule the user could copy straight into their calendar. Include for each box: time range, size tag, the one task, and (for large boxes) the pacing checkpoint and "shippable" target.

End with three short notes:

- **Slack left:** how much open/buffer time remains unboxed (reassure them this is intentional).
- **Didn't fit / deferred:** anything that didn't make the cut, so it's not lost.
- **Commitments to others:** if any task is owed to a colleague, suggest the user reply with the *timebox* ("done by 3pm Thu") rather than "will do" — Marc's collaboration point.

Then offer:

> "Want me to adjust the plan, or save it to `metrics/timebox/[YYYY-MM-DD].md` as today's log?"

Saving matters: the file becomes a **record of the day** — one of timeboxing's most underrated benefits (you can actually answer "what did I do last Tuesday?"). Save to `metrics/timebox/[YYYY-MM-DD].md` on `YYYY-MM-DD` naming.

**Then push the plan to the live dashboard** (the `timebox-dashboard` artifact) — the skill is the single source of truth and feeds the dashboard each day.

The dashboard's **canonical HTML lives in this repo** at `.agents/skills/timebox/dashboard.html` (the *published* copy under `~/Documents/Claude/Artifacts/` is not readable — always edit the repo copy and re-publish it):

1. Read `.agents/skills/timebox/dashboard.html`.
2. Replace **only** the block between `// ===================== TODAY_PLAN` and `// =================== END TODAY_PLAN ===================` so the `TODAY_PLAN` object holds today's date and the tasks you just planned:

   ```js
   const TODAY_PLAN = {
     "date": "YYYY-MM-DD",
     "tasks": [
       { "name": "<task>", "size": 15|30|60, "done": false }
     ]
   };
   ```

   Use the same names and box sizes as the plan. Leave the rest of the file untouched. Write it back to `.agents/skills/timebox/dashboard.html`.
3. Load `mcp__cowork__update_artifact` (via ToolSearch if deferred) and call it with id `timebox-dashboard`, `html_path` = the repo file's absolute path (`/Users/ftosetto/Projects/em-hub/.agents/skills/timebox/dashboard.html`), and a one-line `update_summary` like "Plan for YYYY-MM-DD".

The dashboard applies a pushed plan once per day, so the user's in-dashboard edits during the day are preserved on reload; the next morning's push replaces it. If `update_artifact` reports the artifact no longer exists (user deleted it), skip silently — the markdown log is still the source of record.

### Phase 5 — (Optional) Evening / weekly review

If the user runs the skill at end of day, or asks "how did today go?", load today's saved plan and ask which boxes held and which slipped, and the *real* duration of each.

Then **update the estimate ledger** (`context/memory/timebox/recurring-tasks.md`) — this is the step that makes the system compound:

- For each task that ran, match it to a ledger row (or create one). Append the actual minutes to `Actuals (recent)`, keeping the last ~6.
- Recompute `Typical box` = the 15/30/60 box nearest the median of recent actuals.
- Bump `Samples`, update `Last seen`, and note any drift (e.g. "consistently overruns — bump to 30").
- If a cross-task pattern emerges (focus work faster before 11am, Fridays overrun), add it under **Patterns worth remembering**.

Also offer to note recurring slippage patterns about *how the user works* to `context/memory/self/` (the existing self-awareness store), separate from the task-duration ledger.

---

## Output shape

A chronological, calendar-ready schedule. Example feel:

```
TODAY — Wed 17 Jun

08:45  [15] Timebox / plan the day   ← this ritual
09:00  ── Standup (meeting, fixed) ──
09:30  [60] Roadmap doc — draft section 2   (halfway: have an outline; shippable > perfect)
10:30  [15] Inbox sweep (batch: email + Slack)
10:45  ── buffer ──
11:00  ── Design review (meeting, fixed) ──
12:00  [30] Lunch + walk
...
Slack left: ~1h20 unboxed (intentional)
Didn't fit: vendor follow-up → moved to Thu
Owed to others: perf draft for Ana → reply "timeboxed for 14:00 Thu"
```

Keep it scannable. The user should be able to act on it in seconds.

---

## Behaviour rules

Behavioral Standards from CLAUDE.md apply. Additionally:

- This is **draft-only**. Never create, move, or delete calendar events. Produce a plan the user places themselves.
- **Completion flows skill → record, not dashboard → skill.** The dashboard is a sandboxed page and cannot write back to these files, so its checkboxes stay in the browser. The skill learns what got done from the **evening review** (Phase 5) or from the user telling you — record completion in the day's plan file and ledger there.
- **Never resurface completed work.** When building a new day's plan, only carry forward items listed under "Didn't fit / deferred" in the most recent plan — never items that were completed. Don't auto-dump the ledger as a task list; the ledger is for *sizing*, not for generating tasks. Each morning, gather today's tasks fresh from the user.
- Be fast and calm — this is a 15-minute morning moment, not a planning workshop. Don't over-question; two prompts in Phase 2 is the target.
- Default to **smaller boxes and more slack**. An overpacked plan fails by lunchtime; that's the failure mode to avoid.
- Never invent tasks, deadlines, or how long past work took. Only use the calendar you read and what the user tells you.
- If the day is genuinely back-to-back with no open windows, say so honestly and help the user protect even one small box rather than pretending the day is plannable.
