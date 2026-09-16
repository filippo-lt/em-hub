# Todo dashboard implementation plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** A live open-loops page backed by the artifact `db`, fed by hand, by `/1on1-lifecycle`, and by a scheduled sweep of unprocessed Granola meetings.

**Architecture:** Pure logic lives in `todos/logic.js`, a plain script that attaches `globalThis.TodoLogic`, so `node --test` can exercise it and the browser can load it as a published supporting file. `todos/dashboard.html` holds markup, styling and db wiring only. The artifact `db` capability stores `items/`, `inbox/` and `meta/sync`. Writers other than the page reach the store through the `ArtifactData` tool.

**Tech Stack:** Vanilla HTML, CSS and JS. No framework, no bundler. `node --test` for the logic module. Artifact `db` capability, runtime contract 0.2.49. Google Fonts for type.

**Spec:** `docs/superpowers/specs/2026-09-16-todo-dashboard-design.md`

## Global constraints

- Artifact page contract: no `<!doctype>`, `<html>`, `<head>` or `<body>` tags in the file. Start with `<title>` then `<style>`.
- Title is exactly `Open Loops`. Keep it stable across every republish.
- Favicon `🧾` on the first publish only. Omit it on every later publish.
- Declare `capabilities: {db: {}}` on the first publish. Omit `capabilities` on later publishes so the stored declaration carries forward.
- `await claude.use("db")` resolves `null` when db is unavailable. Branch on `null`. Never read `window.claude.db`.
- Subscribe once per collection, never from render code.
- One write at a time per document. Await each write before the next to the same document.
- Every colour is a token declared on bare `:root`, redefined under `@media (prefers-color-scheme: dark)` guarded by `:root:not([data-theme="light"])`, and again under `:root[data-theme="dark"]`. `body` sets an explicit token background.
- Phone width 400px must work. 16px side gutter, no horizontal page scroll.
- Priority values are exactly `P0`, `P1`, `P2`. Owner `"me"` means Filippo. Dates are `YYYY-MM-DD` strings compared lexically.
- Git author on every commit: `filippo-lt <filippo.tosetto@leadtech.com>`.

## Design tokens

Ledger identity, not a card grid. Neutrals carry a slight green bias like accounting paper. The accent is a deep slate ink. Semantic colours are separate from the accent.

Light: `--paper #F2F4F1`, `--card #FFFFFF`, `--ink #1A1F1C`, `--muted #5F6B63`, `--rule #D8DED8`, `--accent #2F4858`, `--overdue #A3402B`, `--waiting #8A6410`, `--ok #2F6B4F`.

Dark: `--paper #14181A`, `--card #1C2225`, `--ink #E4E9E4`, `--muted #94A199`, `--rule #2C3438`, `--accent #7FB0C4`, `--overdue #E08A72`, `--waiting #D4A544`, `--ok #6FBF95`.

Type: `Archivo` 600/700 for headings, `Source Sans 3` 400/600 for body, `JetBrains Mono` 500 for labels, dates and counts.

## File structure

| File | Responsibility |
| --- | --- |
| `todos/logic.js` | Pure functions. No DOM, no db, no clock reads. Every function takes `today` explicitly. |
| `todos/logic.test.mjs` | `node --test` suite for `logic.js`. |
| `todos/dashboard.html` | Markup, styling, db subscriptions, event handlers. Calls `TodoLogic` for every derived value. |
| `todos/ARTIFACT.md` | Records the published artifact URL and the publish arguments, so later sessions redeploy instead of creating a second artifact. |
| `.agents/agents/todo-sweep-agent.md` | Extraction prompt shared by the manual run and the cloud routine. |
| `.agents/skills/todos/SKILL.md` | `/todos` for adding and querying from the terminal. |
| `.claude/skills/todos` | Symlink into `.agents/skills/todos`. |
| `.agents/skills/1on1-lifecycle/SKILL.md` | Gains step 4.5. |
| `CLAUDE.md` | Routing table row, folder structure entry. |

---

### Task 1: Pure logic module

**Files:**
- Create: `todos/logic.js`
- Test: `todos/logic.test.mjs`

**Interfaces:**
- Consumes: nothing.
- Produces: `globalThis.TodoLogic` with `HORIZONS: string[]`, `HORIZON_LABELS: Record<string,string>`, `PRIORITY_RANK: Record<string,number>`, `nextPriority(p: string): string`, `endOfWeek(today: string): string`, `endOfMonth(today: string): string`, `horizonOf(item: object, today: string): string`, `ageDays(item: object, today: string): number`, `normaliseText(s: string): string`, `dedupeKey(item: object): string`, `isDuplicate(candidate: object, existing: object[]): boolean`, `groupKeyOf(item: object, mode: string, today?: string): string`, `groupsOf(items: object[], mode: string, today: string): Array<{key: string, label: string, items: object[], open: number}>`, `sortItems(items: object[]): object[]`, `counts(items: object[], inbox: object[], today: string): {overdue: number, week: number, waiting: number, pending: number}`.

- [ ] **Step 1: Write the failing test**

Create `todos/logic.test.mjs`:

