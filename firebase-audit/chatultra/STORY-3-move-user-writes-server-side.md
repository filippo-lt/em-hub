# STORY 3 — ChatUltra

**Created:** [CBMAU-278](https://leadtech.atlassian.net/browse/CBMAU-278) — status `Created`, unassigned

**Jira project:** `CBMAU`
**Issue type:** User Story
**Priority:** Critical
**Summary:** `[Backend] Move client-side user-record writes behind a trusted path`
**Epic:** `[Security] Protect ChatUltra Firestore user and chat data`
**Blocks:** Story 4 (the rules cannot close writes on `users` until this ships)

---

## Context

ADO-1570's third acceptance criterion is that **writes with an anonymous token return
403** on the probed collection. For ChatUltra the probed collection is `users`, and the
client writes it directly: `_saveCrudUser()` at `auth_service.dart:185` writes the entire
`AppUser` record, `isPremium` and `premiumProduct` included.

This cannot be satisfied by a rules change alone. Unlike a telemetry or feedback
collection, `users` is load-bearing application state — the client writes it and reads it
back — so the write cannot simply be removed. It has to move behind a trusted path before
the collection can be closed to anonymous writes.

This story is the reason ChatUltra is more expensive than the other apps in this batch.

## Provenance

These findings were produced through an AI-assisted review of the application code,
cross-referenced against the non-destructive Firebase permission probe recorded in
ADO-1570. They must be validated by the technical owner before implementation.
Contact: filippo.tosetto@leadtech.com

## Technical guidance

**Understand the schema constraint before designing the endpoint.**
`module/core/.../firebase_crud_provider.dart` creates user records with
`instance.collection(path).add(json)` — **auto-generated document IDs** — and locates the
caller's own record with `collection(path).where('uid', isEqualTo: uid).get()`. The
Firebase uid is a *field*, not the document key. This means:

- `match /users/{uid}` path-scoping is impossible without a data migration.
- Owner-scoped **reads** are still achievable without one, because the client query is
  already constrained on `uid` (see Story 4).
- Owner-scoped **writes** are not, because a client can supply any `uid` value it likes
  in the document body. This is precisely why the write has to move server-side.

**Move user-record creation and updates to a backend endpoint** using the Firebase Admin
SDK, which bypasses Firestore rules. The endpoint must derive the `uid` from the verified
ID token rather than trusting a `uid` supplied in the request body, and must reject any
attempt to set `isPremium`, `premiumProduct` or `canMakePayments` from the client —
entitlement belongs to RevenueCat/Helium, which is already the in-app source of truth.

**Also review `read<T>()` in the same provider**, which performs an unfiltered
`collection(path).get()`. It must never be pointed at `users`, `chatHistory` or
`creditInfo`. Confirm its call sites and constrain or remove it.

**Consider migrating to uid-keyed documents** as a follow-up. It is not required for this
story, but it would allow straightforward path-scoped rules on all three collections and
remove a recurring source of this class of bug. Raise it separately rather than expanding
this ticket.

## Validation

- The client no longer writes `users` directly on any path — sign-up, sign-in, provider
  upgrade, profile update and premium-state change.
- The backend endpoint derives `uid` from the verified token and ignores any `uid` in the
  request body.
- A request attempting to set `isPremium` or `premiumProduct` from the client is rejected.
- Sign-up, anonymous startup, provider upgrade and premium purchase flows all verified
  working end to end.
- Backend Admin SDK operations continue to function after Story 4 closes client access.

## Acceptance criteria

- No client-side write path to `users` remains in the app.
- User-record creation and update go through a trusted backend path that derives identity
  from the verified ID token.
- Entitlement fields cannot be set by the client.
- Writes to `users` with an anonymous token return 403 once Story 4 ships.
- All authentication and purchase flows verified working.
