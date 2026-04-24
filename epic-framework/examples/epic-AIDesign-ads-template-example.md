# Epic: Ads Before Creation (Rewarded Ad Gateway)

> **Status:** Ready for Grooming
> **Project:** ADIOSMAU
> **Epic Key:** ADIOSMAU-1317
> **Epic Type:** UI Feature

---

## TL;DR

Free users who tap "Generate" will see a modal offering two paths: watch a rewarded ad or upgrade to PRO. This gates AI generation behind a monetization step without blocking the experience, using a daily quota and per-flow toggles managed via Remote Config.

---

## Business Goal

Monetize the high-volume free user segment and offset LLM/image generation costs (OpenAI, Stability AI) while increasing PRO conversion through "feature friction."

## Problem Statement

Free users consume expensive AI generation credits at no cost. Without a monetization gate, CAC is not recoverable from ad revenue alone and the free tier subsidises heavy users indefinitely.

---

## Scope

### In Scope

**Mobile (iOS / Android)**

- AdMob SDK integration (Rewarded and Rewarded Interstitial ad units)
- Monetization Modal UI: two-option overlay ("Watch Ad" / "Go PRO")
- Ad pre-loading and loading state animation
- Daily ad quota counter (local + Remote Config-driven)
- Subscriber bypass logic (PRO users never see the modal)
- "Reward not granted" error message when ad fails or exits early

**Backend / Infra**

- Firebase Remote Config keys: `ads_enabled_per_flow`, `daily_ad_quota`, `ad_unit_ids`
- RevenueCat subscription status check before modal trigger

**Analytics**

- Events: `modal_shown`, `ad_started`, `ad_completed`, `ad_skipped`, `upgrade_tapped`, `generation_bypassed_subscription`

**Remote Config / Feature Flags**

- `ads_enabled_per_flow` — per-feature toggle (e.g. enabled for Paint, disabled for Garden Design)
- `daily_ad_quota` — hard daily limit (default: 5)
- `ad_unit_ids` — per-platform unit IDs, swappable without app update

### Out of Scope

- Interstitial ads (non-rewarded) — future iteration
- Paywall redesign — separate epic
- Changes to the PRO subscription price or offer — separate epic
- Ads on any screen other than the Generate trigger point

---

## Delivery Plan

| Milestone | User-visible outcome | Scope (high level) | Exit criteria (QA verifiable) | Release / Flagging |
| --------- | -------------------- | ------------------ | ----------------------------- | ------------------ |
| M1 | Modal appears for free users; PRO bypass works | Modal UI + subscription check; block generation until user action | Free users see modal; PRO never sees modal; generation never fires before decision | Behind `ads_enabled_per_flow` (off by default) |
| M2 | Rewarded ad gating is functional | AdMob SDK integration + reward callback gating; error/retry path | Generation fires only on reward callback; failure path never grants generation | Keep behind flag |
| M3 | Quota + analytics are production-ready | Daily quota enforcement + Remote Config keys + all analytics events | Quota enforces and resets at midnight; all events fire with required properties | Gradual rollout by feature |

> **EM estimate:** ~2 person-weeks total

---

## User Flows

### Happy Path — Free user watches ad

1. User configures their design (e.g. selects room style, uploads photo)
2. User taps "Generate"
3. App checks: is user PRO? → No
4. App checks: has user hit daily quota? → No
5. Monetization Modal appears with two CTAs: "Watch Ad" and "Go PRO"
6. User taps "Watch Ad"
7. Ad pre-loads (loading animation shown); ad plays
8. User watches ad to completion
9. Modal dismisses; AI generation call fires; result shown to user
10. Daily quota counter increments by 1

### Variant — User hits daily quota

1. Steps 1–4 above, but quota check returns: limit reached
2. Modal appears with "Watch Ad" CTA disabled and a message: "You've used all your free generations today. Come back tomorrow or go PRO."
3. Only "Go PRO" CTA is active

### Variant — Ad fails to load or user exits early

1. Steps 1–7 above; ad fails to load or user closes it before completion
2. App receives no reward callback
3. Modal re-appears; generation does NOT fire
4. "Reward not granted" message shown below the CTA

### Variant — PRO user

1. User taps "Generate"
2. App checks: is user PRO? → Yes
3. Modal is skipped entirely; generation fires immediately

---

## Acceptance Criteria

- Modal appears after "Generate" tap, before the API call fires, for all free users across all features
- PRO users never see the modal — subscription check must use RevenueCat status, not a local flag
- Generation fires **only** if the ad reward callback is received (not on ad start)
- If ad exits early or fails, generation does not fire and the modal re-appears
- Daily quota is enforced: after N completions (N = `daily_ad_quota` Remote Config value), "Watch Ad" is disabled
- Quota resets at midnight local time
- `ads_enabled_per_flow` Remote Config can disable the modal for a specific feature without an app update
- AdMob labelling complies with policy (ad must be clearly identified as an ad)
- A/B test cohort assignment is stable per user (not re-randomised on each session)

