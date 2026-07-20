# Garden Design — Coverage Gaps & Open Questions

> Generated alongside `garden-design.feature` from the ADIOSMAU 2026-05-04 export.
> This file lists what the QA tests *don't* cover, ambiguous assertions that
> need PM/eng confirmation, and conflicts found while normalising the tests.
> Resolve these before using the Gherkin to drive codegen or audit code.

## 1. Ambiguous test assertions (need confirmation before codegen)

| ID            | Ambiguity                                                                                                                              | Suggested resolution                                                                                                |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| ADIOSMAU-1284 | Event spec is incomplete — `view_screen_garden` lists property `screen_number` with no value enumeration or type.                      | Confirm with PM: integer 1/2/3? Strings? Also fired on result screen?                                               |
| ADIOSMAU-310  | `${Language}` placeholder with no enumeration — supported locales not specified.                                                       | Pull list from `Localizable.strings` / project config; bake into the Examples table.                                |
| ADIOSMAU-158  | "Image of acceptable quality" / "correct details wrt parameters" — non-mechanical assertion.                                           | Tagged `@manual-only`. Codegen should skip; QA owns.                                                                |
| ADIOSMAU-158  | Parenthetical "Also, do check the *content violation* scenarios" — entirely unspecified.                                               | Treat as a missing test family (see §3).                                                                            |
| ADIOSMAU-157  | "UI of garden design in light/dark modes" → "matches Figma".                                                                           | Tagged `@manual-only`; consider snapshot tests as a partial automation path.                                        |
| ADIOSMAU-307  | "Last saved custom prompt" — scope of persistence unspecified (per-user? per-feature? across app reinstalls? cleared on logout?).      | Confirm with eng: where is it stored (UserDefaults? backend?), what clears it?                                      |
| ADIOSMAU-305  | "Blocked palettes should not appear" — but no test for blocked **styles**, despite styles also having an entitlement model (inferred). | Likely missing test — see §3.                                                                                       |
| ADIOSMAU-93   | Steps mix Firestore paths with no clear contract for how the app reacts (live update? on next app launch?).                            | Confirm cache strategy — affects whether the scenario should include "after restart" or "without restart" preconds. |
| ADIOSMAU-175  | "Events should not be duplicated" — which event(s) specifically? Only the step-advance event, or all events on that step?              | Confirmed in feature as "the event for advancing to step 2"; PM to validate.                                        |
| ADIOSMAU-314  | Tooltip "first time open" — what re-triggers it? App reinstall? Clear app data? Never again?                                           | Confirm with PM, then update the second tooltip scenario.                                                           |

## 2. Internal conflicts in the source tests

- **Three different prefixes** for the same feature: `Garden -`, `[Garden]`, `[Garden design]`. Suggest standardising on `[Garden Design]` in Xray.
- **ADIOSMAU-313 (offline)** is filed under `[Garden]` but its steps say "Go to a feature (e.g. Interior Design, Replace Objects, Paint, Style Transfer, Garden design)" — it's actually a cross-feature test. Either duplicate per feature or extract into a shared `[Connectivity]` suite.
- **ADIOSMAU-315 (Original style + palette with template)** is filed under `[Garden]` but its first step says "Go to the interior design". Likely a copy-paste error — confirm whether it's actually testing Garden or Interior. Mirrored in feature as Garden, flag for QA.
- **ADIOSMAU-308** says "step 3" closing terminates flow, but only verifies main-screen redirect + state discard. Missing: same behaviour from steps 1 and 2 (likely covered implicitly; not asserted).

## 3. Missing scenarios (coverage gaps to flag for QA)

These are behaviours the spec implies exist but no test covers. Worth raising with the QA team — and also worth using as prompts for the LLM to suggest *additional* tests.

### Step 1
- Photo source = **gallery** is asserted only indirectly (via the `${Camera or gallery}` outline in -94/-146). No standalone gallery-source test.
- **Permission denied** for camera or photo library. iOS permission flow.
- **Photo too large / corrupt / unsupported format** — no error path tested.

### Step 2
- Style entitlement: free vs premium vs blocked styles on step 2 (parallel to ADIOSMAU-305 for palettes, but for styles).
- Custom prompt: **max length**, **empty prompt**, **profanity / content moderation** on user-provided text.
- Custom prompt: behavior when the user clears the saved prompt.

### Step 3
- Palette = `surprise-me` interaction with **blocked** palettes — does it draw from all enabled (free + premium) or only free?
- `Original` palette + non-`Original` style (and vice versa) — generation paths only tested in the both-Original combination.

### Generation
- **Server error** / 5xx response — no error path test.
- **Generation timeout** beyond the ~45s expectation.
- **Content violation** path mentioned in -158 but never specified.
- **Cancel during generation** — is the request abortable? No test.
- **Backgrounding the app** during generation.

### Result
- Behaviour after a successful generation: explicit assertions on the result screen (share, save, retry, return to flow). Tests imply Project persistence (-146) but nothing else.

### Cross-cutting
- **Free user vs premium user** matrix is not systematically applied.
- **Concurrent flows** — what happens if the user backgrounds Garden Design and starts Interior Design? (May be a global app concern, not Garden-specific.)
- **Accessibility** — VoiceOver labels, Dynamic Type, reduced motion. No tests.
- **Analytics** — only entry events specified; no `complete_garden` / `generation_started` / `generation_succeeded` / `generation_failed` events asserted.

## 4. Tests that should probably move

| Test          | Currently in | Belongs in                                                                |
| ------------- | ------------ | ------------------------------------------------------------------------- |
| ADIOSMAU-313  | `[Garden]`   | shared `[Connectivity]` (cross-feature)                                   |
| ADIOSMAU-315  | `[Garden]`   | likely `[Interior]` based on its actual steps — confirm                   |
| ADIOSMAU-1284 | `[Garden]`   | could split: entry events here, screen-view events into `[Analytics]` set |

## 5. What to use this file for

- **Before LLM codegen**: resolve §1 ambiguities so generated code/tests have concrete targets.
- **Before LLM audit**: feed §3 to the LLM as "expected gaps" so it doesn't hallucinate coverage that isn't there.
- **Back to QA**: §3 and §4 are conversations to have with the QA lead — the gaps may already be covered elsewhere (cross-feature suites) or may genuinely be open.
