# Interview Exercise — Feature Briefs

The candidate receives two short feature briefs framed as if a Product Owner had written them in a Jira ticket. They are deliberately concise and partially ambiguous. Part of what we are testing is whether the candidate (and their AI) can identify and resolve that ambiguity.

The interviewer plays the PO role: available to answer clarifying questions, but should not volunteer detail unless asked.

---

## Feature 1 — Favourite confirmation

> **As a user**, when I tap the favourite button on a smoothie, I want to see that the action worked, so I'm confident the item has been saved to my favourites.

### What "good" looks like (interviewer notes — not shared with the candidate)

There is no single correct answer. Reasonable interpretations include:

- A small animation on the icon (scale, bounce, fill transition)
- A short haptic on tap
- A subtle toast / inline confirmation
- Combination of the above

Things to listen for:

- **Do they ask where this applies?** (List row, detail screen, both?)
- **Do they ask about platform behaviour?** (iOS vs. macOS — Fruta is multiplatform)
- **Do they ask about the unfavourite path?** (Does removing also need feedback?)
- **Do they check the existing favourite implementation first** before designing on top of it?

---

## Feature 2 — Share a smoothie

> **As a user**, I want to share a smoothie I love with a friend, so they can check it out too.

### What "good" looks like (interviewer notes — not shared with the candidate)

Reasonable interpretations include:

- A `ShareLink` (iOS 16+) with the smoothie name and a short description
- Sharing an image of the smoothie card
- Sharing a deep link (even if the deep link itself doesn't fully work in this exercise)
- A custom share sheet via `UIActivityViewController`

Things to listen for:

- **Do they ask what to share?** (Text, image, link, all of the above?)
- **Do they ask about discoverability?** (Toolbar button? Context menu? Both?)
- **Do they consider iPad / macOS share behaviour?**
- **Do they verify the API they choose actually exists** rather than trusting the AI's first suggestion? (`ShareLink` requires iOS 16+; the AI may hallucinate APIs.)

---

