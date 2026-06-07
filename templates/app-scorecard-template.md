# App Scorecard — [App Name]

**As of:** [YYYY-MM-DD] · **Next review:** [date]
**Governance owner:** Filippo · **Delivery owner (studio/team):** [name]
**PM / Product owner:** [name] · **Advisor:** [name or —]

> A *decision* document, not a data dump. The live numbers live in the Portfolio Tracker (`templates/ma-portfolio-tracker.md`); this is pulled out only when an app needs a tier or takeover call. For repo-level evidence behind a Remediate/Rebuild call, see `templates/ma-app-technical-scorecard.md`.

---

## 1. Position

**Posture:** [ Govern-in-place · Remediate · Rebuild · Sunset ]
**Tier:** [ Build · Scale · Maintain · Wind-down · Sunset ] → [proposed, if changing]
**2×2:** Eng [ INVEST · MAINTAIN · STOP ] × Mktg [ INVEST · MAINTAIN · STOP ]

---

## 2. Snapshot (from the tracker)

| | Value | 3-mo trend | Source |
|---|---|---|---|
| Monthly cost | €X | ↑→↓ | GCP + contract |
| MRR | €X | ↑→↓ | RevenueCat |
| MAU | X | ↑→↓ | Amplitude |
| **Crash-free %** | X% | ↑→↓ | Crashlytics |

**Unit-economics read (1 line):** [are we making money per user? — pull full CAC/LTV/payback only if the decision turns on it]

---

## 3. Score → Action

**Recommendation:** [ one of the four verbs ]

**Why (2–3 lines, evidence-based):**
- [value signal — MRR/MAU/trend]
- [health/savability signal — crash-free %, codebase, AI-SE viability: codebase quality + product-context recoverability]
- [cost / opportunity signal]

**If Remediate or Rebuild:** discovery + execution cost = [person-weeks] (remember: SE-on-app = discovery + rewrite; discovery is ~half).

---

## 4. Triggers (pre-agreed, dated, named action)

- [ ] **Down-tier / kill:** if [metric] is not [value] by [date] → [verb] · action: [eng exit / mktg stop / sunset]
- [ ] **Up-tier:** if [metric] reaches [value] by [date] → [verb] · action: [add resource / increase spend]
- [ ] **Hard floor:** if [metric] falls below [floor] at any time → [action]

---

## 5. Quality & release

| | State |
|---|---|
| Crash-free % vs threshold | X% / [threshold] |
| Last release-floor result | ✅ / ❌ [date] — crash-free + smoke + secret scan + consent |
| QA in place | Tier 1 automated floor · Tier 2 exploratory signal · Tier 3 sign-off mandate |
| Open security items | [count + pointer; see technical scorecard §4] |

---

## 6. The ask + decision log

**The ask:**
- From David: [access / sign-off / air cover] — by [date]
- From Product: [the kill/continue call] — by [date]. **Default if no decision by then:** [wind-down to maintenance-only / proceed as recommended].

**Decision log (most recent first):**

| Date | Decision | Owner |
|---|---|---|
| [YYYY-MM-DD] | [what was decided] | [name] |
