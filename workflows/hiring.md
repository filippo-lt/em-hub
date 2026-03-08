# Workflow: Hiring

Support the full hiring loop: role definition → interview prep → debrief → decision.

---

## Routing

Activate when the user says:
- "I need to hire for [role]"
- "Help me build an interview scorecard"
- "Debrief this interview"
- "Help me decide between candidates"

---

## Agents Used

1. **Prep Agent** (`agents/prep-agent.md`) — adapted for interview prep instead of 1-on-1 prep
2. **Analysis Agent** (`agents/analysis-agent.md`) — adapted for interview debrief
3. **Decision Agent** (`agents/decision-agent.md`) — candidate comparison and hire/no-hire
4. **Writing Agent** (`agents/writing-agent.md`) — rejection/offer comms, recruiter briefs
5. **Memory Agent** (`agents/memory-agent.md`) — capture hiring learnings

---

## Phases

### Phase 1 — Role Definition
Help the user define what they're actually looking for:
- What problem does this hire solve?
- What does the first 90 days look like?
- What are the must-haves vs. nice-to-haves?
- Output: Job scorecard → save to `context/hiring/[role]/scorecard.md`

### Phase 2 — Interview Prep
Before each interview:
- Load the candidate's CV/notes from `context/hiring/[role]/candidates/`
- Load the scorecard
- Generate targeted questions based on the criteria
- Output: Interview guide

### Phase 3 — Interview Debrief
After each interview:
- User provides notes or transcript
- Analysis agent evaluates against scorecard criteria
- Flag strengths, concerns, and open questions
- Output: Candidate assessment → save to `context/hiring/[role]/candidates/[name]_assessment.md`

### Phase 4 — Candidate Comparison & Decision
When the user has multiple assessments:
- Decision agent structures the comparison
- Side-by-side against scorecard criteria
- Surface trade-offs explicitly
- Output: Decision brief

### Phase 5 — Memory Extraction
After any phase completes (debrief, decision, or full loop):
- Memory agent extracts durable hiring learnings using `[hiring]` and `[self]` tags
- Focus: criteria that predicted well, interview red flags that proved true/false, calibration of your own judgment, process improvements
- Output: Memory entries → save to `context/memory/hiring/YYYY-MM-DD_[role]_memory.md`

---

## File Outputs

| Output | Location |
|--------|----------|
| Role scorecard | `context/hiring/[role]/scorecard.md` |
| Interview guide | Shared in chat |
| Candidate assessment | `context/hiring/[role]/candidates/[name]_assessment.md` |
| Decision brief | `context/hiring/[role]/decision.md` |
| Memory | `context/memory/hiring/YYYY-MM-DD_[role]_memory.md` |
