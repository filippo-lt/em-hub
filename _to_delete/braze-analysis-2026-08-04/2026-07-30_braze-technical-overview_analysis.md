# Analysis — Leadtech ↔ Braze, Technical Overview Session — 2026-07-30

**Duration:** ~90 min · **Braze:** Robert Low (solutions) · **Leadtech:** Vlad Moskalets (Martech, chairing), Alejandro Culebras (Martech/tech), Heitor Pinheiro (web), Sergio Hueso, Jorge Andres, Pablo Lombillo, Francisco Carbonero, Oriol Riba, Alejandro Reinoso, Andre Montenegro, Fernando Ortega, Louize Colombo (Braze commercial), Filippo

> ⚠️ **Name disambiguation — this matters.** "Vlady/Vlad" throughout this transcript is **Vlad Moskalets (Martech)**, *not* Vladyslav Krut, your MartechKit engineer. Two different people, and the confusion is easy to make when reading notes later.
>
> **ASR decodes used:** *"expert sender"* → ExpertSender · *"one signal"* → OneSignal · *"AppsFire / Appslar"* → AppsFlyer · *"data brace / data breaks"* → Databricks · *"revenue cat / CAD"* → RevenueCat · *"hamburger"* → Amplitude · *"trace check"* → TraceCheck · *"Hedor / Hetero / Heiro"* → Heitor · *"Andrea"* → Andrey · *"Mao"* → MAU. Speaker labels are almost entirely `Them`, so **attributions below are inferred from content and should be verified before quoting anyone.**

---

## Executive summary

**Three things happened in this meeting, and only one of them was on your radar.**

**1. Your two "blocking data points" were live on the table for twenty minutes — with Alejandro in the room — and nobody stated the apps requirement.** You've told Andrey the Braze integration is blocked on Martech answering *which user ID* and *which events*. Both questions were actively debated in this session. Neither was closed. The user-ID discussion ended with Alejandro saying, in effect, *"until we share an ID across platforms, the user is anonymous in Braze"* — a restatement of the problem, not an answer. **The blocker is not that Martech owes you an answer. It's that nobody has told Martech the apps side is gated on it.** That reframes your ask entirely, and it's cheaper than you think.

**2. A material correction to your technical model.** You told Andrey on 3 August that the shape is *initialise the SDK → set the user ID → send events*, and the prep doc for David carries *"we trigger SDK init on login/user recognition, so we don't inflate MAU."* Robert corrected exactly this in the room: **initialisation happens when a user opens the app. `changeUser` is the login-time method.** Delaying initialisation to login is a non-default customisation, not the standard flow — and it was explicitly punted to the SDK session, undecided. **Do not repeat the "we init on login" line to David as though it's settled.**

**3. You were assigned ownership of the apps section of the company-wide Braze blueprint, and said nothing.** Vlad Moskalets named three review stakeholders — *"Alejandro from tech, Heitor from web, and someone from apps"* — then: *"Filippo and Andrey, I'll add you as the representatives from apps."* Your total spoken contribution to a 90-minute session was **three utterances: "Thank you," "As well," "Thank you. Bye bye."**

That third point is the same pattern your last six 1:1 analyses have flagged, appearing in a new venue. This one is worse in one specific way: it wasn't a 1:1 with a manager who knows your work. It was a cross-functional vendor session in which **Martech and Web defined the integration architecture for the whole portfolio, apps was represented by silence, and apps got handed a deliverable anyway.**

---

## What was actually decided

