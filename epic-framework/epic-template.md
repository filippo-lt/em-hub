# Epic: [Title]

> **Status:** Draft | Ready for Engineering | In Progress | Done
> **Project:** [Jira Project Key]
> **Epic Key:** [PROJ-XXX]
> **Epic Type:** UI Feature | Backend/Infra | Algorithm/ML | Tech Debt | Spike/Discovery

---

## TL;DR

> **What to write:** 2–3 sentences max. Cover three things in one go: what we are building, who it is for, and why we are doing it now. If you cannot summarise the epic in three sentences, the scope is probably too large.
>
> **Bad example:** "This epic improves the app experience for users."
> **Good example:** "Free users who tap Generate will see a modal offering two paths: watch a rewarded ad or upgrade to PRO. This gates AI generation behind a monetisation step without blocking the experience, using a daily quota and per-flow toggles managed via Remote Config."

---

## Business Goal

> **What to write:** The business outcome this feature moves. Be specific — name the metric or behaviour you expect to change (retention, conversion, cost reduction, competitive parity). Avoid generic statements like "improve the user experience."
>
> **Bad example:** "Keep users happy and improve the app."
> **Good example:** "Monetise the high-volume free user segment and offset LLM/image generation costs while increasing PRO conversion through feature friction."

## Problem Statement

> **What to write:** The specific user problem or failure mode this epic fixes. Describe what goes wrong today, for whom, and what the consequence is. This is user-facing — avoid internal/business framing here.
>
> **Bad example:** "Users don't have this feature yet."
> **Good example:** "The current Retouch tool fails users on fine detail work in two ways: the zoom limit prevents pixel-level precision, and fast brush strokes leave behind blurry smears rather than a clean heal. Users who notice this drop off or leave the app to use a competitor."

---

## Scope

### In Scope

> **What to write:** A concrete list of what will be built, broken down by layer. Be specific enough that an engineer can estimate each item. Use the layers below and remove any that don't apply to this epic.
>
> **Rule:** If it is not listed here, it is out of scope. Ambiguity here is the most common source of scope creep.

**Mobile (iOS / Android)**

- [List each screen, component, interaction, or behaviour being added or changed]

**Backend / Infra**

- [List each new endpoint, service, or infrastructure change]

**Analytics**