```js
import { test } from "node:test";
import assert from "node:assert/strict";
import "./logic.js";

const L = globalThis.TodoLogic;

// 2026-09-16 is a Wednesday. ISO week ends Sunday 2026-09-20.
const TODAY = "2026-09-16";

const item = (over) => ({
  text: "Send the metrics sheet",
  project: "M&A",
  owner: "me",
  priority: "P1",
  due: null,
  source: { kind: "1on1", person: "David", date: "2026-09-15", meetingTitle: "David 1:1", granolaId: "g1" },
  done: false,
  createdAt: "2026-09-15",
  order: 1,
  ...over,
});

test("endOfWeek returns the Sunday of the current ISO week", () => {
  assert.equal(L.endOfWeek("2026-09-16"), "2026-09-20");
  assert.equal(L.endOfWeek("2026-09-20"), "2026-09-20", "Sunday is its own week end");
  assert.equal(L.endOfWeek("2026-09-21"), "2026-09-27", "Monday starts a new week");
});

test("endOfMonth handles month lengths and leap years", () => {
  assert.equal(L.endOfMonth("2026-09-16"), "2026-09-30");
  assert.equal(L.endOfMonth("2026-02-01"), "2026-02-28");
  assert.equal(L.endOfMonth("2028-02-01"), "2028-02-29");
  assert.equal(L.endOfMonth("2026-12-31"), "2026-12-31");
});

test("horizonOf buckets by due date", () => {
  assert.equal(L.horizonOf(item({ due: "2026-09-15" }), TODAY), "overdue");
  assert.equal(L.horizonOf(item({ due: "2026-09-16" }), TODAY), "today");
  assert.equal(L.horizonOf(item({ due: "2026-09-20" }), TODAY), "week");
  assert.equal(L.horizonOf(item({ due: "2026-09-30" }), TODAY), "month");
  assert.equal(L.horizonOf(item({ due: "2026-10-01" }), TODAY), "someday");
});

test("an undated P0 lands in today, not someday", () => {
  assert.equal(L.horizonOf(item({ due: null, priority: "P0" }), TODAY), "today");
  assert.equal(L.horizonOf(item({ due: null, priority: "P1" }), TODAY), "someday");
  assert.equal(L.horizonOf(item({ due: null, priority: "P2" }), TODAY), "someday");
});

test("a dated P0 keeps its real bucket", () => {
  assert.equal(L.horizonOf(item({ due: "2026-10-30", priority: "P0" }), TODAY), "someday");
});

test("ageDays counts days since createdAt", () => {
  assert.equal(L.ageDays(item({ createdAt: "2026-09-16" }), TODAY), 0);
  assert.equal(L.ageDays(item({ createdAt: "2026-08-17" }), TODAY), 30);
  assert.equal(L.ageDays(item({ createdAt: null }), TODAY), 0, "missing createdAt is not an error");
});

test("normaliseText strips case, punctuation and repeated space", () => {
  assert.equal(L.normaliseText("  Send   the METRICS sheet! "), "send the metrics sheet");
  assert.equal(L.normaliseText("Andrey's SE e-mail"), "andrey s se e mail");
  assert.equal(L.normaliseText(null), "");
});

test("dedupeKey joins granolaId and normalised text", () => {
  assert.equal(L.dedupeKey(item()), "g1|send the metrics sheet");
  assert.equal(L.dedupeKey(item({ source: { kind: "manual" } })), "|send the metrics sheet");
});

test("isDuplicate matches same meeting and same wording", () => {
  const existing = [item()];
  assert.equal(L.isDuplicate(item({ text: "send the METRICS sheet" }), existing), true);
  assert.equal(L.isDuplicate(item({ text: "Something else entirely" }), existing), false);
});

test("isDuplicate matches wording alone across different meetings", () => {
  const existing = [item({ source: { kind: "1on1", person: "David", granolaId: "g1" } })];
  const fromLaterMeeting = item({ source: { kind: "1on1", person: "David", granolaId: "g2" } });
  assert.equal(L.isDuplicate(fromLaterMeeting, existing), true,
    "the same commitment re-raised in a later meeting is not a new item");
});

test("isDuplicate ignores items already done", () => {
  const existing = [item({ done: true })];
  assert.equal(L.isDuplicate(item(), existing), false,
    "a finished loop can legitimately reopen");
});

test("groupKeyOf keys person on who the loop is with, not the owner", () => {
  const owed = item({ owner: "me", source: { kind: "1on1", person: "David" } });
  assert.equal(L.groupKeyOf(owed, "person"), "David");

  const owedToMe = item({ owner: "David", source: { kind: "1on1", person: "David" } });
  assert.equal(L.groupKeyOf(owedToMe, "person"), "David");
});

test("groupKeyOf falls back for manual items with no person", () => {
  assert.equal(L.groupKeyOf(item({ owner: "Vlad", source: { kind: "manual" } }), "person"), "Vlad");
  assert.equal(L.groupKeyOf(item({ owner: "me", source: { kind: "manual" } }), "person"), "No person");
  assert.equal(L.groupKeyOf(item({ owner: "me", source: null }), "person"), "No person");
});

test("groupKeyOf handles project and horizon modes", () => {
  assert.equal(L.groupKeyOf(item({ project: "TruthSeeker" }), "project"), "TruthSeeker");
  assert.equal(L.groupKeyOf(item({ project: "" }), "project"), "No project");
  assert.equal(L.groupKeyOf(item({ due: "2026-09-15" }), "horizon", TODAY), "overdue");
});

test("sortItems puts open before done, then priority, then due, then order", () => {
  const rows = [
    item({ text: "d", done: true, priority: "P0" }),
    item({ text: "c", priority: "P2" }),
    item({ text: "a", priority: "P0", due: "2026-09-01" }),
    item({ text: "b", priority: "P0", due: null }),
  ];
  assert.deepEqual(L.sortItems(rows).map((r) => r.text), ["a", "b", "c", "d"]);
});

test("groupsOf returns horizon groups in fixed order and hides empties", () => {
  const rows = [
    item({ text: "late", due: "2026-09-10" }),
    item({ text: "later", due: "2026-09-29" }),
  ];
  const groups = L.groupsOf(rows, "horizon", TODAY);
  assert.deepEqual(groups.map((g) => g.key), ["overdue", "month"]);
  assert.equal(groups[0].label, "Overdue");
  assert.equal(groups[0].items.length, 1);
});

test("groupsOf sorts person and project groups by open count descending", () => {
  const rows = [
    item({ text: "1", source: { person: "Vlad" } }),
    item({ text: "2", source: { person: "David" } }),
    item({ text: "3", source: { person: "David" } }),
  ];
  assert.deepEqual(L.groupsOf(rows, "person", TODAY).map((g) => g.key), ["David", "Vlad"]);
});

test("counts summarises the strip", () => {
  const rows = [
    item({ due: "2026-09-10" }),
    item({ due: "2026-09-18" }),
    item({ owner: "David" }),
    item({ done: true, due: "2026-09-10" }),
  ];
  const c = L.counts(rows, [{ text: "proposed" }], TODAY);
  assert.deepEqual(c, { overdue: 1, week: 1, waiting: 1, pending: 1 });
});

test("nextPriority cycles P0 to P1 to P2 and back", () => {
  assert.equal(L.nextPriority("P0"), "P1");
  assert.equal(L.nextPriority("P1"), "P2");
  assert.equal(L.nextPriority("P2"), "P0");
  assert.equal(L.nextPriority("nonsense"), "P1");
});
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `cd /Users/ftosetto/Projects/em-hub && node --test todos/`
Expected: FAIL. The run cannot resolve `./logic.js`, so every test errors before asserting.

- [ ] **Step 3: Write the implementation**

Create `todos/logic.js`:

```js
/* Pure helpers for the Open Loops dashboard.
   No DOM, no db, no clock reads: every function that needs the date takes
   `today` as a "YYYY-MM-DD" string so it can be tested and so the page can
   recompute at midnight without reloading. */
(function (root) {
  const HORIZONS = ["overdue", "today", "week", "month", "someday"];

  const HORIZON_LABELS = {
    overdue: "Overdue",
    today: "Today",
    week: "This week",
    month: "This month",
    someday: "Someday",
  };

  const PRIORITY_RANK = { P0: 0, P1: 1, P2: 2 };
  const PRIORITY_NEXT = { P0: "P1", P1: "P2", P2: "P0" };

  function nextPriority(p) {
    return PRIORITY_NEXT[p] || "P1";
  }

  function utc(day) {
    return new Date(day + "T00:00:00Z");
  }

  function iso(d) {
    return d.toISOString().slice(0, 10);
  }

  /* ISO weeks start Monday, so the week ends on the following Sunday. */
  function endOfWeek(today) {
    const d = utc(today);
    const dow = d.getUTCDay() || 7;
    d.setUTCDate(d.getUTCDate() + (7 - dow));
    return iso(d);
  }

  /* Day 0 of the next month is the last day of this one. */
  function endOfMonth(today) {
    const d = utc(today);
    return iso(new Date(Date.UTC(d.getUTCFullYear(), d.getUTCMonth() + 1, 0)));
  }

  /* An undated P0 belongs in today. Nobody dated it, but P0 already says
     it is urgent, and burying it in Someday is how these go quiet. */
  function horizonOf(item, today) {
    if (!item.due) return item.priority === "P0" ? "today" : "someday";
    if (item.due < today) return "overdue";
    if (item.due === today) return "today";
    if (item.due <= endOfWeek(today)) return "week";
    if (item.due <= endOfMonth(today)) return "month";
    return "someday";
  }

  function ageDays(item, today) {
    if (!item.createdAt) return 0;
    const ms = utc(today).getTime() - utc(item.createdAt).getTime();
    return Math.max(0, Math.round(ms / 86400000));
  }

  function normaliseText(s) {
    return String(s == null ? "" : s)
      .toLowerCase()
      .replace(/[^\p{L}\p{N}\s]/gu, " ")
      .replace(/\s+/g, " ")
      .trim();
  }

  function dedupeKey(item) {
    const gid = (item.source && item.source.granolaId) || "";
    return gid + "|" + normaliseText(item.text);
  }

  /* Two ways to be a duplicate: the same line from the same meeting, or the
     same wording anywhere. The second one matters more. A commitment raised
     in five consecutive 1:1s is one open loop, not five. Done items never
     block a new one, because a closed loop can legitimately reopen. */
  function isDuplicate(candidate, existing) {
    const key = dedupeKey(candidate);
    const words = normaliseText(candidate.text);
    if (!words) return false;
    return (existing || []).some(
      (e) => !e.done && (dedupeKey(e) === key || normaliseText(e.text) === words),
    );
  }

  /* Person grouping keys on who the loop is WITH, which is not the owner.
     Something Filippo owes David has owner "me" and person "David", and it
     belongs under David, because the grouping exists to prepare a 1:1. */
  function groupKeyOf(item, mode, today) {
    if (mode === "project") return item.project || "No project";
    if (mode === "person") {
      const src = item.source || {};
      if (src.person) return src.person;
      if (item.owner && item.owner !== "me") return item.owner;
      return "No person";
    }
    return horizonOf(item, today);
  }

  function sortItems(items) {
    return items.slice().sort(
      (a, b) =>
        Number(!!a.done) - Number(!!b.done) ||
        (PRIORITY_RANK[a.priority] ?? 9) - (PRIORITY_RANK[b.priority] ?? 9) ||
        String(a.due || "9999-99-99").localeCompare(String(b.due || "9999-99-99")) ||
        (a.order || 0) - (b.order || 0),
    );
  }

  function groupsOf(items, mode, today) {
    const bucket = new Map();
    items.forEach((i) => {
      const key = groupKeyOf(i, mode, today);
      if (!bucket.has(key)) bucket.set(key, []);
      bucket.get(key).push(i);
    });

    const made = [...bucket.entries()].map(([key, rows]) => ({
      key,
      label: mode === "horizon" ? HORIZON_LABELS[key] : key,
      items: sortItems(rows),
      open: rows.filter((r) => !r.done).length,
    }));

    if (mode === "horizon") {
      return made.sort((a, b) => HORIZONS.indexOf(a.key) - HORIZONS.indexOf(b.key));
    }
    return made.sort((a, b) => b.open - a.open || a.key.localeCompare(b.key));
  }

  function counts(items, inbox, today) {
    const open = items.filter((i) => !i.done);
    const inWeek = (i) => {
      const h = horizonOf(i, today);
      return h === "today" || h === "week";
    };
    return {
      overdue: open.filter((i) => horizonOf(i, today) === "overdue").length,
      week: open.filter(inWeek).length,
      waiting: open.filter((i) => i.owner && i.owner !== "me").length,
      pending: (inbox || []).length,
    };
  }

  root.TodoLogic = {
    HORIZONS,
    HORIZON_LABELS,
    PRIORITY_RANK,
    nextPriority,
    endOfWeek,
    endOfMonth,
    horizonOf,
    ageDays,
    normaliseText,
    dedupeKey,
    isDuplicate,
    groupKeyOf,
    sortItems,
    groupsOf,
    counts,
  };
})(globalThis);
```

- [ ] **Step 4: Run the test to verify it passes**

Run: `cd /Users/ftosetto/Projects/em-hub && node --test todos/`
Expected: PASS, 19 tests.

If `isDuplicate` fails the "across different meetings" case, do not weaken the test. The wording match is the point: the Sept 15 David analysis shows the August metrics sheet raised in five consecutive meetings, and five inbox rows for one loop would make the dashboard worse than the notes.

- [ ] **Step 5: Commit**

```bash
cd /Users/ftosetto/Projects/em-hub
git add todos/logic.js todos/logic.test.mjs
git commit --author="filippo-lt <filippo.tosetto@leadtech.com>" -m "Add todo dashboard logic module

