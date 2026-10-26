// jira-monthly-stats.js — monthly Jira delivery stats per developer, two views.
//
// HOW TO RUN: open any page on https://leadtech.atlassian.net while signed in,
// paste this whole file into the console (or a browser-automation JS tool), then:
//   await jiraMonthlyStats({ month: '2026-09', people: ['Viacheslav Lypchenko', ...] })
// Read-only: only GET/search calls, uses the browser session (no API token).
//
// VIEW 1 — "eazyBI" (company standard, matches the cross-company eazyBI boards)
//   Issue counts if its Resolved date is inside the month. Credited to the CURRENT assignee.
//   Story points = "Story Points" (customfield_10004). All issue types, User Stories also shown apart.
//   Caveat: follows release timing. A release bulk-closed on day X credits all its tickets
//   to X's month, even if dev work was done months before ("carriedIn" shows how much).
//
// VIEW 2 — "Flow" (when the developer actually finished the work)
//   devDone    = first move into "Ready for Testing" in the month (MAU workflow)
//   accepted   = first move into "Waiting for Deployment" in the month (QA + PO passed)
//   bounces    = every move into "No QA Pass" / "No Pass" / "No-QAPass" in the month
//   MTSDK (no QA step): review = into "Waiting for Approval", done = into "DONE"
//   Credited to the assignee AT THE MOMENT of the transition (rebuilt from the changelog).