| Decision | Detail | Owner |
|---|---|---|
| **Sequencing confirmed** | TraceCheck → Apollo → Faxer. **Web first, deliberately** — Heitor's reasoning: highest impact because that's where email volume is, and easy/new projects first so later ones learn from them. Apps last. | Vlad Moskalets |
| **SDK is mandatory** | Alejandro floated API-only for apps. Robert closed it: push is *"almost impossible"* without the SDK, *"I'd 100% suggest doing it."* All channels are built on the SDK. | Closed |
| **Amplitude is the baseline** | Heitor's strategic frame, adopted: leverage the transactional normalisation already done in Amplitude rather than designing Braze from scratch. *"We should go in a unified way."* | Heitor / Alejandro |
| **The blueprint is the governing artifact** | One document, contributed to by all, distributed to product and dev teams. Reviewed by Alejandro (tech), Heitor (web), **Filippo + Andrey (apps)**. | **You** |
| **Instance: US-07** | Cluster and REST endpoint fixed. API keys created per-purpose, never one-key-all-permissions; keys can be deleted but not edited. | — |
| **Migrating off two vendors** | **ExpertSender** (email) and **OneSignal** (push). Neither has a direct Braze connector — historical data goes in via `users/track`. Robert to confirm. | Robert |
| **One external Currents connection** | Amplitude **or** Databricks, not both. Alejandro leaning Databricks; Robert to confirm against the contract. | Open |

---

## The five things nobody wrote down, and at least three land on apps

### 1. SDK initialisation timing vs MAU — unresolved, and it's a contract-cost issue

Vlad Moskalets raised it well: *"one of the problems… of our contract is the MAU, which is tracked by unique users tracked with SDK. So the sooner we initiate the SDK, the more users we track as active."* His concern was web bounce traffic — *"we don't want to pay for them."*

**Robert's correction is the part that matters to you:** initialisation is on app open; `changeUser` is the login-time identification method. Delaying init is possible but it is a deviation, and Robert asked directly *"are you saying you'd rather delay it?"* before parking it for the SDK session.

> **Consequence for apps:** an app is not a website. Bounce traffic is a *web* problem — an app open is a much stronger signal of a real user. **The right initialisation policy is probably different for apps and web, and right now there's one undecided policy for both.** If web's answer (delay init) becomes the standard and gets applied to apps, you lose automatic session/device/push-token collection for no MAU saving worth having. **This is a genuine apps-specific position you could have stated and didn't.**

### 2. `changeUser` is irreversible, and there is no logout

Robert, verbatim in substance: you cannot revert an identified user to anonymous, and **after a user logs out Braze keeps writing events and attributes to that same profile until another `changeUser` fires with a new external ID.**

> **Nobody flagged the shared-device case.** For a TV-adjacent product like iMote, or any app where a device is used by more than one person, this is a live data-correctness trap of exactly the class MartechKit was built to prevent. It has no ticket and no owner.

### 3. RevenueCat may be sending the wrong event type

Braze has **deprecated purchase events in favour of structured e-commerce recommended events** (product ID, price, quantity, fixed schema). Robert flagged that you'd need to check the RevenueCat side to confirm which it sends, because purchase events lose most of the out-of-box dashboard functionality.

> **This is an apps item.** You confirmed in the room that you have one-time purchase, subscription-start and renewal events. Nobody was assigned to check what RevenueCat actually emits. Given that you have just spent three weeks establishing that `originalAppUserID` is the canonical identity, **the RevenueCat↔Braze seam is yours and it now has a second open question on it.**

### 4. Currents is not retrospective — and that creates a sequencing constraint

Robert: data exported before the Currents connection exists is never backfilled. Combined with the ExpertSender/OneSignal historical migration, **the order of operations matters and nobody wrote it down.** Connect Currents before you import history, or the imported history never reaches the downstream warehouse.

### 5. Weekly user archival

Every Sunday 05:30 EST, Braze deletes **inactive** users (unreachable + no profile update in 6 months) and **dormant** users (valid push token but no activity in 12 months), along with their custom data, device data and engagement stats. Escape hatch is a `do_not_archive` custom event.

> For iMote at 30–50k installs/day with a long-tail install base, **this deserves an explicit decision rather than a default.** Unowned.

---

## The user-identity problem — the actual centre of the meeting

This is where your two blocking data points live, so it's worth reading closely.