- [List the event names that must be implemented — use the project's existing naming convention]

**Remote Config / Feature Flags**

- [List each key, its type, and its default value]

### Out of Scope

> **What to write:** Explicitly list everything that is NOT included in this epic, even if it seems obvious. This section protects Engineering from scope creep and prevents the PO from being surprised later.
>
> **Rule:** If you had to make a deliberate decision to exclude something related to this feature, write it here.

- 

---

## Delivery Plan

> **What to write:** How this epic will be delivered in small, shippable increments. This table defines the slicing — what ships in each milestone, how to verify it, and how it gets released. Sprint assignment happens at sprint planning, not here.
>
> **Rules:**
> - Each milestone must be independently testable and have a QA-verifiable exit criterion.
> - If you can’t describe at least one shippable first milestone, the epic is too large or too vague.

| Milestone | User-visible outcome | Scope (high level) | Exit criteria (QA verifiable) | Release / Flagging |
| --------- | -------------------- | ------------------ | ----------------------------- | ------------------ |
| M0 (opt)  |                      |                    |                               |                    |
| M1        |                      |                    |                               |                    |
| M2        |                      |                    |                               |                    |

> **EM estimate:** ~X person-weeks total *(filled during or after grooming)*

---

## User Flows

> **What to write:** Step-by-step numbered sequences covering every path a user can take through this feature. Start with the happy path, then add one subsection per meaningful variant (error, edge case, different user state).
>
> **If this epic has no UI:** Write system flows instead (e.g. “1. Client calls endpoint… 2. Service validates… 3. Job enqueued…”). If flows truly do not apply, write “N/A” explicitly.
>
> **Rule:** Be specific enough that a developer can implement each step without asking a question. If a step depends on a condition (e.g. user is PRO, quota is reached), state it explicitly.
>
> **Bad example:** "User opens the tool and edits their photo."
> **Good example:** "1. User taps Generate. 2. App checks: is user PRO? → No. 3. App checks: has user hit daily quota? → No. 4. Modal appears with two CTAs..."

### Happy Path — [describe in a few words]




### Variant — [e.g. "User hits daily quota"]




### Variant — [e.g. "API call fails"]




---

## Acceptance Criteria

> **What to write:** A checklist of testable, pass/fail conditions. Every item must be verifiable by QA without asking anyone — no subjective criteria. Use "must" for hard requirements, "should" for strong preferences.
>
> **Bad example:** "The tool works correctly and feels smooth."
> **Good example:** "Fast brush strokes produce no blurry smears — the healed area must blend naturally into the surrounding texture."
>
> **Rule:** If QA cannot verify an item on a device with no context from the developer, rewrite it.

- [ ]
- [ ]

---

## Non-functional Requirements (NFRs)

> **What to write:** Constraints and quality bars that are easy to miss in UI-focused specs but are often the reason engineers say “this isn’t enough info.” If an item is not relevant, write “N/A” explicitly.
>
> **Rule:** If an NFR would change the estimate or design decisions, it must be written here before “Ready for Engineering.”

- **Performance**: [Targets like max latency, frame rate, memory, CPU, payload size]
- **Reliability**: [Retries, offline behavior, idempotency, failure modes, fallback behavior]
- **Privacy & Security**: [PII, permissions, data retention, threat considerations, compliance constraints]
- **Accessibility**: [VoiceOver/TalkBack, contrast, dynamic type, touch targets]
- **Observability**: [Logs/metrics/traces needed, key dashboards/alerts, debug hooks]
- **Localization**: [Any new strings, formatting, RTL considerations]

---

## UI States

> **What to write:** Every visual state the UI can be in for this feature. Add a row for each state. For each state, describe the exact behaviour or copy shown to the user. Do not leave any state undefined — undefined states become bugs.
>
> **If this epic has no UI:** Write “N/A” explicitly.
>
> **Minimum required states:** Loading, Success, Error. Add Empty, Disabled, and any feature-specific states as needed.


| State   | Behavior / Copy |
| ------- | --------------- |
| Loading |                 |
| Success |                 |
| Empty   |                 |
| Error   |                 |


---

## Analytics Events

> **What to write:** Every event that must fire as part of this feature. Use the project's existing Amplitude event naming convention (snake_case). For each event, specify exactly when it fires and which properties it must include.
>
> **Rule:** "We'll add analytics later" is not acceptable. Events missed here are missed permanently once the feature ships.
>
> **If no new events are needed:** Write "No new events — existing [tool name] events cover this flow." and optionally note any existing event properties that should be extended.


| Event Name | Trigger | Key Properties |
| ---------- | ------- | -------------- |
|            |         |                |


---

## Technical Context

> **What to write:** High-level architecture and technical decisions — no code, class names, method names, file paths, or API endpoints. The goal is to surface decisions that affect scope or estimate before Engineering opens the codebase.
>
> **Owner:** PM/PO fills what they know at product level. Engineering fills the rest during grooming.
>
> **Rule:** If you would need to read the codebase to answer something, leave it blank and flag it for grooming. Do not guess.

- **Builds on / reuses:** [What existing features, screens, or flows does this build on? e.g. "Reuses the existing Retouch screen and brush interaction"]
- **New integrations or services needed:** [What new external services, SDKs, or third-party capabilities does this require? e.g. "Requires AdMob SDK integration" or "None — uses existing pipeline"]
- **What data does this read or write:** [What information does this feature consume or produce? e.g. "Reads user subscription status; writes daily ad quota counter to local storage"]
- **Remote Config / feature flags needed:** [List flag names and what they control, or "None"]
- **Key architecture decisions:** [Any decisions already made that affect how this is built, e.g. "Quota is per-device (local storage), not per-account (server-side)" or "iOS only for this iteration"]
- **Known constraints:** [Any hard limits Engineering should know upfront, e.g. "Must not affect load time of the editor screen" or "No new backend services — client-side only"]

---

## Design References

> **What to write:** A link to the Figma file and any competitor or benchmark references.
>
> **Rule:** If `Epic Type` is **UI Feature**, designs are a hard gate. If the epic has no UI change (Backend/Infra, Algorithm/ML, Tech Debt), designs can be marked “Not required.”

- **Figma:** [link] — or — `Not ready — Epic is in Draft`
- **Competitor / benchmark references:** [App names and what to look at, e.g. "Facetune — zoom depth and brush precision at pixel level", screenshots or screen recordings of the competitor feature]

---

## Open Questions (Must be resolved to start)

> **What to write:** Unknowns that block implementation or meaningfully affect scope/estimate. These are not “risks”; these are unanswered questions.
>
> **Rule:** This section must be empty (or explicitly accepted as a Spike/Discovery epic) before moving to **Ready for Engineering**.

- 

---

## Dependencies & Prerequisites

> **What to write:** Everything that must exist or be completed before Engineering can start. Include both internal dependencies (e.g. another epic, a backend endpoint, a design deliverable) and external ones (e.g. a third-party account, an approved SDK).
>
> **Rule:** If Engineering picks up this epic and hits a blocker on day one because of something listed here, it means this section was incomplete.

- 

---

## Assumptions

> **What to write:** Decisions that have already been made and that Engineering should not re-open without flagging. These are the things you decided during scoping that are load-bearing for the estimate.
>
> **Rule:** If an assumption turns out to be wrong, the estimate is likely wrong too. Flag it — don't silently adjust scope.

- 

---

## Risks

> **What to write:** Known unknowns — things that could go wrong, expand scope, or affect quality that we are aware of but have not resolved. Do not try to resolve risks here; just name them clearly so Engineering can plan around them.
>
> **Rule:** "No risks" is almost never true. If you have no risks, you have not thought hard enough.

- 

---


