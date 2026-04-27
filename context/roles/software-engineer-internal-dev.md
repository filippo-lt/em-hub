# Software Engineer — Role Definition (Internal)

> **Audience:** Internal. EM-level reference. Not for circulation to POs, PMs, or candidates.
> **Status:** High-level, deliberately evolving. Last revised 2026-04-27.
> **Companion doc:** [software-engineer.md](software-engineer.md) is the public-facing version. This document captures the parts that stay internal — the per-app calibration, the political reasoning, and the historical context.

---

## Purpose

The Software Engineer is the in-house, AI-native counterpart to the external dev model we are phasing out. One SE owns the delivery of one or more products end-to-end, using AI as a core force multiplier. The role exists to compress the path from idea to shipped product, and to make external dev teams unnecessary.

## Identity & Scope

- Title is **Software Engineer** — deliberately not platform-specific.
- Today the role is **mobile-anchored** (iOS-primary, Android secondary, light backend when projects require). Vlad is the first and currently only SE in the company.
- As more SEs join and the family structure lands, scope generalizes. The role's boundary is "what the product needs," not "what platform."
- AI tooling is what bridges platform and skill gaps; it is not optional, it is the operating model.

## What the SE Produces (2026 → 2027)

- **2026: Builder + AI stack steward.** Ships product end-to-end. Maintains and evolves the shared AI dev stack — rules, skills, agents, workflow automation. Their AI work compounds across the team.
- **2027: + Force multiplier.** As the team grows, the SE is also expected to lift others — mentorship, standards, code review, raising the floor.

## Ownership & Authority

### What is now public (as of 2026-04-27)

The public role doc commits to a clear R/A split, endorsed by David:

- The SE is **responsible** for bringing the product to life and **takes product decisions when POs do not provide them in a timely manner**.
- The PO remains **accountable** for the product itself.
- Architectural authority sits with the SE; Staff Engineers are technical partners.
- Delivery accountability (App Store / Play Store, quality, on-time commitments) sits with the SE.

This is more authority than a traditional executor-with-voice framing. It legitimizes the SE making product calls when POs are slow, without requiring an EM to broker each case.

### What stays internal (operating layer)

Even with the public R/A split, product authority in practice is a **spectrum, calibrated by the EM app-by-app**. The public bullet covers the "PO is slow" case but does not name the full range:

- **Strong PO present** → SE operates closer to executor-with-voice. PO drives direction.
- **PO slow / inconsistent** → public-doc bullet kicks in: SE takes product decisions to keep delivery moving.
- **Weak or absent PO** → SE operates as co-owner or product driver. Examples: the Vlad / Face AI epic experiment (epics replace user stories, SE moves forward with Jira-tracked questions and SLA), candidate apps for PO removal (Screen Mirroring, Face AI Android).

The EM owns the calibration. SEs do not self-declare which mode they are in for a given project; that is set in 1:1s and adjusted as PO strength changes.

**Why this stays internal:** naming the full spectrum publicly — particularly the "product driver" end — creates political exposure with PO/PM leadership before we have evidence the model holds. The public bullet is enough cover for current operating reality (Face AI pilot fits inside "POs not providing direction in a timely manner"). Hold the rest in 1:1s until David greenlights more.

## Seniority

6–8 years of software engineering experience, with depth in at least one platform (currently iOS). AI-tooling fluency as part of daily workflow, not occasional use.

## What This Role Is NOT

- Not a coordinator of external developers. External coordination is being eliminated (Phase 2 end-state: no externals by end of June 2026).
- Not a manager. People management lives with the EM.
- Not a generalist-by-default. Depth in their primary platform is the anchor; AI fills gaps.
- Not a successor to the Developer Advisor model (90% coordination / 10% coding). That model has been discontinued.

## Success

Delivers on commitments, uses AI as a core workflow, takes ownership of outcomes. Specific KRs are set yearly via OKRs and will evolve as company-wide metrics shift toward "money per developer." Not baked into this definition.

## Evolution

This document is intentionally high-level. Expect annual revision as:

- The team grows beyond Vlad and the role generalizes off mobile.
- The family structure lands (David's H2 direction).
- The AI Transformation program moves into Phase 3.
- The bonus framework and "money per developer" KPI mature and feed back into success criteria.

## Context Anchors (for future-you)

- **Hiring signal:** the JD published in April 2026 (`Senior Mobile Software Engineer — Apps`) is the public hiring artifact. The Victor reference candidate (Apr 21) advanced under this definition.
- **Replaces:** Developer Advisor model (Andre Patricio role, discontinued).
- **Sits inside:** AI Transformation Program, Phase 2.
- **Parallel hire track:** Javier Serrano (external → internal SE, would report to André, not Filippo) — separate path, same role definition.
