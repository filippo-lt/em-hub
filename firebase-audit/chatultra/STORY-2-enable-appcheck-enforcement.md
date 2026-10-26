# STORY 2 — ChatUltra

**Created:** [CBMAU-277](https://leadtech.atlassian.net/browse/CBMAU-277) — status `Created`, unassigned

**Jira project:** `CBMAU`
**Issue type:** User Story
**Priority:** Critical
**Summary:** `Enable App Check enforcement for Firestore on chatai2-32311`
**Epic:** `[Security] Protect ChatUltra Firestore user and chat data`

---

## Context

This is the fastest available reduction in exposure and it requires no code change.

App Check is **already implemented in the client**. `firebase_app_check_service.dart`
activates it with Play Integrity on Android and App Attest on iOS in release builds. The
client-side work is done.

Because raw anonymous tokens minted with the public API key evidently reach the data
plane, **App Check enforcement is switched off for Firestore in the Firebase console**.
Turning it on requires an attestation from a genuine, unmodified app build before
Firestore will serve a request, which blocks the curl-and-public-API-key attack path
described in ADO-1570 outright.

This does not replace the rules work. App Check attests *that the caller is the real app*,
not *that the caller is entitled to the data* — a real app instance with an anonymous
token would still be able to read whatever the rules allow. It is a containment measure
that buys time for the write-path migration and the rules change, both of which carry
deploy risk on a project with no staging environment.

## Provenance

These findings were produced through an AI-assisted review of the application code,
cross-referenced against the non-destructive Firebase permission probe recorded in
ADO-1570. They must be validated by the technical owner before implementation.
Contact: filippo.tosetto@leadtech.com

## Technical guidance

1. Confirm current App Check enforcement state for Firestore on `chatai2-32311`.

2. Before enforcing, check the App Check metrics page for the proportion of requests
   arriving with a valid attestation. Enforcing while a meaningful share of live traffic
   is unattested will break those clients. Older app versions still in the field are the
   usual cause.

3. Enforce for Firestore once the attested share is high enough to be safe. Monitor
   rejection rates immediately after.

4. `chatai2-32311` has no dev/prod split, so this change lands directly on production.
   Enable during a low-traffic window and be prepared to disable quickly.

## Validation

- App Check metrics show the attested request share before enabling enforcement.
- After enforcement: a request carrying only an anonymous ID token and the public API key,
  without an App Check token, is rejected.
- The shipped app on both platforms continues to sign in, load chat history and read
  credit info normally.
- Rejection rates are monitored for at least 24 hours after enabling.

## Acceptance criteria

- App Check enforcement is enabled for Firestore on `chatai2-32311`.
- A request without a valid App Check token is rejected at the data plane.
- No regression in live traffic; rejection rate returns to baseline.
- The pre-enforcement attested share is recorded on the ticket.
