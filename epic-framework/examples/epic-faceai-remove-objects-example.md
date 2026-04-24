# Epic: Remove Objects (Magic Eraser)

> **Status:** Created — NOT ready for Engineering (see gaps below)
> **Project:** FAIOSMAU
> **Epic Key:** FAIOSMAU-366
> **Epic Type:** UI Feature

---

## TL;DR

Add a "Magic Eraser" tool that lets users paint over unwanted objects in their selfies — a bin, a person in the background, a sign — and have the app intelligently fill the space to match the surrounding area. The tool reuses the existing Retouch brush infrastructure and delegates inpainting to an AI/ML API.

---

## Business Goal

Keep the app competitive by matching a high-end AI editing feature already present in top competitors. Also serves as a monetization enabler — the feature can be gated behind PRO.

## Problem Statement

Users can fix small skin blemishes with the existing Retouch tool, but cannot remove large distractions from the background of a photo. If a great selfie is ruined by something in the background, users currently have no recourse in the app and must leave to a competitor tool.

---

## Scope

### In Scope

**Mobile (iOS)**

- New "Remove Objects" toolbar entry in the main editing toolbar
- Full-screen editing view reusing Retouch screen structure (view + view model)
- Brush selection for painting over target objects
- Pinch-to-zoom (1x–4x) and two-finger pan for precise work
- "Remove" CTA that triggers the API call
- Loading state while AI processes the image
- Error state if API call fails
- Undo/redo support for brush strokes and for the removal result

**Backend API**

- New `/remove-objects` endpoint
- Request validation (image format, mask format, size limits)
- Routing to AI/ML pipeline

**AI / ML Pipeline**

- AI inpainting for large regions via third-party or cloud vendor
- Vendor integration, quality tuning, fallback handling

**Analytics**

- Events: `tool_opened`, `mask_painted`, `remove_tapped`, `removal_completed`, `removal_failed`, `undo_tapped`

### Out of Scope

- Android — not in this iteration
- Video / multi-frame support
- Selecting objects by tapping (smart selection) — brush-only for now
- Removing multiple separate objects in a single session (one removal per tap)
- Background replacement after removal (fill-only, no background swap)
- PRO gating logic — to be handled in a separate monetization epic if needed

---

## Delivery Plan

| Milestone | User-visible outcome | Scope (high level) | Exit criteria (QA verifiable) | Release / Flagging |
| --------- | -------------------- | ------------------ | ----------------------------- | ------------------ |
| M1        | Tool shell exists with mask painting UX | Screen + brush canvas + zoom/pan + undo/redo for strokes | Users can open tool, paint mask, undo strokes; no crashes; no API calls | Behind feature flag (off by default) |
| M2        | End-to-end removal works | Backend endpoint + upload contract + inpainting integration + result apply/undo | “Remove” triggers API; success replaces image; error preserves mask | Keep behind flag |
| M3        | Quality + analytics ready for rollout | Vendor quality tuning + analytics + regression coverage | Quality bar met on defined test set; all key events fire | Gradual rollout |

> **EM estimate:** ~3.5 person-weeks total *(filled during or after grooming)*

---

## User Flows

### Happy Path — User removes an unwanted object

1. User is on the Editor screen with a photo loaded
2. User taps the "Remove Objects" tool in the toolbar
3. Remove Objects screen opens with the photo and an empty brush canvas overlaid
4. User pinches to zoom in on the area they want to remove
5. User paints over the object with their finger (brush stroke recorded as a mask)
6. User taps "Remove"
7. Loading state shown while AI processes image + mask
8. Result is displayed: object removed, area filled naturally
9. User accepts the result → edit is committed to the editing stack (undo/redo available)

### Variant — User is not happy with the result

1. Steps 1–8 above
2. User taps Undo → the removal is reversed, mask is restored
3. User adjusts the mask and taps "Remove" again

### Variant — API call fails

1. Steps 1–6 above
2. API returns an error or times out
3. Error state shown: "Something went wrong. Please try again."
4. "Remove" CTA is re-enabled; mask is preserved so the user doesn't have to repaint

### Variant — User over-paints or makes a mistake with the brush

1. Steps 1–5 above
2. User taps Undo on the brush canvas → last brush stroke is removed
3. User corrects and taps "Remove"

---

## Acceptance Criteria

- "Remove Objects" entry is visible in the main editing toolbar
- Brush canvas overlays the full image; strokes are rendered in a semi-transparent highlight colour
- Pinch gesture zooms 1x–4x; two-finger pan works at all zoom levels (reused from `BezierDrawingView`)
- Tapping "Remove" uploads the original image + mask to `/remove-objects` endpoint and displays a loading state
- Generation fires **only** after "Remove" is tapped, not during brush painting
- On success, the processed image replaces the canvas view and is added to the undo stack
- On API failure, the error state is shown and the mask is preserved (user can retry without repainting)
- Undo reverts one step at a time (brush strokes and removal results are separate undo items)
- Regression: Retouch and Paint tools are unaffected by this change

