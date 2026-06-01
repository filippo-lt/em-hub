# MartechKit — Presentation Outline

> Audience: Mixed — Product team (POs, PMs, product leadership) + Engineering (SEs, EMs, Staff Engineer, Technical Director)
> Duration: ~15-20 min + questions
> Tone: Strategic framing (Filippo) + accessible technical overview (Victor) — no code-level deep-dives
> Presenters: **Filippo (EM)** — high-level / strategy · **Victor Jalencas (Staff Engineer)** — in-depth / technical
> Handoffs: 2 only — slide 4→5 (Filippo→Victor), slide 8→9 (Victor→Filippo)

### Visual Style Guide

All generated images should follow this consistent style:

> **Style prompt prefix (use for all image prompts below):**
> "Flat, minimal corporate infographic style. Clean vector shapes, no gradients. Colour palette: white (#FFFFFF) background, dark charcoal (#2D2D2D) text, accent colours teal (#2EC4B6), coral (#FF6B6B), and soft gold (#FFD166). No drop shadows, no 3D effects, no photorealism. Rounded rectangles for containers, thin connecting lines. Modern sans-serif typography (e.g. Inter or similar). Presentation slide aspect ratio (16:9). High contrast, clean whitespace, suitable for projecting in a meeting room."

---

## Slide 1 — Cover

**Presenter:** Filippo

**Title:** MartechKit — One SDK for All Our Martech

**Message:** Set the frame: this isn't just a new library, it's how we stop re-wiring the same vendor integrations in every app. Part of the broader shared-components strategy.

**Format:** Text only. Title + subtitle (e.g. "Unified Amplitude, RevenueCat & AppsFlyer across the portfolio").

---

## Slide 2 — Same Integration, Wired 10 Times

**Presenter:** Filippo

**Title:** Same Integration, Wired 10 Times

**Message:** Every app integrates the same third-party Martech tools — Amplitude, RevenueCat, AppsFlyer — from scratch. Different implementations, different versions, different event names. The result is drift: no two apps wire these the same way, and every Martech change becomes a portfolio-wide ticket.

Don't dwell — everyone in the room has felt this.

**Format:** Schematic showing N apps each with their own duplicated vendor stack. The point is the redundancy, not the architecture.

**🖼 Image prompt:**

> [Style prefix] + "Six app icons arranged in a row, each sitting on top of its own identical vertical stack of three rounded rectangles labelled 'Amplitude', 'RevenueCat', 'AppsFlyer'. Each stack is isolated — no connections between them. Use coral for the app icons and teal for the stacked boxes. Below the row, a subtle label: '6 apps × 3 vendor integrations = 18 implementations to maintain'. The visual should emphasise wasteful duplication and drift."

---

## Slide 3 — What That Costs Us

**Presenter:** Filippo

**Title:** What That Costs Us

**Message:** The duplication isn't just wasteful — it actively breaks things:

- **Mis-tracked events.** Each app names and structures events differently, so cross-app product analysis is unreliable or impossible.
- **Martech bottlenecked on engineering.** Every experiment or vendor change waits on per-app dev work.
- **Cognitive load on engineers.** Every developer has to learn the quirks of each vendor SDK.

This is the slide for the product half of the room — the cost is in the data and the speed, not just the code.

**Format:** Three plain cost blocks. Keep it about impact, not implementation.

**🖼 Image prompt:**

> [Style prefix] + "Three rounded rectangle cards in a row on white background, each with a simple line icon and a short label. Card 1: broken/disconnected chart icon (coral), 'Mis-tracked events — no cross-app analysis'. Card 2: hourglass/blocked icon (coral), 'Martech waits on per-app engineering'. Card 3: tangled/overloaded brain icon (coral), 'Every dev learns every vendor'. Icons in coral to signal cost/pain, labels in dark charcoal. Clean, calm, not alarmist."

---

## Slide 4 — One Library, Single Point of Implementation

**Presenter:** Filippo → *hand off to Victor*

**Title:** One Library, Single Point of Implementation

**Message:** The shift: the vendor tooling lives behind a single shared library. Apps integrate MartechKit once; Martech changes ship as a version bump instead of a portfolio-wide re-implementation.

This is the same pattern as Parapet — build once, integrate everywhere. MartechKit is the Martech piece of a growing shared-components platform.

**Handoff line (Filippo):** "That's the why and the what. Victor built this end-to-end — he'll take you through how it actually works."

**Format:** The "before vs after" shift. Left: each app wiring vendors directly. Right: apps integrating one library that owns the vendors.

**🖼 Image prompt:**

> [Style prefix] + "Split-screen layout separated by a thin vertical line. LEFT SIDE titled 'Before' (coral accent): three app icons each with three messy lines connecting directly to three vendor boxes ('Amplitude', 'RevenueCat', 'AppsFlyer') — a tangle of duplicated connections. RIGHT SIDE titled 'With MartechKit' (teal accent): the same three app icons each connecting with a single clean line to one rounded rectangle labelled 'MartechKit', which in turn connects to the three vendor boxes. The contrast: many tangled lines vs one clean integration point."

---

## Slide 5 — Technical Overview: The Facade

**Presenter:** Victor

**Title:** One Clean API, Vendors Hidden Inside

**Message:** MartechKit is a facade over the vendor SDKs. The app calls one simple, stable API — track an event, identify a user, check an entitlement. Inside, MartechKit fans that call out to Amplitude, RevenueCat, AppsFlyer, and whatever else we add. Vendor specifics — initialisation order, quirks, SDK upgrades — stay inside the library, never in app code.

Adding or swapping a vendor is a change inside MartechKit; the app-facing API doesn't move.

**Format:** Conceptual layered diagram — app layer → MartechKit facade → vendor SDKs. No code. Engineers should grasp the boundary; product should grasp "one door in."

