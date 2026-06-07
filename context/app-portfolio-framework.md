# App Portfolio Investment Framework — v1

**Owner:** Filippo (EM, Mobile App Unit)
**Author date:** 2026-05-13
**Audience:** David (CTO), and product/marketing owners by extension
**Status:** Proposal — for v1 sign-off in next 1:1

---

## Purpose

Make app-level investment decisions explicit, dated, and visible at the EM layer.

Today, "is this app worth continuing to invest in?" gets answered in scattered conversations across product (Sergio, Christian, Emilio), marketing/sales (Sail), and engineering (David, me). There is no shared scoreboard, no agreed kill triggers, and no quarterly forcing function. Decisions drift; closures arrive late; extensions get conceded without a price tag (cf. AI Design externals → end Q3, ~€75k unnamed in the 12 May 1:1).

This framework converts every app into a numbered bet with a horizon, a trigger, and a tier.

---

## Why now

- David's explicit framing on 12 May: *"You are the goalkeeper of these kilos of money."* Engineering owns the human-resources investment decision per app because product won't.
- David's own mental model is already a 2×2 (Eng invest/stop × Marketing invest/stop). Today it lives in his head; this framework makes it shared.
- M&A scope is landing in Q3; carve-out readiness is a recurring ask. Both require defensible per-app investment data.

---

## Scope

**In:** All apps where the Mobile App Unit owns engineering capacity — currently AI Design, Face AI, Tattooist, Truth Seeker, iMode, Screen Mirroring, plus M&A apps (ChatUltra, Sat AI, Lorca) as ownership lands.

**Out (v1):** Internal tooling, infra-only components, shared services (Langfuse, AI Gateway). These need a different lens.

---

## Inputs

### Investment (I source)
- Engineering FTE — internal + external + advisor + QA
- Infrastructure — cloud + material 3rd-party APIs
- AI tooling — Codex, model APIs (when material)

### Investment (sourced from PM / marketing)
- Marketing spend (ads + agency + creative)
- Studio / production cost (if applicable)

### Return (sourced from PM)
- MRR / monthly revenue
- Active users (MAU)
- CAC, LTV, LTV/CAC, payback period

### Health (I source)
- Codebase state
- Team sustainability + key-person risk
- Roadmap clarity + product ownership
- Vendor / contract risk
- Security / compliance
- **AI-SE viability indicators** — codebase quality + product context recoverability. Either must be recoverable to justify rewrite-tier investment. Measured per app at scorecard time. Reference data point: pair session 2026-05-14 (Vlad on Face AI) — 40% PO/QA info gathering, 40% bad-codebase friction, 20% feature production. "SE on app" is not rewrite; it's discovery + rewrite. Discovery is SE-driven (code + analytics + reviews + QA), not PM-driven, and gated on a 1-pager that defines what the app actually is and what's in/out of the rewrite scope.

---

## The 2×2 (made explicit)

|  | **Mktg INVEST** | **Mktg MAINTAIN** | **Mktg STOP** |
|---|---|---|---|
| **Eng INVEST** | Build / Scale | Optimize unit economics | Rare — usually illegitimate |
| **Eng MAINTAIN** | Harvest | Maintain | Decline-manage |
| **Eng STOP** | Illegitimate | Run-down | Sunset |

Each app sits in exactly one cell. Quarterly review = does this app still belong in this cell, or does a kill/promote trigger fire?

---

## Tiers

| Tier | Eng posture | Mktg posture | Meaning |
|---|---|---|---|
| **Build** | Full team, evolving | Investing | Early bet — both sides spending to find product-market fit |
| **Scale** | Full team, optimising | Increasing | Unit economics proven; pour fuel |
| **Maintain** | Light touch, no roadmap | Steady | Healthy app; defend, don't grow |
| **Wind-down** | Reducing, dated exit | Reducing | Triggered for closure; running off |
| **Sunset** | Closed | Stopped | People/budget redirected |

---

## Decision cadence

| Cadence | Forum | Output |
|---|---|---|
| **Monthly** (in 1:1 with David) | Cost + revenue snapshot per app; kill-trigger status | Tier confirmation or flag |
| **Quarterly** | Full portfolio review with David | Tier reassignment; new kill triggers; budget reallocation |
| **Ad-hoc** | When any single move >€20k impact | Decision + price-tag named in the moment |

---

## What I'll deliver, when

| Item | Date |
|---|---|
| Framework v1 sign-off | Next 1:1 |
| AI Design scorecard — fully populated | Next 1:1 (first concrete bet on the table) |
| Face AI + Tattooist scorecards | +1 week |
| Truth Seeker + iMode + Screen Mirroring | +2 weeks |
| M&A app scorecards (ChatUltra, Sat AI, Lorca) | After Sergio Wetzel + Listen + Christian conversations land |
| First quarterly portfolio review | End Q2 (target: last week of June) |

---

## What I need

### From David
1. **Sign-off on the framework structure** in the next 1:1 (or push back on the shape — better now than after I've built 9 scorecards on the wrong shape)
2. **Air cover with PMs** to ask for marketing + revenue data as a standing monthly request. Specifically: *"Filippo is going to ask each of you for ad spend + MRR + CAC per app monthly. Please reply within 5 working days."*
3. **Joint sign-off on kill triggers** per app at quarterly review. Pre-agreed triggers stop closure conversations from becoming political.

### From PM / marketing (David's air cover required)
1. Monthly marketing spend per app
2. Monthly MRR, MAU, CAC, LTV per app
3. Heads-up on any spend change >20% month-on-month

### From Finance / David's data
1. Continued share of the Tableau / cost spreadsheet view
2. Per-developer AI tooling visibility (already in progress per 12 May)

---

## What this changes about my role

This framework formalises the financial-goalkeeper role David named on 12 May. I'm accepting it explicitly, on the following operating model:

- I integrate the cost + value picture and propose tier + trigger per app
- I do not own marketing spend or revenue performance — I consume those
- I do not unilaterally close apps — I bring the case; David and PMs decide
- I do not absorb new portfolio asks without naming the trade-off

**Conditions still open (April H2 deal):** Flutter capability, Mobile SE backfill, Victor cadence. These conditions are not displaced by this framework — they are the conditions under which this framework can be delivered well. To be raised separately.

---

## Risks / what could go wrong

- **Marketing data doesn't arrive** → framework becomes engineering-cost-only and I'm an accountant. Mitigation: David's air cover with PMs (item #2 above) is non-optional.
- **Triggers get re-litigated at closure time** → political friction. Mitigation: pre-agree triggers in writing per app at quarterly review; David co-signs.
- **Framework becomes another "built but not presented" doc** (cf. app-assignments-doc, monthly infra cost report — 4-week pattern). Mitigation: bring AI Design fully populated to the next 1:1, not just the framework.
- **Scope expansion absorbs more than April conditions allow** → silent overload. Mitigation: each new portfolio ask priced against trade-offs in the 1:1, in the moment.

---

## Appendix — first proposed decisions

1. **AI Design** — proposed tier: *Wind-down with kill trigger.* Quarterly bet: ~€75k externals (Oleksi + Dmytro through 30 Sept) + ~€12k Vlad-as-advisor through Q3. Proposed kill trigger: if CAC has not improved by 30 Sept, externals exit on schedule and Vlad redirects to next bet. (Full scorecard attached.)
2. **Tattooist** — graduation to Growth pending (unofficial per Jorge). Hold scorecard until official.
3. **Codex / AI tooling spend** — pull into the framework as a cross-cutting line once David's per-developer visibility tooling lands.