Horizon bucketing, dedupe and grouping as pure functions so they can be
tested with node --test and reused by the page."
```

---

### Task 2: Dashboard page, read path

**Files:**
- Create: `todos/dashboard.html`
- Create: `todos/ARTIFACT.md`

**Interfaces:**
- Consumes: `globalThis.TodoLogic` from Task 1, loaded via `<script src="logic.js">` before the inline script.
- Produces: a published artifact URL recorded in `todos/ARTIFACT.md`; db document shapes `items/`, `inbox/`, `meta/sync` exactly as the spec defines them.

- [ ] **Step 1: Write the page**

Create `todos/dashboard.html`. The file starts at `<title>`, with no doctype or wrapper tags.

```html
<title>Open Loops</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700&family=JetBrains+Mono:wght@500&family=Source+Sans+3:wght@400;600&display=swap">
<style>
:root{
  --paper:#F2F4F1; --card:#FFFFFF; --ink:#1A1F1C; --muted:#5F6B63; --rule:#D8DED8;
  --accent:#2F4858; --on-accent:#FFFFFF;
  --overdue:#A3402B; --overdue-bg:#F7E9E5;
  --waiting:#8A6410; --waiting-bg:#F7F0DD;
  --ok:#2F6B4F; --ok-bg:#E6F0EA;
  --chip:#EAEEE9;
}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    --paper:#14181A; --card:#1C2225; --ink:#E4E9E4; --muted:#94A199; --rule:#2C3438;
    --accent:#7FB0C4; --on-accent:#10161A;
    --overdue:#E08A72; --overdue-bg:#341F1A;
    --waiting:#D4A544; --waiting-bg:#332A15;
    --ok:#6FBF95; --ok-bg:#16291F;
    --chip:#252D30;
  }
}
:root[data-theme="dark"]{
  --paper:#14181A; --card:#1C2225; --ink:#E4E9E4; --muted:#94A199; --rule:#2C3438;
  --accent:#7FB0C4; --on-accent:#10161A;
  --overdue:#E08A72; --overdue-bg:#341F1A;
  --waiting:#D4A544; --waiting-bg:#332A15;
  --ok:#6FBF95; --ok-bg:#16291F;
  --chip:#252D30;
}
*{box-sizing:border-box}
body{
  background:var(--paper); color:var(--ink);
  font:16px/1.5 "Source Sans 3",system-ui,-apple-system,sans-serif;
  padding-inline:16px; padding-block:24px 72px;
}
.wrap{max-width:1040px;margin:0 auto;display:flex;flex-direction:column;gap:24px}
h1,h2,h3{font-family:Archivo,system-ui,sans-serif;margin:0;text-wrap:balance}
h1{font-size:30px;font-weight:700;letter-spacing:-.015em}
h2{font-size:17px;font-weight:600}
h3{font-size:14px;font-weight:600}
.mono{font-family:"JetBrains Mono",ui-monospace,monospace;font-variant-numeric:tabular-nums}
.eyebrow{font:500 11px "JetBrains Mono",monospace;letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
a{color:var(--accent)}

header p{margin:6px 0 0;color:var(--muted);max-width:62ch}
#status{margin-top:10px;font:500 12px "JetBrains Mono",monospace;color:var(--muted)}
#status[data-bad="1"]{color:var(--overdue)}

/* The four figures are the point of the top of the page, so they get the
   only genuinely card-like treatment on it. */
.strip{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px}
.stat{background:var(--card);border:1px solid var(--rule);border-radius:8px;padding:12px 14px;display:flex;flex-direction:column;gap:1px}
.stat b{font:700 26px Archivo,sans-serif;font-variant-numeric:tabular-nums;line-height:1.15}
.stat span{color:var(--muted);font-size:13px}
.stat.is-overdue b{color:var(--overdue)}
.stat.is-waiting b{color:var(--waiting)}
.stat.is-pending b{color:var(--accent)}

.controls{display:flex;flex-wrap:wrap;gap:16px;align-items:center}
.group{display:flex;gap:6px;align-items:center;flex-wrap:wrap}
.group>.eyebrow{margin-right:2px}
.chip{
  font:500 13px "Source Sans 3",sans-serif;border:1px solid var(--rule);
  background:var(--card);color:var(--ink);border-radius:999px;padding:5px 12px;cursor:pointer;
}
.chip[aria-pressed="true"]{background:var(--accent);border-color:var(--accent);color:var(--on-accent)}
.chip:focus-visible,button:focus-visible,input:focus-visible,select:focus-visible{outline:2px solid var(--accent);outline-offset:2px}

/* The list is a ledger, not a stack of cards: hairlines between rows, one
   surface per group, a severity stripe only where it means something. */
.ledger{background:var(--card);border:1px solid var(--rule);border-radius:8px;overflow:hidden}
.grouphead{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap;padding:12px 14px 10px;border-bottom:1px solid var(--rule)}
.grouphead .count{color:var(--muted);font:500 12px "JetBrains Mono",monospace}
section.grp{display:flex;flex-direction:column;gap:0}
section.grp.sev .ledger{border-left:3px solid var(--overdue)}
.rows{list-style:none;margin:0;padding:0}
.row{display:grid;grid-template-columns:auto 40px 1fr auto;gap:12px;align-items:start;padding:11px 14px;border-top:1px solid var(--rule)}
.rows>.row:first-child{border-top:0}
.row input[type=checkbox]{width:17px;height:17px;margin-top:3px;accent-color:var(--accent);cursor:pointer}
.pri{font:500 11px "JetBrains Mono",monospace;text-align:center;border:0;border-radius:4px;padding:3px 0;margin-top:2px;cursor:pointer;width:100%}
.pri.P0{background:var(--overdue-bg);color:var(--overdue)}
.pri.P1{background:var(--waiting-bg);color:var(--waiting)}
.pri.P2{background:var(--chip);color:var(--muted)}
.txt{min-width:0;cursor:pointer}
.txt .t{font-weight:400}
.meta{color:var(--muted);font-size:13px;margin-top:3px;display:flex;flex-wrap:wrap;gap:4px 10px;align-items:center}
.tag{font:500 10px "JetBrains Mono",monospace;letter-spacing:.06em;text-transform:uppercase;background:var(--chip);border-radius:3px;padding:1px 6px;color:var(--muted)}
.tag.wait{background:var(--waiting-bg);color:var(--waiting)}
.tag.age{background:var(--overdue-bg);color:var(--overdue)}
.due{font:500 13px "JetBrains Mono",monospace;white-space:nowrap;color:var(--muted);text-align:right;font-variant-numeric:tabular-nums}
.due.late{color:var(--overdue)}
.row.done .t{text-decoration:line-through;color:var(--muted)}
.row.done{opacity:.6}

#empty{background:var(--card);border:1px dashed var(--rule);border-radius:8px;padding:28px 18px;text-align:center;color:var(--muted)}

@media (max-width:560px){
  .row{grid-template-columns:auto 40px 1fr}
  .due{grid-column:3;text-align:left;margin-top:2px}
}
</style>

<div class="wrap">
  <header>
    <div class="eyebrow" id="asof">Open loops</div>
    <h1>Open Loops</h1>
    <p>Everything you owe and everything you are owed, in one place. Items proposed from your meetings wait in the review band until you add them.</p>
    <div id="status">Connecting to your list…</div>
  </header>

  <div class="strip" id="strip"></div>

  <div class="controls">
    <div class="group" role="group" aria-label="Group by">
      <span class="eyebrow">Group</span>
      <button class="chip" data-mode="horizon" aria-pressed="true">When</button>
      <button class="chip" data-mode="person" aria-pressed="false">Person</button>
      <button class="chip" data-mode="project" aria-pressed="false">Project</button>
    </div>
    <div class="group" role="group" aria-label="Filter by owner">
      <span class="eyebrow">Show</span>
      <button class="chip" data-own="all" aria-pressed="true">All</button>
      <button class="chip" data-own="me" aria-pressed="false">Mine</button>
      <button class="chip" data-own="others" aria-pressed="false">Waiting on</button>
    </div>
    <div class="group" role="group" aria-label="Filter by priority">
      <span class="eyebrow">Priority</span>
      <button class="chip" data-pri="all" aria-pressed="true">All</button>
      <button class="chip" data-pri="P0" aria-pressed="false">P0</button>
      <button class="chip" data-pri="P1" aria-pressed="false">P0+P1</button>
    </div>
    <div class="group">
      <button class="chip" id="hidedone" aria-pressed="false">Hide done</button>
    </div>
  </div>

  <main id="board" style="display:flex;flex-direction:column;gap:20px"></main>
  <div id="empty" hidden>Nothing open. Add something below, or wait for the next sweep of your meetings.</div>
</div>

<script src="logic.js"></script>
<script>
const L = globalThis.TodoLogic;
const $ = (id) => document.getElementById(id);
const esc = (s) => String(s == null ? "" : s).replace(/[&<>"]/g, (c) => ({"&":"&amp;","<":"&lt;",">":"&gt;","\"":"&quot;"}[c]));

