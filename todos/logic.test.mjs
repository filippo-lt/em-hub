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
