# M&A App — Technical Scorecard

> **Purpose.** Give Filippo enough technical signal on an acquired app to make a confident 3-way call in front of the PM:
> **(1)** hand to an external team · **(2)** keep with current team (broken or not) · **(3)** move to an internal developer (then choose: full rewrite · partial rewrite · fix-and-stabilise · keep).
>
> **Filler.** A Claude Code session, working against the repo(s). Every claim must cite evidence (file paths, command output, version strings, commit SHAs). When something can't be determined, write `unknown — <reason>`. Never fabricate.
>
> **Output contract.** This file ends on a single opinionated recommendation with a confidence tag and a "what would flip this" line. After filling, also append/update the row in `m-and-a/portfolio-technical.csv`.

---

**App:** [name]
**Date:** [YYYY-MM-DD]
**Filled by:** Claude Code (session)
**Reviewed by:** Filippo · [date]
**Repos audited:** [list with URLs / paths]
**Acquisition date:** [date or unknown]
**Current owners:** [team / contractors / external vendor]

---

## 1. Snapshot (objective scrape — no judgement)

Claude: fill every cell. Use `unknown — <reason>` when not measurable. Cite evidence in the Notes column.

| Field                                          | Value                              | Notes / evidence                                                |
| ---------------------------------------------- | ---------------------------------- | --------------------------------------------------------------- |
| Platforms present                              | BE / Android / iOS / Web / Desktop | [paths]                                                         |
| Primary language(s) per platform               |                                    |                                                                 |
| Frameworks + versions                          |                                    | [file:line e.g. `build.gradle`, `Podfile.lock`, `package.json`] |
| LOC per platform                               |                                    | [tool used]                                                     |
| Last commit (per repo)                         |                                    | [SHA · date · author]                                           |
| Last release / tag                             |                                    |                                                                 |
| Contributors in last 12 months                 |                                    | [git shortlog summary]                                          |
| Bus factor estimate (≥50% commits by N people) |                                    |                                                                 |
| Build attempt — BE                             | pass / fail / N/A                  | [command run, first error line]                                 |
| Build attempt — Android                        | pass / fail / N/A                  |                                                                 |
| Build attempt — iOS                            | pass / fail / N/A                  |                                                                 |
| Build attempt — Web                            | pass / fail / N/A                  |                                                                 |
| CI present?                                    | yes / no                           | [path to config]                                                |
| CI provider + last run status                  |                                    |                                                                 |
| CI covers what?                                | build / test / lint / deploy       |                                                                 |
| Dependencies — total                           |                                    | per platform                                                    |
| Dependencies — outdated (major behind)         |                                    |                                                                 |
| Dependencies — EOL / unsupported               |                                    | [list]                                                          |
| Known CVEs ≥ High                              | count + list                       | [tool used]                                                     |
| Secrets / hardcoded keys in repo               | hit count                          | [file:line for each]                                            |
| Tests present per slice                        | BE / AND / iOS / Web               |                                                                 |
| Tests runnable?                                |                                    |                                                                 |
| Coverage if measurable                         |                                    |                                                                 |
| Docs — README adequacy                         | absent / thin / usable / good      |                                                                 |
| Docs — onboarding steps reproducible?          |                                    |                                                                 |
| ARCHITECTURE.md or equiv                       | yes / no                           |                                                                 |
| Infra-as-code present?                         |                                    | [terraform / pulumi / none]                                     |
| Observability (logs, metrics, alerts)          |                                    |                                                                 |

---

## 2. Per-slice health

For each slice present, fill the block. Omit slices that don't apply.

### Backend
- **State:** working / degraded / broken / absent
- **Top 3 risks (with evidence):**
  1.
  2.
  3.
- **Bring-to-shippable-baseline effort:** [person-weeks, rough]

### Android
- **State:**
- **Top 3 risks:**
- **Effort to baseline:**

### iOS
- **State:**
- **Top 3 risks:**
- **Effort to baseline:**

### Web
- **State:**
- **Top 3 risks:**
- **Effort to baseline:**

### Infra / CI
- **State:**
- **Top 3 risks:**
- **Effort to baseline:**

---

## 3. Red flags

