# Brief — Build the Technical Interview scoring spreadsheet

Handoff to Claude Cowork. This brief is self-contained; no other context is required.

---

## Goal

Build a Google Sheet used to score candidates during a 40-minute live AI-assisted coding interview. The sheet supports a 5-dimension rubric, one row per candidate, with formulas, data validation, conditional formatting, and reference tabs.

A starter version already exists at:
**https://docs.google.com/spreadsheets/d/1jkiaD2sSRmmCFpY2O1SJoxLKpr92_xSwjhYLDmpd-CU/edit**

You can either extend that file or create a fresh one named `Software Engineer - Technical Interview` and delete the old one. Either is fine — extending is faster.

---

## Final state — what "done" looks like

The workbook has **three tabs** in this order: `Scoring`, `Rubric`, `Calibration`.

### Tab 1 — `Scoring`

**Columns (row 1 headers):**

| Col | Header                    |
| --- | ------------------------- |
| A   | Date                      |
| B   | Candidate                 |
| C   | Role / Level              |
| D   | Interviewer               |
| E   | AI tool used              |
| F   | D1 — Repo Onboarding      |
| G   | D1 notes                  |
| H   | D2 — Prompt Design        |
| I   | D2 notes                  |
| J   | D3 — Planning             |
| K   | D3 notes                  |
| L   | D4 — Critical Evaluation  |
| M   | D4 notes                  |
| N   | D5 — Recovery             |
| O   | D5 notes                  |
| P   | Total                     |
| Q   | Any-1 flag                |
| R   | Band                      |
| S   | Qualitative notes         |
| T   | Final recommendation      |
| U   | Recording link            |

**Formulas** (rows 2 through ~50, drag-fill so adding rows extends automatically):

- **P (Total):** `=IF(COUNT(F2,H2,J2,L2,N2)=5, F2+H2+J2+L2+N2, "")`
- **Q (Any-1 flag):** `=IF(P2="", "", IF(MIN(F2,H2,J2,L2,N2)=1, "⚠ score of 1", ""))`
- **R (Band):** `=IF(P2="", "", IFS(P2>=17,"Strong hire", P2>=13,"Hire", P2>=9,"Mixed", TRUE,"No hire"))`

**Data validation:**

- Columns F, H, J, L, N (the five score columns): dropdown with values `1, 2, 3, 4`, reject other input.
- Column T (Final recommendation): dropdown with `Strong hire, Hire, Mixed, No hire`.
- Column A (Date): valid date.

**Conditional formatting:**

- F, H, J, L, N — red fill when cell = 1, amber when = 2, light green when ≥ 3.
- Q — red text when not blank.
- R — colour band by recommendation: `Strong hire` dark green, `Hire` light green, `Mixed` amber, `No hire` red.

**Layout:**

- Freeze row 1 and columns A–B.
- Bold the header row, slightly larger font, contrast background.
- Wrap text on all `notes` columns and column S.
- Sensible column widths: scores ~80px, notes columns ~280px, qualitative notes ~400px.

---

### Tab 2 — `Rubric`

Reference-only tab. Interviewers open this alongside `Scoring` while filling in scores.

**Structure:**

- A top section with the format summary:
  - Format: 40-minute live coding, screenshare + think-aloud.
  - Exercise: Implement two features in Apple's `Fruta` sample repo using the AI tool of the candidate's choice.
  - Completion is not required. Scoring is on process, not output.
  - Scoring scale: 1 (Concerning) / 2 (Below bar) / 3 (Solid) / 4 (Strong).
  - Any single score of 1 is a strong no-hire signal even if the total is acceptable.
  - Recommendation bands: 17–20 Strong hire / 13–16 Hire / 9–12 Mixed / ≤8 No hire.
- A 5-row × 5-column anchor table, one row per dimension. Columns: `Dimension`, `Score 1`, `Score 2`, `Score 3`, `Score 4`. Use the content below verbatim.

**Anchor content (use as-is):**