let db = null;
let items = [];
let inbox = [];
let view = { mode: "horizon", owner: "all", pri: "all", hideDone: false };

function today() {
  const d = new Date();
  return [d.getFullYear(), String(d.getMonth() + 1).padStart(2, "0"), String(d.getDate()).padStart(2, "0")].join("-");
}

function status(text, bad) {
  const el = $("status");
  el.textContent = text;
  if (bad) el.dataset.bad = "1"; else delete el.dataset.bad;
}

/* Errors say what happened and what to do about it. */
function reportWriteFailure(err) {
  const code = err && err.code;
  if (code === "quota_exceeded") return status("Your list is full. Delete some finished items to add more.", true);
  if (code === "revoked") return status("Your access to this list ended. Reload the page.", true);
  if (code === "invalid_argument") return status("That change was rejected. Reload and try again.", true);
  status("That change did not save. Try again.", true);
}

function visible() {
  return items.filter((i) => {
    if (view.hideDone && i.done) return false;
    if (view.owner === "me" && i.owner !== "me") return false;
    if (view.owner === "others" && i.owner === "me") return false;
    if (view.pri !== "all" && (L.PRIORITY_RANK[i.priority] ?? 9) > L.PRIORITY_RANK[view.pri]) return false;
    return true;
  });
}

function dueLabel(item, now) {
  if (!item.due) return "—";
  const d = new Date(item.due + "T00:00:00Z");
  const sameYear = item.due.slice(0, 4) === now.slice(0, 4);
  return d.toLocaleDateString("en-GB", { day: "numeric", month: "short", ...(sameYear ? {} : { year: "numeric" }), timeZone: "UTC" });
}

function rowHTML(item, now) {
  const age = L.ageDays(item, now);
  const overdue = L.horizonOf(item, now) === "overdue";
  const waiting = item.owner && item.owner !== "me";
  const src = item.source || {};
  const where = src.meetingTitle || (src.kind === "manual" ? "Added by hand" : "");
  const bits = [];
  if (item.project) bits.push('<span class="tag">' + esc(item.project) + "</span>");
  if (waiting) bits.push('<span class="tag wait">waiting on ' + esc(item.owner) + "</span>");
  if (where) bits.push("<span>" + esc(where) + (src.date ? " · " + esc(src.date) : "") + "</span>");
  if (!item.done && age >= 21) bits.push('<span class="tag age">open ' + age + "d</span>");
  if (item.verify) bits.push('<span class="tag">check if done</span>');

  return (
    '<li class="row' + (item.done ? " done" : "") + '" data-id="' + esc(item.id) + '">' +
      '<input type="checkbox" id="cb-' + esc(item.id) + '" ' + (item.done ? "checked" : "") + ' aria-label="Mark done">' +
      '<button class="pri ' + esc(item.priority) + '" data-act="cycle" title="Change priority">' + esc(item.priority) + "</button>" +
      '<label class="txt" for="cb-' + esc(item.id) + '"><div class="t">' + esc(item.text) + "</div>" +
        '<div class="meta">' + bits.join("") + "</div></label>" +
      '<div class="due' + (overdue && !item.done ? " late" : "") + '">' + esc(dueLabel(item, now)) + "</div>" +
    "</li>"
  );
}

function render() {
  const now = today();
  const c = L.counts(items, inbox, now);
  $("strip").innerHTML =
    '<div class="stat is-overdue"><b>' + c.overdue + "</b><span>overdue</span></div>" +
    '<div class="stat"><b>' + c.week + "</b><span>due this week</span></div>" +
    '<div class="stat is-waiting"><b>' + c.waiting + "</b><span>waiting on someone</span></div>" +
    '<div class="stat is-pending"><b>' + c.pending + "</b><span>proposed, not yet added</span></div>";

  const groups = L.groupsOf(visible(), view.mode, now);
  $("board").innerHTML = groups
    .map(
      (g) =>
        '<section class="grp' + (g.key === "overdue" ? " sev" : "") + '">' +
          '<div class="ledger">' +
            '<div class="grouphead"><h2>' + esc(g.label) + '</h2><span class="count">' + g.open + " open</span></div>" +
            '<ul class="rows">' + g.items.map((i) => rowHTML(i, now)).join("") + "</ul>" +
          "</div>" +
        "</section>",
    )
    .join("");
  $("empty").hidden = groups.length > 0;
}

render();

