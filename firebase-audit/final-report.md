# Firebase / Firestore Security Audit — Portfolio Report

**Date:** 2026-08-28
**Author:** Filippo Tosetto
**Trigger:** ADO-1570 — *[Firestore] Close public data plane (anonymous Auth) on remaining Apps GCP projects* (Critical, IT Security, status **Closed**, resolved 2026-08-25)

---

## 1. What ADO-1570 found

Firebase security rules on many Apps GCP projects grant read — and often write — once
`request.auth != null`, while Anonymous Authentication is enabled on the same project.
Anyone on the internet can call `accounts:signUp` with the public API key already shipped
inside the apps, receive an ID token, and then list user collections.

An unauthenticated GET returns 403, which makes a pasted REST URL look closed. **That is a
false closed signal.** The hole is not "no token" — it is "any anonymous token".

IT Security probed 207 targets across the Leadtech and 1eapp.net GCP orgs. Counts are
from 2026-08-21, with HTTP 200 reconfirmed on 2026-08-24.

## 2. Scope and method of this audit

Eight apps were reviewed against the ticket: AI Design, iMote, Screen Mirroring, Face AI,
ChatUltra, PDF Editor, Step Counter, Music Player. Goya and Mirage were added afterwards
as portfolio-risk checks. Tattooist was reviewed but is excluded from the filing plan
because tickets already exist for it.

Each app was audited from its local clone: Firestore rules or their absence, the full set
of collections the client touches, whether the app depends on anonymous auth, evidence of
remediation since 2026-08-21, blast radius of a default-deny publish, and whether a
sibling Jira ticket exists.

**One limitation applies to every finding below.** No live ruleset could be read. Rules
are console-managed on every project audited except TruthSeeker web — there is no
`firestore.rules` in any of these repositories. Every statement about a *current* rule is
inferred from IT Security's probe results plus client code, not read from the deployed
configuration. Exporting the live rules is the first step of every remediation story.

## 3. Headline

**ADO-1570 is Closed. Nothing was fixed on any of the audited apps.** No deployed rules
change exists anywhere in the portfolio as of 2026-08-28. The ticket's own acceptance
criteria require a per-project 403/403 verifier transcript; none exists for these apps.

## 4. Per-app findings

### 4.1 Apps with tickets in this batch

**ChatUltra — `chatai2-32311` — Critical.** The largest confirmed personal-data exposure
in the portfolio: ~52,355 `users` documents with name, email, deviceId, premium state and
an adult-content flag. The `AppUser` model matches ADO-1570's field list exactly, which
positively identifies the collection. **Two further collections are declared in the app
and were never probed** — `chatHistory` (conversation content) and `creditInfo`. If the
deployed rule is a blanket grant, this is a chat-content leak, not just a user-record
leak. Anonymous auth is load-bearing. No rules-as-code. No dev/prod split, so any rules
publish lands directly on production. `users` is written client-side, so ADO-1570's
acceptance criterion #3 requires a backend write-path migration — the only app in the
batch where that is true. Only recent committers are from the studio being off-ramped.

**iMote — `imote-dev` probed, `imote-prod` not — Critical.** ~14,600 `deviceInfo`
documents, each holding a TV serial number, LAN IP, Wi-Fi network name, user-set device
name, make and model. Personal data under GDPR Art. 4(1). Two aggravating facts: the
`Dev`/`DevRelease` build configurations ship to **TestFlight** under the production bundle
id, so "only dev" is false comfort; and **`imote-prod` is absent from ADO-1570 entirely**
while running identical client code as the target of every App Store build — its exposure
is unknown rather than closed. Before June 2026 the build config sent all non-Debug builds
to Prod, so its document count is structurally likely to exceed dev's. Nothing reads
`deviceInfo` in either app — it is write-only telemetry.

**Screen Mirroring — `screenmirroring-prod` / `-dev` — Major.** The smallest exposure in
ADO-1570: 57 production `reviews` documents, no PII beyond a rating and free text, with an
anonymous uid that maps to a device. Genuinely low severity. Two things raise it above
"ignore": the app also writes **`users/{uid}/quotas`**, which ADO-1570 never probed and
which is free-tier paywall enforcement; and the repository has had no merge since
2026-07-03, so there is no active owner. Nothing reads `reviews`.

