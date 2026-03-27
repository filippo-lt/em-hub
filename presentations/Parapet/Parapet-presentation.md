# Parapet — Presentation Outline

> Audience: Product team (POs, PMs), CPMO, COO, Technical Director
> Duration: ~15-20 min + questions
> Tone: Strategic, concise, no technical deep-dives

### Visual Style Guide

All generated images should follow this consistent style:

> **Style prompt prefix (use for all image prompts below):**
> "Flat, minimal corporate infographic style. Clean vector shapes, no gradients. Colour palette: white (#FFFFFF) background, dark charcoal (#2D2D2D) text, accent colours teal (#2EC4B6), coral (#FF6B6B), and soft gold (#FFD166). No drop shadows, no 3D effects, no photorealism. Rounded rectangles for containers, thin connecting lines. Modern sans-serif typography (e.g. Inter or similar). Presentation slide aspect ratio (16:9). High contrast, clean whitespace, suitable for projecting in a meeting room."

---

## Slide 1 — Cover

**Title:** Parapet & the Shared Components Strategy

**Message:** Set the frame from the first second — this isn't just a system demo, it's a strategic shift in how we build across the portfolio.

**Format:** Text only. Title + subtitle (e.g. "Unified Quota Management for the MAU Portfolio").

---

## Slide 2 — Same Problem, Solved 10 Times

**Title:** Same Problem, Solved 10 Times

**Message:** Every app that needs quotas, auth, or subscription handling builds it from scratch. Different implementations, different bugs, no shared foundation. Product teams wait on custom development every time a new app needs something that already exists elsewhere.

Don't dwell — one slide. Everyone in the room already feels this.

**Format:** Simple visual showing N apps each with their own isolated stack (quota logic, sub handling, database). Keep it schematic, not architectural. The point is the redundancy, not the technology.

**🖼 Image prompt:**

> [Style prefix] + "Six app icons arranged in a row, each sitting on top of its own identical vertical stack of three rounded rectangles labelled 'Quota Logic', 'Sub Handling', 'Database'. Each stack is isolated — no connections between them. Use coral for the app icons and teal for the stacked boxes. Below the row, a subtle label: '6 apps × 3 custom implementations = 18 problems'. The visual should emphasise wasteful duplication."

---

## Slide 3 — The Shift: Build Once, Integrate Everywhere

**Title:** Build Once, Integrate Everywhere

**Message:** We're moving from a collection of apps that each reinvent the wheel to a portfolio that shares infrastructure. The approach: cloud services + client libraries that any app can plug into.

Four shared components are already in motion:

- **Parapet** — quota, auth, tokens (live)
- **AI Gateway** — centralised AI access (in progress)
- **TVFoundationSDK** — shared TV platform capabilities (in progress)
- **MartechSDK** — shared martech for apps (in progress)

This is a repeatable pattern, not a one-off project.

**Format:** A matrix-style infographic showing which apps adopt which shared components — not everything is for everyone. The visual should also convey that more components are coming. This is the slide that makes C-level lean in — make the vision tangible.

**🖼 Image prompt:**

> [Style prefix] + "An adoption matrix on white background. No title. COLUMNS (left to right): 'Parapet' (teal header), 'AI Gateway' (teal header), 'TVFoundationSDK' (teal header), 'MartechSDK' (teal header), then two additional columns with no label — just a subtle '?' or '...' in soft grey, representing unnamed future components. ROWS: 6-8 app names listed vertically on the left side in dark charcoal text (e.g. Photo Up, Face AI, Tattooist, App 4, App 5, App 6, App 7, App 8). At each intersection, show a filled teal dot where the app adopts that component, and an empty/absent dot where it doesn't. The key pattern: the 'MartechSDK' column is fully filled (every app has a dot) — it's universal. The 'Parapet' and 'TVFoundationSDK' columns have dots for only some apps (roughly half). The 'AI Gateway' column has dots for a few apps. The two unnamed future columns have no dots yet — they are visually lighter and faded, showing the platform is growing. The overall impression: a shared platform with selective adoption per component, and room to grow. Clean grid lines, generous spacing, no clutter."

---

## Slide 4 — What Parapet Handles

**Title:** What Parapet Handles

**Message:** Four things, stated plainly:

1. **Device authentication** — verifies real users on real devices (App Check)
2. **Quota management** — tracks feature usage limits per user, resets automatically
3. **Token / credit system** — persistent credits users buy via in-app purchase
4. **Subscription sync** — RevenueCat integration keeps everything in sync automatically

Multi-tenant: one system, all apps. Works across iOS, Android, Flutter, and any backend. Web support is ready — looking for the first web app to integrate.

**Format:** Text with four clear blocks or icons. No architecture diagram — keep it functional. The audience should walk away knowing what Parapet does, not how it's built.

**🖼 Image prompt:**

