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
