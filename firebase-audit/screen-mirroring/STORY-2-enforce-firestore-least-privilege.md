# STORY 2 — Screen Mirroring

**Created:** [SMIOSMAU-531](https://leadtech.atlassian.net/browse/SMIOSMAU-531) — status `Created`, unassigned

**Jira project:** `SMIOSMAU`
**Issue type:** User Story
**Priority:** Major
**Summary:** `[Backend] Implement and validate least-privilege Firestore access for Screen Mirroring`
**Epic:** `[Security] Protect Screen Mirroring Firestore review and quota data`
**Depends on:** Story 1 (the outcome decides whether `reviews` is closed outright)

---

## Context

This story implements Screen Mirroring's response to ADO-1570.

Affected Firebase projects: `screenmirroring-prod` and `screenmirroring-dev`. Requests
without a Firebase identity return 403; requests with a fresh anonymous identity returned
200 on `reviews` on 2026-08-24.

**Anonymous authentication cannot be disabled.** It is the only identity mechanism in the
app. `ScreenMirroring/Managers/AuthenticationManager.swift:33-46` signs in anonymously,
called on the boot path at `AppStateManager.swift:52-53`. Free-tier quota gating keys
entirely off `Auth.auth().currentUser?.uid`
(`ScreenMirroring/Shared/Core/FirebaseQuota/FirebaseQuotaService.swift:10`), and the uid
is also used as the Superwall analytics user id (`SuperwallManager.swift:225`). There is
no real sign-in anywhere in the app. Disabling anonymous auth breaks the free-tier limits
and the paywall analytics join.

**Two collections are in scope, not one.** ADO-1570 probed `reviews` only. The app also
writes `users/{uid}/quotas/{featureId}` at `FirebaseQuotaService.swift:24`, `:93` and
`:176`, holding `featureId`, `usageCount`, `lastResetDate`, `dailyLimit` and `periodDays`
for `screen_mirror`, `photos`, `videos` and `iptv`. This is paywall enforcement state and
must be owner-scoped, with `list` on the `quotas` collection group denied so one user
cannot enumerate another's.

**A ruleset already exists and was abandoned.** Branch
`origin/chore/firestore-security-rules`, commit `f773098`, adds a 62-line
`firestore.rules` plus `firebase.json` and `.firebaserc`. It was opened as PR #178, passed
CI (90.26% coverage, zero SwiftLint/Periphery issues), and was closed unmerged 70 minutes
later with no human review and no stated reason. Start from that branch rather than
rewriting. Its shape validation was checked against `UserQuotaUsage.swift` and the three
call sites and matches the Codable model field for field.

## Provenance

These findings were produced through an AI-assisted review of the application code,
cross-referenced against the non-destructive Firebase permission probe recorded in
ADO-1570. They must be validated by the technical owner before implementation.
Contact: filippo.tosetto@leadtech.com

## Technical guidance

**Export the deployed rules before changing anything.** There is no rules-as-code in the
repository today. As the abandoned PR's own description put it: *"Until now the rules
lived only in the Firebase console."* Capture the live ruleset from both projects and
diff it against the branch before publishing.

**Target shape:**

- Terminal `match /{document=**} { allow read, write: if false; }` as the floor.
- `reviews` — if Story 1 removed the write: `allow read, write: if false`. If retained:
  `allow create` only, with `request.resource.data.userId == request.auth.uid`, `rating`
  constrained to 1–5, `reviewText` length-capped, and `timestamp == request.time`
  (the client uses `serverTimestamp()`, which evaluates equal to `request.time`).
  `get`, `list`, `update` and `delete` denied.
- `users/{uid}/quotas/{featureId}` — owner-scoped read and write on
  `request.auth.uid == uid`, with `list` and `delete` denied, and a field allowlist
  matching `UserQuotaUsage`.

**Wire up deployment.** Merging deploys nothing — there is no CI step for
`firebase deploy --only firestore:rules`. Add it, or document the manual deploy path and
who holds console access.

**Deploy to `screenmirroring-dev` first, verify, then production.**

## Validation

Note the failure mode before deploying: `checkQuota` returns `.error` on a rules denial,
not `.exceeded`. Read `HomeQuotaCoordinator` to confirm how that error state is presented
before publishing, so a denial does not silently degrade into an unexpected paywall state.
Review submission failures set `lastError` and are not surfaced to the user.

- Emulator: anonymous read and list of `reviews` fail.
- Emulator: `collectionGroup("quotas")` list fails; a user cannot read another user's
  quota documents.
- Emulator: if review submission is retained, a valid create passes and list, get, update
  and delete fail; malformed, out-of-range and oversized submissions fail.
- `screenmirroring-dev` app: exercise screen mirror, photos, videos and IPTV to confirm
  quota checks still pass, plus a review submission if retained.
- Confirm rules-denial counts in the console are zero for legitimate flows after deploy.

## Acceptance criteria

- `reviews` cannot be listed, read, updated or deleted by mobile or anonymous clients on
  both projects.
- Unauthenticated GET `?pageSize=1` on `reviews` returns 403 on both projects.
- Anonymous-Auth-then-GET `?pageSize=1` on `reviews` returns 403 on both projects.
- Writes to `reviews` with an anonymous token return 403 on both projects.
- Quota documents are readable and writable only by their owner, and the `quotas`
  collection group cannot be listed.
- Free-tier gating for `screen_mirror`, `photos`, `videos` and `iptv` continues to work.
- Rules and automated tests are stored in source control and validated on
  `screenmirroring-dev` before production.
- A deploy path for rules exists and is documented.
- Verification evidence attached showing 403/403. No customer document dump attached.