### 4.2 Apps with no tickets in this batch

**AI Design — `aihomedesign-prod` / `-dev` — covered by existing work.** Absent from
ADO-1570, and **more exposed than anything in it**: `allow read: if true` on 17
collections, in both projects, byte-identical rulesets. No token required at all — this is
the AI Chat shape, not the anonymous-token shape. What leaks is catalog and prompt IP
rather than user PII, which is almost certainly why the sweep dropped it (see §5.3).
Already diagnosed and ticketed by Vlad on 2026-08-27 — `ADIOSMAU-2259` (rules),
`ADIOSMAU-2260` (iOS silent sign-in failure), `ADIOSMAU-2261` (Android ordering + swallowed
failure). No new tickets needed. One residual item sits inside `2261`: `androidUserStats`
carries `allow read, write: if request.auth != null` and holds leftover data Android no
longer uses — Vlad flagged it and offered to split it out. That is the one collection in
AI Design that genuinely matches the ADO-1570 pattern.

**Face AI — `faceai-prod` / `-dev` — nothing to do.** `iOSUserCredits` (~835 prod, ~836
dev) is **dead code**. It was written by `CreditManager.swift`, deleted on 2026-02-17 in
commit `b2b1f8cb` during the quota refactor. Credits now run through the backend quota
service behind App Check and a bearer JWT, and `UserQuotaModel` is read-only from the
server. An anonymous write to `iOSUserCredits` today would grant nothing the app would
honour — there is no monetisation bypass. Residual is ~835 stale `revenueCatId` billing
identifiers and an `iOSAppRatings` write hole. Both are real but minor.

**PDF Editor — `main-pdf-editor` — a real issue, but not this one.** No Firestore and no
Firebase Auth at all. Zero ADO-1570 exposure; correctly absent from the ticket. Its
problem is **Cloud Storage**: user PDFs upload to `uploads/{original-basename}` — flat,
unscoped, and named after the user's own filename — with no `storage.rules` in the
repository and no auth in the app, so the rule can only be `if true` or App Check-gated.
Filenames like `invoice.pdf` or `CV.pdf` are trivially guessable. Worse, a flat namespace
means **two users uploading the same filename overwrite each other**, and
`getDownloadURL()` then returns user B a link to user A's document — a data leak arising
from normal use, not only from attack. This is the app that already had a GDPR incident.
Also: `release.keystore` has been committed since 2025-12-10 (passwords are in CI, not the
repo — still a rotate-and-purge). **Deserves its own ticket, outside this batch.**

**Step Counter and Music Player — clean.** Firebase dependencies are Crashlytics,
Analytics and Remote Config only. No Auth, no Firestore, nothing in the data plane to
expose. One residual: `google-services.json` is gitignored and CI-injected, so their GCP
project ids could not be confirmed from source — meaning it cannot be *proven* they were
absent from the sweep under some other name. With no Auth and no Firestore SDK, even a
provisioned database has no client path into it. No action recommended.

### 4.3 Portfolio risk found outside the audited set

**Goya (~158,606 docs) and Mirage (~113,855 docs) are Tattooist-class exposures.**
Verified, not inferred. Both `_infra` repositories contain
`shared/services/token.services.js` byte-identical to Tattooist's:

```js
db.collection("tokens").doc(customer_id).set({ token, tokenExpirationTime,
  refreshToken, refreshTokenExpirationTime }, { merge: true })
```

and both compare the stored value directly as the bearer credential — Goya
`openai/middlewares/auth.middleware.js:34`, Mirage `shared/utils/auth.util.js:33`:

```js
const usersToken = await fetchTokens(user);
if (!usersToken || usersToken.token !== token) { ... }
```

So `goyaai-prod/tokens` and `mirageai-prod/tokens` are **not token metadata — they are
replayable session credentials keyed by RevenueCat customer_id**, exactly as in Tattooist's
1.18M-document collection. Approximately 272,000 additional impersonation sets across the
two apps. ADO-1570 describes all three with the same flat framing and undersells all three
identically.

