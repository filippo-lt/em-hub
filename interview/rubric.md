# Technical Interview Rubric — AI-Assisted Implementation

**Format:** 40-minute live coding session, screenshare + think-aloud.
**Exercise:** Implement two features in the Apple `Fruta` sample repo using the AI tool of the candidate's choice.
**Completion is not required.** We are scoring *process*, not output.

---

## What we are measuring

How a candidate uses AI as a working partner to:

1. Onboard into an unfamiliar codebase
2. Turn a vague product request into something an AI can act on
3. Plan before coding
4. Critically read what the AI produces
5. Recover when the AI is wrong

The code shipped at the end of the 40 minutes is the *least* interesting artifact. The conversation with the AI, the candidate's narration, and the decisions they make along the way are what we score.

---

## Scoring

Five dimensions, scored 1–4. Anchors below. Total out of 20.

- **1 — Concerning.** Would struggle to be productive with AI tooling.
- **2 — Below bar.** Some signs of competence, significant gaps.
- **3 — Solid.** Clearly able to work effectively with AI.
- **4 — Strong.** Models the behaviour we want others to learn from.

A score of 1 on any single dimension is a strong no-hire signal even if the total is acceptable.

---

### 1. Repo Onboarding & Exploration

*Does the candidate orient themselves in an unfamiliar codebase using AI, or do they dive in blind?*


| Score | Looks like                                                                                                                                                   |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1     | Opens files at random or starts coding immediately without understanding the structure. Doesn't use AI to map the repo.                                      |
| 2     | Asks the AI a couple of generic questions ("what is this project?") but doesn't go deeper. Misses key context.                                               |
| 3     | Uses AI to map structure, identify the relevant files for the feature, and surface conventions before touching code.                                         |
| 4     | Builds a working mental model quickly. Asks targeted questions (data model, navigation flow, state management). Verifies AI answers against the actual code. |


---

### 2. Prompt Design & Context Framing

*Can they translate a vague product one-liner into something the AI can act on well?*


| Score | Looks like                                                                                                                                                                                            |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | Pastes the one-liner verbatim into the AI and accepts whatever comes back.                                                                                                                            |
| 2     | Adds some context but leaves ambiguity unresolved. Doesn't pull in relevant repo files.                                                                                                               |
| 3     | Reframes the request with constraints, references the relevant files, and resolves obvious ambiguities (where in the UI, what platform behaviour, etc.).                                              |
| 4     | Treats prompting as engineering. Iterates on the prompt itself. Provides examples or counter-examples. Asks the interviewer (acting as PO) clarifying questions when the spec is genuinely ambiguous. |


---

### 3. Planning & Decomposition

*Do they make the AI plan before it codes, or do they vibe-code?*


| Score | Looks like                                                                                                                                      |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | Asks for code immediately. No plan.                                                                                                             |
| 2     | Has a rough plan in their head but doesn't externalise it. AI ends up driving.                                                                  |
| 3     | Asks the AI for a plan, reviews it, adjusts. Breaks the feature into steps before coding.                                                       |
| 4     | Decomposes the work into reviewable chunks. Plans tests or verification steps. Knows when to stop the AI and re-plan if the direction is wrong. |


---

### 4. Critical Evaluation of AI Output

*Do they read what the AI produces, or paste and pray?*


| Score | Looks like                                                                                                                                                                                         |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | Accepts AI output without reading it. Doesn't notice obvious problems (wrong API, broken imports, hallucinated symbols).                                                                           |
| 2     | Skims the output. Catches some issues but misses others. Trusts the AI's confidence.                                                                                                               |
| 3     | Reads diffs carefully. Catches hallucinations, suggests corrections, asks the AI to justify choices.                                                                                               |
| 4     | Spots subtle issues — naming conventions that don't match the repo, missing edge cases, over-engineering. Pushes back on the AI when it's wrong. Would catch a leaked secret or an unsafe pattern. |


---

### 5. Recovery & Iteration

*What happens when the AI is wrong or gets stuck?*


| Score | Looks like                                                                                                                                                 |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | Keeps re-prompting with the same approach. Gets stuck in a loop. Gives up or starts copy-pasting from elsewhere.                                           |
| 2     | Tries one or two reframings, then plateaus. Doesn't change strategy.                                                                                       |
| 3     | Recognises when the current path isn't working. Resets context, provides new examples, or changes the approach.                                            |
| 4     | Diagnoses *why* the AI is failing (missing context, wrong file, ambiguous instruction) and fixes the root cause. Treats AI failure as a debugging problem. |


---

## Overall Signal (not scored, but noted)

Beyond the five dimensions, capture qualitative impressions:

- **Engineering judgment underneath the AI** — would this code pass review if we removed the "AI wrote it" label?
- **Communication** — did they narrate clearly? Could a teammate follow their reasoning?
- **Ownership** — did they act like they were responsible for the output, or like the AI was?
- **Curiosity** — did they explore beyond the minimum required to satisfy the prompt?

---

## Calibration Notes

- **Tool variance is real but not penalised.** A candidate using Cursor or Claude Code will look different from one using a web ChatGPT tab. Score the *behaviour*, not the tool's surface.
- **Seniority adjusts the bar, not the rubric.** A senior should drive the AI. A junior may be more driven by it; that's acceptable if the other dimensions are strong.
- **Watch for pre-baked solutions.** The Fruta repo is public. If the candidate moves suspiciously fast or skips exploration, ask them to extend the feature in a small unexpected way and see what happens.
- **Interviewers should calibrate before running candidates.** Two interviewers do the exercise themselves, watch each other's recordings, and reconcile scores. Without this, scoring drifts.

---

## Recommendation Guidance


| Total | Guidance                                |
| ----- | --------------------------------------- |
| 17–20 | Strong hire.                            |
| 13–16 | Hire, with notes on growth areas.       |
| 9–12  | Mixed. Lean on other interview signals. |
| ≤8    | No hire on this dimension.              |


Any single score of 1 overrides the total — discuss in debrief before moving forward.