(async () => {
  db = await claude.use("db");
  if (!db) {
    status("This list only runs inside Claude. Open the artifact there to see and edit it.");
    return;
  }
  const onErr = () => status("Lost the connection to your list. Reload the page.", true);
  const rows = (snap) => snap.docs.map((d) => ({ ...d.data(), id: d.id }));

  db.collection("items").onSnapshot((snap) => {
    items = rows(snap);
    status("Live. Changes save as you make them.");
    render();
  }, onErr);

  db.collection("inbox").onSnapshot((snap) => {
    inbox = rows(snap);
    render();
  }, onErr);

  db.doc("meta/sync").onSnapshot((snap) => {
    const m = snap.exists ? snap.data() : null;
    if (m && m.lastRun) {
      $("asof").textContent = "Open loops · meetings last checked " +
        new Date(m.lastRun).toLocaleString("en-GB", { weekday: "short", day: "numeric", month: "short", hour: "2-digit", minute: "2-digit" });
    }
  }, onErr);
})();

document.querySelectorAll(".chip").forEach((b) => {
  b.addEventListener("click", () => {
    const set = (key, val, attr) => {
      view[key] = val;
      document.querySelectorAll("[data-" + attr + "]").forEach((x) => x.setAttribute("aria-pressed", String(x === b)));
    };
    if (b.dataset.mode) set("mode", b.dataset.mode, "mode");
    else if (b.dataset.own) set("owner", b.dataset.own, "own");
    else if (b.dataset.pri) set("pri", b.dataset.pri, "pri");
    else if (b.id === "hidedone") {
      view.hideDone = !view.hideDone;
      b.setAttribute("aria-pressed", String(view.hideDone));
    }
    render();
  });
});
</script>
```

- [ ] **Step 2: Publish the artifact**

Call the Artifact tool once:

```
Artifact(
  file_path: "/Users/ftosetto/Projects/em-hub/todos/dashboard.html",
  files: {"logic.js": "todos/logic.js"},
  root: "/Users/ftosetto/Projects/em-hub",
  capabilities: {"db": {}},
  favicon: "🧾",
  icon: "checklist",
  description: "Filippo's open loops: what he owes, what he is owed, and what his meetings proposed."
)
```

Expected: a claude.ai artifact URL, and a confirmation that the `db` capability is declared.

- [ ] **Step 3: Verify the empty page renders**

Open the returned URL with the Playwright MCP browser (`browser_navigate`, then `browser_snapshot`).

Expected:
- The heading "Open Loops" and four stat tiles all reading `0`.
- The empty-state line "Nothing open."
- `#status` reads "Live. Changes save as you make them." (db resolved) rather than the "only runs inside Claude" fallback.
- `browser_console_messages` shows no errors. A `TodoLogic is not defined` error means `logic.js` did not publish as a supporting file. Re-check the `files` argument.

- [ ] **Step 4: Record the artifact URL**

Create `todos/ARTIFACT.md`:

```markdown
# Open Loops artifact

URL: <paste the published URL here>

Redeploy with the same file path in a session that has already read or
published it, or from a fresh session by passing that URL as `url` after an
`action: "read"`. Publishing without the URL creates a second artifact and
splits the data, because the db belongs to the artifact.

Publish arguments that must stay stable:

- `file_path`: `todos/dashboard.html`
- `files`: `{"logic.js": "todos/logic.js"}`
- `favicon`: 🧾 (first publish only, omit afterwards)
- `capabilities`: `{"db": {}}` (first publish only, omit afterwards so the
  stored declaration carries forward)

Collections: `items/`, `inbox/`, `meta/sync`. Shapes are in
`docs/superpowers/specs/2026-09-16-todo-dashboard-design.md`.
```

- [ ] **Step 5: Commit**

```bash
cd /Users/ftosetto/Projects/em-hub
git add todos/dashboard.html todos/ARTIFACT.md
git commit --author="filippo-lt <filippo.tosetto@leadtech.com>" -m "Add Open Loops dashboard page, read path

Ledger layout grouped by when, person or project, reading items and inbox
live from the artifact db."
```

---

### Task 3: Dashboard page, write path

**Files:**
- Modify: `todos/dashboard.html` (add the quick-add form, the inbox band, and the click and change handlers)

**Interfaces:**
- Consumes: `db` from Task 2's IIFE, `L.nextPriority`, `L.isDuplicate` from Task 1.
- Produces: the accept transform that Task 6's seeding and Task 7's `/todos` skill must match: accepting an `inbox/` document writes an `items/` document carrying `text, project, owner, priority, due, source, verify` plus `done:false, doneAt:null, order:Date.now(), createdAt:<inbox proposedAt date or today>`, and drops `why` and `proposedAt`.

- [ ] **Step 1: Add the inbox band and quick-add markup**

In `todos/dashboard.html`, insert directly after the closing `</div>` of `<div class="strip" id="strip"></div>`:

```html
  <section class="inboxband" id="inboxband" hidden></section>

  <details class="addbox" id="addbox">
    <summary>Add an item by hand</summary>
    <form class="addform" id="addform">
      <input type="text" id="add-text" placeholder="What needs to happen" required>
      <input type="text" id="add-project" list="known-projects" placeholder="Project">
      <datalist id="known-projects"></datalist>
      <input type="text" id="add-owner" list="known-people" placeholder="Owner (blank = you)">
      <datalist id="known-people"></datalist>
      <select id="add-pri" aria-label="Priority">
        <option>P0</option><option selected>P1</option><option>P2</option>
      </select>
      <input type="date" id="add-due" aria-label="Due date">
      <button class="btn primary" type="submit">Add</button>
    </form>
  </details>
```

- [ ] **Step 2: Add the styles for both**

Append to the `<style>` block, before the `@media (max-width:560px)` rule:

```css
.inboxband{background:var(--card);border:1px solid var(--accent);border-radius:8px;padding:14px 16px;display:flex;flex-direction:column;gap:12px}
.inboxband .meeting{display:flex;flex-direction:column;gap:6px}
.prop{display:grid;grid-template-columns:40px 1fr auto;gap:10px;align-items:center;border:1px solid var(--rule);border-radius:6px;padding:9px 11px}
.prop .why{color:var(--muted);font-size:13px;font-style:italic;margin-top:3px}
.acts{display:flex;gap:6px;flex-wrap:wrap;justify-content:flex-end}
.btn{font:500 13px "Source Sans 3",sans-serif;border:1px solid var(--rule);background:var(--card);color:var(--ink);border-radius:6px;padding:6px 12px;cursor:pointer}
.btn.primary{background:var(--accent);border-color:var(--accent);color:var(--on-accent)}
.btn[disabled]{opacity:.5;cursor:default}
.addbox summary{cursor:pointer;color:var(--accent);font-weight:600;font-size:14px}
.addform{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-top:10px}
.addform input[type=text]{flex:1 1 220px;min-width:0}
.addform input,.addform select{font:14px "Source Sans 3",sans-serif;padding:7px 9px;border:1px solid var(--rule);border-radius:6px;background:var(--card);color:var(--ink)}
```

Add to the `@media (max-width:560px)` block:

```css
  .prop{grid-template-columns:40px 1fr}
  .acts{grid-column:1/-1;justify-content:flex-start}
  .addform input[type=text]{flex:1 1 100%}
```

- [ ] **Step 3: Add the inbox render and the write handlers**

In the inline script, add `renderInbox` and call it from `render`. Insert `renderInbox` immediately before `function render()`:

```js
function renderInbox() {
  const band = $("inboxband");
  if (!inbox.length) {
    band.hidden = true;
    band.innerHTML = "";
    return;
  }
  band.hidden = false;
  const byMeeting = new Map();
  inbox.forEach((x) => {
    const key = (x.source && x.source.meetingTitle) || "Proposed";
    if (!byMeeting.has(key)) byMeeting.set(key, []);
    byMeeting.get(key).push(x);
  });

  let html =
    '<div><div class="eyebrow">Review · ' + inbox.length + " proposed</div>" +
    "<h2>From your recent meetings. Which ones go on the list?</h2></div>";

  for (const [meeting, list] of byMeeting) {
    html += '<div class="meeting"><h3>' + esc(meeting) + "</h3>";
    list.forEach((x) => {
      const waiting = x.owner && x.owner !== "me";
      html +=
        '<div class="prop" data-id="' + esc(x.id) + '">' +
          '<button class="pri ' + esc(x.priority) + '" data-act="cyclep" title="Change priority">' + esc(x.priority) + "</button>" +
          '<div><div class="t">' + esc(x.text) + "</div>" +
            '<div class="meta">' +
              (x.project ? '<span class="tag">' + esc(x.project) + "</span>" : "") +
              (waiting ? '<span class="tag wait">waiting on ' + esc(x.owner) + "</span>" : "") +
              (x.due ? "<span>due " + esc(x.due) + "</span>" : "") +
            "</div>" +
            (x.why ? '<div class="why">“' + esc(x.why) + "”</div>" : "") +
          "</div>" +
          '<div class="acts"><button class="btn primary" data-act="accept">Add</button>' +
          '<button class="btn" data-act="skip">Skip</button></div>' +
        "</div>";
    });
    html += "</div>";
  }
  html += '<div class="acts" style="justify-content:flex-start">' +
    '<button class="btn primary" data-act="acceptall">Add all</button>' +
    '<button class="btn" data-act="skipall">Skip all</button></div>';
  band.innerHTML = html;
}
```