Both also carry `api_keys` collections that ADO-1570 never probed — Goya `api_keys`,
Mirage `api_keys` **and** `all_api_keys`. On Tattooist that collection proved stale
(credentials had moved to Secret Manager) but potentially still valid. Goya's and Mirage's
contents are unknown.

Neither repository has a `firestore.rules` or `.firebaserc`. **Neither has had a commit
since October 2025** — these are the two genuinely ownerless apps in the estate, and they
hold the second and third largest credential exposures in it.

*Caveat: these clones were last synchronised in October 2025 and origin may have moved.
Re-fetch before quoting line numbers.*

## 5. Cross-cutting findings

### 5.1 Two finished fixes were thrown away

iMote PR #604 and Screen Mirroring PR #178 were both authored by the same engineer, both
passed CI, and were both **closed unmerged at the identical timestamp, 2026-08-26T13:53Z**,
with no human review and no stated reason. That is one bulk action, not two independent
decisions; the timing coincides with that engineer's reassignment. iMote's only review was
automated, flagging `created_date == request.time` as rejecting valid writes — **that flag
is incorrect**, since the client uses `serverTimestamp()`, which evaluates equal to
`request.time` inside rules. Both branches are intact and reusable.

Separately, **merging either PR would have deployed nothing.** Neither repository has CI
wiring for `firebase deploy --only firestore:rules`. Both tickets could have been closed
with the hole still open.

### 5.2 Ticket coverage is incomplete and the parent hides it

Sibling per-app tickets exist for Translator GO (`TGIOSMAU-1906`), QR Now
(`QRNIOSMAU-877`), Video Up (`VUIOSMAU-2744/2745`), Photo Up (`PUIOSMAU-2263/2264`),
Tattoo (`TTIOSMAU-2570/2571`), Spam Safe and AI Cleaner. **None existed for Screen
Mirroring, Face AI or iMote.** Of those that exist, only Translator GO and QR Now are
linked to ADO-1570 — the Video Up, Photo Up and Tattoo pairs, and Vlad's AI Design set,
are all orphaned. A `Closed` parent with unlinked, unstarted children is how this work
gets lost.

### 5.3 The sweep's inclusion filter dropped a whole class of exposure

ADO-1570's stated criterion is "a stranger can read **user or customer** data". AI Design
leaks catalog and prompt IP rather than PII, and was dropped despite being *more* open
than anything on the list — no authentication required at all. The same filter would drop
any app whose exposure is intellectual property, configuration or operational data rather
than personal data. Worth raising with IT Security as a methodology point, not just an
AI Design point.

### 5.4 A prior formal security assessment missed this class entirely

`goya_infra/assessment/security-assessment.md` (September 2025) passed Goya with
"Strong secrets management, Robust token validation". Its Firestore line reads
*"Firestore security rules (implied through Firebase Admin usage)"*, and later
*"Firestore security through Firebase Admin"*. The assessment concluded the data plane was
safe **because the backend uses the Admin SDK** — which bypasses rules entirely and says
nothing about what a client can read.

A formal security review green-lit Goya eleven months before a sweep found ~158,000
exposed credential records in it. The reasoning error is reusable and is arguably the more
important finding than the rules themselves.

### 5.5 Anonymous auth is load-bearing almost everywhere

In iMote, Screen Mirroring, ChatUltra, Face AI, AI Design and Tattooist, anonymous
authentication is the *only* identity mechanism. There is no email, Google or Apple
sign-in. ADO-1570's remediation branch "disable Anonymous Authentication if the product
does not need it" is therefore unavailable across the portfolio; every fix is rules
scoping, write removal, or a backend write path.

### 5.6 App Check is built but not enforced

Face AI, AI Design and ChatUltra all implement App Check client-side with App Attest and
Play Integrity. Because raw anonymous tokens reach the data plane, **enforcement is off in
the console** for those projects. Enabling it is a same-day, zero-code reduction in
exposure that blocks the curl-and-public-API-key path. It does not replace rules work —
it attests that the caller is the real app, not that the caller is entitled to the data.

