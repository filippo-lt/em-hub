# STORY 4 — ChatUltra

**Created:** [CBMAU-279](https://leadtech.atlassian.net/browse/CBMAU-279) — status `Created`, unassigned

**Jira project:** `CBMAU`
**Issue type:** User Story
**Priority:** Critical
**Summary:** `[Backend] Implement and validate least-privilege Firestore access for ChatUltra`
**Epic:** `[Security] Protect ChatUltra Firestore user and chat data`
**Depends on:** Story 1 (baseline ruleset and confirmed exposure), Story 3 (write path)

---

## Context

This story implements ChatUltra's response to ADO-1570.

Affected Firebase project: `chatai2-32311` — a single project with **no dev/prod split**.
Requests without a Firebase identity return 403; requests with a fresh anonymous identity
returned 200 on `users` on 2026-08-24, approximately 52,355 documents.

Collections in scope: `users`, `chatHistory`, `creditInfo`
(`lib/product/constants/enums/firebase_paths.dart`), plus anything Story 1's inventory
turns up.

**Anonymous authentication cannot be disabled.** `auth_cubit.dart:44` signs every user in
anonymously at startup, `auth_service.dart:245` re-anonymises on token failure, and
`getIdToken()` forces an anonymous login when no user is present. ADO-1570's
"require a real signed-in user" branch is unavailable; the achievable target is
owner-scoped access bound to `request.auth.uid`.

**There is no staging project.** ADO-1570's remediation strategy assumes rules can be
tested on staging first. Here they cannot — any publish lands on production, in front of
52,355 users. This is why Stories 2 and 3 come first: they reduce exposure without a
rules publish, so this change can be made carefully rather than urgently.

## Provenance

These findings were produced through an AI-assisted review of the application code,
cross-referenced against the non-destructive Firebase permission probe recorded in
ADO-1570. They must be validated by the technical owner before implementation.
Contact: filippo.tosetto@leadtech.com

## Technical guidance

**Start from the baseline ruleset committed in Story 1.** Remove any broad
authenticated wildcard grant — Firestore `allow` rules are additive, so one broad allow
overrides every narrower deny intention below it.

**Owner-scoped reads work without a data migration.** Documents carry the Firebase uid as
a *field* rather than as the document key, so path-scoping is unavailable — but the client
already queries `collection('users').where('uid', isEqualTo: uid)`, which satisfies
Firestore's query-security constraint. A rule of the form:

```
allow read: if request.auth != null && resource.data.uid == request.auth.uid;
```

is enforceable and requires **no client change**. Apply the same shape to `chatHistory`
and `creditInfo` once Story 1 confirms how those documents carry ownership — if either
lacks a `uid` field, it must be server-only until a migration adds one.

**Writes on `users` become server-only** (`allow write: if false`) once Story 3 has moved
the write path. Do not close them before that ships or sign-up breaks.

**Finish with a terminal deny:**

```
match /{document=**} { allow read, write: if false; }
```

**Add explicit deny rules for each confirmed private collection** even though the terminal
rule already covers them, so their intended classification is visible during review.

**Store the rules in source control with tests.** This repository has never had a
`firestore.rules` file. Add it, add emulator-based rules tests, and add a deploy step or
document the manual deploy path and who holds console access.

**Because there is no staging project**, validate exhaustively in the Firebase emulator
before publishing, publish during a low-traffic window, and keep the previous ruleset
ready to restore. Do not publish a temporary allow-all to recover — that is explicitly
called out in ADO-1570 as what went wrong on AI Chat.

## Validation

- Emulator: a user with anonymous token A cannot read, list or query documents belonging
  to uid B, in `users`, `chatHistory` or `creditInfo`.
- Emulator: an unfiltered `collection('users').get()` fails.
- Emulator: writes to `users` fail for any client identity.
- Emulator: the terminal deny covers unknown and future collections.
- Live smoke after publish: anonymous startup, sign-in, provider upgrade, chat history
  load, credit display and purchase flow all verified on both platforms.
- Confirm backend Admin SDK operations continue working — Admin bypasses rules, so
  correctly configured backends should be unaffected.
- Rules-denial counts monitored in the console for 24 hours after publish.

## Acceptance criteria

- Unauthenticated GET `?pageSize=1` on `users` returns 403.
- Anonymous-Auth-then-GET `?pageSize=1` on `users` returns 403.
- Writes to `users` with an anonymous token return 403.
- `chatHistory` and `creditInfo` cannot be read or listed across users.
- No client can enumerate any of the three collections.
- All app flows verified working after publish.
- Rules and automated tests are stored in source control, with a documented deploy path.
- Verification evidence attached showing 403/403. No customer document dump attached.
