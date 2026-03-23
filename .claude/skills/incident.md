---
name: incident
description: "Structure the aftermath of an incident: timeline, root cause analysis, postmortem, communications, and follow-through. Use when the user says things like: 'we had an incident', 'help me write a postmortem', 'draft incident comms', 'something broke'."
user_invocable: true
---

# Incident

Structure the aftermath of an incident: timeline, postmortem, communications, and follow-through.

---

## Process

### Phase 1 — Timeline & Facts

Help the user build a clear timeline. Ask ONE question at a time:
1. What happened? (Symptoms, impact, duration)
2. When was it detected and by whom?
3. What was done to resolve it?
4. What's the current state?

Output: Structured timeline

---

### Phase 2 — Root Cause Analysis

Guide the user through:
- What broke and why?
- What could have prevented it?
- What made detection/resolution slow?
- Were there contributing human/process factors?

Use blameless framing throughout.

---

### Phase 3 — Postmortem Draft

Using the template at `templates/postmortem.md` (if exists), produce:
- Summary, timeline, root cause, action items, lessons learned
- Blameless framing
- Clear owners for each action item

---

### Phase 4 — Communications

Draft comms for the appropriate audiences:
- **Internal team:** what happened, what we're doing
- **Stakeholders/leadership:** impact, resolution, prevention
- **External (if needed):** customer-facing messaging

For complex or sensitive comms, hand off to `/write`.

---

### Phase 5 — Follow-through & Memory

- Generate action items with owners and review dates
- Run the Memory Agent to extract systemic learnings using `[incident]`, `[planning]`, and `[self]` tags
- Focus: root causes that are structural (not one-off), detection/response gaps, process failures, what worked well, personal patterns in crisis response

Output: Memory entries → save to `context/memory/incidents/YYYY-MM-DD_[name]_memory.md`

---

## Context Loading

Load context per **Context Loading Protocol** in CLAUDE.md. Additionally:
- `context/memory/incidents/` — past incident learnings (are we seeing the same failures?)
- `context/memory/self/` — self-awareness patterns in crisis response

---

## File Outputs

| Output | Location |
|--------|----------|
| Postmortem | `context/incidents/YYYY-MM-DD_[name].md` |
| Comms drafts | Shared in chat |
| Action items | Included in postmortem doc |
| Memory | `context/memory/incidents/YYYY-MM-DD_[name]_memory.md` |

---

## Behaviour Rules

Behavioral Standards from CLAUDE.md apply. Additionally:

- Blameless framing always. Focus on systems and processes, not individuals.
- Push for specifics on timeline — vague timelines make useless postmortems.
- If the user is skipping root cause and jumping to fixes, slow them down.
- Flag if action items are too vague to be actionable (e.g., "improve monitoring" → monitoring of what, by when, by whom?).