async function jiraMonthlyStats({ month, people, tz = 'Europe/Rome', spField = 'customfield_10004' }) {
  const [y, m] = month.split('-').map(Number);
  const start = `${month}-01`;
  const next = m === 12 ? `${y + 1}-01-01` : `${y}-${String(m + 1).padStart(2, '0')}-01`;
  const localDay = iso => new Date(iso).toLocaleDateString('sv-SE', { timeZone: tz }); // YYYY-MM-DD
  const inMonth = iso => { const d = localDay(iso); return d >= start && d < next; };
  const before = iso => localDay(iso) < start;

  // ── helpers ──
  async function search(jql, fields) {
    let out = [], token = null;
    do {
      const body = { jql, fields, expand: 'changelog', maxResults: 100 };
      if (token) body.nextPageToken = token;
      const r = await fetch('/rest/api/3/search/jql', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body) });
      const d = await r.json();
      if (d.errorMessages) throw new Error('JQL error: ' + d.errorMessages.join('; ') + ' — ' + jql);
      out = out.concat(d.issues); token = d.isLast ? null : d.nextPageToken;
    } while (token);
    for (const i of out) { // changelog in search is capped — fetch the full one when truncated
      if (i.changelog && i.changelog.total > i.changelog.histories.length) {
        let all = [], s = 0;
        while (true) {
          const d = await (await fetch(`/rest/api/3/issue/${i.key}/changelog?startAt=${s}&maxResults=100`)).json();
          all = all.concat(d.values); if (d.isLast || all.length >= d.total) break; s = all.length;
        }
        i.changelog.histories = all;
      }
      i.changelog.histories.sort((a, b) => a.created.localeCompare(b.created));
    }
    return out;
  }
  async function resolveUser(name) {
    const us = await (await fetch('/rest/api/3/user/search?query=' + encodeURIComponent(name))).json();
    const exact = us.find(u => u.displayName.toLowerCase() === name.toLowerCase());
    const starts = us.filter(u => u.displayName.toLowerCase().startsWith(name.toLowerCase()));
    const u = exact || (starts.length === 1 ? starts[0] : null);
    return u ? { id: u.accountId, name: u.displayName } : { error: `ambiguous/unknown: ${name} → ${us.map(x => x.displayName).join(', ')}` };
  }
  function assigneeAt(issue, t) {
    let a = issue.fields.assignee ? issue.fields.assignee.accountId : null;
    for (let k = issue.changelog.histories.length - 1; k >= 0; k--) {
      const h = issue.changelog.histories[k]; if (h.created <= t) break;
      for (const it of h.items) if (it.field === 'assignee') a = it.from;
    }
    return a;
  }
  const firstInto = (issue, statuses) => {
    for (const h of issue.changelog.histories) for (const it of h.items)
      if (it.field === 'status' && statuses.includes(it.toString)) return h.created;
    return null;
  };
  const sp = f => Number(f[spField]) || 0;
  const add = (o, k, n = 1) => (o[k] = (o[k] || 0) + n, o);

  // ── people ──
  const resolved = await Promise.all(people.map(resolveUser));
  const errors = resolved.filter(r => r.error).map(r => r.error);
  const users = resolved.filter(r => r.id);
  const byId = Object.fromEntries(users.map(u => [u.id, u.name]));
  const idList = users.map(u => `"${u.id}"`).join(',');
  const fields = ['summary', 'status', 'issuetype', 'project', 'assignee', 'resolutiondate', 'fixVersions', spField];

  const stats = {};
  for (const u of users) stats[u.name] = {
    eazyBI: { issues: 0, sp: 0, userStories: 0, userStoriesSP: 0, byProject: {}, byType: {}, carriedInSP: 0, carriedInIssues: 0, bulkCloseDays: {}, keys: [] },
    flow: { devDone: 0, devDoneSP: 0, accepted: 0, acceptedSP: 0, bounces: 0, bounceTickets: new Set(), mtsdkReview: 0, mtsdkDone: 0, mtsdkDoneSP: 0, byProject: {} },
  };

  // ── VIEW 1: eazyBI — resolved in month, current assignee ──
  const resolvedIssues = await search(`assignee in (${idList}) AND resolved >= "${start}" AND resolved < "${next}"`, fields);
  for (const i of resolvedIssues) {
    const f = i.fields; const name = byId[f.assignee && f.assignee.accountId]; if (!name || !inMonth(f.resolutiondate)) continue;
    const e = stats[name].eazyBI, p = f.project.key, s = sp(f);
    e.issues++; e.sp += s; add(e.byType, f.issuetype.name);
    if (f.issuetype.name === 'User Story') { e.userStories++; e.userStoriesSP += s; }
    e.byProject[p] = e.byProject[p] || { issues: 0, sp: 0, userStories: 0 };
    e.byProject[p].issues++; e.byProject[p].sp += s; if (f.issuetype.name === 'User Story') e.byProject[p].userStories++;
    add(e.bulkCloseDays, localDay(f.resolutiondate));
    const devDoneAt = firstInto(i, p === 'MTSDK' ? ['Waiting for Approval'] : ['Ready for Testing']);
    if (devDoneAt && before(devDoneAt)) { e.carriedInIssues++; e.carriedInSP += s; }
    e.keys.push(`${i.key} (${f.issuetype.name}, ${s} SP, dev done ${devDoneAt ? localDay(devDoneAt) : 'n/a'}, fix ${(f.fixVersions || []).map(v => v.name).join(',') || '-'})`);
  }

  // ── VIEW 2: Flow — transitions in month, assignee at transition time ──
  const flowIssues = await search(`assignee was in (${idList}) DURING ("${start}", "${next}") AND status changed DURING ("${start}", "${next}")`, fields);
  for (const i of flowIssues) {
    const f = i.fields, p = f.project.key, s = sp(f), seen = {};
    for (const h of i.changelog.histories) {
      if (!inMonth(h.created)) continue;
      for (const it of h.items) {
        if (it.field !== 'status') continue;
        const name = byId[assigneeAt(i, h.created)]; if (!name) continue;
        const fl = stats[name].flow, to = it.toString;
        const once = k => (seen[k + name] ? false : (seen[k + name] = true));
        if (p === 'MTSDK') {
          if (to === 'Waiting for Approval' && once('rev')) fl.mtsdkReview++;
          if (to === 'DONE' && once('done')) { fl.mtsdkDone++; fl.mtsdkDoneSP += s; add(fl.byProject, p); }
        } else {
          if (to === 'Ready for Testing' && once('dev')) { fl.devDone++; fl.devDoneSP += s; add(fl.byProject, p); }
          if (to === 'Waiting for Deployment' && once('acc')) { fl.accepted++; fl.acceptedSP += s; }
          if (['No QA Pass', 'No Pass', 'No-QAPass'].includes(to)) { fl.bounces++; fl.bounceTickets.add(i.key); }
        }
      }
    }
  }
  for (const s of Object.values(stats)) s.flow.bounceTickets = [...s.flow.bounceTickets];
  return { month, tz, errors, people: users, stats };
}