---

## Non-functional Requirements (NFRs)

- **Performance**: Modal must appear within 300ms of Generate tap on supported devices; ad pre-loading must not block the main thread.
- **Reliability**: If ad fails to load, user must have a clear retry path; generation must never be granted without reward callback.
- **Privacy & Security**: Ensure ad identifiers/properties comply with policy; do not log PII in analytics properties.
- **Accessibility**: Modal must support Dynamic Type and VoiceOver/TalkBack focus order; CTAs must meet minimum touch targets.
- **Observability**: Log ad load failures with reason codes; track funnel from `modal_shown` → `ad_started` → `ad_completed`.
- **Localization**: All modal copy must be localizable.

---

## UI States


| State                    | Behavior / Copy                                                                              |
| ------------------------ | -------------------------------------------------------------------------------------------- |
| Loading (ad pre-loading) | Skeleton/animation shown; "Watch Ad" button replaced with spinner; "Go PRO" remains active   |
| Ad playing               | Full-screen ad; no app UI visible                                                            |
| Ad completed             | Modal dismisses; generation triggers automatically                                           |
| Ad failed / exited early | Modal re-appears; "Reward not granted. Please try again." message shown                      |
| Quota reached            | "Watch Ad" CTA disabled and greyed out; copy: "You've used all your free generations today." |
| PRO user                 | Modal not shown at all                                                                       |


---

## Analytics Events


| Event Name                         | Trigger                                    | Key Properties                                                     |
| ---------------------------------- | ------------------------------------------ | ------------------------------------------------------------------ |
| `modal_shown`                      | Modal appears                              | `feature` (e.g. "interior_design"), `quota_remaining`, `ab_cohort` |
| `ad_started`                       | User taps "Watch Ad" and ad begins playing | `feature`, `ab_cohort`                                             |
| `ad_completed`                     | Reward callback received                   | `feature`, `ab_cohort`                                             |
| `ad_skipped`                       | User exits ad before completion            | `feature`, `ab_cohort`                                             |
| `upgrade_tapped`                   | User taps "Go PRO" from modal              | `feature`, `source: "ad_modal"`                                    |
| `generation_bypassed_subscription` | PRO user generates without seeing modal    | `feature`                                                          |


---

## Technical Context

- **Builds on / reuses:** Existing "Generate" trigger points across all AI flows; existing RevenueCat subscription check; existing Remote Config integration
- **New integrations or services needed:** Google Mobile Ads SDK (AdMob) — new SDK, not currently integrated
- **What data does this read or write:** Reads subscription entitlement status (RevenueCat); reads Remote Config flag values; writes daily ad quota counter to local device storage
- **Remote Config / feature flags needed:** `ads_enabled_per_flow` (per-feature toggle), `daily_ad_quota` (daily limit), `ad_unit_ids` (platform-specific ad unit IDs)
- **Key architecture decisions:** Quota is per-device (local storage), not per-account — simplifies implementation but quota can be reset by reinstalling the app; modal gates the existing generation API call client-side, no backend changes required
- **Known constraints:** Ad unit IDs for test vs. production must be kept separate; AdMob requires app store approval before live ads can serve

---

## Design References

- **Figma:** [link required]
- **Competitor / benchmark references:** HubX, Renovate AI — two-option modal pattern

---

## Open Questions (Must be resolved to start)

- Confirm final modal copy and design spec (Figma)
- Define A/B test cohort assignment source of truth (Amplitude vs Firebase) and required properties

---

## Dependencies & Prerequisites

- AdMob account active and approved for this app *(confirmed per original epic)*
- A/B test cohort infrastructure must be in place before release (Amplitude or Firebase)
- RevenueCat SDK already integrated *(assumed — confirm with SE)*
- Remote Config already integrated *(assumed — confirm with SE)*
- 

## Assumptions

- The current "Generate" flows across all features have a single, identifiable trigger point that can be intercepted client-side
- AdMob will approve the rewarded ad format for this use case without policy changes
- Quota is per-device (local storage) not per-account (server-side) — simplifies implementation but means quota can be reset by reinstalling

## Risks

- AdMob policy review may delay launch if the ad placement is flagged as non-compliant — mitigate by following Rewarded Video Best Practices early
- No Figma designs attached — UI implementation estimate (+0.5pw) may increase if design requires significant iteration
- A/B test cohort assignment strategy not defined — if not resolved before dev starts, analytics will be unreliable

---