### 5.7 The systemic root cause: rules are not code

Not one audited repository contains a `firestore.rules` file. Rules are console-managed,
unversioned, unreviewable in a pull request, with no record of who changed what or when.
That is why nobody could confirm the current state of any project without console access,
and why drift is invisible.

The single exception is **TruthSeeker web** — committed `firestore.rules`, terminal
default-deny, per-uid scoping, server-only collections, rules regression tests and threat
reasoning documented inline. It is also the only internally owned repository in the set.
It should be used as the reference implementation.

## 6. Filing plan

| App | Filed | Contents |
|---|---|---|
| **iMote** | 1 Epic + 2 Stories | Investigate `deviceInfo` consumers -> enforce least-privilege rules |
| **Screen Mirroring** | 1 Epic + 2 Stories | Investigate `reviews` consumers -> enforce least-privilege rules |
| **ChatUltra** | 1 Epic + 4 Stories | Export rules & confirm exposure -> App Check enforcement -> move user writes server-side -> enforce rules |
| **AI Design** | none | Covered by `ADIOSMAU-2259/2260/2261` |
| **Face AI** | none | `iOSUserCredits` is dead code; no action warranted |
| **PDF Editor** | none *(recommended separately)* | Cloud Storage, not Firestore — different class, own ticket |
| **Step Counter** | none | No Firestore, no Auth |
| **Music Player** | none | No Firestore, no Auth |
| **Goya / Mirage** | none | Route to IT Security — no team to receive a ticket |

**Sequencing rationale.** For iMote and Screen Mirroring the probed collection is
write-only and unread, so the investigation story comes first: if the data has no
consumer, removing the write is cheaper than securing it and satisfies acceptance
criterion #3 by construction. For ChatUltra the probed collection is load-bearing
application state, so removal is unavailable and the write path must move server-side —
which is why that app carries four stories instead of two.

**On acceptance criterion #3.** ADO-1570 requires anonymous writes to the probed
collection to return 403. Face AI meets this trivially (nothing writes the collection).
iMote and Screen Mirroring meet it by removing the write, subject to the investigation
outcome. ChatUltra requires real backend work. This distinction is the largest single
driver of effort across the batch and should be visible when the tickets are estimated.

## 7. Recommendations

**Immediate.** Enable App Check enforcement for Firestore where the client already
supports it — Face AI, AI Design, ChatUltra. Zero code, same day. Ask IT Security to probe
`imote-prod`, whose exposure is currently unknown rather than closed.

**This week.** Link the orphaned tickets to ADO-1570 so real coverage is visible. Re-open
the two abandoned PRs rather than rewriting them, after a conversation with their author
about why they were closed. Route Goya and Mirage back to IT Security as portfolio-risk
discovery — they are Tattooist-class and have no team to receive a ticket.

**Raise with IT Security.** The inclusion filter (§5.3) and the Admin-SDK reasoning error
(§5.4) are both methodology issues that will recur. Neither is specific to one app.

**Structural.** Rules-as-code with a deploy path in every repository, using TruthSeeker
web as the template. Each story in this batch carries that as an acceptance criterion, so
no separate umbrella ticket is required.

## 8. Open questions

1. Does anything outside the apps read iMote's `deviceInfo` or Screen Mirroring's
   `reviews`? Both investigation stories are gated on a named owner answering.
2. Are ChatUltra's `chatHistory` and `creditInfo` exposed under the same rule? This
   determines the true severity of the largest exposure in the portfolio.
3. Do Goya's and Mirage's `api_keys` / `all_api_keys` collections hold live credentials?
   Never probed.
4. What is `imote-prod`'s actual exposure and document count?
5. Who owns ChatUltra once the external studio is off-ramped?
6. Are the deployed rulesets on any of these projects what we assume? Nothing was read
   from a console during this audit.
7. Which GCP projects do Step Counter and Music Player actually use? Config is CI-injected
   and could not be confirmed from source.
8. Who owns `aichat-app-prod` (~110,517 token documents)? Confirmed **not** ChatUltra — no
   repository in the estate references it.