At the end of `render()`, before its closing brace, add:

```js
  renderInbox();
  const known = (pick) => [...new Set(items.map(pick).filter(Boolean))].sort();
  const options = (vals) => vals.map((v) => '<option value="' + esc(v) + '">').join("");
  $("known-projects").innerHTML = options(known((i) => i.project));
  $("known-people").innerHTML = options(known((i) => (i.source && i.source.person) || (i.owner !== "me" ? i.owner : null)));
```

Then append the handlers at the end of the script:

```js
/* Accepting fills the fields inbox rows do not carry and drops the two they
   carry only for triage. Keep this in step with the /todos skill, which
   performs the same transform from the terminal. */
async function accept(proposal) {
  const { id, why, proposedAt, ...rest } = proposal;
  await db.collection("items").add({
    ...rest,
    done: false,
    doneAt: null,
    order: Date.now(),
    createdAt: (proposedAt || new Date().toISOString()).slice(0, 10),
  });
  await db.doc("inbox/" + id).delete();
}

document.addEventListener("click", async (e) => {
  const btn = e.target.closest("button[data-act]");
  if (!btn || !db) return;
  const act = btn.dataset.act;
  try {
    if (act === "cycle") {
      const id = btn.closest(".row").dataset.id;
      const it = items.find((x) => x.id === id);
      await db.doc("items/" + id).update({ priority: L.nextPriority(it.priority) });
      return;
    }
    if (act === "cyclep") {
      const id = btn.closest(".prop").dataset.id;
      const p = inbox.find((x) => x.id === id);
      await db.doc("inbox/" + id).update({ priority: L.nextPriority(p.priority) });
      return;
    }
    if (act === "accept") {
      btn.disabled = true;
      await accept(inbox.find((x) => x.id === btn.closest(".prop").dataset.id));
      status("Added to your list.");
      return;
    }
    if (act === "skip") {
      await db.doc("inbox/" + btn.closest(".prop").dataset.id).delete();
      return;
    }
    if (act === "acceptall") {
      btn.disabled = true;
      for (const p of inbox.slice()) await accept(p);
      status("All added.");
      return;
    }
    if (act === "skipall") {
      btn.disabled = true;
      for (const p of inbox.slice()) await db.doc("inbox/" + p.id).delete();
      status("Cleared the review band.");
    }
  } catch (err) {
    btn.disabled = false;
    reportWriteFailure(err);
  }
});

document.addEventListener("change", async (e) => {
  const cb = e.target;
  if (cb.type !== "checkbox" || !db) return;
  const row = cb.closest(".row");
  if (!row) return;
  try {
    await db.doc("items/" + row.dataset.id).update({
      done: cb.checked,
      doneAt: cb.checked ? new Date().toISOString() : null,
    });
  } catch (err) {
    cb.checked = !cb.checked;
    reportWriteFailure(err);
  }
});

$("addform").addEventListener("submit", async (e) => {
  e.preventDefault();
  if (!db) return;
  const text = $("add-text").value.trim();
  if (!text) return;
  const owner = $("add-owner").value.trim() || "me";
  const candidate = { text, source: { kind: "manual" } };
  if (L.isDuplicate(candidate, items)) {
    status("That looks like something already on your list.", true);
    return;
  }
  try {
    await db.collection("items").add({
      text,
      project: $("add-project").value.trim() || "",
      owner,
      priority: $("add-pri").value,
      due: $("add-due").value || null,
      source: { kind: "manual", person: owner !== "me" ? owner : null, date: today(), meetingTitle: null, granolaId: null },
      verify: false,
      done: false,
      doneAt: null,
      order: Date.now(),
      createdAt: today(),
    });
    $("addform").reset();
    status("Added.");
  } catch (err) {
    reportWriteFailure(err);
  }
});
```

- [ ] **Step 4: Republish**

```
Artifact(
  file_path: "/Users/ftosetto/Projects/em-hub/todos/dashboard.html",
  files: {"logic.js": "todos/logic.js"},
  root: "/Users/ftosetto/Projects/em-hub"
)
```

No `favicon`, no `capabilities`, no `icon`: omitting them carries the stored values forward.

Expected: same URL as Task 2.

- [ ] **Step 5: Smoke-test one write**

In the browser, expand "Add an item by hand", type `Smoke test row`, submit.

Expected: the row appears under Someday, `#status` reads "Added.", the stat strip updates. Tick its checkbox and confirm it strikes through. Reload the page and confirm both the row and its done state survived. Then delete it in the next task's seeding step, or leave it and remove it by hand.

- [ ] **Step 6: Commit**

```bash
cd /Users/ftosetto/Projects/em-hub
git add todos/dashboard.html
git commit --author="filippo-lt <filippo.tosetto@leadtech.com>" -m "Add Open Loops write path

Quick add, done toggle, priority cycling, and the inbox review band with
per-item and bulk accept or skip."
```

---

### Task 4: Seed from the real analyses and verify

**Files:**
- Read: `people/*/transcripts/2026-09-*_analysis.md`
- Create: `todos/seed.json` (the extracted rows, kept in git as the record of what was loaded)

**Interfaces:**
- Consumes: the db shapes from Task 2, the accept transform from Task 3.
- Produces: a populated `items/` and `inbox/` for verification.

- [ ] **Step 1: Extract real action items**

Read every `## Action items` table in:
- `people/david-manager/transcripts/2026-09-01_analysis.md`
- `people/david-manager/transcripts/2026-09-08_analysis.md`
- `people/david-manager/transcripts/2026-09-15_analysis.md`
- `people/vlad-engineer/transcripts/2026-08-31_analysis.md`
- `people/andrey-direct/transcripts/2026-09-14_analysis.md`
- `people/victor-jalencas/transcripts/2026-09-03_analysis.md`
- `people/victor-jalencas/transcripts/2026-09-10_analysis.md`

Column layouts differ between files. Read each table's header row before mapping its columns; do not assume the `analyse` skill's template order.

For each row build:

```json
{
  "text": "<the action, one sentence, imperative>",
  "project": "<from context, or \"\">",
  "owner": "me | <person name>",
  "priority": "P0 | P1 | P2",
  "due": "YYYY-MM-DD or null",
  "source": {"kind": "1on1", "person": "<the 1:1 partner>", "date": "<file date>", "meetingTitle": "<Name> 1:1", "granolaId": null},
  "verify": false,
  "done": false,
  "doneAt": null,
  "createdAt": "<file date>",
  "order": <index>
}
```

Priority mapping: a stated deadline within a week, or an item the analysis marks as repeatedly missed, is P0. A stated deadline beyond a week is P1. No deadline is P2, unless the analysis calls it urgent.

Drop any row whose action already reads as completed in a later analysis. Run each candidate through the same wording check `L.isDuplicate` uses so the August metrics sheet, raised across several meetings, becomes one row and not several.

Write the result to `todos/seed.json` as `{"items": [...], "inbox": [...]}`. Put the three most recent, least certain rows in `inbox` rather than `items`, so the review band has real content to test against.

- [ ] **Step 2: Load the seed into the db**

Load the `ArtifactData` tool: `ToolSearch(query: "select:ArtifactData", max_results: 1)`.

For each entry in `seed.json`, call `ArtifactData` with `action: "set"`, the artifact `url` from `todos/ARTIFACT.md`, and `path` of `items/<slug>` or `inbox/<slug>` where `<slug>` is a short kebab-case id derived from the text. Use `action: "batch"` if the tool's schema accepts a list, which is one call instead of many.