> [Style prefix] + "Four evenly spaced rounded rectangle cards arranged in a 2×2 grid on a white background. Each card has a simple line icon at the top and a label below. Card 1: shield icon, 'Device Auth'. Card 2: gauge/meter icon, 'Quota Management'. Card 3: coin/token icon, 'Token System'. Card 4: sync/circular arrows icon, 'Subscription Sync'. Icons in teal, labels in dark charcoal. Below the grid, a thin horizontal line with platform icons: Apple, Android, Flutter, Web — indicating cross-platform support."

---

## Slide 5 — Configure, Don't Code

**Title:** Configure, Don't Code

**Message:** The Control Center is a web dashboard where product and support teams can:

- Set and change quota limits per app, per feature
- Configure reset schedules (daily, weekly, monthly, billing cycle)
- View any user's quota/token state in real time
- Debug issues directly — no engineering ticket needed

Changes take effect immediately. No sprint, no deploy, no waiting.

**Format:** This slide frames the demo or screenshots. If live demo: a few bullet points that set up what the audience is about to see. If screenshots: 2-3 key screens (app config, user lookup, quota view). Either way, structure the slide so it works standalone.

**🖼 Visual note:** Use actual screenshots from the Control Center dashboard (app config screen, user lookup screen, quota view). Place 2-3 screenshots in a row with thin teal borders and subtle rounded corners to match the presentation style. If screenshots aren't available yet, use placeholder mockups.

---

## Slide 6 — Tokens: Now Available to Every App

**Title:** Tokens: Now Available to Every App

**Message:** Some apps already use consumable credits, but each built its own implementation. With Parapet, any app in the portfolio can offer token packs out of the box — no custom development needed.

- Tokens persist until consumed (no reset)
- Independent of subscriptions — works for free and paying users
- Purchased via RevenueCat, credited automatically
- Backend decides what costs how much — full flexibility for A/B testing pricing

The capability existed in pockets. Now it's a standard, available to every app from day one.

**Format:** Text, possibly with a simple comparison table (Quotas vs Tokens — what each is best for). Keep it focused on the business opportunity, not the mechanics.

**📊 Graph description (build as a styled table/graphic in your slide tool):**

> Two-column comparison table on white background. Left column header: "Quotas" (teal). Right column header: "Tokens" (soft gold). Rows:
>
>
> |                       | Quotas                     | Tokens                                |
> | --------------------- | -------------------------- | ------------------------------------- |
> | Resets?               | Yes (daily/weekly/monthly) | No — persist until used               |
> | Tied to subscription? | Yes                        | No — any user                         |
> | Best for              | Limiting feature usage     | Consumable credits / pay-per-use      |
> | Example               | "5 AI edits per day"       | "Buy 100 credits for premium filters" |
>
>
> Use rounded cells, no harsh grid lines. Teal accent for quota column, gold accent for token column.

---

## Slide 7 — Fraction of the Time, Fraction of the Complexity

**Title:** Fraction of the Time, Fraction of the Complexity

**Message:** Integration time is dramatically reduced — not just faster, but simpler.

**The time:** What used to take weeks is now a fraction of that. The heavy lifting (subscription logic, quota resets, billing cycle handling, device verification) is already done.

**The knowledge burden:** Developers don't need to study RevenueCat integration, token renewal logic, or quota reset scheduling. They integrate an API. That's it. The domain complexity lives in Parapet, not in every app's codebase.

Client libraries ship with Parapet for iOS, Android, and Flutter (Web ready, looking for first integration) — plug in and go.

**Format:** Two-part message. Left side: time reduction (before vs after, without overpromising a specific number). Right side: complexity reduction — show the list of things developers no longer need to learn or build (RevenueCat webhooks, reset logic, subscription state management, device attestation). The complexity angle is the stronger message for this audience.

**🖼 Image prompt:**

> [Style prefix] + "Split-screen layout, left and right halves separated by a thin vertical line. LEFT SIDE titled 'Before' (coral accent): a tall vertical stack of 7 rounded rectangles labelled from top to bottom: 'RevenueCat Webhooks', 'Subscription State Logic', 'Quota Reset Scheduling', 'Device Attestation', 'Token Accounting', 'Billing Cycle Handling', 'Error Recovery'. A developer stick figure stands next to it looking overwhelmed. RIGHT SIDE titled 'With Parapet' (teal accent): a single small rounded rectangle labelled 'Integrate API' with a checkmark. A developer stick figure stands next to it looking relaxed. The contrast in visual weight between left and right tells the story."

---

## Slide 8 — Built in 2 Days with AI

**Title:** Built in 2 Days

**Message:** Parapet wasn't built over months by a large team. The core platform — cloud services, client libraries, Control Center — was built in 2 days by a single engineer working with AI.

This isn't a shortcut story. It's a preview of how we build going forward:

- AI handles the scaffolding, boilerplate, and integration plumbing
- Engineers focus on architecture decisions and domain logic
- What used to require a team and a quarter now requires focus and the right tools

Parapet is both a shared component *and* a proof point for the AI-assisted development model. The same approach applies to AI Gateway, MartechSDK, and whatever comes next.