Each item tagged `BLOCKER` (cannot hand off until fixed) / `MAJOR` (handoff possible but costly) / `MINOR` (note and move on). Cite evidence.

- `BLOCKER` — [e.g. hardcoded prod Stripe key in `apps/api/src/config.js:42`]
- `MAJOR` — [e.g. AngularJS 1.x in web layer, EOL since 2022]
- `MINOR` — [e.g. README missing run command]

---

## 4. Security — immediate action items

Separate section because these may force action regardless of the strategic decision. Each line: severity · what · where · suggested action.

- [ ] CRITICAL — [what] — [file:line or URL] — [action]
- [ ] HIGH —
- [ ] MEDIUM —

---

## 5. Intervention options

Evaluate each path. Be concrete on scope and effort.

### A. Hand to external team as-is
- **Feasibility:** high / medium / low
- **Prep work required before handover:** [bullets]
- **Main risks:**
- **Rough effort to make handover-ready:** [person-weeks]

### B. Keep with current team (status quo)
- **Ongoing risk if nothing changes:**
- **Cost trajectory:**
- **Failure modes within 6 months:**

### C. Move to an internal developer
Pick the most likely sub-path(s) and size them. Don't fill all four unless several are plausible.

- **C1 — Full rewrite**
  - Scope: [platforms / scope cut]
  - Effort: [person-weeks]
  - Risk:
- **C2 — Partial rewrite**
  - Slice(s) to rewrite: [BE / AND / iOS / Web / a specific module]
  - Why this slice (not the others):
  - Effort:
  - Risk:
- **C3 — Fix-and-stabilise (no rewrite)**
  - Fixes in scope:
  - Effort:
  - Residual risk after fixes:
- **C4 — Keep as-is, just own it**
  - What this internal dev would actually do day-to-day:
  - Effort to ramp:

---

## 6. Recommendation

**Picked path:** [A / B / C1 / C2 / C3 / C4]
**Confidence:** low / medium / high

**Why (2–3 reasons):**
1.
2.
3.

**One-paragraph version for the PM:**
> [Plain-language paragraph Filippo can paste or paraphrase to the PM. No jargon. State the call, the reason, and the headline risk.]

**What would flip this recommendation:**
- [Signal 1 — e.g. "if CI cannot be made green within 2 weeks of an external team starting, switch to C2 (partial iOS rewrite internally)"]
- [Signal 2]

**Open questions for Filippo / PM before committing:**
- [bullet]
- [bullet]

---

## 7. Portfolio CSV row

Claude: append/update this row in `m-and-a/portfolio-technical.csv`. Reproduce it here so the per-app file is self-contained.

```
[app],[YYYY-MM-DD],[build_BE pass/fail/NA],[build_AND],[build_iOS],[build_Web],[ci_state green/red/none],[sec_blockers count],[top_red_flag short],[recommendation A/B/C1/C2/C3/C4],[est_person_weeks],[confidence low/med/high]
```

---

## Filler instructions for Claude Code

Read these before filling.

- **Evidence or `unknown`.** Every non-trivial claim cites a file path, command output, or commit SHA. If a thing cannot be determined in the time available, write `unknown — <reason>` rather than guessing. Filippo will defend this document to a PM; fabrication is worse than gaps.
- **Run the builds.** Section 1's "Build attempt" rows mean an actual attempted build per platform on a clean checkout. Capture the command and the first error line if it fails.
- **Don't skip Section 4.** Even if the strategic call is "keep as-is," surfaced security issues may need immediate action. List them regardless.
- **Section 5: don't fill every option.** Evaluate only the paths that are realistically on the table. If C1 (full rewrite) is obviously absurd given the codebase size, say so in one line and move on.
- **Section 6: commit to one path.** Confidence may be "low" — that's fine and useful — but the recommendation field must contain a single picked option. Conditional logic goes in "what would flip this."
- **Tone.** Direct, no hedging language ("it seems," "perhaps"). Either you have evidence or you write `unknown`.
- **Scope.** Technical only. Business metrics (MRR, CAC, etc.) live in `templates/app-scorecard-template.md`; do not duplicate them here. If a business fact is load-bearing for the recommendation (e.g. "app generates <€500/mo so rewrite is uneconomic"), state it as one line in Section 6 and link to the business scorecard.
