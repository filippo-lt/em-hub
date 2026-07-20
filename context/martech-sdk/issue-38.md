author:	MiguelAlvarezLT
association:	member
edited:	false
status:	none
--
Hello team,

As part of the roadmap, we would like to consider adding support in the Martech Kit SDK for AppsFlyer uninstall measurement.

This has already been reviewed internally and is also being extended to apps in the vertical through:

- https://leadtech.atlassian.net/browse/ACANDMAU-1673
- https://leadtech.atlassian.net/browse/ACIOSMAU-2003

The opportunity is to make uninstall measurement part of the standard Martech Kit / AppsFlyer integration, so rolling it out across the portfolio is straightforward and does not require each app team to solve the same setup independently.

From the network side, this is also seen as added value. Their feedback is that the `af_uninstall` flag helps AppsFlyer partners identify users who have uninstalled the app more effectively. This can reduce wasted impressions in install campaigns and improve campaign optimization. They also mentioned that partners without this enabled may increasingly be at a disadvantage in auction dynamics going forward.

The suggested AppsFlyer setup is:

1. Follow AppsFlyer's uninstall measurement setup documentation.
2. In the final step, map the uninstall event to the relevant partners in the AppsFlyer dashboard.
3. Map the event as a post-install event where applicable, for example for Applovin.

AppsFlyer documentation:
https://support.appsflyer.com/hc/en-us/articles/4408933557137#mapping-the-uninstall-event

It would be useful to assess what is required from the SDK side, what remains dashboard/configuration-only, and whether Martech Kit can expose this as a documented and reusable portfolio-level capability.

--
author:	david-leadtech
association:	member
edited:	false
status:	none
--
## Roadmap addition: Block manual AppsFlyer identity wiring (VideoUp incident, Jun 2026)

### Context

