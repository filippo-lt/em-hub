# STORY 2 — iMote

**Jira project:** `IMIOSMAU`
**Issue type:** User Story
**Priority:** Critical
**Summary:** `[Backend] Implement and validate least-privilege Firestore access for iMote`
**Epic:** `[Security] Protect iMote Firestore device and rating data`
**Depends on:** Story 1 (the outcome decides whether `deviceInfo` is closed outright)

---

## Context

This story implements iMote's response to ADO-1570.

Affected Firebase projects: `imote-dev` and `imote-prod`. Requests without a Firebase
identity return 403; requests with a fresh anonymous identity returned 200 on
`imote-dev/deviceInfo` on 2026-08-24. `imote-prod` has not been probed but runs identical
client code and must be treated as equally exposed until proven otherwise.

**Anonymous authentication cannot be disabled.** It is the only identity mechanism in the
app. iOS signs in via `AuthLoginManager.signInAnonymously`
(`iMote/Helper Class/FireStore/Database Managers/AuthLoginManager.swift`), called from
inside `DeviceInfoManager.send/update` and `RateAppManager`. Android calls
`signInAnonymously` unconditionally at `MainActivity.kt:97` on every launch. There is no
email, Google or Apple sign-in anywhere in either codebase. ADO-1570's
"require a real signed-in user" remediation branch is therefore unavailable; the fix is
rules scoping plus the write removal in Story 1.

**A ruleset already exists and was abandoned.** Branch
`origin/chore/firestore-security-rules`, commit `d53ed9cc` (2026-08-26), adds
`firestore.rules`, `firebase.json` and `.firebaserc`
(`{"dev":"imote-dev","prod":"imote-prod","default":"imote-dev"}`). It was opened as
PR #604 and closed unmerged 80 minutes later with no human review. The only review was
an automated one flagging `created_date == request.time` as rejecting valid writes.
**That flag appears to be incorrect** — the client sets `created_date` via
`FieldValue.serverTimestamp()`, which evaluates equal to `request.time` inside rules.
Start from that branch rather than rewriting.

## Provenance

These findings were produced through an AI-assisted review of the application code,
cross-referenced against the non-destructive Firebase permission probe recorded in
ADO-1570. They must be validated by the technical owner before implementation.
Contact: filippo.tosetto@leadtech.com

## Technical guidance

**Export the deployed rules from both projects before changing anything.** There is no
rules-as-code in either repository today — the live rulesets exist only in the Firebase
console and have never been reviewed or diffed. Capture them first.

**Two defects in the drafted ruleset must be fixed before it ships.**

1. *It rejects every Android rating.* Android's `SubmitRatingUseCase` sends an extra field
   `appVersionCode`, and sends `created_date` as a **formatted date String**, not a server
   timestamp (`FirestoreConstants`, `Constants.kt:282`). Both the `hasOnly([...])` clause
   and the `created_date == request.time` clause reject it. Android also writes `rateApp`
   with `documentPath = androidId`, so a repeat rater performs an **update**, which
   `allow update: if false` denies outright. The drafted rules were validated against the
   iOS models only.

2. *iOS `deviceInfo` writes use `setData(merge: true)`.* These succeed today only because
   the document id is always freshly generated. A create-only rule is correct but will
   break if that ever changes.

**Target shape.** Neither app ever reads `deviceInfo` or `rateApp`, so both are write-only
collections and reads can be denied outright:

- `deviceInfo` — if Story 1 removed the write: `allow read, write: if false`. If the write
  was retained in reduced form: `allow create` with shape validation, and
  `get, list, update, delete: if false`.
- `rateApp` — `allow create` with a field allowlist that is the **union of the iOS and
  Android payloads**, accepting `created_date` as timestamp or string, and permitting
  `update` for the Android `androidId`-keyed document (or change Android to a random
  document id and keep create-only). `get, list, update, delete` otherwise denied.
- `ContactUS` and any other confirmed client collection — classified explicitly.
- Terminal `match /{document=**} { allow read, write: if false; }`.

**Wire up deployment.** The PR author noted that merging deploys nothing — there is no CI
step for `firebase deploy --only firestore:rules` in the repository. Add it, or document
the manual deploy path and who holds console access. Without this the ticket can be
closed with the hole still open.

**Deploy to `imote-dev` first, verify, then `imote-prod`.**

## Validation

**A bad rules deploy will not be visible in the app.** `FirestoreService.send` swallows
errors and reports `.success` on a 10-second timeout. Verify through Firestore write
metrics and rules-denial logs in the console, never by exercising the app and seeing no
error. This is the single most important line in this ticket.

- Emulator: anonymous read and list of `deviceInfo` fail.
- Emulator: a valid `rateApp` create passes **on both the iOS and the Android payload
  shape**; list, get, update and delete fail; malformed and oversized submissions fail.
- Emulator: unknown collections are denied by the terminal rule.
- `imote-dev` app: verify TV discovery, connection, casting, screen mirroring and rating
  submission on both platforms.
- Confirm rules-denial counts in the console are zero for legitimate flows after deploy.

## Acceptance criteria

- `deviceInfo` cannot be listed or read by mobile or anonymous clients on `imote-dev` and
  `imote-prod`.
- Unauthenticated GET `?pageSize=1` on `deviceInfo` returns 403 on both projects.
- Anonymous-Auth-then-GET `?pageSize=1` on `deviceInfo` returns 403 on both projects.
- Writes to `deviceInfo` with an anonymous token return 403 on both projects.
- Rating submission continues to work on iOS **and** Android, and submitted ratings
  cannot be read, listed, changed or deleted by clients.
- Rules and automated tests are stored in source control and validated on `imote-dev`
  before production.
- A deploy path for rules exists and is documented.
- Verification evidence (verifier output or equivalent curl transcript) attached showing
  403/403. No customer document dump attached.
