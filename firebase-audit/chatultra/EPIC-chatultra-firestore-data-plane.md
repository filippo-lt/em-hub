# EPIC — ChatUltra

**Created:** [CBMAU-275](https://leadtech.atlassian.net/browse/CBMAU-275) — status `Created`, unassigned

**Jira project:** `CBMAU`
**Issue type:** Epic
**Priority:** Critical
**Summary:** `[Security] Protect ChatUltra Firestore user and chat data`
**Parent:** ADO-1570 (link as *relates to*)

---

## Executive summary

ChatUltra's follow-up to the cross-app Security initiative ADO-1570.

ChatUltra's Firebase project `chatai2-32311` allows a fresh anonymous app identity to
list the `users` collection. ADO-1570 reports approximately 52,355 documents, confirmed
HTTP 200 with anonymous authentication on 2026-08-24. The fields recorded in the ticket
match ChatUltra's `AppUser` model exactly
(`module/gen/lib/src/model/app_user_model.dart`), which positively identifies the
collection as ChatUltra's:

```
canMakePayments, creationTime, deviceId, deviceModel, displayId, email,
isAdult, isPremium, name, premiumProduct, provider, uid, updateTime
```

An attacker could automate anonymous sign-in with the public API key shipped inside the
app, receive an ID token, and bulk-download 52,355 records containing names, email
addresses, device identifiers, premium and payment status, and an adult-content flag —
without knowing any customer or document ID. **This is the largest confirmed
personal-data exposure in the M&A portfolio.**

**The exposure is wider than ADO-1570 records.** The app declares three Firestore
collections at `lib/product/constants/enums/firebase_paths.dart`:

```dart
enum FirebasePaths { users('users'), creditInfo('creditInfo'), chatHistory('chatHistory'); }
```

ADO-1570 probed `users` only. `chatHistory` holds user conversation content. If the
deployed rule is a blanket grant to any signed-in identity — which the probe result
implies — then 52,355 users' chat transcripts are exposed alongside their names and email
addresses. Confirming this is the first story in this epic, and the answer determines
the true severity of the incident.

**Writes are the second concern.** ADO-1570 records that several production collections
accepted anonymous writes. `_saveCrudUser()` (`auth_service.dart:185`) writes the entire
`AppUser` record client-side. If writes are open, any anonymous token can overwrite or
delete user records and tamper with `isAdult` and premium state. Note that this is a
data-integrity and GDPR problem rather than a revenue one: in-app entitlement is read
from `premiumCubit` (RevenueCat/Helium), not from Firestore, and the `isPremium` field
accepted by `BaseCreditServicePayload` is never consumed anywhere in the app. A write
hole here is not a clean paywall bypass.

**Anonymous authentication cannot be disabled.** `lib/product/cubit/auth_cubit.dart:44`
signs every user in anonymously at startup; `auth_service.dart:245` re-anonymises on
token failure; `getIdToken()` forces an anonymous login when no user is present. The
`provider` field exists because users can *upgrade* to a real provider, not because they
start with one. Disabling anonymous auth breaks the app.

**There is no rules-as-code.** No `firestore.rules`, no `firestore` block in
`firebase.json`, no rules tests anywhere in the repository. The deployed ruleset exists
only in the Firebase console, so nobody can review, diff or regression-test the fix, and
there is no record of who last changed it. For an acquired codebase that is a finding in
its own right.

## Expected outcome

- The live ruleset is exported and the full exposure of `users`, `chatHistory` and
  `creditInfo` is confirmed and recorded.
- App Check enforcement is enabled for Firestore, blocking the anonymous-token attack
  path from non-app clients immediately and without a code change.
- Client-side writes to `users` move behind a trusted backend path, so anonymous writes
  to the probed collection return 403.
- `users`, `chatHistory` and `creditInfo` are readable only by their owner, and cannot be
  listed across users.
- Firestore rules are stored in source control with tests and a deploy path.

## Ownership note

`chatai2-32311` is a single Firebase project with no dev/prod split, which removes the
staging step ADO-1570's remediation strategy relies on ("use a staging project to test
rules first"). Rules changes here land directly on production. That materially raises the
risk of the deploy and should shape sequencing — App Check enforcement and the write-path
migration both reduce exposure before any rules change is published.

The only engineers with recent commits on this repository are from the external studio
currently being off-ramped. Assigning this epic requires a staffing decision.