VideoUp v2.9.0 (from 1 Jun) set `AppsFlyerLib.customerUserID` **after** `start()`, violating [AppsFlyer docs](https://dev.appsflyer.com/hc/docs/set-customer-user-id). ~8k installs/day shipped with NULL `customer_user_id` → missing `RCAnonymousId` on install → broken joins across AppsFlyer, RevenueCat, and downstream sources. Direct impact on Meta W2A conversion scoring. Hotfix v2.9.1 restored the field.

**Root cause:** hand-rolled AppsFlyer bootstrap in app code. A single line moved in a refactor broke a P0 identity contract. Code review and manual QA did not validate attribution identity pre-release.

**Key insight:** MartechKit already owns the correct contract in `AppsFlyerConfigurator` (CUID → `start()` → AF UID → RC) and `AppsFlyerStartupTests` already assert CUID is set before `start()`. The gap is not missing SDK logic — it is **adoption** and **enforcement**. We need to make it impossible (or CI-blocking) to reintroduce manual measurement/bootstrap in apps that adopt the kit.

---

### Non-negotiable identity contract

```
RevenueCat.appUserID → AppsFlyer.customerUserID → AppsFlyer.start() → AF UID → RevenueCat
```

Once an app adopts MartechKit, this sequence must **not** be implementable in app code. Changes happen only inside MartechKit, with unit tests and CI blocking regressions there.

---

### Proposed roadmap

#### P0 — Enforcement: no manual AF bootstrap in apps on MartechKit

| # | Item | What it does |
|---|------|--------------|
| 1 | **Migrate VideoUp + Photo/Video portfolio to MartechKit** | Remove hand-rolled `AppsFlyerLib` init from app targets. Identity contract lives in one maintained module. |
| 2 | **Per-app CI gate: block manual AF identity wiring** | Fail PR/build if app sources contain `AppsFlyerLib.shared().start()`, `.customerUserID =`, or `import AppsFlyerLib` for bootstrap purposes. Documented allowlist only for exceptional cases (e.g. OneLink handlers in a single file). |
| 3 | **MartechKit CI: run `swift test` on every PR** | `AppsFlyerStartupTests` already covers the contract; today CI only verifies commits — tests must block merges. |
| 4 | **Codemagic pre-submit gate** | Block App Store upload if manual AF bootstrap is detected in app code. |
| 5 | **Mandatory Martech review on attribution PRs** | Until migration is complete: any PR touching `AppsFlyerLib`, `Purchases.configure`, or attribution wiring requires Martech team approval. |

Example CI check (app repo):

```bash
if rg -l 'AppsFlyerLib\.shared\(\)\.start\(\)|\.customerUserID\s*=' --glob '*.swift' .; then
  echo "ERROR: Direct AppsFlyer identity/bootstrap is forbidden. Use MartechKit."
  exit 1
fi
```

#### P1 — Detect breaks before production (safety net)

| # | Item | What it catches |
|---|------|-----------------|
| 6 | **Pre-release attribution checklist** | Document in `INTEGRATION_GUIDE.md`: clean install → `Martech.requestATT()` → AF debug log shows non-null `customer_user_id` == RC `appUserID` before App Store submit. |
| 7 | **Structured bootstrap logging (`os_log`)** | Log RC configured → CUID set → AF started → AF UID pushed. Validate in TestFlight without waiting for AF dashboard or paid Amplitude events. |
| 8 | **Data alert: NULL `customer_user_id` rate** | BigQuery / AF hourly alert if NULL rate spikes above baseline. Would have surfaced this in hours, not after thousands of broken installs/day. |
| 9 | **Portfolio migration tracker** | Living matrix: app × MartechKit status. No app with paid UA spend should stay on hand-rolled AF bootstrap. |

#### P2 — Additional hardening ideas

| # | Item | Rationale |
|---|------|-----------|
| 10 | **App-level integration contract test** | After migration: CI test/grep that fails if app target links `AppsFlyerLib` directly while also depending on `MartechKit` (double-bootstrap smell). |
| 11 | **TestFlight identity snapshot** | Debug-only screen or log export: RC `appUserID`, AF `customerUserID`, AF UID — single place for QA sign-off before release. |
| 12 | **Incident playbook** | Short runbook: "NULL customer_user_id in AF" — BQ query, who to escalate, SLA. Tied to the data alert above. |
| 13 | **MartechKit adoption KPI** | Quarterly target: % of portfolio installs under kit vs hand-rolled. Makes migration progress visible to Performance Marketing. |
| 14 | **README anti-pattern section** | Explicit "do not do this" examples in `INTEGRATION_GUIDE.md` showing the VideoUp failure mode (CUID after `start()`) so reviewers have a concrete reference during PR review. |

---

### Takeaway

> MartechKit already owns the AF ↔ RC identity contract. The roadmap item is **enforcement**: apps that adopt the kit must not implement AppsFlyer bootstrap in app code; CI must block merges that reintroduce manual `customerUserID` / `start()` calls.

The failure was not a missing feature — it was **unguarded identity wiring in app code that a refactor could break with one line**. MartechKit centralises the contract; per-app CI and data alerts enforce it. Ad-hoc "extra care in review" is not a scalable fix.

Happy to split P0 items into separate tracked issues if useful.
--
author:	david-leadtech
association:	member
edited:	false
status:	none
--
## Portfolio SDK gaps (app audit) — AdMob + mediation focus

Follow-up to the [VideoUp identity enforcement roadmap](https://github.com/rosseca/martech-kit/issues/38#issuecomment-4679032040). Audit of iOS apps in our workspace shows **no app has adopted MartechKit yet** — each still owns its own bootstrap (`AppDelegate+Attribution`, `CoreAppsflyer`, `CoreStartup`, etc.). Beyond AF ↔ RC identity, we should extend the same **centralise + CI-block-manual-setup** pattern to other high-risk SDKs.

---

### Priority: Google AdMob + mediation stack

Several apps are moving (or planning) **Google Mobile Ads as the mediation layer**, with network adapters on top. Today this is entirely app-side and easy to break silently — same class of risk as VideoUp.

**What we need in MartechKit:** an optional `MartechKitAdMob` product that owns:

1. **SDK bootstrap** — `GADMobileAds.sharedInstance().start()` timing (post-ATT / UMP consent, coordinated with MartechKit `ATTGate`)
2. **Mediation adapter wiring** — documented, version-pinned adapter set per app vertical (not reinvented per repo)
3. **Ad revenue attribution** — single `logAdRevenue()` fan-out to AppsFlyer (and optionally Firebase), replacing per-app facades
4. **CI enforcement** — block merges that call `GADMobileAds`, `MobileAds.shared.start`, or manual ad-revenue logging outside the kit

#### Real examples from our codebase (Step Counter)

Placements already modelled in app code (should become kit-level constants / generated config):

| Placement | Format | Example use |
|-----------|--------|-------------|
| `home_bottom_banner` | Banner | `HomeView` bottom banner |
| `onboarding_complete_interstitial` | Interstitial | Post-onboarding full-screen |
| `pro_unlock_rewarded` | Rewarded | Unlock Pro feature via rewarded ad |

Ad lifecycle events already tracked manually (`ad_shown`, `reward_ad_watched`) — these should route through MartechKit `EventTracker`, not scattered `logEvent` calls.

**Ad revenue bridge (today hand-rolled, target: kit-owned):**

Step Counter defines a facade pattern (`AdRevenueService`) intended to send revenue to **AppsFlyer + Firebase** from AdMob `onPaidEvent` callbacks — replacing deprecated direct calls in `AppsFlyerService.logAdRevenue()`. This is exactly the kind of cross-SDK wiring MartechKit should own:

```
AdMob onPaidEvent → MartechKitAdMob.logAdRevenue() → AppsFlyer ad revenue API + (optional) Firebase
```

References already in app docs: [AppsFlyer ad revenue](https://dev.appsflyer.com/hc/docs/ad-revenue-2), [AdMob mediation](https://developers.google.com/admob/ios/mediation).

#### Mediation adapters to standardise (portfolio-level)

We need a **pinned, documented adapter matrix** — not each app team picking pods independently. Typical networks we mediate through AdMob (examples; exact set TBD per vertical):

| Adapter (iOS) | Network | Notes |
|---------------|---------|-------|
| `Google-Mobile-Ads-SDK` | Google AdMob | Core SDK |
| `GoogleMobileAdsMediationFacebook` | Meta Audience Network | Common in UA-heavy apps |
| `GoogleMobileAdsMediationUnity` | Unity Ads | Gaming / rewarded flows |
| `GoogleMobileAdsMediationIronSource` | ironSource (LevelPlay) | Mediation bidder |
| `GoogleMobileAdsMediationMintegral` | Mintegral | APAC inventory |
| `GoogleMobileAdsMediationChartboost` | Chartboost | Legacy inventory |
| `GoogleMobileAdsMediationPangle` | Pangle (TikTok) | Growing network |
| `GoogleMobileAdsMediationVungle` | Liftoff/Vungle | Video inventory |

**Kit deliverables:**

- `MartechAdMobKeyProvider` extension on `MartechKeyProvider` (AdMob app ID, ad unit IDs per placement, adapter keys)
- `MartechKitAdMob.configure()` called from Phase 1/2 (after ATT + UMP if required)
- SwiftUI/UIKit helpers for banner/interstitial/rewarded (optional — or documented patterns only in v1)
- Unit tests: mock ad revenue payload → verify AF fan-out called with correct schema
- CI script: fail if app imports `GoogleMobileAds` directly when `MartechKitAdMob` is a dependency

#### Why this matters for Performance Marketing

- **Ad revenue → AppsFlyer** feeds ROAS / tROAS models and partner optimisation. Wrong schema or missing events = blind UA spend.
- **Mediation misconfiguration** (wrong adapter version, init before consent) = no fill or policy violations — hard to catch without a standard bootstrap.
- Same lesson as VideoUp: **one line moved in app code** should not be able to break revenue attribution.

---

### Other SDK gaps (same enforcement model, no AppLovin)

| Gap | Seen in | MartechKit proposal |
|-----|---------|---------------------|
| Firebase Analytics + Crashlytics user ID | ai-cleaner, step-counter (`CoreFirebase`) | Extend `MartechKitFirebase`: `user_id` / `setUserID` = RC `appUserID` |
| OneSignal identity | ai-cleaner (`OneSignal.login(revenueCatID)`) | `MartechKitOneSignal` — CI blocks manual `OneSignal.login` in app |
| Per-app `Core*` modules | ereasy (`CoreAppsflyer`, `CoreAmplitude`, …) | Deprecate → migrate to MartechKit (ereasy `CoreAppsflyer.startup()` calls `start()` without CUID in same method — same antipattern as VideoUp) |
| Dual analytics (Amplitude + Firebase) | ai-cleaner `EventsManager` | Optional Firebase Analytics bridge from `EventTracker` |
| FCM / push token + identity | step-counter (planned) | `MartechKitMessaging` — token registration tied to RC id |

---

### Suggested roadmap order

1. **P0** — VideoUp / portfolio AF identity enforcement (previous comment)
2. **P1** — `MartechKitAdMob` v1: init + ad revenue → AF + placement constants + CI gate
3. **P1** — Mediation adapter matrix doc + pinned versions in `Package.swift` / Pod reference template
4. **P2** — `MartechKitFirebase+` (Analytics/Crashlytics identity), `MartechKitOneSignal`
5. **P2** — Deprecate per-app `Core*` / `CoreStartup` wrappers

Happy to open separate issues for `MartechKitAdMob` and the shared `verify-no-manual-martech.sh` CI script.
--
author:	MiguelAlvarezLT
association:	member
edited:	false
status:	none
--
## Roadmap addition: Firebase-backed app instance identity in Amplitude

Related Jira task: https://leadtech.atlassian.net/browse/MT-573

We should consider making Firebase App Instance ID / Firebase Installation ID ingestion a standard MartechKit capability for mobile apps.

The goal is to expose a stable Firebase-backed app-instance identifier in Amplitude as a user property, using a consistent property name across the portfolio, for example `firebase_app_instance_id` or `firebase_installation_id`.

At a high level, MartechKit could own or document the common contract:

- retrieve the Firebase Installation ID after Firebase/app init;
- set it in Amplitude as a user property, not as an event property;
- set it early enough that it is available on first-session events where possible;
- keep Amplitude's `device_id` / `user_id` semantics unchanged;
- provide verification guidance for Amplitude User Lookup / Event Stream and downstream exports.

Why this belongs in the SDK roadmap:

- it gives Martech, Support, and app teams a shared identifier across Amplitude, Firebase, Remote Config, Crashlytics, Cloud Messaging, and related tooling;
- it avoids each app team choosing a different property name, timing, or implementation detail;
- it fits the same portfolio-level pattern as the other roadmap items: centralise cross-SDK identity plumbing, document the contract once, and reduce app-side drift.

Potential deliverables:

1. Add a small Firebase identity bridge in MartechKit or document the required integration pattern if Firebase remains app-owned.
2. Standardise the Amplitude user property name across iOS and Android projects.
3. Add tests or sample implementation coverage to ensure the property is sent through the Amplitude wrapper.
4. Add rollout / audit guidance for existing mobile apps so teams can confirm the property is present in Amplitude.

This should not replace Amplitude's own identity fields. It is an additional cross-tool correlation property for debugging, support, and analytics consistency.

--
author:	MiguelAlvarezLT
association:	member
edited:	false
status:	none
--
## Roadmap addition: AppsFlyer Amplitude V2 identifiers before SDK start

Related rollout request: Amplitude V2 integration for apps using AppsFlyer.

We should add this to the MartechKit roadmap as a portfolio-level identity requirement, not only as a Swift implementation detail.

Current Swift package status checked against origin/main on 2026-06-15:

- RevenueCat appUserID is already set as AppsFlyer customerUserID before AppsFlyer start.
- Amplitude user/device identifiers are sent to RevenueCat subscriber attributes.
- The AppsFlyer Amplitude V2 requirement is not fully covered in main yet: AmplitudeDeviceId and AmplitudeSessionId are not merged into AppsFlyer customData before the first AppsFlyer start.

Required contract:

Before initializing/starting AppsFlyer, every app integration should populate:

- Customer User ID / CUID = RevenueCat ID.
- Amplitude Device ID.
- Amplitude Session ID.

Suggested SDK-level scope:

- Swift: extend MartechKit AppsFlyer startup so it merges AmplitudeDeviceId and AmplitudeSessionId into AppsFlyer customData before AppsFlyerLib.start(), preserving any host-provided customData.
- Kotlin / Android: define the equivalent contract in the Android martech layer so AppsFlyer receives CUID, Amplitude device ID, and Amplitude session ID before start/init.
- Flutter: define the same contract for Flutter apps/wrappers, especially where apps still own appsflyer_sdk + amplitude_flutter bootstrap directly.

Why this belongs in the roadmap:

- It is cross-SDK identity plumbing, same family as the existing AppsFlyer customerUserID guardrail.
- Leaving it per app/OS invites drift: Swift may be fixed while Kotlin or Flutter keeps the old ordering.
- The rollout request asks app teams to confirm App/OS readiness and release version, so the kit should provide one standard contract per supported stack.

Suggested acceptance criteria:

- Tests prove CUID, AmplitudeDeviceId, and AmplitudeSessionId are set before AppsFlyer start/init.
- Existing AppsFlyer custom data is preserved when adding Amplitude V2 keys.
- Docs list the expected implementation/verification for Swift, Kotlin, and Flutter.
- Release notes identify the SDK/package version where each stack becomes compliant.

Implementation note: there is already a branch with the Swift shape, origin/feat/amplitude-appsflyer-v2-customdata, but this roadmap item should track the broader Swift + Kotlin + Flutter requirement so we do not ship a one-platform fix and call it done.
--
author:	MiguelAlvarezLT
association:	member
edited:	false
status:	none
--
Follow-up reference for the AppsFlyer Amplitude V2 roadmap item above:

Swift already has a concrete draft implementation that can be used as the reference example for the required behaviour:

- PR: https://github.com/rosseca/martech-kit/pull/15
- Branch: feat/amplitude-appsflyer-v2-customdata
- Scope: adds AmplitudeDeviceId and AmplitudeSessionId into AppsFlyer customData before AppsFlyer start, while keeping CUID = RevenueCat ID before start.

That PR should be treated as the Swift example of the contract we need to replicate/document for the other supported stacks too, especially Kotlin/Android and Flutter. The roadmap item is broader than the Swift PR: the portfolio-level requirement is that every app stack sets CUID, Amplitude device ID, and Amplitude session ID before AppsFlyer init/start.
--
author:	envictor
association:	member
edited:	false
status:	none
--
Very interesting additions, I need some time to analyze them.  Regarding preventing identity (re)wiring, there's little that a library can do at runtime to veto things happening at the app level, but we definitely could add some CI-level checks on the app repositories. Swift Package Manager plugins definitely can analyze the host app code at runtime and fail the build if they detect some improper code (the Swiftlint plugin works in this way). Of course, it would be relatively easy to work around, but the aim is to prevent inadvertent mistakes, not intentional circumvention.
--