**Format:** Simple, high-impact. Left side: "2 days / 1 engineer / AI-assisted" as bold stats. Right side: brief breakdown of what AI accelerated vs what required human judgment. Keep it honest — not "AI wrote everything", but "AI changed the economics of building this."

**🖼 Image prompt:**

> [Style prefix] + "Split layout on white background. LEFT SIDE: three large bold stats stacked vertically — '2 Days' in teal, '1 Engineer' in dark charcoal, 'AI-Assisted' in coral. Each stat has a thin horizontal line beneath it. RIGHT SIDE: two columns side by side. Left column header 'AI Accelerated' (teal) with 4 short items: 'API scaffolding', 'Client libraries', 'Dashboard UI', 'Integration tests'. Right column header 'Human Decisions' (coral) with 4 short items: 'Architecture', 'Security model', 'Multi-tenancy design', 'Domain logic'. The visual contrast shows the partnership between AI speed and human judgment."

---

## Slide 9 — Already Live

**Title:** Already Live

**Message:** Parapet is not a proposal — it's running in production.

- **Photo Up** — live, quota management active
- **Face AI** — live, quota management active
- **Tattooist & 1 more app** — already planned for integration

Share any concrete data or learnings from the live apps if available (e.g. integration went smoothly, support tickets reduced, specific issues caught early via Control Center).

This is the credibility slide. Proof over promises. Don't frame the remaining portfolio as a backlog — frame it as an open door.

**Format:** Text with app names/icons. Show what's live and what's committed. The rest of the portfolio is deliberately left open — no timeline, no pressure. The visual should feel like "this is ready" not "this is coming for you."

**📊 Graph description (build as a styled graphic in your slide tool):**

> On white background, two groups separated by a subtle vertical dashed line. LEFT GROUP titled "Live" (teal): Photo Up and Face AI app icons with teal checkmarks. RIGHT GROUP titled "Planned" (soft gold): Tattooist and one more app icon with soft gold arrow icons. No further pipeline, no greyed-out placeholders. Clean and contained — shows what exists, not what's being imposed.

---

## Slide 10 — Ready When You Are

**Title:** Ready When You Are

**Message:** Parapet is built, proven, and available. Any app in the portfolio can integrate — here's what that looks like:

- **Quota management** — configure limits and resets without a sprint
- **Token system** — offer consumable credits from day one
- **Subscription sync** — RevenueCat integration handled automatically
- **Control Center access** — product and support can self-serve immediately

Integration is lightweight: client libraries for iOS, Android, Flutter (Web ready). Engineering estimates a few days per app, not weeks.

No rollout plan, no mandated timeline. When a product team is ready to move, we're ready to support.

**Format:** This is the "menu" slide — show what's on offer, not what's being scheduled. The tone is invitational, not directive. Think of it as an internal product page: here's what you get, here's how easy it is, come talk to us.

**🖼 Image prompt:**

> [Style prefix] + "On white background, a clean card layout. Four rounded rectangle cards in a row, each with a simple teal line icon and a label: 'Quota Management', 'Token System', 'Subscription Sync', 'Control Center'. Below the cards, a single line of text in dark charcoal: 'Available now — integrate when you're ready.' The overall tone is calm and invitational, not urgent. No timelines, no phases, no arrows pushing forward."

---

## Slide 11 — The Bigger Picture

**Title:** The Bigger Picture

**Message:** Parapet is the first shared component. The same model — cloud service + client libraries, multi-tenant, configure-don't-code — is being applied to:

- **AI Gateway** — centralised AI service access across apps
- **TVFoundationSDK** — shared TV platform capabilities
- **MartechSDK** — shared marketing tech for the app portfolio
- …and more to come

This is how we stop building the same thing ten times. Each shared component saves weeks per app and compounds across the portfolio.

End on the vision: we're building a portfolio, not a collection of apps.

**Format:** A platform architecture map showing where Parapet sits within the broader app infrastructure. Grouped by domain (Infrastructure, Identity, Monetisation, AI, Martech, etc.) with a central "Core App" block. Shared components that are live or in progress are highlighted; everything else is neutral. This should feel strategic — the closing image the audience takes away.

**🖼 Visual note:** Use the platform architecture diagram (slide_11_bigger_picture_v4.html). The layout shows domain groups (Infrastructure, Identity, Monetisation, AI) across the top, the Core App in the centre flanked by supporting services, and cross-cutting concerns (Martech SDK, CRM, Data, Experimentation, Comms, Push, Analytics) along the bottom. Parapet's components (Quota & Tokens, Subscription Sync) are marked as "live" in teal; AI Gateway, TV Foundation Kit, and Martech SDK are marked "in progress" in gold; everything else is neutral grey. The visual reinforces that Parapet is one piece of a growing shared platform.

---

## Slide 12 — Close

**Title:** Thank You / Q&A

**Format:** Minimal. Title + subtitle + branding.