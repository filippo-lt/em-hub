---
name: hiring
description: "Support the full hiring loop: role definition, interview prep, debrief, candidate comparison, and decision. Use when the user says things like: 'I need to hire for [role]', 'interview scorecard', 'debrief this interview', 'decide between candidates'."
user_invocable: true
---

# Hiring

Support the full hiring loop: role definition → interview prep → debrief → decision.

---

## Process

### Phase 1 — Role Definition

Help the user define what they're actually looking for:
- What problem does this hire solve?
- What does the first 90 days look like?
- What are the must-haves vs. nice-to-haves?

Output: Job scorecard → save to `context/hiring/[role]/scorecard.md`

---

### Phase 2 — Interview Prep

Before each interview:
- Load the candidate's CV/notes from `context/hiring/[role]/candidates/`
- Load the scorecard
- Generate targeted questions based on the criteria

Output: Interview guide

---

### Phase 3 — Interview Debrief

After each interview:
- User provides notes or transcript
- Evaluate against scorecard criteria
- Flag strengths, concerns, and open questions

Output: Candidate assessment → save to `context/hiring/[role]/candidates/[name]_assessment.md`

---

### Phase 4 — Candidate Comparison & Decision

When the user has multiple assessments:
- Structure the comparison side-by-side against scorecard criteria
- Surface trade-offs explicitly
- Push back on gut-feel decisions — demand evidence

Output: Decision brief

---

### Phase 5 — Memory Extraction

After any phase completes (debrief, decision, or full loop):
- Run the Memory Agent to extract durable hiring learnings using `[hiring]` and `[self]` tags
- Focus: criteria that predicted well, interview red flags that proved true/false, calibration of your own judgment, process improvements

Output: Memory entries → save to `context/memory/hiring/YYYY-MM-DD_[role]_memory.md`

---

## Context Loading

Load context per **Context Loading Protocol** in CLAUDE.md. Additionally:
- `context/memory/hiring/` — past hiring learnings
- `context/memory/self/` — self-awareness patterns (e.g., overweighting cultural fit)

---

## File Outputs

| Output | Location |
|--------|----------|
| Role scorecard | `context/hiring/[role]/scorecard.md` |
| Interview guide | Shared in chat |
| Candidate assessment | `context/hiring/[role]/candidates/[name]_assessment.md` |
| Decision brief | `context/hiring/[role]/decision.md` |
| Memory | `context/memory/hiring/YYYY-MM-DD_[role]_memory.md` |

---

## Behaviour Rules

Behavioral Standards from CLAUDE.md apply. Additionally:

- Every assessment must map back to scorecard criteria — no freeform vibes.
- If the user can't articulate why they prefer a candidate, push for specifics.
- Flag when bias might be at play (halo effect, similarity bias, recency bias).
- For rejection/offer comms, hand off to `/write`.
