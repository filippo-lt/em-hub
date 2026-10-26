# MAINTENANCE — Face AI

**Created:** [FAIOSMAU-790](https://leadtech.atlassian.net/browse/FAIOSMAU-790) — status `Created`, unassigned

**Jira project:** `FAIOSMAU`
**Issue type:** Maintenance (`Corrective` / `Once`)
**Priority:** Major
**Labels:** `SOC`, `firestore`
**Parent:** ADO-1570 (named in References; no Jira link)
**Modelled on:** `QRNIOSMAU-877`

Single ticket rather than an Epic + Story pair, matching the IT Security fan-out pattern
used for Translator GO and QR Now. Acceptance criteria live in the description body, as
they do in `QRNIOSMAU-877`, rather than in the Acceptance Criteria field.

---

Goal

Close the anonymous-Auth / public Firestore data plane on Face AI Firebase projects so a stranger cannot read user or customer data.

Context

Source: org-wide Firestore sweep after the AI Chat incident — ADO-1570.

Firebase security rules grant read/write once request.auth != null, and Anonymous Authentication is enabled. Anyone on the internet can mint an anonymous token with the public API key and then list user collections. Unauthenticated GET returning 403 is expected and is a false closed signal — the hole is any anonymous token.

Affected Firebase projects

Production
faceai-prod / iOSUserCredits — count ~835
Fields: creditsPurchased, lastDailyQuotaClaimedAt, remainingDailyQuota, remainingPurchasedCredit, revenueCatId

Dev
faceai-dev / iOSUserCredits — count ~836

(Probe confirmed HTTP 200 with anonymous Auth on 2026-08-24. No document values were dumped.)

Findings from code review

These four points change the shape of the fix and should be read before any rules are written.

1. iOSUserCredits is no longer used by the app. It was written by CreditManager.swift, which was deleted on 2026-02-17 in commit b2b1f8cb during the quota refactor. Credits and quota now run through the backend quota service: UserSubscriptionService performs POST /login with an App Check token, receives a bearer JWT, and calls check_user_quota / increment_user_quota. UserQuotaModel is read-only from the server. Consequences: closing iOSUserCredits to clients has zero blast radius and needs no app change, and an anonymous write to it would grant nothing the app honours — there is no monetisation bypass. The residual risk is the exposure of ~835 production and ~836 dev stale records containing revenueCatId billing identifiers with no remaining purpose.

2. Anonymous Authentication cannot be disabled, and a blanket default-deny will break the app. Every Firestore read is gated behind ensureAuthenticated() calling signInAnonymously() (FirebaseService.swift:51, :63, :115, :150). Those reads drive the home screen and the entire filter and editor experience. There is no email, Google or Apple sign-in anywhere in the codebase. Publishing a default-deny, or turning off anonymous Auth, leaves users with a blank home screen and no filters on next launch. This is the same failure mode ADO-1570 records for AI Chat.

3. A second client-writable collection is not in the probe list. iOSAppRatings is written via FirebaseService+RatingExtensions.swift:10 into submitData, which calls setData at FirebaseService.swift:204. Any anonymous token can create or overwrite rating documents. This is the same shape as the screenmirroring-prod / reviews entry in ADO-1570 and should be closed in the same change. Note that submitData does not call ensureAuthenticated() first, so a uid-binding rule could reject legitimate ratings if the session has lapsed — a client-side fix belongs alongside the rule.

4. App Check is already implemented client-side (AppDelegate.swift:31, App Attest on device, debug provider on simulator). Whether enforcement is enabled for Firestore is a console setting that could not be verified from code. Enabling it blocks the public-API-key attack path without a code change, and is the fastest available mitigation.

There is no firestore.rules, firebase.json or rules-as-code in either Face AI repository, and no firestore rules resource in the Terraform monorepo. The deployed ruleset exists only in the Firebase console. Export it before making any change.

Scope

- Export the deployed rules from faceai-prod and faceai-dev before changing anything, and commit them to source control as the baseline.
- iOSUserCredits: server-only (read and write denied) on both projects. No app change required.
- Delete or archive the stale iOSUserCredits documents on both projects once access is closed.
- Content catalogs (MainScreenItems, EditorScreenCatalogs, EditorScreenItems, FilterCatalogs, FilterItems, BackgroundCatalogs, BackgroundItems, AdjustItems, BlurItems, CropItems, PaintItems, OverlayItems, VignetteItems): keep read for authenticated identities and add write denied. Do not default-deny these.
- iOSAppRatings: create-only with a field allowlist and the document userId bound to request.auth.uid; deny read, list, update and delete.
- Finish with a terminal deny-all rule covering current and future collections.
- Enable App Check enforcement for Firestore, after checking the attested-request share in App Check metrics.
- Store rules and rules tests in source control with a documented deploy path.
- Validate on faceai-dev first, then apply to faceai-prod.
- Do not publish a temporary allow-all to keep the app up.

Acceptance criteria

- Unauthenticated GET ?pageSize=1 on iOSUserCredits is 403 (prod + dev).
- Anonymous Auth then GET ?pageSize=1 on iOSUserCredits is 403 (prod + dev).
- Writes to iOSUserCredits with an anonymous token are 403.
- iOSAppRatings cannot be listed, read, edited or deleted by clients, and invalid or oversized rating documents are rejected.
- Rating submission continues to work from the app.
- The home screen, filter list and editor catalogs continue to load on both projects after the change.
- Rules and automated tests are stored in source control and validated in faceai-dev before production.
- Verification evidence (HTML verifier or equivalent curl transcript) attached as a comment with 403/403.
- No customer document dump attached to Jira.

Risks

A default-deny publish can break the live app (this happened on AI Chat). Face AI is specifically exposed to this because every content read requires an anonymous identity — a blanket deny produces an empty home screen with no error message. Scope the change to iOSUserCredits and iOSAppRatings, leave catalogue reads working for authenticated identities, and test on faceai-dev first.

Provenance

The probe results are from ADO-1570. The code-review findings above were produced through an AI-assisted review of the faceai_ios and faceai_backend repositories and must be validated by the technical owner before implementation. Contact: filippo.tosetto@leadtech.com

References

Parent: ADO-1570
Related closed AI Chat fix: ADO-1565
Sibling per-app tickets: TGIOSMAU-1906, QRNIOSMAU-877, TTIOSMAU-2570 / TTIOSMAU-2571, VUIOSMAU-2744 / VUIOSMAU-2745, PUIOSMAU-2263 / PUIOSMAU-2264, ADIOSMAU-2259, SMIOSMAU-529, CBMAU-275
