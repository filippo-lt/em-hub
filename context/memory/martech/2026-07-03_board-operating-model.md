# MartechKit — Board operating model & MTSDK ranking

**Captured:** 2026-07-03 (EM brainstorm session)
**Artifact:** `context/martech-sdk/board-operating-model.md`
**Board:** Jira project **MTSDK** (MartechSDK), cloudId `e0d32791-26d8-4839-8507-72bd12b565ed`

## Board reality (pulled live 2026-07-03)
- **5 epics, 13 tasks, every one at priority _Minor_ / status _Created_ / unassigned.** No ranking at all — which is why "Victor is slow" had no #1 to be slow against.
- Epics: MTSDK-1 Developer QoL · MTSDK-2 AppsFlyer Improvements · MTSDK-3 Amplitude Improvements · MTSDK-4 AdMob Module · MTSDK-7 Flutter port (no child tickets yet).
- The board is a **library feature backlog** — it does NOT contain the operating-model/adoption work from `q3-strategy.md`.

## Recommended ranking (P0/P1/P2 — tiers, since Jira priority has 5 buckets)
- **P0 stabilise/enforce:** MTSDK-14 & 15 (Amplitude V2 IDs → AF, iOS in-flight PR #15 then Android) · MTSDK-10 & 11 (spikes: block host-app SDK re-init) · MTSDK-18 (structured logging).
- **P1 routing + demand:** MTSDK-5 & 6 (selective event routing — 5 ⚠ blocked on Martech refinement, gates AdMob) · MTSDK-8 & 9 (uninstall measurement).
- **P2 correlation + new surface:** MTSDK-12 & 13 (Firebase app-instance id → Amplitude) · MTSDK-16 & 17 (AdMob module — large, depends on routing, needs shaping).
- Apply as: priority Critical/Major/Minor + labels p0-now/p1-next/p2-later; drag within-tier order in UI (true rank not API-settable).

## Gaps — strategy P0 work NOT ticketed on the board
`swift test` merge gate · NULL `customer_user_id` rate alert · `verify-no-manual-martech.sh` per-app CI gate · AI Design adoption (Vlad, mid-July) · Dashboard v0. Add at least the first two as P0 so the board reflects the real top of stack.

## Operating model
- **Columns/WIP:** Backlog(ranked) · Ready(3) · In Progress(2) · In Review(2) · Blocked(owner+date) · Done. ~1.5 engineers → a full In-Progress column means *finish, don't start*.
- **Stale-flags** (auto quick-filters): In Progress >5d → `stale`; In Review >2d → flag (the failure that rotted the Andrey PR); Blocked >3d → escalate.
- **15-min weekly:** run it as a fixed first segment inside the **Victor 1:1** for now (weekly, not bi-weekly — Victor 50%, active build); spin out a dedicated slot with Victor + Vlad once Vlad joins mid-July. Filippo moving the Victor 1:1 earlier in the week to prioritize the board *with* Victor and stand up the weekly.
- **Governance:** Victor reports to Matellano — run through the artifact + cadence, escalate via Matellano, ask at initiative level.

## Sponsor & demand
- Sponsor conversation: David Sánchez (Head of Martech) — H2 Martech 1:1 Mon 7/6. Bring the operating model + adoption boundary (Eng builds rails; app teams migrate their own app; Victor's 50% ≠ a company-wide migration service).
- Demand side (issue #38): Miguel Alvarez + david-leadtech. Monthly-ish prioritisation ritual feeds the backlog; keep it separate from the weekly execution review.