**Robert's requirement:** one consistent `external_id` across the whole stack, GUID or hashed — explicitly *not* an email address.

**Alejandro's answer:** *"everybody have different user IDs that are unique for the project."* Per-project identity, not portfolio identity.

**Vlad Moskalets raised the hard case, and it's Faxer:** web + iOS, users matched today via **RevenueCat ID**, and — critically — matched *without logging in*, via an AppsFlyer OneLink deep link. His question was the right one: *"at the point in time when we match those users, should Braze also know it's the same user?"*

**Alejandro's response:** if we don't push a shared ID at that moment, the user stays anonymous in Braze — same as Amplitude. On iOS it's worse, because attribution matching is **probabilistic** and may not resolve on first open.

**Then Alejandro left for another meeting and the thread died.**

Vlad Moskalets closed it with the only forward-looking thing said: *"we don't have many multi-platform apps yet, but given the strategy of the company we'll have more by the end of the year — at this point when we only design the integration, we should build it in a way that powers those cases later on."*

> **Read this against your own record.** You have just spent three weeks and an audit establishing that **RevenueCat `originalAppUserID` is the canonical identity** for the apps portfolio, that the SDK was silently substituting an alias, and that Face AI is in production reading the wrong one. **You are the only person in the company holding a settled answer to the exact question this meeting failed to close** — and you didn't put it on the table.
>
> That is not a missed opportunity to look good. It's a live risk: if Martech settles portfolio identity without the apps constraint in the room, you'll be migrating to their answer in Q4.

---

## Your participation — honest assessment

**Three utterances in ninety minutes: *"Thank you," "As well," "Thank you. Bye bye."*** The "As well" was confirming that TraceCheck is web.

I want to be fair about context: this was a vendor overview, largely a deck walkthrough, and much of it was genuinely Martech's and web's domain. You are not obliged to fill airtime. **But three things happened in this specific meeting that were yours:**

1. **The apps initialisation policy** was being set by web's cost logic, with no apps voice.
2. **The identity question you have the answer to** was debated and left open, with the person who needed the answer sitting silent.
3. **You were assigned the apps section of the portfolio blueprint** and accepted it without a word — no scope, no date, no "Andrey and I will cover apps, and here's what we need from Martech to do it."

The last one is the pattern. Your 28 July analysis records *"I'm happy"* three times as the largest silent scope absorption on record. **This is the same shape in a different room**, and it's the fourth venue it's appeared in: David 1:1s, the Victor conditions, the carve-out list, now a vendor session.

**The one thing that would have changed all three outcomes is a single intervention of about forty seconds:**

> *"From apps: our canonical identity is the RevenueCat `originalAppUserID` — we've just finished an audit that established that, and we have a live production bug from getting it wrong. If the portfolio external ID is going to be something else, apps needs to know now rather than in Q4. And initialisation timing shouldn't be one policy — an app open is a real user, a web landing isn't, so we'd want to init on open and use `changeUser` at login."*

That sentence puts your strongest technical work in front of Martech, Web and the vendor at once, establishes apps as a decision-maker rather than a recipient, and pre-empts the exact rework you'd otherwise discover in October. **You had it. It cost forty seconds. It didn't happen.**

**The mitigating read, and it's real:** you were four days from a launch and three from holiday, and this was a session where sitting back is defensible. The problem isn't this meeting in isolation. It's that it's the eighth consecutive datapoint for the same mechanism — **you perform when there's an artifact in front of you and recede when there isn't** — and here the artifact existed. It was the audit you'd just completed.

---

## What this changes in your Braze position

