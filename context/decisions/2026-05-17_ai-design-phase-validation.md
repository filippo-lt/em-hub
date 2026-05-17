# AI Design — Phase Validation Brainstorm

**Date:** 2026-05-17
**Status:** Thinking doc — not a decision. Sleeping on it overnight, revisit before May 19 1:1.
**Origin:** Brainstorm prompted by AI Design financial snapshot (Jan–Apr 2026). Question: keep externals / move to SE / drop?
**Relation to other plans:**
- Builds on `2026-05-16_resource-planning-strategy.md` (the 6-week operational plan)
- Sharpens the AI Design wind-down proposal in `context/app-portfolio-framework.md` (appendix item 1)
- Affects: KR1 (externals -20% by end Q2), Q2 evidence engineering plan, FaceAI 40/40/20 Phase 2 evidence

---

## Trigger

April was AI Design's first net-positive month (+€6.4k). MRR climbed €1.4k → €41k in 4 months. A new feature is "showing promise." But LTV/CAC still 0.2–0.3 and marketing-spend data hasn't arrived from Sergio Wetzel.

The framework's current proposal — Wind-down with Sep 30 kill trigger — was drafted before the April flip. Question: does this change the call, and if so to what?

Brainstorm surfaced something bigger: the entire capacity model (1 SE / 2 apps cross-platform) is unvalidated. AI Design isn't the real conversation — it's the first concrete test of whether the math holds.

---

## State of AI Design today

**Financials (from Tableau / cost sheet):**
| Month | Burn | MRR | Net | LTV/CAC |
|---|---|---|---|---|
| 01/2026 | €18.1k | €1.4k | -€16.7k | 0.24 |
| 02/2026 | €20.4k | €9.8k | -€10.6k | 0.29 |
| 03/2026 | €34.9k | €30.8k | -€4.2k | 0.20 |
| 04/2026 | €34.7k | €41.0k | **+€6.4k** | 0.23 |

**Resources:**
- Externals: Oleksi + Dmytro, ~€24k/month, scoped to exit Sep 30
- Internal: Vlad as advisor, capped 1–1.5 hr/day
- PM: Sergio Wetzel (marketing spend not shared)
- QA: external, €4k/month

**Framework position:**
- Proposed tier: Wind-down with Sep 30 kill trigger
- Not yet signed off — May 19 is the presentation
- Sergio Wetzel not yet briefed (sequenced after David sign-off)

