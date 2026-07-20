# MartechKit — Board Operating Model

**Owner:** Filippo (initiative lead)
**Purpose:** Make the `MTSDK` board the touch point for the initiative, so visibility comes from the artifact — not from you pinging Victor.
**Date:** 2026-07-03 · **Board pulled live:** 2026-07-03

> Snapshot: **5 epics, 13 tasks, every one at priority _Minor_ / status _Created_ / unassigned.** Nothing ranked — so "Victor is slow" has no #1 to be slow against. Ranking below is a recommendation to react against; you + Victor lock it in the first weekly.

---

## 1. Ranking pass (strict — no two cards share a rank)

### P0 — Stabilise & enforce *(prevent another VideoUp-class break)*

| Rank | Ticket | Epic | Note |
|------|--------|------|------|
| 1 | **MTSDK-14** — Amplitude V2 IDs → AppsFlyer (iOS) | AppsFlyer | In-flight: draft PR #15. `main` isn't V2-compliant yet — finish the one closest to done. |
| 2 | **MTSDK-15** — Amplitude V2 IDs → AppsFlyer (Android) | AppsFlyer | Cross-platform completion — don't ship a one-platform fix. |
| 3 | **MTSDK-10** — Spike: block host-app SDK re-init (iOS) | Dev QoL | The enforcement mechanism (SPM lint plugin Victor proposed). Spike to de-risk. |
| 4 | **MTSDK-11** — Spike: block host-app SDK re-init (Android) | Dev QoL | Android equivalent. |
| 5 | **MTSDK-18** — Structured logging (iOS) | Dev QoL | OSLog — lets QA validate identity in TestFlight without waiting on dashboards. |

### P1 — Foundational routing + committed demand

| Rank | Ticket | Epic | Note |
|------|--------|------|------|
| 6 | **MTSDK-5** — Selective event routing (iOS) | AppsFlyer | ⚠ Needs Martech refinement (`rs_ad_revenue`). Unblocks AdMob (16). Resolve the question first. |
| 7 | **MTSDK-6** — Selective event routing (Android) | AppsFlyer | Pairs with 5. |
| 8 | **MTSDK-8** — Uninstall measurement (iOS) | AppsFlyer | Miguel's roadmap ask; network optimisation value. |
| 9 | **MTSDK-9** — Uninstall measurement (Android) | AppsFlyer | Pairs with 8. |

### P2 — Correlation + new surface *(needs shaping)*

| Rank | Ticket | Epic | Note |
|------|--------|------|------|
| 10 | **MTSDK-12** — App Instance Identity → Amplitude (iOS) | Amplitude | Firebase install ID (MT-573). Correlation id, lower urgency. |
| 11 | **MTSDK-13** — App Instance Identity (Android) | Amplitude | Pairs with 12. |
| 12 | **MTSDK-16** — AdMob module (iOS) | AdMob | Large; depends on routing (5); "mediator wiring" undefined — shape before building. |
| 13 | **MTSDK-17** — AdMob module (Android) | AdMob | Depends on routing (6). |

**Epic MTSDK-7 (Flutter port):** no child tickets yet — parked until you confirm the Flutter approach with Catalá. Don't rank build work until it's scoped.

**Rule you enforce:** anything new gets *inserted at a rank* — it displaces something or goes below it. Nothing lands as "also high."

---

## 1b. Gaps — top-priority strategy work NOT on the board

`q3-strategy.md` calls these P0/committed, but they aren't ticketed on `MTSDK`. If the board is the single touch point, they're currently invisible:

- **`swift test` blocks merges** on the kit (cheapest prevention).
- **NULL `customer_user_id` rate alert** — the safety net that catches breaks in *hours*.
- **`verify-no-manual-martech.sh`** per-app CI gate — the app-side half of MTSDK-10/11.
- **AI Design adoption** (Vlad's ramp) + **Dashboard v0** — adoption/visibility; arguably a separate board, but right now nobody can see them.

Recommendation: add at least the first two as **P0** tickets so the board reflects the real top of the stack.

---

## 2. Column & WIP structure

| Column | Means | WIP limit |
|--------|-------|-----------|
| **Backlog (ranked)** | Everything, in the strict order above | — |
| **Ready** | Top 3, groomed, acceptance criteria clear | **3** |
| **In Progress** | Actively being worked | **2** (Victor ~50% + Vlad ramping → really ~1 each) |
| **In Review** | PR open, awaiting review/merge | **2** |
| **Blocked** | Needs a decision/dependency — *must* carry an owner + unblock date | flag, not a parking lot |
| **Done** | Merged/shipped this cycle | — |

With ~1.5 engineers, more than 2 things "in progress" means nothing is moving. A full In Progress column is a signal to *finish*, not start.

Note: MTSDK-5/6 and MTSDK-16/17 have a real dependency (routing → AdMob) and MTSDK-5 is blocked on a Martech clarification — those belong in **Blocked** with an owner + date until resolved, not sitting half-started in In Progress.

---

## 3. Stale-flag rules (the board pings you, not the reverse)

Set these as Jira quick-filters / a board dashboard so they surface automatically:

| Condition | JQL sketch | Action |
|-----------|-----------|--------|
| In Progress untouched > **5 working days** | `project = MTSDK AND status = "In Progress" AND updated <= -5d` | Auto-label `stale` → top of the weekly |
| In Review > **2 working days** | `project = MTSDK AND status = "In Review" AND updated <= -2d` | Flag — reviews are a fast lane; PRs must not rot |
| Blocked, no update > **3 days** | `project = MTSDK AND status = Blocked AND updated <= -3d` | You escalate to the dependency owner / Martech / Matellano |
| In Progress > 3 days, **no linked PR** | `project = MTSDK AND status = "In Progress" ...` | Visibility flag — is it actually moving? |

The In-Review rule exists on purpose: a merge-ready PR aging unseen is the exact failure that bit the earlier Andrey PR. Don't let finished work rot waiting on a review call.

---

## 4. The 15-minute weekly (execution ritual)

**When:** fixed slot, e.g. Tuesday. **Who:** Filippo + Victor (+ Vlad once ramped).
**Pre-req:** board updated *before* the meeting. If it isn't, that's signal #1.

| Time | Segment | What happens |
|------|---------|--------------|
| 0–2 | **Shipped** | What moved to Done since last week. |
| 2–7 | **Flags only** | Walk `stale` / blocked / in-review flags. For each: still moving? what unblocks it? You take escalations as an action **with a date**. |
| 7–12 | **Top of stack** | Confirm the ranked top 3 — *"still the priorities, or changed?"* Re-rank out loud if needed. No ties. |
| 12–15 | **Capacity & decisions** | Victor's split this week, Vlad's ramp, decisions you owe (Flutter/Catalá, MTSDK-5 Martech refinement, data owner). Owner + date each. |

You review an **initiative**, not a person — legitimate for a lead to run, and it doesn't step on Matellano's line to Victor.

**Keep separate:** the demand-side prioritisation with Miguel + david-leadtech feeds the backlog (monthly-ish). The weekly is execution only.

---

## 5. First-week setup checklist

- [ ] Apply priority tiers on the 18 issues (P0→Critical, P1→Major, P2→Minor) — see §6.
- [ ] Add labels `p0-now` / `p1-next` / `p2-later` for the tier, then drag within-tier backlog order for strict rank.
- [ ] Assign owners: Victor on P0 build items; leave Vlad's AI Design/adoption items on a separate lane until mid-July.
- [ ] Add the two missing P0 tickets (`swift test` gate, NULL-rate alert).
- [ ] Move MTSDK-5 to Blocked with a Martech-refinement owner + date.
- [ ] Add/confirm columns + WIP limits (Ready 3, In Progress 2, In Review 2).
- [ ] Create the four stale-flag quick-filters + a board dashboard gadget.
- [ ] Book the recurring 15-min weekly with Victor; put "board updated before" in the invite.
- [ ] One-line heads-up to Matellano: "here's how I'm running MartechKit visibility across the team."

---

## 6. How the ranking maps to Jira (what I can/can't set)

The priority field has 5 buckets (Blocker/Critical/Major/Minor/Trivial) — it can encode **tiers**, not a strict 1-of-13 order. True backlog rank is a drag-order I can't set through the API. So the scheme is:

- **Priority field (I can set):** P0 → **Critical**, P1 → **Major**, P2 → **Minor** (unchanged).
- **Label (I can set):** `p0-now` / `p1-next` / `p2-later`.
- **Strict within-tier order (you do):** drag the backlog in the UI — a 2-minute job once the tiers are colored.