---

## Non-functional Requirements (NFRs)

- **Performance**: Mask painting must remain responsive at max zoom; API processing time target defined with vendor.
- **Reliability**: Upload retries and timeouts defined; failures must preserve mask for retry.
- **Privacy & Security**: Clarify whether images are sent to third-party vendor; define retention and consent requirements.
- **Accessibility**: Touch targets and tool controls must be accessible; ensure error messaging is announced.
- **Observability**: Track processing time, failure reasons, and vendor response codes.
- **Localization**: All tool copy must be localizable.

---

## UI States


| State                                | Behavior / Copy                                                                                                                                    |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Initial (tool opened)                | Photo shown full-screen with empty brush canvas; toolbar shows brush size control and Undo; "Remove" CTA disabled until at least one stroke exists |
| Painting                             | Semi-transparent highlight overlay appears as user paints; "Remove" CTA enabled                                                                    |
| Loading                              | Full-screen loading indicator over the photo; "Remove" CTA replaced with spinner; Undo disabled                                                    |
| Success                              | Processed image displayed; editing tools available; result added to undo stack                                                                     |
| Error                                | Error toast/banner: "Something went wrong. Please try again."; "Remove" CTA re-enabled; mask preserved                                             |
| Empty mask (user clears all strokes) | "Remove" CTA disabled again                                                                                                                        |


---

## Analytics Events


| Event Name          | Trigger                                | Key Properties                         |
| ------------------- | -------------------------------------- | -------------------------------------- |
| `tool_opened`       | User enters the Remove Objects screen  | `source` (toolbar entry point)         |
| `mask_painted`      | User lifts finger after a brush stroke | `stroke_count` (cumulative in session) |
| `remove_tapped`     | User taps "Remove"                     | `stroke_count`, `zoom_level`           |
| `removal_completed` | Success response received from API     | `processing_time_ms`                   |
| `removal_failed`    | API error or timeout                   | `error_code`                           |
| `undo_tapped`       | User taps Undo                         | `undo_target` (`stroke` or `removal`)  |


---

## Technical Context

- **Builds on / reuses:** Existing Retouch screen structure and brush canvas with pinch-to-zoom and two-finger pan; existing image upload infrastructure from Retouch and Paint tools
- **New integrations or services needed:** AI/ML inpainting vendor — not yet selected (see Open Questions); new backend endpoint required to route image + mask to the inpainting pipeline
- **What data does this read or write:** Reads original image and brush mask; writes inpainted image back to the editing stack. No new persistence beyond the existing edit stack.
- **Remote Config / feature flags needed:** None for MVP; add if PRO gating is introduced in a follow-up
- **Key architecture decisions:** None locked yet — AI/ML vendor, image upload contract, and PRO gating are all open (see Open Questions)
- **Known constraints:** iOS only for this iteration; backend endpoint and vendor integration are on the critical path — mobile UI can start in parallel but cannot complete without them

---

## Design References

- **Figma:** 
- **Competitor / benchmark references:** Competitor apps with similar tools (Snapseed Healing, Samsung Object Eraser) for UX reference

---

## Open Questions (Must be resolved to start)

- Select AI/ML vendor and define quality bar + cost constraints
- Define request/response contract for `POST /remove-objects` (formats, limits, error codes)
- Confirm whether PRO gating is required for MVP (and if so, which entitlement logic)
- Provide Figma designs for the new screen/tool controls

---

## Dependencies & Prerequisites

- `/remove-objects` backend endpoint must be available (or mocked) before mobile business logic work begins
- AI/ML vendor must be selected and integrated in the pipeline before the backend endpoint is live — **this is the longest lead-time item**
- Figma designs must be delivered before Mobile UI work begins
- `BezierDrawingView` compatibility confirmed for this new context

## Assumptions

- Brush and pinch-to-zoom interaction is fully reusable from `BezierDrawingView` with no modifications
- AI inpainting will use a third-party/cloud API — not built in-house; if YouCam supports inpainting, the AI/ML estimate reduces
- One removal per "Remove" tap (not batch/multi-object in a single call)
- iOS only for this iteration

## Risks

- **AI/ML vendor not selected** — the entire backend estimate depends on this. Until decided, the 1.0pw AI/ML block is a placeholder. This is the single biggest blocker.
- **No Figma designs attached** — Mobile UI cannot start without them; +0.5pw risk if significant design iteration occurs
- **Inpainting quality on selfies** — background fill quality varies significantly by vendor and image complexity; quality tuning time is hard to estimate upfront. Build in a QA quality gate before release.
- `**BezierDrawingView` adaptation** — if the existing component needs non-trivial modification for this context, the 1.0pw Mobile UI estimate may increase

