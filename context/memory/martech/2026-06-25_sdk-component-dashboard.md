# Open item — Martech SDK / component visibility dashboard

**Captured:** 2026-06-25 (Bi-Weekly Managers Apps Sync)
**Status:** Parked — to brainstorm a solution in a dedicated session
**Owner:** Filippo

## The ask
Managers can't currently answer "which app uses which version of which internal component?"
The request (raised by David, echoed by Andre) is a single place to see, per app:

- **Martech SDK** — which version each app integrates
- **Pipelines** — which steps/flavour each project uses
- **Parapet** — what each app is using (esp. web projects: Stripe, customer service, payment requirements)

## Why it matters
- No centralised view today — Filippo knows his own apps; nobody has the cross-app picture.
- Bus-factor problem: "what happens when you're on holiday?" — the answer must be queryable, not in someone's head.
- Andre wants this as a prerequisite for the Q3 push (more Martech adoption, AI agents on pipelines, Parapet on more apps). Each is a bandwidth multiplier, but only if you can see current state.

## Target
- **By end of Q3** every manager knows the component versions across their apps.
- Form factor is open: spreadsheet, "beautiful dashboard with Cursor", or an HTML view. Andre is fine with a spreadsheet to start ("it could be on a napkin") but wants it ideally **automated**, not manually copy-pasted (the manual ones go stale — cf. the still-missing pipelines spreadsheet).

## Threads to pull next session
- Source of truth: parse each repo (SPM/Gradle/pubspec manifests) vs. manual entry. Andre suggested "go to Cursor, ask the project" — automate that.
- Andre offered: "if you provide me an MCP, I'll point Cursor at it" — possible MCP/tool surface to expose component versions.
- Scope decision: Martech SDK only first, or all three components (Pipelines / Parapet / Martech SDK) together?
- Who consumes it: managers' self-serve view vs. a shared live dashboard.
- Cost concern: Andre noted token spend should go to priority work — favour a cheap/automated approach.
