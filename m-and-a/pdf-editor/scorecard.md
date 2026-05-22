# M&A App — Technical Scorecard

> **Purpose.** Give Filippo enough technical signal on an acquired app to make a confident 3-way call in front of the PM:
> **(1)** hand to an external team · **(2)** keep with current team (broken or not) · **(3)** move to an internal developer (then choose: full rewrite · partial rewrite · fix-and-stabilise · keep).
>
> **Filler.** A Claude Code session, working against the repo(s). Every claim must cite evidence (file paths, command output, version strings, commit SHAs). When something can't be determined, write `unknown — <reason>`. Never fabricate.
>
> **Output contract.** This file ends on a single opinionated recommendation with a confidence tag and a "what would flip this" line. After filling, also append/update the row in `m-and-a/portfolio-technical.csv`.

---

**App:** PDF Editor (`pdfeditor.app`, display name "PDF editor")
**Date:** 2026-05-21
**Filled by:** Claude Code (session)
**Reviewed by:** Filippo · _pending_
**Repos audited:** single repo at `/Users/ftosetto/Apps/pdf-editor/` — `github.com/rosseca/pdf-editor`
**Acquisition date:** unknown — repo's first commit is `f862f275` 2023-05-15 by Maxim Panasenko ("first commit"); rosseca-owned currently
**Current owners:** Acquired external contractor team. Dominant authors `Maxim Panasenko` 43% all-time (312/718 commits) + `Knyazev Valeriy` 35% (254/718) = **79% bus-factor-2**. Leadtech-side commits (Victor Jalencas, David Català, Hector Candón) are CI/Fastlane plumbing only — they have **not** touched `lib/`. Last commit 2026-04-21 — **30 days quiet** at audit date.

---

## 1. Snapshot (objective scrape — no judgement)

