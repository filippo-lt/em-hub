# Garden Design — Spec

> Source: ADIOSMAU Xray export 2026-05-04, 21 manual tests prefixed `[Garden]` / `Garden` / `[Garden design]`.
> Anything below not directly derivable from those tests is marked `(inferred)` and should be confirmed against code.

## Purpose

Garden Design generates an AI-rendered garden image from a user-supplied
photo (or template) plus a chosen style and color palette.

## Entities

| Entity              | Fields / notes                                                                                              |
| ------------------- | ----------------------------------------------------------------------------------------------------------- |
| `Photo`             | source ∈ {camera, gallery, template}; orientation ∈ {portrait, landscape}                                   |
| `Style`             | id; kind ∈ {preset, custom-prompt, original}; entitlement ∈ {free, premium, blocked} *(inferred from -305)* |
| `Palette`           | id; entitlement ∈ {free, premium, blocked}; special tiles: `surprise-me`, `original`                        |
| `CustomPrompt`      | text; persisted across flows (last-saved is preselected — ADIOSMAU-307)                                     |
| `Template`          | id; tier ∈ {free, pro}                                                                                      |
| `GenerationRequest` | photo + style + palette → result image                                                                      |
| `Project`           | persisted result image, listed in Projects tab (ADIOSMAU-146)                                               |

## State machine

```
                          ┌───────────────┐
                          │   MainScreen  │
                          └───────┬───────┘
                                  │ tap Garden Design tile
                                  ▼
                          ┌───────────────┐
                ┌────X────│    Step 1     │   provide photo
                │         │  (photo)      │   (camera | gallery | template)
                │         └───────┬───────┘
                │                 │ continue (enabled iff photo set)
                │                 ▼
                │         ┌───────────────┐
                │         │    Step 2     │   pick style
                │         │  (style)      │   (preset | custom-prompt | original)
                │         └───────┬───────┘
                │                 │ continue (enabled iff style set)
                │                 ▼
                │         ┌───────────────┐
                │         │    Step 3     │   pick palette
                │         │  (palette)    │   (preset | surprise-me | original)
                │         └───────┬───────┘
                │                 │ generate (enabled iff palette set)
                │                 ▼
                │         ┌───────────────┐
                │         │  Generating   │   ~45s; loader shown
                │         └───────┬───────┘
                │                 │ success
                │                 ▼
                │         ┌───────────────┐
                │         │    Result     │ ──► persisted to Projects
                │         └───────────────┘
                │
                └─► tap X (header) at any step → MainScreen, ALL selections discarded
```

**Invariants** *(asserted by tests)*:
- `Continue` button on step N is disabled iff step N's required input is unset.
- `Generate` button on step 3 is disabled iff palette is unset.
- Cancelling via header X discards all in-flow state (ADIOSMAU-308).
- Tapping `Continue` repeatedly is idempotent — both for navigation and for analytics events (ADIOSMAU-175).
- Last saved custom prompt persists across flows and is the default selection on next entry to step 2 (ADIOSMAU-307).

## External dependencies

### Firebase / Firestore
- `styles/styleOriginalStyle` — boolean enable flag for the "Original style" tile on step 2 (ADIOSMAU-93).
- `gardenDesignColorPalettes/colorPaletteOriginalPalette-0` — boolean enable flag for the "Original palette" tile on step 3 (ADIOSMAU-93).
- Palette entries carry per-entry entitlement state ∈ {enabled-free, enabled-premium, blocked}; blocked entries must not appear in step 3 (ADIOSMAU-305).

### Analytics (Amplitude)
- `start_garden` — fired on entry to Garden Design; no properties (ADIOSMAU-1284).
- `view_screen_garden` — fired on each step view; property `screen_number` (ADIOSMAU-1284). *(Property type/values not specified in source — needs PM confirmation.)*
- Analytics events must be debounced against multi-tap on `Continue` (ADIOSMAU-175).

### Network / connectivity
- Image generation requires network. Offline at generate-time presents the No Internet screen with a "Try again" affordance; recovery is in-place (ADIOSMAU-313).

### Monetisation
- Tapping a PRO template in the Garden footer presents the Payment screen (ADIOSMAU-212). *(Whether premium palettes/styles also gate via the same screen is not asserted by tests — gap.)*

### Localisation
- All copy in steps 1–3 must render in the device language (ADIOSMAU-310). Supported locale list is not specified in tests — pull from `Localizable.strings` / project config.

## Out-of-scope assertions (non-automatable)

These are present in tests but should be tagged `@manual-only` and excluded from LLM-generated unit tests:

- "Image is of acceptable quality" (ADIOSMAU-158)
- "Layout matches Figma" (ADIOSMAU-157, ADIOSMAU-93)
- "Content violation scenarios working correctly" (ADIOSMAU-158, parenthetical)

## Glossary

- **AID** — the app (Garden Design lives inside it alongside Interior Design, Paint, etc.)
- **Step N** — the user-visible step indicator; the flow has 3 selection steps + a generation step.
- **Original style / Original palette** — special tiles that pass through input characteristics rather than transforming them.
