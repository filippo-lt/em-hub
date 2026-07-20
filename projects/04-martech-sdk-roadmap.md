# Martech SDK — 3-Month Roadmap

**Owner:** Filippo Tosetto
**Team:** 1 Staff Engineer, 1 Senior Engineer
**Jira:** [MTSDK board](https://leadtech.atlassian.net/jira/software/c/projects/MTSDK/boards/11469/backlog)
**Drafted:** 2026-07-14

---

## Strategic priorities

1. **Integrate Martech SDK into every app in the portfolio.**
2. **Give devs confidence that integrating the SDK didn't break anything.**

Priority 1 is gated on a Flutter library (most of the portfolio is Flutter), which is gated on
Android/iOS parity. Priority 2 is gated on knowing whether automated verification is even
technically possible — which is currently an open question, not a build task.

So the real shape of the next three months is: **prove it (M1) → build it (M2) → ship it (M3)**.

---

## Board state as found (2026-07-14)

| Epic | Items | Notes |
|---|---|---|
| **MTSDK-25** Platform Convergence | 17 | The real Android↔iOS parity epic. MTSDK-26 in progress. |
| **MTSDK-3** Martech SDK for Flutter | 2 | MTSDK-6 (bridge), MTSDK-24 (parity — *duplicate*) |
| **MTSDK-2** Developer Experience | 4 | MTSDK-9/12 (re-init spikes), MTSDK-10 (identity test), MTSDK-21 (logging) |
| **MTSDK-4** AppsFlyer Improvements | 6 | Not in this roadmap |
| **MTSDK-5** Amplitude Improvements | 2 | Not in this roadmap |
| **MTSDK-1** AdMob Module | 2 | Not in this roadmap |

Nothing is assigned. Nothing is estimated. No sprints.

### Two structural fixes to make before sprint 1

**1. Kill MTSDK-24.** "Bring Martech Pack and Martech Kit to feature Parity" is a *story* under the
Flutter epic. But MTSDK-25 (17 stories) **is** that work. The same deliverable currently exists at two
levels of the hierarchy, which means it will be reported on twice and finished never.

→ Close MTSDK-24. Replace it with a Jira link: **MTSDK-3 is blocked by MTSDK-25.**

**2. Repurpose MTSDK-2 rather than creating a new integration epic.**
MTSDK-2 already contains the three stories that *are* the integration-confidence work:
MTSDK-9/12 (prevent host apps re-initialising 3rd-party SDKs) and MTSDK-10 ("Create a script that
queries RC, Amplitude, and AppsFlyer to confirm cross-SDK identity stays aligned").

A new epic would fragment the same work across two containers.

→ Rename **MTSDK-2 → "Integration Confidence & Verification Suite"**, restate its description as an
outcome, move MTSDK-21 (Structured Logging) out to a DX/quality epic, and add the new stories below.

---

## Track A — Staff Engineer: Parity → Flutter

The 17 MTSDK-25 stories are **not equal**. Nine of them define the *public API surface the Flutter
bridge will call into*; the rest are behaviour and module-level fixes that the bridge doesn't care
about. Sequencing them as one undifferentiated block delays Flutter by a month for no reason.

### Month 1 — freeze the bridge surface (10 stories)

These change the shape of the public API, the init signature, or the DI graph. The Flutter bridge
cannot be designed against a surface that is still moving.

| Story | Why it blocks the bridge |
|---|---|
| MTSDK-26 | `MartechKeyProvider` properties — the config surface the bridge passes through |
| MTSDK-27 | `MartechModuleHooks` refactor — module architecture |
| MTSDK-28 | Re-phase modules — depends on 27 |
| MTSDK-29 | `CustomerInfo` accessor — description explicitly names Flutter as a collector |
| MTSDK-31 | `requestConsentAndStartMarketing(Application)` — description says *"Flutter bridge will pass context.application"* |
| MTSDK-32 | `Martech.purchases` / `appUserID` accessor — public API |
| MTSDK-35 | `EventTracker.track(event:)` overload — the core tracking call |
| MTSDK-37 | `MartechDependencies` — DI graph |
| MTSDK-41 | `Martech.amplitude` public on Android, hidden on iOS — the asymmetry must be *resolved* before the bridge can expose either |
| MTSDK-34 | Testability (`MartechDependencies` + `SuperwallWrapping`) — **pulled forward**: Track B needs this to write Android assertions |

**MTSDK-34 is the one to watch.** It looks like a trailing quality story, but Track B cannot write
meaningful Android integration assertions without an injectable dependency graph. If it slips,
Track B's month-2 work stalls. It belongs in month 1.

### Month 2 — trailing parity (7 stories) + bridge scaffold

MTSDK-30, 33, 36, 38, 39, 40, 42.

Note that **MTSDK-33 (AppsFlyer canonical events), MTSDK-39 (TikTok doesn't sync RC identify) and
MTSDK-40 (Meta doesn't sync RC)** are *identity- and event-wiring defects* — precisely the class of
bug the Track B suite is being built to catch. They are the suite's first real test cases. Fix them
in month 2 and the suite proves itself on real bugs rather than synthetic ones.

Second half of month 2: **MTSDK-6** — Flutter bridge scaffold + a codegen-vs-handwritten spike.

### Month 3 — Flutter bridge feature-complete

MTSDK-3 closes against the frozen native surface.

---

## Track B — Senior Engineer: Integration Confidence (MTSDK-2)

### Month 1 — spikes only. Deliberately.

| Story | Status |
|---|---|
| MTSDK-9 | Spike: prevent host-app re-initialisation of 3rd-party SDKs (Android) — exists |
| MTSDK-12 | Same, iOS — exists |
| MTSDK-10 | Spike: can we assert cross-SDK identity at all? — exists, needs to become the month's centrepiece |

**MTSDK-10 is the highest-uncertainty item on this roadmap and it is not a build task — it is a
go/no-go.** The proposed design reads back from Amplitude, RevenueCat and AppsFlyer APIs to confirm
identity alignment. Three things can kill that design:

- **Amplitude ingestion latency.** Events are not queryable the instant they're sent. If the lag is
  minutes, a CI check that polls the export API is either flaky or slow enough that nobody runs it.
- **AppsFlyer attribution windows.** Install/attribution data is not immediately readable either.
- **Debug-build filtering.** If debug traffic is excluded from these platforms (or pollutes prod
  dashboards if it isn't), the whole read-back approach needs a separate project/app-id per platform.

**The fallback if read-back fails:** assert at the **SDK boundary** instead of the vendor API —
intercept the outbound payloads (test transport / local proxy / injected fake via MTSDK-34's
dependency graph) and assert that the correct events, with the correct user IDs, were *emitted*.
Weaker guarantee, dramatically more reliable, runs in seconds in CI.

The month-1 exit criterion is a **decision**, not a suite: *read-back, boundary, or both?* — with a
working prototype against AI Design proving whichever we pick.

### New stories to create under MTSDK-2

| Story | Scope |
|---|---|
| Verification harness — Amplitude event assertions | Given a scripted user journey, assert the expected events landed with expected properties |
| Verification harness — Amplitude ↔ RevenueCat identity | Assert RC `appUserID` matches the Amplitude user/device ID |
| Verification harness — AppsFlyer identity wiring | Assert AF customer user ID matches the canonical user ID |
| CI integration | Run the suite on PR + nightly; fail loud, report which SDK broke |
| Pilot: AI Design (iOS) | First real integration; the suite must go green |
| Pilot: AI Design (Android) | Second real integration; the suite must go green |
| Integration playbook | How to integrate the SDK *and how to verify you didn't break anything* — the docs are the product for priority #1 |

### Month 2 — build the suite, wire CI, go green on AI Design (iOS + Android)

### Month 3 — roll to a second app, write the playbook

Rolling to a **second** app in month 3 is not padding. Until the suite has run against an app it
wasn't written for, you don't have a suite — you have a bespoke script for AI Design.

---

## Milestones

| | Exit criteria |
|---|---|
| **M1** (end of month 1) | Bridge surface frozen — 10 API-shaping stories closed. Verification approach **decided** with a working prototype (or explicitly killed and replaced with the boundary approach). |
| **M2** (end of month 2) | MTSDK-25 closed. Suite green in CI on AI Design, both platforms. Flutter bridge scaffolded. |
| **M3** (end of month 3) | Flutter SDK usable by an app team. Second app integrated. Integration playbook published. |

---

## Where I disagree with the current plan

> *"I believe these 2 major tasks should be enough for covering the 1st month."*

**They aren't — and that's not a capacity problem, it's a sequencing one.**

Two devs is roughly 8 dev-weeks per month. Month 1 as originally framed asks for: 17 parity stories
*plus* a spike *plus* a script suite *plus* a real integration *plus* documentation. That's a
quarter's work, not a month's.

More importantly, **half of that work is uncosted because it depends on an unanswered question.** You
cannot scope "implement scripts to run in CI" until the MTSDK-10 spike tells you whether the vendor
APIs can even be read back inside a CI time budget. Committing to build the suite in month 1 means
committing to a design you haven't validated.

So: month 1 buys you **two decisions and one frozen interface** —
- the bridge surface stops moving (Flutter can now be designed), and
- you know whether identity verification is an API-read-back problem or an SDK-boundary problem.

Both tracks then have a costed month 2. That's a slower-sounding month 1 that finishes the quarter
faster.

**One more thing I'd cut:** MTSDK-21 (Structured Logging, iOS) is in MTSDK-2 but does nothing for
either priority this quarter. Move it out; don't let it ride along.

---

## Open questions

1. **Is AI Design already on the SDK, or is the pilot a from-scratch integration?** Changes the month-2/3 estimate materially.
2. **Do debug builds hit the same Amplitude/AppsFlyer projects as production?** If yes, the verification suite will pollute prod analytics — needs solving before CI wiring.
3. **How many apps in the portfolio are Flutter vs native?** Determines whether MTSDK-3 is the critical path for priority #1 or a side quest.
4. **Who owns the SDK after this quarter?** Two people is enough to build it, not enough to build it *and* support N integrating app teams.