Expected: the browser tab, still open, updates live without a reload.

- [ ] **Step 3: Verify every interaction against real data**

With Playwright MCP on the artifact URL, check each of these and record the result:

1. Stat strip figures match the seed. Overdue count matches the rows with a past `due`.
2. Group toggle: When, Person, Project each regroup the board. Under Person, an item with `owner: "me"` and `source.person: "David"` appears under David.
3. Owner filter: Mine hides the rows owned by others. Waiting on shows only those.
4. Priority filter: P0 shows only P0. P0+P1 excludes P2.
5. Hide done: tick a row, then toggle Hide done, and confirm it disappears.
6. Priority badge cycles P0 to P1 to P2 to P0, and the change survives a reload.
7. Inbox: Add moves a proposal into the right group. Skip removes it. Both update the pending count.
8. Quick add with a due date lands in the correct horizon group.
9. Duplicate guard: add an item whose wording matches an existing one and confirm the status line refuses it.
10. `browser_console_messages` is clean throughout.

- [ ] **Step 4: Check both themes and phone width**

Run `browser_resize` to 390x844 and take a snapshot. Confirm no horizontal scroll, the row grid collapses to three columns with the due date on its own line, and the add form stacks.

Then check dark mode. The artifact viewer's theme drives it, so if the current theme is light, verify the dark tokens by evaluating `document.documentElement.setAttribute("data-theme","dark")` through `browser_evaluate` and taking one screenshot. Confirm text contrast holds and no colour falls back to a light-only literal.

- [ ] **Step 5: Fix anything broken, republish once**

Make one pass of fixes for whatever steps 3 and 4 turned up, republish with the Task 3 argument set, and re-check only the specific things that were broken.

- [ ] **Step 6: Commit**

```bash
cd /Users/ftosetto/Projects/em-hub
git add todos/seed.json todos/dashboard.html todos/logic.js
git commit --author="filippo-lt <filippo.tosetto@leadtech.com>" -m "Seed Open Loops from September 1:1 analyses

Records what was loaded and the fixes the first pass against real data
turned up."
```

---

### Task 5: The /todos skill

**Files:**
- Create: `.agents/skills/todos/SKILL.md`
- Create: `.claude/skills/todos` (symlink)
- Modify: `CLAUDE.md`

**Interfaces:**
- Consumes: the artifact URL in `todos/ARTIFACT.md`, the db shapes from Task 2, the accept transform from Task 3.
- Produces: `/todos` as a user-invocable skill.

- [ ] **Step 1: Write the skill**

Create `.agents/skills/todos/SKILL.md`:

```markdown
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
- Report counts honestly. If a write failed, say which one.
- The dashboard is open in the user's browser and updates live. Tell them to look
  there rather than re-listing everything you just wrote.
```

- [ ] **Step 2: Create the Claude Code symlink**

```bash
cd /Users/ftosetto/Projects/em-hub
ln -s ../../.agents/skills/todos .claude/skills/todos
ls -l .claude/skills/todos
```

Expected: the symlink resolves to `.agents/skills/todos`. Compare with an existing one (`ls -l .claude/skills/prep`) and match its relative form. If the existing symlinks use a different depth, copy that instead.

- [ ] **Step 3: Add the routing table row**

In `CLAUDE.md`, in the "Skill Routing" table, after the `/timebox` row, add:

```markdown
| "What's on my list" / "Add a todo" / "What's overdue" / "What do I owe [name]" | Todos      | `/todos`      |
```

In the folder structure block, after the `templates/` line, add:

```
├── todos/           ← Open Loops dashboard source (published as an artifact)
```

- [ ] **Step 4: Verify the skill loads**

Run `/todos what is overdue` in a fresh Claude Code turn.

Expected: the skill loads, reads `todos/ARTIFACT.md`, lists `items/` through `ArtifactData`, and answers with the overdue rows from the Task 4 seed. If it instead offers to create an artifact, the "never create a new artifact" instruction is not landing. Strengthen it before moving on.

- [ ] **Step 5: Commit**

```bash
cd /Users/ftosetto/Projects/em-hub
git add .agents/skills/todos/SKILL.md .claude/skills/todos CLAUDE.md
git commit --author="filippo-lt <filippo.tosetto@leadtech.com>" -m "Add /todos skill

Read and write the Open Loops list from the terminal, against the same
artifact db the dashboard uses."
```

---

### Task 6: Push action items from /1on1-lifecycle

**Files:**
- Modify: `.agents/skills/1on1-lifecycle/SKILL.md`

**Interfaces:**
- Consumes: `inbox/` shape from Task 2, `todos/ARTIFACT.md` from Task 2.
- Produces: nothing later tasks depend on.

- [ ] **Step 1: Insert the new step**

In `.agents/skills/1on1-lifecycle/SKILL.md`, between the section that ends step 4 (memory extraction) and the heading for step 5 (keeping source docs current), insert:

```markdown
### 4.5 Push action items to the Open Loops list

Read `todos/ARTIFACT.md` for the artifact URL and load `ArtifactData` with
`ToolSearch(query: "select:ArtifactData", max_results: 1)`.

Take the `## Action items` table you just wrote into the analysis file. For each
row, write one document to `inbox/`, never to `items/`. The user accepts or skips
each one on the dashboard.

```json
{
  "text": "<the action, one imperative sentence>",
  "project": "<project name, or \"\">",
  "owner": "me | <the person who owns it>",
  "priority": "P0 | P1 | P2",
  "due": "YYYY-MM-DD, or null when the analysis says not specified",
  "source": {"kind": "1on1", "person": "<name>", "date": "<meeting date>", "meetingTitle": "<Name> 1:1", "granolaId": "<Granola meeting id>"},
  "verify": false,
  "why": "<the short transcript quote the action came from>",
  "proposedAt": "<ISO timestamp>"
}
```

Priority: a stated deadline inside a week is P0, further out is P1, none is P2.
An item the analysis flags as missed or repeated is P0 regardless of its date.

Before writing, list open `items/` and pending `inbox/`. Skip any candidate whose
wording already appears there, compared lowercased and stripped of punctuation.
A commitment carried across several meetings is one open loop, not one per
meeting.

Report the count: "Queued N items for review on the dashboard."

**This step never blocks the write-up.** If `ArtifactData` is unavailable, or
`todos/ARTIFACT.md` is missing, say so in one line and carry on to step 5. The
transcript, analysis and memory files are the deliverable. The todo push is not.
```

- [ ] **Step 2: Renumber nothing else**

Check that the following section still reads "### 5." and the closing section's numbering is untouched. The new step is deliberately 4.5 so that no other step number moves.

Run: `grep -n "^### " .agents/skills/1on1-lifecycle/SKILL.md`
Expected: a monotonic sequence with `4.5` between `4` and `5`.

- [ ] **Step 3: Verify against a real meeting**

Run `/1on1-lifecycle` for the most recent 1:1 that already has an analysis file, and answer "no" when it offers to commit.

Expected: the run reaches step 4.5, queues items to `inbox/`, and the open dashboard shows the review band populate live. If nothing was queued because everything deduped, that is a pass: say so rather than loosening the dedupe.

- [ ] **Step 4: Commit**

```bash
cd /Users/ftosetto/Projects/em-hub
git add .agents/skills/1on1-lifecycle/SKILL.md
git commit --author="filippo-lt <filippo.tosetto@leadtech.com>" -m "Push 1:1 action items to the Open Loops inbox

New step 4.5 queues each action item for review. Never blocks the write-up
if the artifact is unreachable."
```

---

### Task 7: The sweep agent

**Files:**
- Create: `.agents/agents/todo-sweep-agent.md`
- Modify: `CLAUDE.md` (agent routing table)

**Interfaces:**
- Consumes: `meta/sync` and `inbox/` shapes from Task 2.
- Produces: a prompt file that Task 8's cloud routine invokes verbatim.

- [ ] **Step 1: Write the agent**

Create `.agents/agents/todo-sweep-agent.md`:

```markdown
---
name: todo-sweep-agent
description: "Read Granola meetings that have not been processed yet and propose todo items. Use when the user says: 'sweep my meetings', 'check for new todos', or on the weekday morning schedule."
---

