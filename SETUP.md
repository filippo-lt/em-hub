# Setup Guide

## Prerequisites

- Cursor IDE installed (with Pro subscription or API key configured)
- Your meeting transcripts (even just a couple to start)

---

## Step 1 — Place the Folder

Place the `em-hub/` folder somewhere stable on your machine:

```
~/Documents/em-hub/
```

This is your working directory for all EM workflows.

---

## Step 2 — Set Up in Cursor

Open the `em-hub/` folder in Cursor. The `.cursorrules` file will automatically point Cursor to `CLAUDE.md`, which contains the master orchestrator.

**Alternative: Project Rules (if you prefer explicit control)**

1. Go to **Cursor Settings → Project Rules**
2. Create a new rule and paste the contents of `CLAUDE.md` as the system prompt
3. Set it to apply to **all files** in this project

---

## Step 3 — Fill In Your Context

The system works best with context. Fill in these files (15–20 min total):

### People profiles
Edit `people/david-manager/profile.md` and `people/andrey-direct/profile.md`:
- Who they are and their role
- Your relationship dynamic
- Communication style / preferences
- Current priorities
- Sensitivities

### Team context
Edit `teams/mobile-app-unit/roster.md` and `teams/mobile-app-unit/okrs.md`:
- Team members, roles, vendor affiliations
- Current quarter goals

### Global context
Edit files in `context/`:
- `my-goals.md` — what you're personally working toward
- `company-priorities.md` — what leadership cares about
- `org-chart.md` — key stakeholders and relationships

---

## Step 4 — Add Historical Transcripts

If you have past meeting transcripts:

1. Save them as plain text or markdown
2. Name with date prefix: `2025-01-15_transcript.md`
3. Drop into `people/[name]/transcripts/`

**Don't have transcripts yet?** That's fine — agents will ask more questions to compensate. After your first recorded meeting, the system starts building context.

**Getting transcripts:**
- Otter.ai, Fireflies, Fathom, Notion AI — export as plain text
- Local recording — use Whisper (free, runs locally) to transcribe

---

## Step 5 — Add Extra Context (Optional)

Drop relevant documents into `people/[name]/context/` or `teams/[team]/context/`:

- Performance reviews
- Project roadmaps
- OKRs or goals docs
- Email thread exports
- Your own notes

The agents read these when preparing or analysing.

---

## Step 6 — Your First Session

Open Cursor in the `em-hub/` folder and try:

**Before a 1-on-1:**
```
I have a 1-on-1 with David coming up on Thursday. Help me prepare.
```

**After a 1-on-1:**
```
I just finished my 1-on-1 with David. Here's the transcript. Analyse how it went.
```

**Status update:**
```
Help me write my weekly status update for David.
```

**Performance review:**
```
Help me draft a performance review for Andrey.
```

**Decision support:**
```
I need to decide whether to extend the Brainvire contract. Help me think through it.
```

---

## Step 7 — Keeping It Tidy

After each meeting cycle:
- Talking points saved to `people/[name]/talking-points/`
- Transcripts saved to `people/[name]/transcripts/`
- Memory files saved to `people/[name]/memory/`

For memory entries, paste the code block into Claude.ai with: *"Please update your memory with these entries"*

Over time the system gets smarter because it has more history to work with.

---

## Adding New People

```bash
mkdir -p people/firstname-role/{transcripts,talking-points,memory,context}
cp templates/context-profile.md people/firstname-role/profile.md
# Edit the profile
```

See `CUSTOMISATION.md` for how to modify agent behaviour, add workflows, and improve the system.
