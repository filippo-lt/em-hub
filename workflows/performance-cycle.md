# Workflow: Performance Cycle

Draft reviews, prepare for calibration, plan feedback delivery conversations.

---

## Routing

Activate when the user says:
- "Performance review for [name]"
- "Draft feedback for [name]"
- "Prep me for calibration"
- "I need to deliver difficult feedback to [name]"
- "Help me assess [name]'s performance"

---

## Agents Used

1. **Review Agent** (`agents/review-agent.md`) — drafts reviews, calibration briefs
2. **Prep Agent** (`agents/prep-agent.md`) — prepares the feedback delivery conversation
3. **Analysis Agent** (`agents/analysis-agent.md`) — analyses how the feedback conversation went
4. **Memory Agent** (`agents/memory-agent.md`) — captures outcomes and commitments

---

## Typical Flow

```
1. User: "Write a review for Andrey"
   → Review Agent gathers evidence, drafts review

2. User: "Prep me for calibration"
   → Review Agent produces calibration brief

3. User: "Help me prepare to deliver this feedback"
   → Prep Agent runs with review as context input

4. [Feedback conversation happens]

5. User: "Here's the transcript from my review conversation with Andrey"
   → Analysis Agent evaluates the delivery

6. User: "Extract memory"
   → Memory Agent captures outcomes using [perf], [people], and [self] tags
   → Focus: calibration insights, feedback that landed vs didn't, rating patterns, self-awareness about how you deliver reviews
```

Memory can be triggered after any step — not just step 6. For example, after drafting the review (step 1) you might capture insights about evidence gaps or rating calibration.

---

## Context Loading

- `people/[name]/profile.md`
- `people/[name]/context/` — previous reviews, goals docs
- `people/[name]/transcripts/` — recent 1-on-1 history
- `teams/[team]/okrs.md` — team goals for context

---

## File Outputs

| Output | Location |
|--------|----------|
| Performance review | `people/[name]/context/YYYY-MM-DD_review.md` |
| Calibration brief | `people/[name]/context/YYYY-MM-DD_calibration.md` |
| Delivery prep | `people/[name]/talking-points/YYYY-MM-DD_review-prep.md` |
| Memory | `people/[name]/memory/YYYY-MM-DD_memory.md` |
