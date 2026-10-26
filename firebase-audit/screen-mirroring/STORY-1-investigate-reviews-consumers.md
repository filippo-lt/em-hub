# STORY 1 — Screen Mirroring

**Created:** [SMIOSMAU-530](https://leadtech.atlassian.net/browse/SMIOSMAU-530) — status `Created`, unassigned

**Jira project:** `SMIOSMAU`
**Issue type:** User Story
**Priority:** Major
**Summary:** `Confirm whether reviews has any consumer, then remove or retain the write`
**Epic:** `[Security] Protect Screen Mirroring Firestore review and quota data`

---

## Context

This story decides the shape of the fix. It must complete before the rules story ships.

`reviews` is written by the iOS app at
`ScreenMirroring/Managers/FirestoreManager.swift:78` and `:86`. The `userId` field is
taken from `authManager.currentUserId` (`FirestoreManager.swift:45`), which is the
anonymous Firebase uid — it identifies a device, not a person.

**No code in the app reads this collection back.** There is no in-app admin view, no
moderation screen and no display surface for submitted reviews. A repository-wide search
found writes only.

The volume is itself a signal: approximately 57 documents in production across the app's
entire lifetime. For a shipped consumer app that suggests the submission entry point is
either buried, vestigial or rarely reached. Confirm whether the flow is still reachable
in the current UI as part of this investigation.

That the app does not read the collection does not prove nobody does. A BigQuery export,
a periodic console check by product or support, or a dashboard would not appear in the
codebase.

## Provenance

These findings were produced through an AI-assisted review of the application code,
cross-referenced against the non-destructive Firebase permission probe recorded in
ADO-1570. They must be validated by the technical owner before implementation.
Contact: filippo.tosetto@leadtech.com

## Technical guidance

1. Ask the Screen Mirroring PO, and whoever owns app-feedback or growth reporting, one
   question: does anything read `reviews`? Name the person who answered and record the
   answer on this ticket.

2. Confirm whether the review submission UI is still reachable in the shipped app. If it
   is dead UI, that settles the question.

3. **If there is no consumer:** remove the write. The collection then receives no new
   documents and can be closed server-only in Story 2. Archive or delete the existing 57
   production and 30 dev documents.

4. **If there is a consumer:** retain submission as a create-only path with field and
   length validation, and note that read, list, update and delete must still be denied to
   clients in Story 2. Free-text `reviewText` should carry an explicit length cap, since
   whoever reads it downstream is the party exposed to unvalidated input.

## Validation

- Search the codebase and confirm no remaining client write to `reviews` (removal branch).
- Confirm with the named owner that removal breaks no downstream report or process.
- Exercise the app and confirm screen mirroring, photos, videos and IPTV are unaffected.
  Firestore is not on the mirroring path.

## Acceptance criteria

- A named owner has answered whether `reviews` has a consumer, and the answer is recorded
  on this ticket.
- A decision is recorded on whether the submission UI is still reachable.
- Either the client write is removed, or the retained submission path is specified with
  its field allowlist and length limits for Story 2 to implement.
- Existing `reviews` documents are archived or deleted where the write was removed.
