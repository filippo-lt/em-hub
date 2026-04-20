---
name: format-candidate-review
description: Formats raw interview notes into structured candidate reviews with PROs, CONs, and a final recommendation. Use when the user provides interview notes and asks for a formatted review, candidate evaluation, or hiring recommendation.
---

# Format Candidate Review

Transforms unstructured interview notes into a consistent, readable candidate review document.

## Instructions

When the user provides interview notes:

### Step 1: Check for completeness
Review the notes against the question categories below. If critical areas are missing or thin, ask the user for more information before proceeding.

### Step 2: Extract PROs and CONs
Once notes are complete, identify key strengths and concerns across all dimensions.

### Step 3: Formulate recommendation
Synthesize a clear hiring recommendation with justification.

### Step 4: Format output
Use the template below to present the review.

## Pre-Review Question Categories

Before formatting the review, ensure the notes cover these key areas. If any are missing or unclear, ask follow-up questions:

### Technical Competency
- Does the candidate have the required technical skills for the role?
- How did they perform on technical exercises or coding questions?
- Can they explain complex technical concepts clearly?
- Any gaps between their claimed skills and demonstrated ability?

### Experience and Track Record
- Is their previous experience relevant to this role?
- Have they worked on projects of similar scope/complexity?
- What was their specific contribution vs. team contribution?
- Any career progression or leadership experience?

### Problem-Solving and Critical Thinking
- How do they approach unfamiliar problems?
- Can they break down complex requirements?
- Do they ask clarifying questions or make assumptions?
- How do they handle being stuck or not knowing something?

### Communication and Collaboration
- Did they communicate clearly throughout the interview?
- Are they able to explain their thought process?
- How do they describe working with others (engineers, PMs, designers)?
- Any red flags in how they discuss previous teams or conflicts?

### Motivation and Fit
- Why are they interested in this role/company?
- Do their career goals align with what this role offers?
- What type of work environment do they thrive in?
- Any concerns about commitment or job-hopping?

### Culture Add
- What unique perspectives or experiences do they bring?
- How do they handle feedback or disagreement?
- Would they complement the existing team dynamics?
- Any values misalignment concerns?

## Output Template

```markdown
## Candidate Review: [Candidate Name] - [Position/Role]

### PROs
- [Specific strength with supporting context from interview]
- [Specific strength with supporting context from interview]
- [Additional strengths as relevant]

### CONs
- [Specific concern with supporting context from interview]
- [Specific concern with supporting context from interview]
- [Additional concerns as relevant]

### Final Recommendation
**[HIRE / NO HIRE / CONSIDER WITH RESERVATIONS]**

[2-3 sentences explaining the rationale, referencing specific PROs/CONs that influenced the decision. Include any conditions or caveats if applicable.]
```

## Guidelines

- **Ensure completeness**: Before writing the review, verify notes cover all 7 question categories above. Ask follow-up questions if areas are missing.
- **Be specific**: Reference actual examples from the notes, not vague generalities
- **Balance the picture**: Include both PROs and CONs unless the candidate is exceptional in one direction
- **Recommendation clarity**: Use one of the three standard options (HIRE / NO HIRE / CONSIDER WITH RESERVATIONS)
- **Justify the call**: The recommendation paragraph should tie back to specific points above
- **Stay objective**: Use evidence from the notes, not subjective impressions
- **Flag uncertainty**: If notes are insufficient in a critical area, note this as a CON (e.g., "Insufficient data on X - recommend follow-up interview")

## Example

**Input notes:**
"Spoke with Sarah about the senior dev role. She has 6 years of React experience, led a team of 3 at her last company. Good communication, answered system design questions well. However, she struggled with the coding exercise - took a long time and needed hints. Says she's rusty on algorithms but strong on practical work."

**Output:**
```markdown
## Candidate Review: Sarah - Senior Developer

### PROs
- Strong practical experience with 6 years in React and team leadership (managed 3 people)
- Excellent communication skills and solid system design knowledge
- Honest self-assessment about strengths and areas for growth

### CONs
- Struggled with the coding exercise, requiring hints and additional time
- Self-identified rustiness with algorithms, which may impact certain project needs

### Final Recommendation
**CONSIDER WITH RESERVATIONS**

Sarah brings strong practical experience and leadership capabilities that align well with the senior developer role. However, the coding exercise performance raises concerns about technical depth for algorithm-heavy work. Recommend follow-up technical screen focused on practical coding scenarios relevant to our codebase, or consider for teams with less algorithmic complexity.
```
