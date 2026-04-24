# Epic: Retouch Tool Enhancements

> **Status:** Created — NOT ready for Engineering (see gaps below)
> **Project:** FAIOSMAU
> **Epic Key:** FAIOSMAU-255
> **Epic Type:** Algorithm/ML

---

## TL;DR

Upgrade the existing Retouch tool to feel precise and professional. The two main improvements are: deeper zoom so users can edit at pixel level, and a smarter healing algorithm that eliminates the blurry "smear" artifacts the current tool produces on fast brush strokes.

---

## Business Goal

Match market standards for retouching quality. A tool that produces clean, natural results reduces frustration and increases the perceived value of the app, directly supporting retention and PRO conversion.

## Problem Statement

The current Retouch tool fails users on fine detail work in two ways: the zoom limit prevents pixel-level precision, and fast brush strokes leave behind blurry smears rather than a clean heal. Users who notice this drop off or leave the app to use a competitor.

---

## Scope

### In Scope

**Mobile (iOS)**

- Increase maximum zoom level on the canvas to allow pixel-level editing
- Optimise touch response so the brush follows the finger with no perceptible delay
- Improve stroke and mask rendering quality (no blurry trails on fast strokes)

**Backend / Infra**

- Upgrade the healing/inpainting algorithm to produce texture-matched, seamless results
- Benchmark new algorithm against current output quality before shipping

**Analytics**

- No new events required — existing Retouch tool events cover this flow

**Remote Config / Feature Flags**

- None required for MVP

### Out of Scope

- UI or visual redesign of the Retouch screen — layout and controls stay the same
- Brush size or opacity controls — separate enhancement
- Undo/redo changes — existing behaviour is unchanged

---

## Delivery Plan

| Milestone | User-visible outcome | Scope (high level) | Exit criteria (QA verifiable) | Release / Flagging |
| --------- | -------------------- | ------------------ | ----------------------------- | ------------------ |
| M1        | Deeper zoom available | Increase max zoom + ensure rendering stays crisp | Zoom max increased; no regressions/crashes; acceptable FPS on supported devices | Behind config/flag if needed |
| M2        | Brush feels responsive | Touch-response and stroke/mask rendering improvements | No perceptible lag on target device set; no blur trails on fast strokes | Incremental rollout |
| M3        | Healing quality improved | Backend algorithm upgrade + benchmarking vs current | New algorithm meets defined quality bar on test set; no regressions on baseline cases | Rollout after QA gate |

> **EM estimate:** ~3.0 person-weeks total *(filled during or after grooming)*

---

## User Flows

### Happy Path — User retouches a fine detail

1. User opens the Editor screen with a photo loaded
2. User taps the Retouch tool
3. User pinches to zoom in to the area they want to fix — zoom goes deeper than currently possible
4. User paints over the imperfection with the brush
5. The heal result is applied immediately: texture matches the surrounding area with no smear
6. User pinches back out and continues editing or saves

### Variant — User works quickly with broad strokes

1. Steps 1–3 above
2. User moves the brush fast across a larger area
3. The heal is applied along the stroke path with no trailing blur or artifact
4. Result is clean on first pass

---

## Acceptance Criteria

- Users can zoom in significantly further than the current maximum — enough to target individual pixels on a standard selfie resolution
- The brush follows the user's finger in real time with no visible lag on supported devices
- Fast brush strokes produce no blurry smears — the healed area must blend naturally into the surrounding texture
- The healed result is visually indistinguishable from the original photo background (no visible patch border)
- Existing Retouch tool behaviour (entry point, undo/redo, save flow) is unchanged
- No regression on Paint or Remove Objects tools

---

## Non-functional Requirements (NFRs)

- **Performance**: Target FPS and max frame drops defined for zoomed-in painting; memory overhead bounded for high-res images.
- **Reliability**: Ensure consistent behavior across supported devices; handle backend failures with existing error UX.
- **Privacy & Security**: No new data collection; confirm any backend logging does not include raw image content.
- **Accessibility**: Existing Retouch UI must remain accessible after performance/gesture changes.
- **Observability**: Add/confirm metrics for heal latency and failure rates; log zoom level + device tier for performance analysis.
- **Localization**: No new strings expected (confirm).

---

## UI States


| State               | Behavior / Copy                                                                  |
| ------------------- | -------------------------------------------------------------------------------- |
| Zoomed in (new max) | Canvas renders crisp pixels at maximum zoom; no blurring of the source image     |
| Painting            | Brush stroke renders with no lag; healing applied in real time along stroke path |
| Heal completed      | Result blends seamlessly; no visible artifact or border                          |
| Error (heal fails)  | Existing error handling unchanged                                                |


---

## Analytics Events

No new events. Existing Retouch tool analytics cover this flow.

---

## Technical Context

- **Builds on / reuses:** The existing Retouch tool — same screen, same entry point, same brush interaction. This is an upgrade to the underlying behaviour, not a new feature.
- **New integrations or services needed:** None. The healing algorithm runs in the existing backend image processing pipeline — this is an in-place upgrade to that algorithm.
- **What data does this read or write:** Same as current Retouch tool — input image and brush mask in, healed image out. No new data model.
- **Remote Config / feature flags needed:** None.
- **Key architecture decisions:** Algorithm upgrade is in-place within the existing backend pipeline — no new service or vendor required; iOS only for this iteration
- **Known constraints:** Quality improvement must be validated against the current output before shipping — a regression in healing quality on simple cases is worse than no change at all.

---

## Design References

- **Figma:** Not required — no UI changes in this epic.
- **Competitor / benchmark references:** Facetune, AirBrush — reference for expected zoom depth and healing quality at pixel level.

---

## Open Questions (Must be resolved to start)

- Define target max zoom level (by device tier) and measurable “acceptable performance” thresholds
- Define QA quality bar for healing results (reference images + pass/fail examples)
- Confirm whether a feature flag/config is needed to ship zoom and algorithm changes independently

---

## Dependencies & Prerequisites

- Backend algorithm upgrade must be complete and benchmarked before iOS integration and QA can begin — this is the critical path
- QA needs a defined quality bar (e.g. reference images showing acceptable vs. unacceptable heal results) before testing starts

## Assumptions

- The UI and layout of the Retouch screen stay exactly as-is — this epic is algorithm and performance only
- iOS only for this iteration; Android follows separately
- The existing brush/canvas interaction component can support deeper zoom without a full rewrite

## Risks

- **Algorithm quality is hard to estimate upfront** — inpainting quality varies significantly by photo type (skin texture, lighting, background complexity). Build in a QA quality gate before release and define "good enough" criteria before development starts.
- **Zoom performance on older devices** — rendering at higher zoom levels may cause frame drops on older supported devices. Needs device-range testing.
- **No design references** — for a quality-focused epic with no UI changes, this is acceptable, but the QA team needs reference images to test against.

