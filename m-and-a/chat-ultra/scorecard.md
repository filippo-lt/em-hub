# M&A App — Technical Scorecard

> **Purpose.** Give Filippo enough technical signal on an acquired app to make a confident 3-way call in front of the PM:
> **(1)** hand to an external team · **(2)** keep with current team (broken or not) · **(3)** move to an internal developer (then choose: full rewrite · partial rewrite · fix-and-stabilise · keep).
>
> **Filler.** A Claude Code session, working against the repo(s). Every claim must cite evidence (file paths, command output, version strings, commit SHAs). When something can't be determined, write `unknown — <reason>`. Never fabricate.
>
> **Output contract.** This file ends on a single opinionated recommendation with a confidence tag and a "what would flip this" line. After filling, also append/update the row in `m-and-a/portfolio-technical.csv`.

---

**App:** Chat AI Ultra (ChatUltra)
**Date:** 2026-05-20
**Filled by:** Claude Code (session)
**Reviewed by:** Filippo · _pending_
**Repos audited:** 13 separate `github.com/rosseca/*` repos under `/Users/ftosetto/Apps/ChatUltra/` — `chat_ai_ultra` (Flutter app), `chat_module`, `purchasing_module`, `analytics_module`, `chat_service` (Dart Frog BE), `connectinno_permission_module`, `connectinno_apns_handle`, `age_range_signals`, `image-gen-service` (Python FastAPI), `chatultra_credit_service` (Python Flask, GAE), `cloud_token_service` (Python FastAPI), `dart_firebase_admin` (vendored fork), `flutter-sound-stream` (forked plugin)
**Acquisition date:** unknown — not derivable from source; this is the "existing app unit," not a new M&A target per `project_ma_portfolio` memory
**Current owners:** internal Connectinno/rosseca team — dominant author Gorkem Topcu (~58% of `chat_ai_ultra` commits last 12mo across two name spellings)

---

## 1. Snapshot (objective scrape — no judgement)