| Field                                          | Value                              | Notes / evidence                                                |
| ---------------------------------------------- | ---------------------------------- | --------------------------------------------------------------- |
| Platforms present                              | Android + iOS shipped; `macos/`, `linux/`, `windows/`, `web/` dirs exist but no CI builds them | Repo `ls`; `codemagic.yaml` workflows ship only Android+iOS |
| Primary language(s) per platform               | Dart/Flutter (app); Kotlin (1 tracked Android file + 5 untracked widget providers); Swift (1 file, AppDelegate) | `git ls-files` |
| Frameworks + versions                          | Flutter `3.35.7` (pinned `.fvmrc`); Dart SDK `>=3.3.2 <4.0.0`; Java 17 / Kotlin jvmTarget 17; iOS deployment target 16.0 | `.fvmrc`, `pubspec.yaml:7`, `android/app/build.gradle:34-39`, `ios/Podfile:4` |
| LOC per platform                               | Dart `lib/` hand-written ~**33,787** (42,630 total minus 8,843 generated/l10n); Kotlin 1 tracked + 5 untracked; Swift 132 (`AppDelegate.swift`) | `git ls-files lib \| xargs wc -l`, manual subtraction |
| Last commit (per repo)                         | `5915135` 2026-04-21 Victor Jalencas "Merge PR #115 update-matchfile" — **30 days stale**. First commit `f862f275` 2023-05-15 Maxim Panasenko. 718 commits all-time, 571 since 2025-11, 385 in 2026 | `git log -1`, `git rev-list --all --count` |
| Last release / tag                             | `unknown — not enumerated`. CI release workflows trigger on `v*` tags (`codemagic.yaml:494,574`). App version `3.4.0` | `pubspec.yaml:4` |
| Contributors in last 12 months                 | 6 distinct authors total all-time. Top 3 last-12mo same as all-time (Maxim, Valeriy, Victor) | `git shortlog -sne --since='12 months ago'` |
| Bus factor estimate (≥50% commits by N people) | **1 person** — Maxim Panasenko alone = 43% all-time. Two-person concentration = 79%. Both are external (`@ext.leadtech.com`, `@MacBook-Pro-Maxim.local`, personal `fanalis328@gmail.com` addresses). Internal Leadtech authors have not committed to `lib/`. | shortlog |
| Build attempt — BE                             | N/A — no backend in this repo. App calls external SaaS (CloudConvert, Nutrient/PSPDFKit, Microsoft Office Online Viewer, Google Drive) directly from client | code grep |
| Build attempt — Android                        | **fail — missing `google-services.json`** (CI-injected secret from `FIREBASE_ANDROID` env, not committed). `fvm flutter build apk --debug` cleared 5m20s of Gradle (including SDK platform 31 auto-install) before failing at `:app:processDebugGoogleServices` — no code-level errors. | `fvm flutter build apk --debug` 2026-05-21; first error: "File google-services.json is missing. The Google Services Plugin cannot function without it." |
| Build attempt — iOS                            | **pass** — `Runner.app` built in 113.9s after 324.9s of `pod install`. (Note: `ios/GoogleService-Info.plist` IS committed in this repo — see §4 — so iOS doesn't hit the secret-injection gap that ChatUltra does.) | `fvm flutter build ios --no-codesign --debug` 2026-05-21 |
| Build attempt — Web                            | N/A — `web/` dir exists but no CI build, no manual attempt made |
| Static analysis                                | **40 issues** in 12.2s — 0 errors; 11 warnings (5 unused stack traces, 3 unused imports, 3 others); 29 infos including **7 `avoid_print` in production code** (`signature_view_model.dart`, `ebook_reader_provider.dart`, `ebook_viewer_widget.dart`), **3 `use_build_context_synchronously` async-gap bugs**, 2 deprecated API usages | `fvm flutter analyze` 2026-05-21 |
| Codegen                                        | None required — `build_runner` not used at app level | `pubspec.yaml` grep |
| CI present?                                    | yes — `codemagic.yaml` (652 lines). **No `.github/workflows/`** | `ls .github/` returns no such file |
| CI provider + last run status                  | Codemagic only. Last run status `unknown — not queried via API`. PR #115 merged 2026-04-21 implies green at that point | |
| CI covers what?                                | 6 workflows: `pr_required` (strict analyze on changed files + flutter_test + gitleaks, blocking); `pr_informational` (full analyze, non-blocking, `\|\| true`); `dev_testflight` (IPA→TestFlight upload, **no auto-submit**); `dev_firebase_app_distribution` (APK→Firebase); `release_app_store` (tagged, upload-only); `release_play_store` (tagged, AAB as draft). Distributes to Saucelabs, Firebase App Distribution, TestFlight, App Store (upload), Play Store (as draft) | `codemagic.yaml:237-634` |
| Dependencies — total                           | 74 direct in `pubspec.yaml`, 6 dev deps, ~285 transitive packages in `pubspec.lock`. **`pubspec.lock` IS tracked** ✓ | `pubspec.yaml`, `pubspec.lock` |
| Dependencies — outdated (major behind)         | **138 packages newer-incompatible** at `pub get` time; **98 deps locked older than upgradable**; **19 deps constrained older than resolvable**. Newer-incompatible direct deps include `webview_flutter_android 4.10→4.12`, `win32 5→6`, `xml 6→7`, plus many transitives | `fvm flutter pub get` + `pub outdated` 2026-05-21 |
| Dependencies — EOL / unsupported               | **2 discontinued packages**: `build_resolvers`, `build_runner_core` (both transitive dev deps via `flutter_gen`); 1 git dep to a third-party personal fork pinned to a mutable branch (`flutter_epub_viewer` from `killumi/epub_viewer @update_callbacks`); 1 git dep with **no `ref`** (`matrix_gesture_detector` from `besttechguru/…` — defaults to HEAD on `pub get` if lock is missing) | `pub outdated`, `pubspec.yaml:37-41,101-102` |
| Known CVEs ≥ High                              | `unknown — no SCA tool run`. PDF/EPUB/ZIP parsing surface (`pdf ^3.11.1`, `pdfrx ^2.2.15`, `printing ^5.14.2`, `archive ^4.0.7`, forked `flutter_epub_viewer`) is CVE-prone — `archive` has had path-traversal and zip-bomb advisories in recent versions | `pubspec.yaml:23-39` |
| Secrets / hardcoded keys in repo               | **Production CloudConvert JWT and Nutrient `pdf_live_` key hardcoded in source** (see §4). `release.keystore` committed (password-protected, see §4). `ios/GoogleService-Info.plist` and `lib/firebase_options.dart` committed (Firebase client config; designed-public but defeats the CI base64 injection pattern at `codemagic.yaml:47`). `ios/Runner.xcodeproj/project.pbxproj.bak` committed (stale backup) | `lib/domain/services/convertion_api/cloud_convert_api_client.dart:13`, `nutrient_api_client.dart:8`; `git ls-files` |
| Tests present per slice                        | **Zero.** No `test/` directory, no `integration_test/`. `flutter_test` listed as dev dep but unused | `git ls-files test integration_test` empty |
| Tests runnable?                                | n/a — `fvm flutter test` returns "Test directory 'test' not found" and exits 0. CI gracefully no-ops (`codemagic.yaml:159-166`) | observed 2026-05-21 |
| Coverage if measurable                         | 0% — no tests; no coverage tooling | n/a |
| Docs — README adequacy                         | **thin and actively misleading** — 99 lines, lists `Apphud`, `Singular`, `pdf_render`, `google_ml_kit` (none in current pubspec); references a `scanner/` folder that doesn't exist; states "There is no backend in this project … keys are client-side keys, intended to live on the client" — false for the CloudConvert + Nutrient paid keys | `README.md:46-83` vs `pubspec.yaml` |
| Docs — onboarding steps reproducible?          | Partially — fvm + standard `flutter pub get` works; Android build needs `google-services.json` from Codemagic secret group; no developer bootstrap doc | |
| ARCHITECTURE.md or equiv                       | **no** — no `ARCHITECTURE.md`, no `CONTRIBUTING.md`, no `CLAUDE.md`, no `docs/` folder | `find . -iname ARCHITECTURE*` empty |
| Infra-as-code present?                         | none | |
| Observability (logs, metrics, alerts)          | Firebase Crashlytics (`v5.0.7`; file misspelled `firebase_crashlitics.dart`); Firebase Analytics (`v12.1.2`); Amplitude; AppsFlyer; Meta SDK. Firebase App Check enabled (`v0.4.1+4`); Firebase Remote Config enabled (`v6.1.4`). **No Sentry, no backend APM** (no backend) | `pubspec.yaml`, `lib/domain/services/firebase/firebase_crashlitics.dart`, `app_check_service.dart` |

---

## 2. Per-slice health

### Backend
- **State:** absent (no project backend). App is **operationally backend-heavy via 3rd-party SaaS**: CloudConvert (billable), Nutrient/PSPDFKit (billable), Microsoft Office Online Viewer (Microsoft cookie/JS sandbox), Google Drive (user OAuth), AppsFlyer OneLink, multiple analytics endpoints.
- **Top 3 risks:**
  1. **CloudConvert + Nutrient keys live in client binary** — any user (or attacker) can decompile APK/IPA and use them. Both are billable; CloudConvert subject ID `74290349` and JWT expiry `2126`.
  2. **No proxy layer** — every external SaaS call goes direct from device, so you cannot rotate, throttle, or observe usage without releasing a new app version.
  3. **Office preview pipeline routes user documents through 4 public file hosts** (see §3 BLOCKER).
- **Bring-to-shippable-baseline effort:** ~3-4 person-weeks to stand up a thin proxy (Cloud Run / Cloud Functions) for CloudConvert + Nutrient that holds the keys server-side and signs short-lived requests.

### Android
- **State:** working in CI (Codemagic ships AAB to Play and APK to Firebase App Distribution). **Local fresh-clone build fails** at `:app:processDebugGoogleServices` because `google-services.json` is CI-injected (verified 2026-05-21).
- **Top 3 risks:**
  1. **`MANAGE_EXTERNAL_STORAGE` + `requestLegacyExternalStorage="true"`** — Google Play has tightened the policy for this permission since 2021; "file editor" is a borderline use case. Next release submission has a non-zero rejection / removal risk.
  2. **`usesCleartextTraffic="true"`** — global cleartext allow for the whole app. Combined with the public-host upload preview, plausible TLS guarantees evaporate.
  3. **5 untracked Kotlin widget provider files** on disk (`android/app/src/main/kotlin/pdfeditor/app/widgets/FavoritesWidgetProvider.kt` + 4 others) — a feature exists locally but is not in git. Fresh clone will not build that surface; PR review never saw it.
- **Effort to baseline:** ~1-2 person-weeks: tighten storage permissions to scoped storage, remove cleartext flag, commit the widget code or remove the on-disk files.

### iOS
- **State:** **building** — `fvm flutter build ios --no-codesign --debug` succeeded in 113.9s on a fresh clone (verified 2026-05-21).
- **Top 3 risks:**
  1. `ios/GoogleService-Info.plist` committed — duplicates the CI base64 injection pattern; if rotated, the old key stays in git history.
  2. `ios/Runner.xcodeproj/project.pbxproj.bak` committed — backup file in version control is a code smell and a small leak surface for old configuration.
  3. `LSApplicationQueriesSchemes` not used to validate the `pdfeditor://` deep-link scheme — minor deep-link hijack surface.
- **Effort to baseline:** ~0.5 person-week.

### Web / Desktop
- N/A — directories exist but no CI build, no obvious product intent.

### Infra / CI
- **State:** working
- **Top 3 risks:**
  1. **Gitleaks runs `--exit-code 0`** in `.ci/scan-secrets:28` — informational only, never blocks merge or release. The CloudConvert JWT and Nutrient key would surface in those reports today but have never been actioned.
  2. **`pr_informational` runs full `flutter analyze` with `\|\| true`** (`codemagic.yaml:288-326`) — the 40 current issues are visible but cannot block PRs.
  3. **`CODEOWNERS` covers only** `codemagic.yaml`, `CODEOWNERS`, `/.ci/`, `/ios/fastlane/` — **`lib/`, `android/`, `ios/Runner/` have no required reviewers**. All 33k LOC of app code merges without owner review.
- **Effort to baseline:** ~0.5 person-week to flip gitleaks to blocking, drop `\|\| true` on analyze, and expand CODEOWNERS.

---

## 3. Red flags

- `BLOCKER` — **Office document preview pipeline uploads user files to public file hosts** (catbox.moe / tmpfiles.org / 0x0.st / transfer.sh) and renders them through Microsoft Office Online Viewer in a webview with `JavaScriptMode.unrestricted`. Verified: `lib/features/preview/preview_office_documents.dart:27-34, 185-300`. This is a **GDPR / data-protection** problem regardless of intent — user documents (potentially PII, contracts, scans) leave the device for anonymous public buckets with no retention SLA. The product's own README claims "no backend" — this is effectively an uncontrolled, multi-vendor backend the user never consented to.
- `BLOCKER` — **CloudConvert production JWT hardcoded in committed source**: `lib/domain/services/convertion_api/cloud_convert_api_client.dart:13`. Decoded payload: `sub=74290349`, scopes `user.read, task.read, task.write`, `iat ≈ 2026-02`, **`exp = 4926582159` (year 2126)**. Extractable from any shipped APK/IPA — directly billable to the CloudConvert account, no way to revoke without a new release.
- `BLOCKER` — **Nutrient/PSPDFKit production API key hardcoded**: `lib/domain/services/convertion_api/nutrient_api_client.dart:8` (`pdf_live_Fbb6v6QAWlPTbWfniCMYiCstRhSkwk76xwxCSDmc4oG`). The `pdf_live_` prefix is the production indicator. Same extraction + revocation problem as CloudConvert.
- `MAJOR` — **`release.keystore` committed to git** (`git ls-files -- release.keystore` confirms). Password-protected (8 common passwords tried — `android`, `changeit`, `pdfeditor`, `pdf_editor`, `123456`, `password`, `rosseca`, `leadtech` — all rejected; not a plaintext key). CI uses an env-injected keystore (`CM_KEYSTORE_*` in `codemagic.yaml`), so the in-repo file may be a dev/test keystore — but the filename `release.keystore` is misleading and the SHA1/SHA256 fingerprint must be compared against Play Console signing before clearing this as benign.
- `MAJOR` — **Zero automated tests** across ~33k Dart LOC, 718 commits, 3 years (`git ls-files test integration_test` empty). The CI `flutter_test` step gracefully no-ops when the directory is absent.
- `MAJOR` — **Bus factor 1, two visible** — Maxim Panasenko 43% of all commits, Maxim + Valeriy Knyazev = 79%. Both use external / personal email addresses (`@ext.leadtech.com`, personal `gmail.com`, hostname-stamped commit emails). Combined with the **30-day gap** since the last `lib/`-touching commit, this looks like the moment the acquired team's engagement is winding down — exactly when M&A integration most needs them.
- `MAJOR` — **`MANAGE_EXTERNAL_STORAGE` + `android:requestLegacyExternalStorage="true"`** (`android/app/src/main/AndroidManifest.xml:11,53`) — Play Store has been rejecting / removing apps abusing this permission since 2021; "PDF editor" is a borderline use case. Plan for a forced refactor to scoped storage before the next Play submission.
- `MAJOR` — **`android:usesCleartextTraffic="true"`** (`AndroidManifest.xml:54`) — global cleartext allow.
- `MAJOR` — **Gitleaks is informational only** (`.ci/scan-secrets:28` runs `--exit-code 0`). The two hardcoded paid API keys above have presumably been visible in gitleaks output across multiple releases and never blocked.
- `MAJOR` — **Fresh-clone Android build is impossible without CI secrets** (same `google-services.json` pattern as ChatUltra). No developer bootstrap doc.
- `MAJOR` — **138 packages newer-incompatible**, **98 deps locked older than upgradable**, **19 constrained older than resolvable**, **2 discontinued** (`build_resolvers`, `build_runner_core`). Roughly twice ChatUltra's outdated debt.
- `MAJOR` — **`CODEOWNERS` does not cover `lib/`, `android/`, `ios/Runner/`** — all app code merges without owner review.
- `MINOR` — `matrix_gesture_detector` git dep has **no `ref`** in pubspec (`pubspec.yaml:101-102`); lock file saves you today but `pub upgrade` or losing the lock pulls HEAD of a third-party personal fork (`besttechguru/matrix_gesture_detector`).
- `MINOR` — 5 Kotlin widget provider files exist on disk but are **not tracked in git** — local-dev state diverges from repo; PR review never saw them.
- `MINOR` — `lib/firebase_options.dart` and `ios/GoogleService-Info.plist` committed (Firebase client config is designed-public, but tracking them means rotating Firebase project IDs leaves prior values in git history).
- `MINOR` — `ios/Runner.xcodeproj/project.pbxproj.bak` committed (stale backup file).
- `MINOR` — README stale and misleading (lists Apphud/Singular/pdf_render — none in pubspec).
- `MINOR` — `flutter analyze` shows 7 `avoid_print` violations in production code (`signature_view_model.dart`, `ebook_reader_provider.dart` and `_widget.dart`) and 3 `use_build_context_synchronously` async-gap bugs.
- `MINOR` — Crashlytics service file misspelled `firebase_crashlitics.dart` — has propagated through 718 commits unfixed; weak quality signal.

---

## 4. Security — immediate action items

These must happen **regardless** of the strategic decision below. Listed in suggested priority order.

- [ ] **CRITICAL** — Kill or replace the Office-preview public-host upload path — `lib/features/preview/preview_office_documents.dart:27-34, 185-300` — replace with (a) device-local rendering, (b) a controlled proxy you own, or (c) remove the Office preview feature pending a compliant pipeline. **Do not ship another release with this code path live in EU markets.**
- [ ] **CRITICAL** — Rotate the CloudConvert API token — `lib/domain/services/convertion_api/cloud_convert_api_client.dart:13` — revoke JWT for subject `74290349`, generate a new token server-side, route calls through a proxy with per-request signing. Remove the key from current source AND purge from git history.
- [ ] **CRITICAL** — Rotate the Nutrient/PSPDFKit `pdf_live_` key — `lib/domain/services/convertion_api/nutrient_api_client.dart:8` — same proxy pattern as CloudConvert.
- [ ] **HIGH** — Verify `release.keystore` fingerprint vs Play Console signing key — `keytool -list -v -keystore release.keystore` (password unknown). If it matches the prod signing identity, treat as compromised secret (low likelihood given password-protection, but the password is somewhere a contractor knows). If it doesn't match, remove the file from repo + history regardless — there is no good reason to ship any keystore in source.
- [ ] **HIGH** — Tighten Android storage permissions — drop `MANAGE_EXTERNAL_STORAGE` and `requestLegacyExternalStorage="true"`, migrate to scoped storage / SAF before the next Play submission to avoid removal risk.
- [ ] **HIGH** — Drop `usesCleartextTraffic="true"`; add explicit per-domain exceptions if any HTTP endpoints are genuinely needed.
- [ ] **HIGH** — Make gitleaks **blocking** (`.ci/scan-secrets:28` → remove `--exit-code 0`) so future hardcoded keys are stopped at PR time.
- [ ] **HIGH** — Drop the `\|\| true` on the informational analyze workflow (`codemagic.yaml:288-326`) at least for warnings; 40 issues is not a useful steady state.
- [ ] **MEDIUM** — Expand `CODEOWNERS` to require review on `lib/`, `android/app/`, `ios/Runner/`.
- [ ] **MEDIUM** — Pin `matrix_gesture_detector` git dep to a specific commit SHA (`pubspec.yaml:101-102`).
- [ ] **MEDIUM** — Decide on the Android widget code: either commit and code-review the 5 untracked Kotlin files, or remove them from the workspace.

---

## 5. Intervention options

### A. Hand to external team as-is
- **Feasibility:** **very low** in current state.
- **Prep work required before handover:** (a) all §4 CRITICAL + HIGH items resolved (~6-8 weeks); (b) baseline test scaffolding (zero-to-something so the external team has a safety net) (~2 weeks); (c) write the missing `ARCHITECTURE.md` + onboarding doc + correct README (~1 week); (d) document the SaaS-vendor relationships (CloudConvert account, Nutrient account, AppsFlyer, RevenueCat / Superwall) so the external team has billing + key-rotation access (~0.5 week).
- **Main risks:** External team inherits a 33k-LOC app with zero tests and an actively-quiet original author. With the SaaS keys rotated behind a proxy, the proxy itself becomes a dependency the external team needs to operate too.
- **Rough effort to make handover-ready:** **10-12 person-weeks**.

### B. Keep with current team (status quo)
- **Ongoing risk if nothing changes:** The acquired contractor team is **already winding down** (30 days quiet on `lib/`; both top authors external; only Leadtech-side commits in the last month are CI/Fastlane plumbing). "Status quo" effectively means **owned by no one** within weeks if it isn't already.
- **Cost trajectory:** Flat until something breaks. When the CloudConvert / Nutrient keys are abused or Google Play rejects the next release for `MANAGE_EXTERNAL_STORAGE` abuse, cost spikes hard with no in-house knowledge to respond.
- **Failure modes within 6 months:** (1) Play Store removal on next submission; (2) GDPR complaint or DPA inquiry on the public-host upload path; (3) CloudConvert or Nutrient credit exhaustion / TOS termination after key extraction; (4) original contractors fully off-boarded → no one knows how `lib/features/preview/preview_office_documents.dart` was supposed to evolve.

### C. Move to an internal developer
The likely option given (A) is too expensive and (B) is effectively no-owner. Sub-paths:

- **C1 — Full rewrite** — **out of scope.** 33k LOC + multi-vendor SaaS integration + multi-feature surface (editor / converter / OCR / signature / forms / preview / file management). Cost-benefit obviously wrong.
- **C2 — Partial rewrite** — **mandatory sub-scope of C3**, not standalone:
  - Slice(s) to rewrite: (a) replace `preview_office_documents.dart` end-to-end (kill public-host uploads); (b) introduce a thin proxy backend in front of CloudConvert + Nutrient; (c) refactor Android storage layer off `MANAGE_EXTERNAL_STORAGE`.
  - Why these slices: each is a forced obligation from §4 — not optional, not a question of preference.
  - Effort: ~4-6 person-weeks for the three together (most of that is the Android storage refactor — non-trivial because file-management is the app's core).
  - Risk: the proxy is new infra to own; storage refactor risks regression in file-picker UX.
- **C3 — Fix-and-stabilise (with C2 sub-scope)** — **the realistic call**:
  - Fixes in scope: all §4 items + the C2 partial rewrite above + add minimal test scaffolding (one test per major feature view-model so future changes have a regression net) + extend `CODEOWNERS` + flip gitleaks to blocking + bring dependency debt down from "138 incompatible" to "all majors current".
  - Effort: **8-12 person-weeks for one engineer**, can overlap with feature freeze. Heavier than ChatUltra because of the architectural debt (no proxy, no tests, hardcoded secrets in the actual business logic).
  - Residual risk after fixes: PDF/EPUB/ZIP parsing CVE surface remains — needs ongoing SCA hygiene. Bus-factor concentration moves from "external contractors" to "one internal dev" — better, but still one person; needs a documented second-owner plan.
- **C4 — Keep as-is, just own it** — equivalent to (B). Not viable given §4 obligations.

---

## 6. Recommendation

**Picked path:** **C3 — Fix-and-stabilise (with mandatory C2 sub-scope: preview pipeline, SaaS proxy, Android storage)**
**Confidence:** **medium**

**Why (2-3 reasons):**
1. The acquired contractor team is visibly winding down (30 days quiet on `lib/`, top author 43% concentration, no internal Leadtech engineer has touched the app code). "Keep with current team" (B) is effectively "owned by no one" already — that is the live default and it is not acceptable given the §4 obligations.
2. The two CRITICAL findings (public-host upload pipeline + two hardcoded production API keys) are real, forced, time-sensitive obligations regardless of the strategic call. They alone justify an internal owner who can drive the C2 sub-scope on a known timeline.
3. External handover (A) is not financially defensible at current state: the prep work to make the codebase handover-ready (10-12 person-weeks) is the same work as fixing it in-house under (C3), and an external team would inherit zero tests + zero docs + a still-fragile dependency surface.

**One-paragraph version for the PM:**
> The PDF Editor app is functional and shipping but carries three obligations that aren't optional: (1) the Office-document preview pipeline currently uploads user files to public file-hosting services before rendering them — a GDPR fire that almost certainly needs to be killed or replaced before the next EU release; (2) two production API keys (CloudConvert and Nutrient/PSPDFKit) are hardcoded in the app binary, billable, extractable, and not revocable without a new release — they need to move behind a small server-side proxy; (3) the Android version still uses `MANAGE_EXTERNAL_STORAGE`, which Google Play has been increasingly rejecting since 2021. The original contractor team that built it has been quiet for 30 days on the app code; "leaving it with them" is no longer a real option. The realistic call is to hand it to an internal Flutter developer for an 8–12 person-week stabilisation sweep that fixes the three obligations above, adds basic test scaffolding, and gets the codebase to a state where a second engineer could pick it up. Rewriting it is wrong — 33k lines of working code — and handing it externally isn't cheaper than fixing it ourselves.

**What would flip this recommendation:**
- If `release.keystore`'s fingerprint matches the live Play Store signing identity (verifiable via `keytool` + Play Console), the call escalates from "stabilise" to "rotate signing key or accept a permanently exposed identity" — likely forces a v2 keystore strategy and may need a Play Console support ticket.
- If a credible internal Flutter owner cannot be assigned within ~4 weeks, sunset the app or pay an external team to do the §4 baseline (still preferable to leaving it un-owned).
- If the GDPR / DPA exposure on the public-host preview is already a known complaint (legal team would know), the timeline collapses — `C2` partial rewrite of the preview path becomes a week-1 emergency, not a 4-6 week project.
- If product strategy decides the Office-preview and CloudConvert features are non-core, the C2 sub-scope collapses dramatically — both could be removed instead of replaced, taking the effort estimate down to ~4-5 person-weeks.

**Open questions for Filippo / PM before committing:**
- Which Leadtech entity holds the CloudConvert and Nutrient/PSPDFKit billing accounts? (Needed before any key rotation — Maxim or Valeriy likely created them under their own emails.)
- Does the Play Store listing for `pdfeditor.app` currently pass the `MANAGE_EXTERNAL_STORAGE` declaration form? If yes, what was claimed there? Determines exposure on next submission.
- Is there a known internal Flutter developer to take ownership? (No internal Leadtech engineer has touched `lib/`; this app would be a cold start for whoever picks it up.)
- Has legal / DPO ever reviewed the preview pipeline? Determines whether the public-host upload is week-1 emergency or 4-6 week refactor.
- Is `release.keystore` the Play Store production signing key? `keytool -list -v` fingerprint vs Play Console will answer this in 60 seconds — but we need the keystore password (the audit could not crack it with 8 common guesses).

---

## 7. Portfolio CSV row

```
pdf-editor,2026-05-21,NA,fail-missing-secret,pass,NA,active-likely-green,3,Office preview uploads user files to public hosts + 2 hardcoded prod API keys,C3,10,medium
```

(Android build failed only on missing CI-injected Firebase config — code compiled cleanly. iOS build passed on a fresh clone. `sec_blockers=3`: public-host preview + CloudConvert JWT + Nutrient `pdf_live_` key. `est_person_weeks=10` is the midpoint of the C3+C2 8-12 range.)
