# EPIC — Screen Mirroring

**Created:** [SMIOSMAU-529](https://leadtech.atlassian.net/browse/SMIOSMAU-529) — status `Created`, unassigned

**Jira project:** `SMIOSMAU`
**Issue type:** Epic
**Priority:** Major
**Summary:** `[Security] Protect Screen Mirroring Firestore review and quota data`
**Parent:** ADO-1570 (link as *relates to*)

---

## Executive summary

Screen Mirroring's follow-up to the cross-app Security initiative ADO-1570.

Screen Mirroring's Firebase projects allow a fresh anonymous app identity to list
`reviews`. ADO-1570 reports approximately 57 documents in `screenmirroring-prod/reviews`
and 30 in `screenmirroring-dev/reviews`, confirmed HTTP 200 with anonymous
authentication on 2026-08-24. Each document holds a rating, free-text review body, a
timestamp and an anonymous user id.

**This is the smallest exposure in ADO-1570 and should be triaged accordingly.** There
are no tokens, emails, billing identifiers or credentials here. The user id is an
anonymous Firebase uid that maps to a device rather than a person. Read exposure is a
nuisance-grade leak. The write side matters slightly more: any anonymous token can create
review documents, which allows review spam and puts unvalidated free text in front of
whoever reads the collection downstream.

Two things nonetheless make this worth doing properly rather than closing as low value.

**There is a second collection ADO-1570 did not probe.** The app also writes
`users/{uid}/quotas`, holding `featureId`, `usageCount`, `lastResetDate`, `dailyLimit`
and `periodDays` for the features `screen_mirror`, `photos`, `videos` and `iptv`. This is
free-tier paywall enforcement. Under a rule that grants access to any signed-in user,
an anonymous token can read or tamper with quota documents. That is a monetisation
bypass, not a data breach, and it is the more consequential of the two collections.

**The fix already exists.** Branch `origin/chore/firestore-security-rules` (commit
`f773098`) adds a 62-line `firestore.rules` plus `firebase.json` and `.firebaserc`. It was
opened as PR #178, passed CI at 90.26% coverage with zero lint issues, and was closed
unmerged 70 minutes later with no human review and no stated reason. The engineering work
is essentially done; what is missing is a decision, a merge and a deploy.

Nothing in the app reads `reviews` back. As with iMote, the first question is whether the
data needs to be collected at all.

## Expected outcome

- Confirmed whether any consumer outside the app reads `reviews`, with a named owner for
  the answer.
- If it has no consumer: the write is removed and the collection becomes server-only.
- If it has a consumer: review submission is retained as a validated create-only path.
- `reviews` cannot be listed, read, updated or deleted by clients.
- `users/{uid}/quotas` is scoped to its owner and cannot be listed across users.
- Firestore rules are stored in source control with a deploy path.

## Ownership note

This repository has had no merge to `develop` since 2026-07-03, consistent with its
engineer's reassignment. There is no active owner today, and no Jira ticket existed for
Screen Mirroring under `SMIOSMAU` while sibling per-app tickets were cut for Tattoo,
Video Up, Photo Up, Translator GO, QR Now, Spam Safe and AI Cleaner. Assigning this epic
requires a staffing decision, not just a triage decision.