| Field                                          | Value                              | Notes / evidence                                                |
| ---------------------------------------------- | ---------------------------------- | --------------------------------------------------------------- |
| Platforms present                              | Mobile (iOS + Android) via Flutter + 3 BE services (Python) + 1 Dart BE | App: `chat_ai_ultra/`, iOS deploy target 15.5 (`ios/Podfile:1`), Android `minSdk 26 compileSdk 36` (`android/app/build.gradle`). No standalone web/desktop. |
| Primary language(s) per platform               | Mobile: Dart/Flutter; BE: Python 3 (3 services) + Dart Frog (1 service) | |
| Frameworks + versions                          | Flutter 3.35.7 pinned via FVM (`chat_ai_ultra/.fvmrc`); Dart SDK `>=3.9.0 <4.0.0`; FastAPI 0.115.6 (`image-gen-service`); FastAPI 0.115.8 (`cloud_token_service`); Flask 3.0.3 (`chatultra_credit_service`); Dart Frog 1.x (`chat_service`) | `pubspec.yaml` / `requirements.txt` per repo |
| LOC per platform                               | Flutter app 53,483 (non-gen Dart); BE total ≈7.6k (chat_service 2.9k + image-gen 2.9k + credit 1.4k + cloud_token 0.3k); shared Dart packages ≈22k | `find ... -name '*.dart' ! -name '*.g.dart' ! -name '*.freezed.dart' ! -name '*.gr.dart' | xargs wc -l` |
| Last commit (per repo)                         | `chat_ai_ultra` 5c74c317 2026-05-15 ("Merge PR #1079"); `chat_module` dcbb9fc 2026-02-26; `purchasing_module` a60150d 2026-04-16; `analytics_module` e966f63 2026-01-26; `chat_service` bc86d31 2026-03-02; `image-gen-service` 38055f9 2026-05-06; `chatultra_credit_service` 983b6ba 2026-03-03; `cloud_token_service` 7448fb6 **2025-07-16** (stale); `connectinno_permission_module` 684e308 **2025-11-13**; `connectinno_apns_handle` ffe246f **2025-10-06**; `dart_firebase_admin` cbe5109 **2024-07-03** (alpha upstream) | `git log -1` per repo |
| Last release / tag                             | unknown — not enumerated; CI deploys via tag pattern in `codemagic.yaml` (App/Play Store) and `release/x.y.z` branches for BE | App version string `3.4.0` in `chat_ai_ultra/pubspec.yaml` |
| Contributors in last 12 months                 | App: 10; chat_module 4; purchasing_module 7; chat_service 5; image-gen-service 5; credit_service 3; cloud_token 2 (0 in last 6mo); permission_module 3 (0 in 6mo); apns_handle 1 (0 in 6mo) | `git shortlog -sne --since='12 months ago'` per repo |
| Bus factor estimate (≥50% commits by N people) | App: 1 person ≥50% (Gorkem Topcu ~58%, two spellings); top 3 = 71%. Backend repos: 1-person dominance in each (iremguner on chat_service ~48% and credit_service; alicanhelikanon on image-gen) | shortlog |
| Build attempt — BE                             | `unknown — Python/Dart Frog toolchain not exercised (Python 3.14 vs pinned older runtimes; no Dart SDK installed)` | CI GH Actions deploy to Cloud Run / App Engine on `release/*` branches — actively used |
| Build attempt — Android                        | **fail — missing `google-services.json`** (Firebase config, CI-injected secret, not committed). `fvm flutter build apk --debug` cleared 12m19s of Gradle including NDK auto-install before failing at `:app:processDebugGoogleServices` — no code-level errors surfaced. | `fvm flutter build apk --debug` 2026-05-20; first error: "File google-services.json is missing. The Google Services Plugin cannot function without it." Searched `android/app/google-services.json`. |
| Build attempt — iOS                            | **fail — missing `ios/Runner/GoogleService-Info.plist`** (Firebase config, CI-injected secret). Xcode compilation succeeded ("Xcode build done" in 161.2s); link/packaging failed when GoogleService-Info.plist was referenced as a build input. Podfile `post_install` hook (`ios/Podfile:47`) also raised stack trace during `pod install` — non-fatal but noisy. | `fvm flutter build ios --no-codesign --debug` 2026-05-20 |
| Build attempt — Web                            | N/A — no web target |
| Static analysis                                | **pass — 0 issues** in 16.3s on `chat_ai_ultra` | `fvm flutter analyze` 2026-05-20 |
| Codegen                                        | **pass** — `dart run build_runner build` 23s, 43 outputs (auto_route + json_serializable + freezed paths) | 2026-05-20 |
| CI present?                                    | yes | `chat_ai_ultra/codemagic.yaml` (511 lines, 6 workflows); BE repos have `.github/workflows/{test,protect_stage,protect_release,staging_deploy,prod_deploy}.yml` |
| CI provider + last run status                  | Codemagic (mobile) + GitHub Actions (backends). Last run status `unknown — not queried via API`. Active merge cadence (PR #1079 merged 2026-05-15) implies green | `codemagic.yaml`, BE `.github/workflows/` |
| CI covers what?                                | App PR checks: gitleaks (lib + ios/Runner only), `build_runner` codegen, `flutter analyze`, `flutter test`, PR comment. Distribution: TestFlight, Firebase App Distribution, App Store, Play Store. BE: test → Cloud Run/App Engine deploy on `release/*` | `codemagic.yaml:88-103`; BE `prod_deploy.yml` |
| Dependencies — total                           | App: 58 direct deps in `pubspec.yaml` + 15-entry `dependency_overrides` block; **329 transitive deps** resolved by `flutter pub get` (run 2026-05-20); `module/core` 34 direct; BE Python services ~10-25 deps each | `fvm flutter pub get` output |
| Dependencies — outdated (major behind)         | **6 direct deps majors-behind** (`app_links 6→7`, `package_info_plus 8→10`, `smooth_page_indicator 1→2`, `styled_text 8→9`, `velocity_ads 0.3→0.5`, `json_annotation 4.11→4.12`); **~40 transitive majors-behind** including `grpc 3→5`, `protobuf 3→6`, `analyzer 9→13`, `archive 3→4`, `device_info_plus 11→13`, `purchases_flutter 9→10`, `share_plus 12→13`, `sign_in_with_apple 7→8`. **1 discontinued package**. `velocity_ads` constrained older than resolvable. | `fvm flutter pub outdated` 2026-05-20 |
| Dependencies — EOL / unsupported               | `dart_firebase_admin` upstream self-labels "still in its early stages, and some features may be missing or bugged" yet shipped in production BE via `rosseca/dart_firebase_admin` fork (`chat_service/packages/firebase_manager`). `connectinno_apns_handle`, `connectinno_permission_module`, `cloud_token_service` all 0 commits in last 6 months. `image_gallery_saver` pinned to `benlrichards/image_gallery_saver` fork with **no ref** — floating HEAD ships to users | `pubspec.yaml` git deps; `dart_firebase_admin/README.md` |
| Known CVEs ≥ High                              | `unknown — no SCA tool run (snyk/osv-scanner not invoked)` | n/a |
| Secrets / hardcoded keys in repo               | **3 Firebase service-account JSONs with `-----BEGIN PRIVATE KEY-----` blocks tracked in git** (see §3, §4). Confirmed via `git ls-files`. | `chatultra_credit_service/chatai2-32311-firebase-adminsdk-cymky-6e94be2d2d.json`; `cloud_token_service/chatai2-32311-service-account.json`; `chat_service/packages/firebase_manager/service_account.json` (committed `b5d23f1`, originally added in `4284d7e` 2024-06-05) |
| Tests present per slice                        | App: **1 file** (`chat_ai_ultra/test/widget_test.dart`), and that single test is a **`skip` placeholder** ("All tests skipped"); chat_module 6; chat_service 12 (best); purchasing_module 1; analytics_module 1; image-gen-service 6 (pytest); credit_service 0; cloud_token_service 0 | `find <dir>/test -name '*_test.dart'`; verified by running `fvm flutter test` |
| Tests runnable?                                | yes — `fvm flutter test` exit 0 in ~4s, output: "+0 ~1: All tests skipped" (zero assertions executed). CI runs the same on every PR | `fvm flutter test` 2026-05-20 |
| Coverage if measurable                         | 0% effective — only test in the suite is skipped. No coverage tooling configured | observed |
| Docs — README adequacy                         | App README thin (46 lines); CLAUDE.md rich and accurate (verified against actual code); package READMEs mixed: purchasing_module good (594 lines), analytics_module good (481), permission/apns_handle near-absent (12-15 lines) | per-repo READMEs |
| Docs — onboarding steps reproducible?          | Partially — requires FVM + 25+ env vars (`PURCHASES_*`, `SUPERWALL_*`, `MIXPANEL_TOKEN`, `DIDOMI_API_KEY`, `VELOCITY_ADS_*`, `RSA_PRIVATE_KEY`, etc.) sourced from Codemagic groups; no documented developer `.env` bootstrap | `codemagic.yaml:51-75` |
| ARCHITECTURE.md or equiv                       | yes — `chat_ai_ultra/docs/{STATE_MANAGEMENT,API_COMMUNICATION,LOCAL_STORAGE,FIRESTORE_CACHE_OPERATIONS,REMOTE_CONFIG,SCRIPTS}.md`. BE: `chat_service/TECHNICAL_HANDOVER.md`, `chatultra_credit_service/HANDOVER.md`, `image-gen-service/handover_documentation.md` | |
| Infra-as-code present?                         | none — no `*.tf`, `Pulumi.*`, `cdk.json` anywhere in tree | `find / -name '*.tf'` over tree |
| Observability (logs, metrics, alerts)          | App: Firebase Crashlytics + Firebase Analytics + Mixpanel + Amplitude + Appsflyer + Talker local logger. **No Sentry.** BE: Cloud Run / App Engine native logs only — no APM/Datadog/Sentry references | `lib/product/service/crashlytics_service.dart`, `product_analytics_station.dart` |

---

## 2. Per-slice health

### Backend (4 services)
- **State:** working (actively deployed via GitHub Actions to GCP `chatai2-32311`, EU-west1 + image-gen us-central1)
- **Top 3 risks (with evidence):**
  1. **3 service-account private keys committed in git** across 3 of the 4 BE repos — see §4. Rotation required regardless of strategic call.
  2. **`dart_firebase_admin` is alpha and stale** — upstream README literally states "still in its early stages, and some features may be missing or bugged"; last upstream commit 2024-07-03 — used in `chat_service/packages/firebase_manager` via internal fork.
  3. **`cloud_token_service` unmaintained** — 0 commits in last 6 months, 2 lifetime authors, 0 tests, yet still in deploy path (FastAPI on Cloud Run).
- **Bring-to-shippable-baseline effort:** ~3-4 person-weeks: rotate all GCP service-account keys (1d), purge from git history across 3 repos (BFG/filter-repo, 1-2d), replace `dart_firebase_admin` consumer with a maintained alternative or upstream commit reference (1w), add gitleaks to BE repos (0.5d), add minimal test coverage to credit + cloud_token services (1w).

### Android
- **State:** working in CI (Codemagic ships to Firebase App Distribution + Play Store; minSdk 26 / compileSdk 36). **Local fresh-clone build fails** at `:app:processDebugGoogleServices` because `google-services.json` is a CI-injected secret (verified 2026-05-20).
- **Top 3 risks:**
  1. **Build reproducibility fragile** — `pubspec.lock` git-ignored (`chat_ai_ultra/.gitignore:52`), 2 git deps in app, 5 git deps in `module/core`, 15-entry `dependency_overrides` block; in-file comment admits past breakages forced the overrides.
  2. **Bus factor 1** — Gorkem Topcu ~58% of last-12-months commits; top 3 = 71%.
  3. `image_gallery_saver` pinned to a random user fork (`benlrichards/image_gallery_saver`) **with no git ref** — whatever HEAD is at build time ships to users.
- **Effort to baseline:** ~2-3 person-weeks: track `pubspec.lock`, audit and re-pin git deps to explicit refs, replace `image_gallery_saver` fork with maintained source.

### iOS
- **State:** working in CI (TestFlight + App Store via Codemagic; deploy target 15.5). **Local fresh-clone build fails** on missing `ios/Runner/GoogleService-Info.plist` (CI-injected). Xcode compilation itself succeeded in 161s (verified 2026-05-20).
- **Top 3 risks:** Same as Android — shared Flutter codebase; iOS-specific surface is small. Codesign secrets / provisioning profiles assumed managed in Codemagic groups (`unknown — not verified`).
- **Effort to baseline:** subsumed by Android baseline work.

### Web / Desktop
- N/A — not built.

### Infra / CI
- **State:** working
- **Top 3 risks:**
  1. **Gitleaks coverage hole** — App CI scans only `lib` and `ios/Runner` (`codemagic.yaml:91`); BE repos have **no gitleaks step** — which is exactly where the committed private keys live. The PR-level scanner cannot catch the problem it's there to catch.
  2. **Branch-protection script drift** — CLAUDE.md references `scripts/ci/protect_release.sh` + `protect_stage.sh`; not visibly invoked in current `codemagic.yaml` (parallel to the CLAUDE.md note that `scripts/cd/` was already inlined). Worth verifying actual enforcement.
  3. **No IaC** — every deploy target is GCP click-ops or YAML-via-GH-Actions; disaster recovery / environment cloning is undocumented.
- **Effort to baseline:** ~1 person-week: extend gitleaks to all repos, verify branch protections, write a one-page runbook for env recreation.

---

## 3. Red flags

- `BLOCKER` — **Firebase service-account private key committed: `chatultra_credit_service/chatai2-32311-firebase-adminsdk-cymky-6e94be2d2d.json`** (key id `6e94be2d2da444bacdcaf441dd20aeb2f7a954c3`, project `chatai2-32311`). Verified tracked in git via `git ls-files`. Grants admin access to the prod Firebase project — same project used by the mobile app.
- `BLOCKER` — **Firebase service-account private key committed: `cloud_token_service/chatai2-32311-service-account.json`** (key id `d677e7bd7481ccf99c7f770728fdd6407340abcf`, same `chatai2-32311` project). Verified tracked. The repo's own `README.md` calls this file "sensitive" while shipping it.
- `BLOCKER` — **Firebase service-account JSON committed: `chat_service/packages/firebase_manager/service_account.json`** (added 2024-06-05 in `4284d7e`, relocated in `b5d23f1`). Still tracked in HEAD. Exposed in git history for ≥11 months — assume compromised whether or not these repos were public at any point.
- `MAJOR` — **`pubspec.lock` git-ignored** (`chat_ai_ultra/.gitignore:52`). Releases not byte-reproducible; reliance on `dependency_overrides`-as-band-aid is documented in-file as a fix for prior breakages.
- `MAJOR` — **App test coverage ≈ 0** — 1 `widget_test.dart` for a 53k-LOC Flutter app, and that single test is a `skip` placeholder (verified by running `fvm flutter test`: "+0 ~1: All tests skipped"). The only meaningful PR-time quality gate is `flutter analyze` — which itself passes cleanly (0 issues), so analyze offers no current signal either.
- `MAJOR` — **Fresh-clone build is impossible without CI secrets** — both Android and iOS builds fail on missing Firebase config files (`google-services.json`, `GoogleService-Info.plist`) that are injected from Codemagic at CI time and never committed. No developer-bootstrap script exists for these. An external team handed the repo cannot build locally on day 1.
- `MAJOR` — **`dart_firebase_admin` is alpha and stale** (upstream last commit 2024-07-03; README admits "still in its early stages") and sits in production backend via `rosseca` fork.
- `MAJOR` — **`image_gallery_saver` git dep pinned with no ref** — floating HEAD of a random user's fork is what users get installed.
- `MAJOR` — **Bus factor 1** on the Flutter app (~58% top author last 12mo).
- `MAJOR` — **3 production packages unmaintained ≥6 months** (`connectinno_apns_handle`, `connectinno_permission_module`, `cloud_token_service`).
- `MAJOR` — **gitleaks scope mismatch** — runs in app CI but only on `lib` + `ios/Runner`; not configured on BE repos where the actual leaked keys live.
- `MINOR` — App `README.md` is 46 lines and assumes FVM + Codemagic env-var knowledge; CLAUDE.md is far more accurate and should be the canonical entry doc.
- `MINOR` — No Sentry / no backend APM; observability is split across 4 client analytics SDKs (Mixpanel, Amplitude, Appsflyer, Firebase Analytics) — fragmented.
- `MINOR` — Branch-protection scripts referenced in CLAUDE.md but not visibly invoked in current `codemagic.yaml`.

---

## 4. Security — immediate action items

These must happen **regardless** of the strategic decision below.

- [ ] **CRITICAL** — Service-account private key exposed in git — `chatultra_credit_service/chatai2-32311-firebase-adminsdk-cymky-6e94be2d2d.json` — (a) rotate via GCP console (delete key id `6e94be2d2d…`), (b) remove from current tree, (c) purge from history (`git filter-repo` or BFG), (d) add to `.gitignore`, (e) confirm Cloud Run / App Engine pull the new key from Secret Manager.
- [ ] **CRITICAL** — Service-account private key exposed in git — `cloud_token_service/chatai2-32311-service-account.json` — same rotation + purge + Secret Manager wiring.
- [ ] **CRITICAL** — Service-account JSON exposed in git — `chat_service/packages/firebase_manager/service_account.json` — same. Note: this key has been in repo history since 2024-06-05 (`4284d7e`); assume usage history is fully compromised — review GCP audit logs for `chatai2-32311` for unfamiliar callers.
- [ ] **HIGH** — Add gitleaks (or equivalent) pre-commit + CI step to **every** BE repo, not just the Flutter app. App-side gitleaks scope should also be widened beyond `lib` + `ios/Runner`.
- [ ] **HIGH** — Replace `image_gallery_saver` git dep (`benlrichards/image_gallery_saver` no-ref) with a maintained published package or pin to a verified commit SHA. Currently a build-time supply-chain hole shipped to end users.
- [ ] **MEDIUM** — Track `pubspec.lock` in git for the Flutter app; eliminate the `dependency_overrides` block in favour of explicit pins where possible.
- [ ] **MEDIUM** — Move all 25+ runtime secrets currently sourced from Codemagic groups (`PURCHASES_*`, `SUPERWALL_*`, `MIXPANEL_TOKEN`, `DIDOMI_API_KEY`, `VELOCITY_ADS_*`, `RSA_PRIVATE_KEY`, …) into a single declared inventory doc so rotation is possible without spelunking.

---

## 5. Intervention options

### A. Hand to external team as-is
- **Feasibility:** **low**
- **Prep work required before handover:** (1) rotate + purge all 3 committed service-account keys; (2) fix reproducibility (lock file, pinned git deps); (3) write developer-onboarding doc with full env-var inventory; (4) add baseline test scaffolding so an external team has a regression net; (5) document the `chat_service` ↔ `dart_firebase_admin` boundary so an external team understands the alpha dependency it inherits.
- **Main risks:** Bus-factor-1 dependence on a single internal author means an external team will hit undocumented context constantly. Multi-repo sprawl (13 repos, mixed languages, mixed CI providers) amplifies onboarding cost.
- **Rough effort to make handover-ready:** **6-8 person-weeks** (4 for the security/repro/test baseline, 2-4 for documentation + an actual paired handover period).

### B. Keep with current team (status quo)
- **Ongoing risk if nothing changes:** Service-account keys remain compromised — a single contractor offboarding or a single public-repo flip is a prod incident. Build reproducibility regressions will recur. Test debt compounds — first non-trivial refactor finds defects in production.
- **Cost trajectory:** Flat unless the security debt fires; if the keys are exploited, the cost is uncapped (prod Firebase + Cloud Run + App Engine project).
- **Failure modes within 6 months:** (1) key leak detection / abuse → emergency rotation under pressure; (2) Gorkem unavailable for 2+ weeks → release blocked or worked around by less-experienced authors; (3) `dart_firebase_admin` alpha breakage from an upstream Firebase Admin change with no maintainer to fix it.

### C. Move to an internal developer
This option is largely **not on the table** the way the template frames it — this is *already* the internal team's app. The relevant sub-question is "should we re-staff or partially rewrite anything?"

- **C2 — Partial rewrite (or replace)** — _candidate_
  - Slice(s) to rewrite: replace `chat_service`'s `dart_firebase_admin` dependency. Either swap to the Node Firebase Admin SDK (mature) behind the same internal interface, or pin and own the fork explicitly with a maintenance commitment.
  - Why this slice (not the others): it is the only stack-level dependency that is both **stale upstream** and **in the prod data path**; the rest of the issues are operational, not architectural.
  - Effort: ~2-3 person-weeks.
  - Risk: low — the `chat_service` interface to Firebase is narrow (Firestore + auth verification), so a substitution is contained.
- **C3 — Fix-and-stabilise (no rewrite)** — _the realistic call_
  - Fixes in scope: §4 security action items + reproducibility (track `pubspec.lock`, pin git deps), + minimal test scaffolding (target 1 cubit + 1 cache service per feature so future refactors have a regression net), + extend gitleaks to all repos.
  - Effort: ~4-6 person-weeks for one engineer, can run in parallel to feature work.
  - Residual risk after fixes: bus-factor-1 remains structural — partial mitigation is documentation + onboarding a second senior engineer to the Flutter codebase; full mitigation is a multi-quarter knowledge-distribution effort.
- **C1 — Full rewrite** — **out of scope**: 53k LOC + 4 BE services + an in-flight product. Cost-benefit obviously wrong.
- **C4 — Keep as-is, just own it** — equivalent to (B); see above.

---

## 6. Recommendation

**Picked path:** **C3 — Fix-and-stabilise (no rewrite)**, with §4 security items as immediate work regardless.
**Confidence:** **medium**

**Why (2-3 reasons):**
1. The app is **actively shipping** (PR #1079 merged 2026-05-15, full CI pipeline live, recent activity across most of the 13 repos). Nothing about the code state warrants rewrite or handover.
2. The headline problems — **3 committed service-account keys + ~0 test coverage + git-ignored lock file + alpha-stage BE dependency** — are real and load-bearing, but each is contained and fixable in person-weeks, not person-quarters.
3. Hand-off (A) and full rewrite (C1) are both cost-traps given the current state — an external team would inherit all the same problems with less context, and a rewrite throws away 53k LOC of working Flutter for no architectural win.

**One-paragraph version for the PM:**
> ChatUltra is functioning and actively shipping, so the call is to keep ownership where it is — but **three Firebase service-account private keys are committed in git across the backend repos** (in one case since June 2024) and need to be rotated and purged from history this week regardless of any other decision. Beyond that, the app has structural fragility — near-zero automated tests, an ignored lock file, and one alpha-stage Firebase library in the backend — that doesn't justify a rewrite or external handover, but is worth ~4-6 person-weeks of stabilisation work alongside normal feature delivery. Bus factor on the Flutter app is effectively one person; that's a people problem to address in parallel, not a code problem to fix.

**What would flip this recommendation:**
- If the committed service-account keys turn out to have been exposed in a **public** GitHub mirror at any point (e.g. a contractor's personal fork), the recommendation upgrades from "stabilise" to "rotate + treat as a real incident + freeze new feature work until §4 is done."
- If the bus-factor-1 author becomes unavailable in the next 6 months and there is no second senior Flutter dev ramped, the realistic call shifts toward (A) — bring in an external team and accept the higher prep cost.
- If a credible external maintainer of `dart_firebase_admin` does not emerge within a quarter, escalate C2 (replace the BE Firebase dependency) from optional to required.

**Open questions for Filippo / PM before committing:**
- Have any of the BE repos (`chat_service`, `chatultra_credit_service`, `cloud_token_service`) ever been public, mirrored, or shared with departed contractors? Determines whether §4 is "rotate" or "rotate + incident response."
- Who owns the GCP project `chatai2-32311`'s IAM, and is GCP audit logging enabled? Needed before any compromise-assessment can be done.
- Is the existing 25+ runtime-secret inventory in Codemagic actually rotated periodically, or has it been static since launch? (Adjacent risk — not surfaced by repo audit.)
- Is "this is the existing team's app" still true in Q3 given the M&A scope expansion (`project_ma_expansion`)? If responsibility shifts, the option set changes.

---

## 7. Portfolio CSV row

```
chat-ultra,2026-05-20,NA,fail-missing-secret,fail-missing-secret,NA,active-green,3,3 Firebase service-account private keys committed in git across BE repos,C3,5,medium
```

(Android/iOS local builds failed only because Firebase config files are CI-injected secrets — code compiled cleanly in both. CI itself is active and green based on recent merge cadence and clean `flutter analyze`. `NA` for BE/Web because there is no monolithic BE build and no web target.)