# Todo Sweep Agent

You read meetings Filippo has had since the last sweep and propose open loops
from them. You never add anything to his list directly. Everything you write goes
to `inbox/`, where he accepts or skips it.

## Setup

1. Read `todos/ARTIFACT.md` for the artifact URL. If you are running without the
   repo, the URL is the one the routine passes you.
2. Load `ArtifactData`: `ToolSearch(query: "select:ArtifactData", max_results: 1)`.
3. Load the Granola tools:
   `ToolSearch(query: "select:mcp__claude_ai_Granola__list_meetings,mcp__claude_ai_Granola__get_meeting_transcript", max_results: 2)`.

## Steps

1. Read `meta/sync`. If it does not exist, treat `lastGranolaTs` as 14 days ago
   and `processedIds` as empty.
2. List Granola meetings with a start time after `lastGranolaTs`.
3. Drop any whose id is in `processedIds`.
4. For each remaining meeting, fetch the transcript and pull out commitments.
5. Read open `items/` and all of `inbox/`. Drop any candidate whose wording
   already appears in either, compared lowercased and stripped of punctuation.
6. Write the survivors to `inbox/`.
7. Update `meta/sync` **last**, after the inbox writes succeed: set `lastRun` to
   now, `lastGranolaTs` to the newest meeting you processed, and append the
   processed ids, keeping the most recent 200.

If a write fails partway, stop and leave `meta/sync` alone. The next run re-reads
the same meetings and the dedupe in step 5 absorbs the repeat. A stalled
watermark is recoverable; a watermark that ran ahead of failed writes loses
meetings silently.

## What counts as a commitment

Include:
- Something Filippo said he would do.
- Something someone else committed to him, with that person as `owner`.
- A dated thing he needs to be ready for.

Exclude:
- Discussion, context, opinions, decisions with no follow-up.
- Anything already tracked in Jira as team delivery work. This list is his own.
- Vague intent with no action in it ("we should think about X").

Prefer the speaker's own words for `text`, trimmed to one imperative sentence.

## The document to write

```json
{
  "text": "Send the August metrics sheet to Forward",
  "project": "M&A",
  "owner": "me",
  "priority": "P0",
  "due": "2026-09-17",
  "source": {"kind": "meeting", "person": "David", "date": "2026-09-16", "meetingTitle": "David 1:1", "granolaId": "<id>"},
  "verify": false,
  "why": "<the quote from the transcript that produced this>",
  "proposedAt": "<ISO timestamp>"
}
```

`source.kind` is `1on1` when the meeting is a one-to-one, otherwise `meeting`.
`source.person` is the other attendee for a 1:1, and the meeting organiser
otherwise. Set `verify: true` when the transcript suggests the thing may already
be finished.

Priority: a stated deadline inside a week is P0, further out is P1, none is P2.

## Reporting

Finish with one line: how many meetings you read, how many items you queued, and
how many you dropped as duplicates. If you read no new meetings, say that. Do not
pad the report.

## Never

- Write to `items/`. The accept click is the user's, always.
- Invent a commitment that is not in the transcript.
- Advance the watermark past a meeting whose items failed to write.
```

- [ ] **Step 2: Add the agent routing row**

In `CLAUDE.md`, in the "Agent Routing" table, after the M&A Heartbeat row, add:

```markdown
| "Sweep my meetings" / "Check for new todos" / "What did I commit to this week"                           | Todo Sweep      | `.claude/agents/todo-sweep-agent.md`      |
```

Check whether `.claude/agents/` holds symlinks or real files (`ls -l .claude/agents/`) and match the existing pattern for `todo-sweep-agent.md`.

- [ ] **Step 3: Run the sweep by hand, once**

Dispatch the agent against real Granola data.

Expected: it reports meetings read and items queued, and the dashboard's review band fills. Read every queued row before accepting any. This is the first time the extraction quality is visible, and it is the thing most likely to need the prompt tightened.

If the items are noisy (discussion captured as commitments, duplicates of things already on the list, vague text), revise the "What counts as a commitment" section and run again. Do this before Task 8, never after: a daily routine that queues noise makes the review band something to ignore, and then the whole dashboard is dead.

- [ ] **Step 4: Commit**

```bash
cd /Users/ftosetto/Projects/em-hub
git add .agents/agents/todo-sweep-agent.md .claude/agents/todo-sweep-agent.md CLAUDE.md
git commit --author="filippo-lt <filippo.tosetto@leadtech.com>" -m "Add todo sweep agent

Reads unprocessed Granola meetings, proposes items to the inbox, and only
advances the watermark after the writes land."
```

---

### Task 8: The scheduled routine

**Files:**
- Create: nothing in the repo. The routine lives in the scheduling system.
- Modify: `todos/ARTIFACT.md` (record the routine, or record that it could not be created)

**Interfaces:**
- Consumes: `.agents/agents/todo-sweep-agent.md` from Task 7.
- Produces: nothing.

This task carries the spec's one open assumption. Do not start it until Task 7's manual run produced items worth accepting.

- [ ] **Step 1: Verify the assumption before building anything**

The routine needs both the Granola connector and `ArtifactData` in its
environment. Check this first.

Load the scheduling tools: `ToolSearch(query: "select:CronCreate,CronList", max_results: 2)`, and read the `schedule` skill for how routines declare their tools.

If cloud routines cannot reach the Granola connector, stop and report it. Do not build a routine that will fail silently every morning. Go to step 3 instead.

- [ ] **Step 2: Create the routine**

Schedule: `0 8 * * 1-5`, Europe/Madrid.

Prompt:

```
Run the todo sweep. Follow .agents/agents/todo-sweep-agent.md exactly.
The Open Loops artifact is at <URL from todos/ARTIFACT.md>.
Write proposals to inbox/ only. Never write to items/.
Report meetings read, items queued, duplicates dropped.
```

Verify with `CronList` that it is registered, then trigger one run manually if the scheduler supports it, and check the dashboard.

- [ ] **Step 3: Record the outcome**

Append to `todos/ARTIFACT.md`:

```markdown
## Scheduled sweep

Status: <live | not possible>
Schedule: 0 8 * * 1-5, Europe/Madrid
Agent: `.agents/agents/todo-sweep-agent.md`

<If not possible: the reason, and the local launchd fallback below.>
```

If the cloud routine is not possible, write the launchd fallback into the same file rather than installing it unasked:

```xml
<!-- ~/Library/LaunchAgents/com.filippo.todo-sweep.plist -->
<!-- Install with: launchctl load ~/Library/LaunchAgents/com.filippo.todo-sweep.plist -->
<key>ProgramArguments</key>
<array>
  <string>/bin/zsh</string>
  <string>-lc</string>
  <string>cd ~/Projects/em-hub &amp;&amp; claude -p "Run the todo sweep per .agents/agents/todo-sweep-agent.md"</string>
</array>
<key>StartCalendarInterval</key>
<array>
  <dict><key>Weekday</key><integer>1</integer><key>Hour</key><integer>8</integer></dict>
  <dict><key>Weekday</key><integer>2</integer><key>Hour</key><integer>8</integer></dict>
  <dict><key>Weekday</key><integer>3</integer><key>Hour</key><integer>8</integer></dict>
  <dict><key>Weekday</key><integer>4</integer><key>Hour</key><integer>8</integer></dict>
  <dict><key>Weekday</key><integer>5</integer><key>Hour</key><integer>8</integer></dict>
</array>
```

Then tell the user which of the two happened and let them decide on the fallback.

- [ ] **Step 4: Commit**

```bash
cd /Users/ftosetto/Projects/em-hub
git add todos/ARTIFACT.md
git commit --author="filippo-lt <filippo.tosetto@leadtech.com>" -m "Record the Open Loops sweep schedule"
```

---

## Notes for the executor

- Tasks 1 through 4 are worth having on their own. If Task 8's assumption fails, nothing earlier is wasted.
- Task 4 is where the design meets real data and is the most likely to turn up schema problems. Treat a surprise there as a reason to revise the spec, not to work around it in the page.
- Task 7's step 3 is a quality gate, not a smoke test. Noisy extraction is the single failure that would make this whole thing unused.
