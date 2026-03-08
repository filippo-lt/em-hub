# Workflow: Incident Response

Structure the aftermath of an incident: timeline, postmortem, communications, and follow-through.

---

## Routing

Activate when the user says:
- "We had an incident" / "Something broke"
- "Help me write a postmortem"
- "Draft incident comms"
- "Help me build a timeline of what happened"

---

## Agents Used

1. **Analysis Agent** (`agents/analysis-agent.md`) — adapted for incident timeline and root cause
2. **Writing Agent** (`agents/writing-agent.md`) — drafts comms (stakeholder updates, postmortem doc)
3. **Decision Agent** (`agents/decision-agent.md`) — prioritise remediation actions
4. **Memory Agent** (`agents/memory-agent.md`) — capture learnings

---

## Phases

### Phase 1 — Timeline & Facts
Help the user build a clear timeline:
1. What happened? (Symptoms, impact, duration)
2. When was it detected and by whom?
3. What was done to resolve it?
4. What's the current state?

Output: Structured timeline

### Phase 2 — Root Cause Analysis
Guide the user through:
- What broke and why?
- What could have prevented it?
- What made detection/resolution slow?
- Were there contributing human/process factors?

### Phase 3 — Postmortem Draft
Using the template at `templates/postmortem.md` (if exists), produce:
- Summary, timeline, root cause, action items, lessons learned
- Blameless framing

### Phase 4 — Communications
Draft comms for the appropriate audiences:
- Internal team: what happened, what we're doing
- Stakeholders/leadership: impact, resolution, prevention
- External (if needed): customer-facing messaging

### Phase 5 — Follow-through & Memory
- Generate action items with owners
- Schedule review date
- Memory agent extracts systemic learnings using `[incident]`, `[planning]`, and `[self]` tags
- Focus: root causes that are structural (not one-off), detection/response gaps, process failures, what worked well, personal patterns in crisis response
- Output: Memory entries → save to `context/memory/incidents/YYYY-MM-DD_[name]_memory.md`

---

## File Outputs

| Output | Location |
|--------|----------|
| Postmortem | `context/incidents/YYYY-MM-DD_[name].md` |
| Comms drafts | Shared in chat |
| Action items | Included in postmortem doc |
| Memory | `context/memory/incidents/YYYY-MM-DD_[name]_memory.md` |