**🖼 Image prompt:**

> [Style prefix] + "A clean three-layer horizontal diagram on white background. TOP layer: a single wide rounded rectangle labelled 'App code — one API: track / identify / entitlement' (charcoal text). MIDDLE layer: a prominent teal rounded rectangle labelled 'MartechKit (facade)' connected to the top layer by a single thin line. BOTTOM layer: three smaller rounded rectangles side by side labelled 'Amplitude', 'RevenueCat', 'AppsFlyer', each connected to the MartechKit box by thin lines, plus a faded fourth box with '...' indicating more vendors can be added. The key visual: one connection above the facade, many below it."

---

## Slide 6 — The Shared Event Dictionary

**Presenter:** Victor

**Title:** Same Event, Same Schema, Everywhere

**Message:** The biggest unlock isn't the wrapper — it's the shared event dictionary. Every app tracks the same events with the same names and the same schema, defined once inside MartechKit. No more "purchase_completed" in one app and "buy_success" in another.

The payoff: clean, consistent data across the whole portfolio, so cross-app product analysis actually works — and mis-tracked events drop sharply because the schema is enforced by the library, not by each developer's memory.

**Format:** Before/after on event naming. Left: inconsistent event names per app. Right: one shared dictionary feeding all apps.

**🖼 Image prompt:**

> [Style prefix] + "Split layout on white background. LEFT SIDE titled 'Before' (coral): three app icons, each with a small list of differently-named events ('buy_success', 'purchase_done', 'checkout_ok') — emphasise inconsistency. RIGHT SIDE titled 'With MartechKit' (teal): a single central rounded rectangle labelled 'Shared Event Dictionary' with a clean list ('purchase_completed', 'screen_viewed', 'feature_used'), with thin lines fanning out to the same three app icons — all drawing from one source. The visual contrast: scattered/inconsistent vs single source of truth."

---

## Slide 7 — Integration & Distribution

**Presenter:** Victor

**Title:** From Portfolio-Wide Tickets to a Version Bump

**Message:** Integrating MartechKit means adding one library and a configuration — not wiring each vendor from scratch. MartechKit handles the vendor SDKs, their setup, and the event plumbing.

Once an app is on MartechKit, Martech changes — a new vendor, an updated SDK, a new tracked event — ship as a version bump that every app picks up. What used to be a coordinated ticket across the whole portfolio becomes a routine dependency update.

**Format:** Show the integration as lightweight, and the ongoing model as "bump and go." Keep it conceptual.

**🖼 Image prompt:**

> [Style prefix] + "On white background, two stacked rows. TOP ROW titled 'Integrate once' (teal): an app icon with a single arrow into a rounded rectangle labelled 'Add MartechKit + config', then a checkmark. BOTTOM ROW titled 'Then: every change is a version bump' (soft gold): a 'MartechKit v1.1' box with arrows fanning out to six app icons, each showing a small upward version arrow — all updating from one release. The contrast: integrate once at the top, effortless propagation at the bottom. Clean and calm."

---

## Slide 8 — Where We Are

**Presenter:** Victor → *hand back to Filippo*

**Title:** Live on iOS, Validated in 3 Pilots

**Message:** MartechKit v1.0 for native iOS is live today, validated in three pilot apps — including the integration work, done end-to-end. The pilots prove the facade and the event dictionary hold up in real apps, not just in theory.

Victor speaks to what validation actually looked like: how the pilot integrations went, anything caught early, how the event dictionary behaved across the three apps.

**Handoff line (Victor):** "That's where the technology stands today. Filippo will take you through where it goes from here."

**Format:** Credibility slide — proof over promises. Show iOS v1.0 live + the three pilot apps.

**🖼 Image prompt:**

> [Style prefix] + "On white background, a 'Live' badge in teal at the top with text 'MartechKit v1.0 — native iOS'. Below it, three app icons in a row, each with a teal checkmark, under a label 'Validated in 3 pilot apps'. To the side, a small Apple/iOS platform icon. Clean and contained — the impression is 'this is real and running', not 'this is coming'."

---

## Slide 9 — The Road to Full Coverage

**Presenter:** Filippo

**Title:** The Road to Full Coverage

**Message:** Three steps to portfolio-wide coverage:

1. **Roll out across the rest of the native iOS portfolio.**
2. **Android version of the library — in parallel.**
3. **Flutter version of the library — in parallel.**

Once Android and Flutter land, we have full portfolio coverage. And MartechKit sits alongside the other shared components — Parapet, AI Gateway, TVFoundationSDK — as part of one repeatable platform pattern, not a one-off.

**Format:** Roadmap with the three parallel tracks, plus a callback to the broader shared-components platform.

**🖼 Image prompt:**

> [Style prefix] + "On white background, top half: three horizontal tracks labelled 'iOS portfolio rollout' (teal, marked in progress), 'Android library' (soft gold, parallel), 'Flutter library' (soft gold, parallel), all converging on the right into a single milestone marker labelled 'Full portfolio coverage'. Bottom half: a thin strip showing four small component chips — 'Parapet', 'AI Gateway', 'TVFoundationSDK', 'MartechKit' (MartechKit highlighted in teal) — under a subtle label 'One shared-components platform'. Clean, forward-moving, not cluttered."

---

## Slide 10 — Credit & Close

**Presenter:** Filippo

**Title:** Thank You / Q&A

**Message:** Credit where due: MartechKit was designed and built end-to-end by **Victor Jalencas**, including the three pilot integrations. Thanks also to **David Sanchez and his team** for shaping the initiative and the context behind it.

**Format:** Minimal. Title + subtitle + a clear credit line for Victor. Open for questions (both presenters field).

---
