# STORY 1 — ChatUltra

**Created:** [CBMAU-276](https://leadtech.atlassian.net/browse/CBMAU-276) — status `Created`, unassigned

**Jira project:** `CBMAU`
**Issue type:** User Story
**Priority:** Critical
**Summary:** `Export the deployed ruleset and confirm the full extent of the exposure`
**Epic:** `[Security] Protect ChatUltra Firestore user and chat data`

---

## Context

ADO-1570 probed one collection, `users`. The app declares three
(`lib/product/constants/enums/firebase_paths.dart`): `users`, `creditInfo` and
`chatHistory`. Nobody has confirmed whether the other two are exposed, and one of them
holds user conversation content.

This story exists because **the severity of the incident is currently unknown**. If
`chatHistory` is readable under the same rule, this stops being a user-record leak and
becomes a chat-content leak for 52,355 users. Every downstream decision — priority,
notification obligations, how the remaining stories are sequenced — depends on that
answer. It must be settled before anything else in this epic.

No rules file exists in the repository, so the deployed ruleset can only be obtained from
the Firebase console or via `firebase firestore:rules get`.

## Provenance

These findings were produced through an AI-assisted review of the application code,
cross-referenced against the non-destructive Firebase permission probe recorded in
ADO-1570. They must be validated by the technical owner before implementation.
Contact: filippo.tosetto@leadtech.com

## Technical guidance

1. Export the deployed ruleset from `chatai2-32311` and commit it to the repository
   verbatim as the starting baseline. This is the first time it will exist in source
   control.

2. Enumerate the actual collection inventory in the project. The three declared in
   `FirebasePaths` are what the app uses; the database may hold more, including
   collections left over from the acquisition.

3. Run the ADO-1570 probe method against `chatHistory` and `creditInfo`, not just `users`:
   unauthenticated GET `?pageSize=1`, then anonymous-Auth-then-GET `?pageSize=1`. Record
   the status codes. **Do not dump document values, and do not attach customer content to
   Jira** — record counts and status codes only.

4. Establish whether writes are open on `users`. ADO-1570 states several production
   collections accepted anonymous writes (probe: PATCH with
   `currentDocument.exists=true` returning "No document to update") but does not name
   this project. Confirm it.

5. Record the outcome on the epic. If `chatHistory` is exposed, raise it immediately
   rather than waiting for the remaining stories — that is a disclosure question, not
   only an engineering one.

## Validation

- The exported ruleset is committed and matches what the console reports.
- Probe results for all three collections are recorded with status codes.
- Write-probe result for `users` is recorded.

## Acceptance criteria

- The deployed ruleset for `chatai2-32311` is in source control.
- Read exposure of `users`, `chatHistory` and `creditInfo` is confirmed and documented
  with status codes, not inference.
- Write exposure of `users` is confirmed and documented.
- The full collection inventory of the project is listed.
- No customer document values are recorded in Jira or in the repository.
- If `chatHistory` is confirmed exposed, the finding is escalated the same day.
