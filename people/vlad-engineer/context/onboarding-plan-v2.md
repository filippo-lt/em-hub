# Vlad Krudek — Onboarding Plan v2

**Role:** Software Engineer (AI-powered)
**Start date:** First week of March 2026
**Created:** 2026-03-06

---

## Guiding Principles

- Vlad needs significant daily coding time — this is how he recharges
- Meetings are fine as a *participant*; leading/facilitating is the stressor
- All process knowledge gained through FaceAI shadowing is transferable to future apps
- The onboarding feeds directly into the POC trial — they're not separate tracks

---

## Phase 1: Orientation & Ramp-Up (Week 1–2)

**Goal:** Understand how the company builds products. Get comfortable with tools. Start shadowing FaceAI.

### Process & Product Knowledge
- [ ] Shadow Filippo in FaceAI ceremonies (dailies, refinement, planning) — observe, don't lead
- [ ] Walk through a Jira ticket lifecycle end-to-end: how stories are created, refined, estimated, built, QA'd, shipped
- [ ] Observe PO interactions — how product requirements flow into engineering work
- [ ] Get access to FaceAI repos, project boards, CI/CD pipelines

### People (One-Off Introductions)
- [ ] Meet Staff Engineers (understand technical standards, architecture patterns, how they operate)
- [ ] Meet Lead QA (understand QA process, expectations, how QA interacts with dev)
- [ ] Continue scheduled inductions from HR/company onboarding

### First Task: FaceAI Linting Enforcement (via Cursor)
This is a concrete deliverable that contributes to FaceAI while serving as a structured Cursor learning exercise.

- [ ] Set up Cursor and learn core workflows (editing, AI chat, PR reviews)
- [ ] Audit current FaceAI linting rules — what exists, what's enforced, what's ignored
- [ ] Use Cursor to fix all existing lint violations across the FaceAI codebase
- [ ] Coordinate with Andrey on CI/CD pipeline — understand current setup, then enforce linting rules
- [ ] Document the linting setup for reuse in other apps

**What Vlad learns from this:**
- Cursor workflows (bulk edits, AI-assisted refactoring, PR reviews)
- FaceAI codebase (has to read and understand code to fix it)
- CI/CD pipeline (has to understand it to add enforcement)
- Company code standards (linting rules reflect team conventions)

### Remaining Tooling & Access
- [ ] Set up remaining tooling access: Jira, repos, CI/CD, comms channels

### SE Role Definition
- [ ] Align with Filippo on what the Software Engineer role looks like day-to-day
- [ ] Clarify expectations: autonomy, communication cadence, how/when to escalate

---

## Phase 2: POC Kick-Off (Week 2–3)

**Goal:** Scope is defined. Vlad transitions from observer to builder.

### POC Scope Definition
- [ ] Filippo aligns with David on POC scope and success criteria
- [ ] Filippo briefs Vlad on the POC: what the app is, who it's for, what "done" means
- [ ] Define together: tech stack, architecture approach, AI tooling strategy
- [ ] Set up the project: repo, CI/CD skeleton, project board

### Continued Learning
- [ ] Continue FaceAI shadowing (can taper off as POC ramps up)
- [ ] Apply product process knowledge: create own Jira tickets, write own stories

---

## Phase 3: POC Execution (Weeks 3–8)

**Goal:** Build an app from scratch to store-ready in 4–6 weeks.

### Delivery
- [ ] Build the app independently, using AI tooling (Cursor, etc.)
- [ ] Regular lightweight check-ins with Filippo (async-first, minimal meetings)
- [ ] Interact with Product/QA as needed — as a peer, not a lead
- [ ] Ship to store

### Checkpoints
- [ ] End of Week 4: Functional prototype — core features working
- [ ] End of Week 6: Store-ready build — polished, tested, submittable
- [ ] End of Week 8: Retro — what worked, what didn't, data for David

---

## 3-Month Horizon

| Milestone | Target |
|---|---|
| First app shipped | ~6 weeks from POC start |
| Second app shipped | ~3 months from start |
| SE role model validated | Enough data to present to David for Phase 2 strategy |

---

## What's Explicitly NOT in This Plan

These were in the original DA onboarding and are removed:

- ~~Leading ceremonies for any app~~
- ~~Owning FaceAI, ScreenMirroring, or Tattooist as DA~~
- ~~Vendor management / stakeholder alignment~~
- ~~Shared library development with Andrei~~
- ~~Coaching on DA-specific skills~~
- ~~Code assessment documents for SM~~

---

## Open Items

- [ ] POC scope — Filippo to define with David (target: next week)
- [ ] Meeting cadence with Vlad — define what "lightweight check-ins" means (daily async update? Weekly 15-min sync?)
- [ ] Success criteria for the 4-week trial — needs to be explicit and agreed with David
- [ ] How FaceAI shadowing tapers — at what point does Vlad stop attending ceremonies?

---

*Last updated: 2026-03-06*
