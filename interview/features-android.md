# Interview Exercise — Feature Briefs (Android)

The candidate receives two short feature briefs framed as if a Product Owner had written them in a Jira ticket. They are deliberately concise and partially ambiguous. Part of what we are testing is whether the candidate (and their AI) can identify and resolve that ambiguity.

The interviewer plays the PO role: available to answer clarifying questions, but should not volunteer detail unless asked.

**Codebase:** [Now in Android](https://github.com/android/nowinandroid) — Google's official Jetpack Compose sample app. Multi-module Kotlin + Compose + Hilt + Room.

**Fallback codebase (mid-level candidates):** [JetSnack](https://github.com/android/compose-samples/tree/main/Jetsnack) — single-module Compose sample. Note: JetSnack has no bookmark feature, so Feature 1 must be reworded to "add a favourite button with feedback".

---

## Feature 1 — Bookmark confirmation

> **As a user**, when I tap the bookmark icon on a news item, I want to see that the action worked, so I'm confident the article has been saved for later.

### What "good" looks like (interviewer notes — not shared with the candidate)

There is no single correct answer. Reasonable interpretations include:

- A small animation on the icon (scale, fill transition, Compose `animate*AsState`)
- Haptic feedback on tap (`HapticFeedbackConstants.CONFIRM` or `LocalHapticFeedback`)
- A Snackbar confirmation — ideally with an Undo action (Material 3 guidance)
- Combination of the above

Things to listen for:

- **Do they ask where this applies?** Now in Android surfaces bookmark actions in multiple places — Feed, Topic detail, Search results. Do they consider all three or just one?
- **Do they check the existing bookmark implementation first** before designing on top of it? (`userNewsResourceRepository`, `BookmarksViewModel`)
- **Do they raise the Undo affordance?** Material 3 strongly suggests Snackbar+Undo for reversible actions.
- **Do they consider phone vs. tablet/foldable** behaviour?
- **Do they specify Material 3** (the project uses M3) or do they let the AI default to M2 patterns?

---

## Feature 2 — Share a news item

> **As a user**, I want to share a news article with a friend, so they can read it too.

### What "good" looks like (interviewer notes — not shared with the candidate)

Reasonable interpretations include:

- `Intent.ACTION_SEND` with the article title + URL via `Intent.createChooser`
- `ShareCompat.IntentBuilder` (the recommended AndroidX helper)
- Android 14+ **custom chooser with preview** (title, thumbnail, description)
- A share action exposed from the news card's overflow menu, from a top-app-bar icon on the detail screen, or both

Things to listen for:

- **Do they ask what to share?** (URL only, title + URL, image preview?)
- **Do they ask about discoverability?** (Overflow on the card? Toolbar action on detail? Both?)
- **Do they verify the API works on the project's `minSdk`** rather than trusting the AI's first suggestion? (AI often hallucinates Compose share APIs or suggests newer APIs without checking `minSdk`.)
- **Do they consider tablet/foldable share-sheet behaviour?**
- **Do they pass the activity context correctly** from a Composable? (Common AI mistake: using `LocalContext.current` without checking it's an Activity context for the chooser.)

---