| Your current position | What the transcript says | Revision |
|---|---|---|
| *"Blocked on two data points owned by Martech"* | Both were open in the room; neither was assigned; Alejandro left mid-thread | **Not blocked on Martech's answer — blocked on nobody having stated the apps requirement.** Send it in writing. |
| *"We init on login so we don't inflate MAU"* | Init is on app open by default; `changeUser` is the login method; delay is a customisation, undecided | **Correct this before repeating it to David.** And argue that apps and web need different policies. |
| *"MartechKit vs direct integration"* | Martech's stated preference is server-to-server via Amplitude to avoid per-app SDK work; Robert pushed back that SDK uplift is small | **Strengthens the direct-integration call.** If events go server-side, apps only need init + `changeUser` + push. That's small, and MartechKit is off the critical path. |
| *"Braze order: TraceCheck → Apollo → Faxer"* | Confirmed, and **web-first is deliberate** — apps are last by design | **This buys you time.** Apps isn't next. Use it to settle identity rather than to defer it. |
| *"Andrey attends the vendor calls"* | Correct, and he's now a named blueprint reviewer alongside you | Fine — but the blueprint is a deliverable with your name on it and no date. |

---

## Action items

| # | Action | Owner | When | Notes |
|---|--------|-------|------|-------|
| 1 | **Write the apps identity position to Alejandro + Vlad Moskalets:** RevenueCat `originalAppUserID` is the canonical apps identity; state it as a constraint on the portfolio external ID | **You** | **before Friday** | Two paragraphs. This is the whole "blocked on Martech" problem. |
| 2 | State the **apps initialisation position** — init on open, `changeUser` at login; web's MAU logic shouldn't bind apps | **You** | before the SDK session | Otherwise decided without you |
| 3 | **Scope and date the apps section of the blueprint** — or hand it to Andrey explicitly with a return date | **You** | before Friday | Currently accepted, unscoped, and you're out for two weeks |
| 4 | Check what **RevenueCat actually emits** — custom/purchase events vs Braze e-commerce recommended events | Apps | post-holiday | Robert flagged; unassigned |
| 5 | Flag the **`changeUser` / shared-device** correctness trap | You / Vlad Krut | post-holiday | No logout concept; profile keeps accumulating |
| 6 | Decide **Currents destination** — Amplitude vs Databricks | Alejandro | Robert confirming contract | One connection only |
| 7 | Note the **Currents-before-history** sequencing constraint in the blueprint | You / Alejandro | with blueprint | Non-retrospective |
| 8 | Decide the **archival policy** for long-tail install bases | Apps | post-holiday | `do_not_archive` is the lever |
| 9 | Get Robert's **updated rate-limit slide**; confirm dev/QA traffic won't consume production allowance | Vlad Moskalets | promised | Robert acknowledged the slide was incomplete |
| 10 | ExpertSender + OneSignal historical migration path | Robert | promised | No direct connector expected |

---

## Flags

1. **The Aug 4 API session isn't in Granola.** Either it wasn't captured or the note hasn't synced. If you want it analysed, check Granola synced it — and note the SDK session (Thu 14:30) is the one where initialisation timing gets decided. **That's the meeting where the apps position has to be stated, and you're there.**
2. **Heitor is driving the strategic frame and it's a good one.** Amplitude-as-baseline, unified approach, sequenced learning. He is the person whose thinking is shaping this. Worth aligning with directly rather than through the blueprint.
3. **Vlad Moskalets is chairing Braze for the portfolio** and is doing it well — he raised MAU cost, the multi-platform identity case, and the governance question. He is the counterpart you actually need on the two data points, more than Alejandro.
4. **Apps has no named technical owner in this workstream** other than you and Andrey — and Andrey is solo on TraceCheck for two weeks under a *fix bugs only* brief.
5. **The blueprint is the artifact everything routes through.** You perform when there's an artifact. This is one, it's yours, and it currently has no date.

---

> **Bottom line.** The meeting went well and the plan is sound — web-first sequencing, Amplitude as the baseline, a single governing blueprint. Nothing here is broken. What's missing is apps, and specifically you: the one open question the room couldn't close is the one you've spent three weeks answering. Forty seconds would have put it on the table. **It's still available in writing, and you have until Friday.**