**Critical data gaps:**
- Marketing spend (Sergio Wetzel hasn't sent) → LTV/CAC ratio unverifiable
- "New feature showing promise" not defined in measurable terms
- True CAC trajectory (vs LTV/CAC ratio) unknown
- Cohort retention curves (M3, M6) not available

---

## Phase A → D validation model

The brainstorm surfaced this model. It is **engineering's capacity-validation sequence** — independent of any single app's tier decision.

| Phase | Definition | Status |
|---|---|---|
| **A** | 1 SE on 1 iOS app at healthy ratio (≥30% feature production, sustained 4 wks) | **Not cleared.** Vlad on Face AI = 40/40/20 (20% feature production, May 14 pair session) |
| **B** | Same SE picks up 2nd iOS app, sustains healthy ratio on both | Untried |
| **C** | 1 SE on 1 cross-platform app (iOS + Android) | Untried — gated on new hire landing |
| **D** | 1 SE on 2 cross-platform apps | Untried. **This is David's portfolio math.** |

**Key insight:** KR1 (externals out by Dec 31, 2026) is implicitly committed to Phase D being validated. Phase D realistically can't be validated until Q1–Q2 2027. **The commitment is downstream of math that won't be proven by the deadline.**

---

## Compressed timeline (corrected, working backward from Sep 30)

The earlier draft of this had Phase B starting in September. That was wrong — the Sep 30 externals exit IS the moment Vlad must already own AI Design. For Vlad to own it, rewrite must be complete by Sep 30. Rewrite = 2–3 months + 2 weeks discovery → **Vlad must start AI Design by ~Jul 1.**

```
2026
 May    Jun    Jul    Aug    Sep    Oct    Nov    Dec       2027
═══════════════════════════════════════════════════════════════════

PHASE A  ████████░░░░
(Vlad / Face AI)   only ~4 weeks of clean data before Phase B starts

PHASE B           ░░░████████████████████░░░░
(Vlad / Face AI + AI Design)
                  │  └─disc─┘└──rewrite──┘
                  │  Jul 1   mid-Jul     Sep 30
                  │                      externals exit
                  ▼
              must commit at Jun 9 gate

PHASE C           ████░░░░░░░░░░░░░░░░░░
(new hire / PDF Editor)
                  start ~Jul, discovery + rewrite → cleared ~Nov/Dec

PHASE D                                            ░░░████ 
(1 SE / 2 cross-platform apps)                     Q4 2026 / Q1 2027

═══════════════════════════════════════════════════════════════════
     ▲          ▲                        ▲              ▲
   May 19    Jun 9 gate              Sep 30          Dec 31
   framework  3-way GO/NO-GO         externals       KR1 deadline
              for Jul 1 start        exit
```

**The structural problem:** Phase A has ~4 weeks of clean data before Phase B has to start. Phase A and Phase B effectively overlap — we'd be betting on Phase B before Phase A is validated.

---

## Gates

### Jun 9 — 3-way GO/NO-GO (the actual decision moment)

**All three must be true** or the math collapses:

1. **Gate 1 (data):** Sergio Wetzel ships marketing spend. CAC trajectory is product-driven, not spend-bought.
2. **Gate 2 (capacity):** Vlad's feature-production ratio on Face AI ≥30%, sustained for 4 weeks of data. Face AI 4-week roadmap (delivered May 29) is on track.
3. **Gate 3 (Vlad sign-off):** Vlad explicitly signs that he can run AI Design discovery + rewrite in parallel with Face AI maintenance.

### Three failure paths and what each forces

| Gate that fails | Forced outcome |
|---|---|
| **Gate 1** | Tier stays Wind-down. Sep 30 trigger fires kill. Externals exit, app sunsets, Vlad stays on Face AI. |
| **Gate 2** | Vlad not transferable. AI Design either dies Sep 30 (regardless of PMF) OR externals extend past Sep 30 (breaks framework's first committed deadline). |
| **Gate 3** | Vlad takes it anyway → Face AI collapses → Phase 2 AI-SE evidence dies. OR Vlad refuses → fall back to Gate 2 paths. |

**This is the question to put to David on May 19:** if any one leg fails Jun 9, which would you pick — kill the app, extend externals, or sacrifice Face AI evidence? Force him to name the priority order *before* the data forces him into it.

---

## Political tensions

These are the hidden constraints surfaced by the brainstorm. They shape every move.

### 1. Authority gap

- **Filippo cannot kill apps.** That authority sits above David (Product / exec layer).
- **David is fighting upstream** to acquire that authority for engineering ("you are the goalkeeper of these kilos of money," May 12).
- **Filippo's framework is doing dual duty:**
  - (a) engineering's internal capacity + portfolio tool
  - (b) **political instrument for David's authority fight upstream**
- These two roles sometimes conflict. Optimal-as-tool ≠ optimal-as-ammunition. Need to be deliberate about which dominates each artefact.

### 2. Product is a third player (not yet considered in framework v1)

- Product (Sergio Hueso lead; Sergio Wetzel as AI Design PM) will push for **more** investment, not less
- April hockey-stick is ammunition *for them*, against wind-down
- They have direct relationships with David's peers / above
- If they hear "wind-down" through grapevine, they may pre-empt with their own meeting / data
- **Sergio Wetzel withholding marketing data is itself politically significant** — could be disorganisation, could be strategic
- Implication: don't initiate Sergio Wetzel comms before David signs off framework; let David's air-cover land first

### 3. David's mental model vs framework

- David still expects Vlad → AI Design SE (May 5 memo deferred *sequence*, not destination)
- He floated greenfield M&A for Vlad **twice** on May 5 — that alternative is hiding in his head
- The real Vlad choice isn't "advisor vs SE on AI Design" — it's three-way: AI Design SE / Face AI continued / greenfield M&A SE
- Going to May 19 with a flat "Vlad stays advisor" loses the conversation; better to align with destination, sequence the gates

### 4. Capacity model is structurally unvalidated

- 40/40/20 finding (May 14) is the only data point on SE productivity in our portfolio
- David's resource math (3 SEs × 2 apps × cross-platform) skips 3 unvalidated leaps
- "Externals out by year-end" is downstream of math we haven't tested
- This isn't an opinion — it's a structural observation that the framework should surface

### 5. The "silent absorption" failure mode

- Highest-probability scenario: David accepts the diagnosis but holds the timeline ("compress and deliver")
- Self-discipline principle from May 16 plan: *"each new portfolio ask priced against trade-offs in the moment"*
- May 19 is the test: walk in with the trade-off menu pre-priced, do not absorb silently
- Trade-off menu shape: year-end externals-out at -100% / -50% / 0% with what each requires

---

## What's NOT in scope for Filippo

These are NOT calls Filippo can or should make. Surfacing them as out-of-scope so they don't leak into the May 19 conversation:

- **The kill itself** (Product + exec layer decide; David fighting for authority)
- **KR1 re-base** (David + Finance)
- **Forcing Product to share marketing data** (David's air-cover role)
- **Cross-functional escalation** (must go through David)
- **Org-design / authority change** (above-David)

In scope: structure, evidence, capacity allocation, trade-off pricing, the 1:1 conversation itself, what to absorb vs. name.

---

## May 19 — the sharpened ask shape

Not "convince David to wind-down AI Design." Three components:

1. **Open with role question:**
   > "Before I walk you through the framework — on AI Design specifically, what's the most useful shape I can give you? A recommendation I'm willing to defend, an evidence package you can take to Sergio Hueso, or a capacity ceiling that lets you push back on Product's investment ask?"

2. **Present framework + AI Design scorecard with marketing-spend gap visible.** Make the gap the lever for David's PM air-cover ask.

3. **Don't lock the tier today. Lock the Jun 9 GO/NO-GO and the three gates.** Frame: *"Jun 9 is a 3-way GO/NO-GO. If any leg fails, you choose between killing AI Design / extending externals / sacrificing Face AI evidence. Pick the priority order now, before the data forces it."*

---

## Artefacts needed by May 18 (Mon)

To walk in cleanly to May 19:

- [ ] **Trade-off menu** (1 page): year-end externals-out at -100% / -50% / 0%, what each requires
- [ ] **Phase A→D validation sequence** with dates (this doc has the skeleton — needs to be 1-pager form)
- [ ] **40/40/20 measurement plan** (3 lines): 4 more pair sessions through end-May, hardened finding Jun 2
- [ ] **AI Design scorecard** populated as far as data allows; marketing-spend gap explicit
- [ ] **Sergio Wetzel last push** for marketing spend by EOD Mon May 18

---

## Open questions (to think about overnight)

1. **What's "healthy" feature-production ratio?** I've used ≥30%, sustained 4 wks. Is that defensible? David may push: why not 25%? Why 4 weeks not 2?
2. **Is 4 weeks of Phase A data even meaningful?** Vlad on Face AI for 4 weeks might be noise. Jun 9 GO on Gate 2 may be premature regardless.
3. **What does "new feature shows promise" actually mean?** Engagement? Retention? Revenue per user? Conversion uplift? Need to ask Sergio Wetzel — without this we're brainstorming on vibes.
4. **Should the greenfield M&A alternative for Vlad be surfaced on May 19, or held as Plan B if Gate 1 fails?** Surfacing early makes it real; holding loses the option if David picks AI Design path.
5. **What if Sergio Wetzel pre-empts before May 19?** (Scenario 10 from brainstorm.) Pre-committed response: "we're working through the portfolio framework with David, happy to walk you through it after we've aligned."
6. **Is there a fourth gate we're missing?** E.g., Andrey's capacity confirmation, FaceAI roadmap actually committing, hire offer accepted. None of those force AI Design Jun 9, but any could break the broader plan.
7. **What's the actual rewrite scope on AI Design?** A 2–3 month rewrite assumes scope is known. If discovery reveals it's bigger, Phase B timeline breaks. The discovery 1-pager (Jul 1–14) is the gate, but we're pre-committing to start it Jul 1 without knowing the answer.

---

## Brainstorm meta-notes

What changed during the brainstorm:
- Initial frame: "advisor vs SE vs drop" — too narrow
- Second frame: "what would have to be true for SE move" — better, but still assumed Filippo was the decider
- Third frame: "Product is the third player; Filippo is not the decider" — reframed the whole conversation
- Fourth correction: timeline was forward-from-now; should be backward-from-Sep-30 (externals exit is the hard date)
- Compressed result: Jun 9 is the real decision, not Sep 30. May 19's job is to set up Jun 9 cleanly.

---

## Handoffs (when ready)

- → `/write` for May 19 talking points / opening / framework presentation deck
- → `/decide` to formalise the Jun 9 GO/NO-GO as a structured decision
- → Memory Agent (running in parallel with this doc)
- → 1:1 prep (`/prep` for the May 19 David 1:1)