**D1 — Repo Onboarding & Exploration** — *Does the candidate orient themselves in an unfamiliar codebase using AI, or do they dive in blind?*
- 1: Opens files at random or starts coding immediately without understanding the structure. Doesn't use AI to map the repo.
- 2: Asks the AI a couple of generic questions ("what is this project?") but doesn't go deeper. Misses key context.
- 3: Uses AI to map structure, identify the relevant files for the feature, and surface conventions before touching code.
- 4: Builds a working mental model quickly. Asks targeted questions (data model, navigation flow, state management). Verifies AI answers against the actual code.

**D2 — Prompt Design & Context Framing** — *Can they translate a vague product one-liner into something the AI can act on well?*
- 1: Pastes the one-liner verbatim into the AI and accepts whatever comes back.
- 2: Adds some context but leaves ambiguity unresolved. Doesn't pull in relevant repo files.
- 3: Reframes the request with constraints, references the relevant files, and resolves obvious ambiguities (where in the UI, what platform behaviour, etc.).
- 4: Treats prompting as engineering. Iterates on the prompt itself. Provides examples or counter-examples. Asks the interviewer (acting as PO) clarifying questions when the spec is genuinely ambiguous.

**D3 — Planning & Decomposition** — *Do they make the AI plan before it codes, or do they vibe-code?*
- 1: Asks for code immediately. No plan.
- 2: Has a rough plan in their head but doesn't externalise it. AI ends up driving.
- 3: Asks the AI for a plan, reviews it, adjusts. Breaks the feature into steps before coding.
- 4: Decomposes the work into reviewable chunks. Plans tests or verification steps. Knows when to stop the AI and re-plan if the direction is wrong.

**D4 — Critical Evaluation of AI Output** — *Do they read what the AI produces, or paste and pray?*
- 1: Accepts AI output without reading it. Doesn't notice obvious problems (wrong API, broken imports, hallucinated symbols).
- 2: Skims the output. Catches some issues but misses others. Trusts the AI's confidence.
- 3: Reads diffs carefully. Catches hallucinations, suggests corrections, asks the AI to justify choices.
- 4: Spots subtle issues — naming conventions that don't match the repo, missing edge cases, over-engineering. Pushes back on the AI when it's wrong. Would catch a leaked secret or an unsafe pattern.

**D5 — Recovery & Iteration** — *What happens when the AI is wrong or gets stuck?*
- 1: Keeps re-prompting with the same approach. Gets stuck in a loop. Gives up or starts copy-pasting from elsewhere.
- 2: Tries one or two reframings, then plateaus. Doesn't change strategy.
- 3: Recognises when the current path isn't working. Resets context, provides new examples, or changes the approach.
- 4: Diagnoses *why* the AI is failing (missing context, wrong file, ambiguous instruction) and fixes the root cause. Treats AI failure as a debugging problem.

**Qualitative signals to note in column S of `Scoring` (not numerically scored):**
- Engineering judgment underneath the AI — would this code pass review without the "AI wrote it" label?
- Communication — did they narrate clearly?
- Ownership — did they act responsible for the output, or like the AI was?
- Curiosity — did they explore beyond the minimum?

---

### Tab 3 — `Calibration`

Identical structure to `Scoring`. Used for interviewer-on-interviewer practice runs *before* going live with candidates, and for onboarding new interviewers. Easiest path: duplicate `Scoring` and rename. Add a short note at the top (row above the headers, or via a sheet description) explaining what the tab is for.

---

## Style notes

- Light visual touch. No heavy banding, no logos. This is a working sheet, not a presentation deck.
- Use system default font, size 10 for body, size 11 bold for headers.
- All emoji should stay as plain text (e.g. the ⚠ symbol in the Any-1 flag).

## Sharing

Leave sharing as-is on the existing file. The owner will adjust permissions after review.

## Confirmation

When done, reply with the final shareable URL and a one-line summary of what was built. Flag anything that couldn't be done via the Sheets API.
