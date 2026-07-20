# Martech SDK — Strategy Brainstorm Notes

**Date:** 2026-06-25
**Owner:** Filippo (EM, pushing this as leverage)
**Goal:** Enter Q3 with a clear strategy to present to David — action points, roadmap, stakeholders.

---

## What I know (from context load)

- **Initiative:** Shared between Engineering and Martech. Horizontal priority (David endorses it explicitly).
- **Tech lead:** Victor Jalencas (Staff Eng, 50% capacity). Thorough, humble, politically conscientious. Owns the build. Splits time with M&A app work.
- **State (2026-06-25):**
  - iOS: ready, deployed in a few apps.
  - Android: integrated in one app (iMote), PR open, merging soon.
  - Flutter: next in line — approach TBD, Victor wants David Catalá (Catalá) confirmation.
- **SDK wraps:** RevenueCat, Amplitude, AppsFlyer (init + ID syncing).
- **Resourcing:** Plan to add Vlad (direct report) at 25% to help Victor. David has *approved Vlad going horizontal*.
- **OKR tie-in:** Q2 O1/KR6 = "MartechKit v1 delivered with 4 app integrations." This is a measured OKR.

## Open threads to resolve

1. **Roadmap** — issue #38 (rosseca/martech-kit). Long Martech-requested roadmap Victor needs to triage for feasibility/impact. Open questions on attribution + how Martech wants data organised.
2. **Vlad onboarding** — 25% to support Victor. Constraint: social interaction draining → async-first, minimal meetings. Reliable solo delivery. What's his lane?
3. **Quality gates** — raised today with David + EMs. Need gates for deploying new SDK versions. (What triggered it? TBD.)
4. **Engineering Dashboard** — David wants visibility: where MartechKit / Parapet / Pipelins are integrated, what state, which apps, which version. Idea: spin up as an engineering dashboard initiative.

## Stakeholders (draft)

- **David** (CTO, my manager) — sponsor; wants horizontal integration + visibility; values structured options + recommendation.
- **Victor Jalencas** — tech lead, 50%.
- **Vlad Krudek** — incoming 25% support, my report.
- **David Catalá** — Flutter; Victor wants him looped/confirmed.
- **Martech team** — the demand side / roadmap requesters. (Who specifically? TBD.)
- **Mateo** — possible iOS Martech roadmap owner (to confirm).
- App teams consuming the SDK (iMote, etc.).

## Decisions captured (2026-06-25)

- **Deliverable:** Core Martech SDK strategy doc + the Engineering Dashboard pitched as a SEPARATE standalone initiative.
- **Dashboard ambition:** Undecided — explore both (lightweight tracker vs built platform).
- **Quality gates:** Proactive / scaling risk (no incident yet; getting ahead of fan-out blast radius).
- **My leverage:** Promo / visibility — build a visible cross-cutting win demonstrating staff-level org impact.
- **Vlad's lane:** App integrations + new features (NOTE tension with his async/minimal-meeting constraint — see Pillar 2).
- **Martech demand side:** Diffuse / unclear — no single accountable counterpart. A gap I need to fix.

---

## THE REFRAME (central insight)

These are not 4 separate open points. They are 4 symptoms of ONE thing:

> **The Martech SDK has graduated from a *project* to a *platform* — but has none of a platform's operating model.**

| Symptom | Missing platform discipline |
|---|---|
| Quality gates needed | No versioning/release contract with consumers |
| Diffuse Martech demand | No demand owner / product counterpart |
| David wants a dashboard | No consumer/version visibility |
| Victor 50% + Vlad 25% ad hoc | No staffing/ownership model |

**Q3 strategy = "establish the platform operating model for Martech SDK."** Stronger, more promotable narrative than "keep building the SDK." This is the leverage you sensed.

---

## FOUR PILLARS — exploration

### Pillar 1 — Roadmap (#38)
- Triage #38 into Now/Next/Later by **feasibility × Martech impact**.
- Core tension: **breadth** (more platforms: Flutter → RN/web?) vs **depth** (more SDKs wrapped, better attribution, data organisation).
- Risk: #38 is a Martech wishlist. With no demand owner, Victor triages alone → you inherit scope with no prioritisation authority. Ties to Pillar 2.
- BLOCKER: couldn't read #38 (private repo, GitHub connector not authed). Pull via connector or paste.

### Pillar 2 — Resourcing
- **Victor 50% (shared w/ M&A) = the single biggest risk, and it's NOT on your open list.** The whole platform sits on one Staff Eng at half-time across 3 platforms + gates + dashboard. Bus factor = 1. Name this to David.
- Vlad 25% on app integrations + new features. **Tension:** his constraint is async/minimal-meeting, but in-app integration = coordinating with app teams (high interaction). Better fit: net-new SDK feature modules / core (solo work); let Victor or app-team devs do the in-app handshake. (Defend this.)
- Second-order: Vlad on Martech reduces Face AI / AI-SE evidence time → check vs Q2 evidence plan + David's Phase-2 narrative. Price the trade-off.
- 0.75 FTE does not cover 3 platforms + gates + dashboard. Either narrow scope OR get capacity. This is your **ask-with-a-date** to David (fixes your fold-on-resource-asks pattern).

### Pillar 3 — Quality gates (proactive)
- Framing: **fan-out blast radius** — 1 bad version × N apps = N incidents. As N grows, gate value compounds.
- Gate ladder (light → strict): semver + changelog → automated test suite per platform → CI on PR → canary app before broad rollout → integration smoke tests in consumers → release checklist/sign-off → deprecation policy.
- Sells to David: protects O2 (predictability) + "stability / no public failures."
- Owner: Vlad is the natural fit (self-contained) but you've slotted him on integrations — so Victor defines, automation shared. Name the owner.

### Pillar 4 — Engineering Dashboard (separate pitch)
- David named 3 libs: **MartechKit + Parapet + Pipelins** → the dashboard is inherently a *platform-visibility layer*, broader than Martech. That's why it's a separate initiative.
- **Fork A — Lightweight tracker:** matrix of library × app × version × integration-state × health. Source: parse repos (Podfile.lock, gradle, pubspec) + registry file. Days of work. Could be a script in scripts/delivery or a Cowork artifact. Satisfies David's exact ask now.
- **Fork B — Built platform/service:** live dashboard, version-drift alerts, ownership, health. Weeks+, needs owner + roadmap. Bigger promo, competes with SDK delivery.
- **Recommendation: A now, B as the pitch.** Ship the tracker in 1–2 weeks → bring David the *working tool*, not a proposal (fixes your "built but not presented" pattern). Use it as the wedge to pitch B as a named initiative.

---

## STAKEHOLDER MAP

| Stakeholder | Role | What they want | My move |
|---|---|---|---|
| **David** (CTO) | Sponsor | Visibility, horizontal integration, no surprises | Bring artifact not objection; use the moment to close H2 scope conditions |
| **Victor Jalencas** | Tech lead, 50% | Catalá looped on Flutter; clear Martech requirements | Protect his focus; don't let him become sole product owner |
| **Vlad Krudek** | Incoming 25%, my report | Solo, async work; AI-SE evidence | Match work to constraint; price the Face-AI trade-off |
| **David Catalá** | Flutter | Not be blindsided | Flutter confirmation gate before that workstream |
| **Martech team** | Demand side | Their roadmap delivered | Establish ONE accountable counterpart/sponsor |
| **Mateo** (?) | Poss. Martech roadmap owner | TBC | Confirm if he's the counterpart |
| **Peer EMs** | Raised gates collectively | Shared standards | Align so gates aren't "Filippo imposing" |

---

## BLIND SPOTS / ASSUMPTIONS TO CHECK

1. You framed 4 separate points — it's one platform-maturity story. (the reframe)
2. Vlad on integrations conflicts with his interaction constraint — re-examine the lane.
3. **Victor at 50% is the biggest risk and isn't on your list.** Bus factor = 1.
4. "Promo via visibility" works only if you own the *narrative/operating model*, not the *code*. Lean platform-owner, not IC.
5. Diffuse Martech demand → you silently absorb product-owner work unless you name a counterpart now.
6. Dashboard (3 libs) quietly expands you beyond Martech. Good for promo — but price it with David (your silent-scope-absorption pattern).

---

## SUGGESTED COURSE OF ACTION

**Primary path:** Frame Q3 as *"Martech SDK → Platform operating model."* Four workstreams, each with an owner + date. Ship the lightweight dashboard as the visible wedge. Use the David presentation to: (a) name Victor's capacity risk, (b) propose dashboard-as-initiative, (c) close the open H2 scope conditions (Flutter, Victor cadence, Mobile SE backfill).

---

## ISSUE #38 — TRIAGE (pulled 2026-06-25)

**Authors:** MiguelAlvarezLT + david-leadtech (Martech side) — Victor (envictor) responding. NOT diffuse: Miguel + David(leadtech) ARE the demand side.

**Origin = a real production incident, not proactive.** VideoUp v2.9.0 (1 Jun 2026) set `customerUserID` AFTER `start()` → ~8k installs/day with NULL `customer_user_id` → broke AF↔RC↔Amplitude joins → hit Meta W2A conversion scoring. Hotfix v2.9.1. Root cause: hand-rolled AF bootstrap in app code, one line moved in a refactor. **The quality-gate conversation traces back to this.**

### The roadmap is 3 streams, not a feature list

**P0 — Enforcement & Adoption (do first; this IS the quality-gate pillar)**
- Migrate apps off hand-rolled AF init → MartechKit (VideoUp + Photo/Video portfolio first)
- MartechKit CI: `swift test` blocks merges (contract tests `AppsFlyerStartupTests` already exist — low effort, high value)
- Per-app CI gate: fail build on manual `AppsFlyerLib...start()` / `.customerUserID =` (Victor: doable as SPM build plugin, SwiftLint-style — prevents accidents not malice)
- Codemagic pre-submit gate (block App Store upload on manual bootstrap)
- Data alert: NULL `customer_user_id` rate spike (would've caught VideoUp in hours)
- Mandatory Martech review on attribution PRs (interim, until migration done)
- **Portfolio migration tracker: "app × MartechKit status" (item 9) + adoption KPI (item 13) ← THIS IS DAVID'S DASHBOARD**

**P1 — New SDK surface (breadth; after enforcement)**
- Amplitude V2 customData: CUID + AmplitudeDeviceId + AmplitudeSessionId before AF start. Swift draft exists = PR #15; must replicate Kotlin + Flutter.
- AppsFlyer uninstall measurement (`af_uninstall`) — portfolio-level capability
- `MartechKitAdMob` v1: mediation bootstrap + ad-revenue fan-out to AF + placement constants + adapter matrix + CI gate

**P2 — More identity bridges / cleanup**
- Firebase App Instance ID → Amplitude user property (MT-573)
- Firebase Analytics/Crashlytics identity, `MartechKitOneSignal`, `MartechKitMessaging`
- Deprecate per-app `Core*` modules (ereasy `CoreAppsflyer` has the same antipattern as VideoUp)

**Cross-cutting rule (explicit in #38):** every contract must land Swift + Kotlin + Flutter — don't ship one-platform and call it done.

### Strategic shifts from #38

1. **Quality gates = roadmap P0.** They're not a separate pillar — they ARE the top of the roadmap. Four pillars collapse to three: Adoption+Enforcement / New surface / Dashboard, with Resourcing cross-cutting.
2. **"Flutter next" is misaligned with Martech's priority.** Their P0 is migrate + enforce existing (mostly iOS) apps. Building Flutter breadth on an unenforced, barely-adopted foundation is the wrong sequence. Re-sequence: enforcement first.
3. **Gates are incident-driven (VideoUp), not proactive.** Stronger pitch to David — he hates exec-visible failures; this already cost Meta conversion accuracy.
4. **Demand side isn't diffuse** — it's Miguel Alvarez + david-leadtech. The real gap is *prioritization authority + throughput*: they file faster than 0.75 FTE delivers, with no agreed priority order.
5. **Dashboard is double-demanded** — CTO David (visibility) AND Martech (migration tracker, item 9 + adoption KPI item 13). Ship lightweight tracker first; it's the highest-ROI wedge and now serves two stakeholders.
6. **ADOPTION DISCREPANCY to verify:** Miguel's iOS audit says "no app has adopted MartechKit yet"; you said iOS is deployed in a few apps. Likely different portfolios (Martech/Photo-Video vertical vs your Mobile App Unit). Reconcile before quoting status to David.
7. **Open PR #15** = Swift reference for Amplitude V2 customData. Linked Jira: ACANDMAU-1673, ACIOSMAU-2003, MT-573.

## ADOPTION RECONCILED (2026-06-25) — and the scope boundary it reveals

**Filippo's Mobile App Unit — MartechKit adopters (the well-behaved reference apps):**
- Tattooist iOS ✅
- FaceAI iOS ✅
- ScreenMirroring iOS ✅
- iMote Android (PR open) ⏳
- AI Design iOS → planned via Vlad (onboarding integration)

**Martech / Photo-Video vertical (Miguel's audit) — ZERO adopted, still hand-rolled:**
- VideoUp (the incident), Step Counter, ai-cleaner, ereasy, … → all own `CoreAppsflyer`/`AppDelegate+Attribution`.

> **The VideoUp incident happened in apps Filippo does NOT own.** His unit is the *clean adopter*; the un-migrated mess is the other vertical.

### Strategic implication — THE SCOPE BOUNDARY (make explicit with David)
Two very different jobs are hiding inside "push MartechKit":
- **What Filippo OWNS:** the SDK platform + his unit's integrations (already done well) + the gates/tooling/dashboard (the rails).
- **What Filippo ENABLES but must NOT absorb:** migrating *other teams'* apps off hand-rolled bootstrap. He provides the CI-gate script, integration guide, and tracker; those teams do the migration work.

If this boundary isn't named, Victor's 0.75 FTE silently inherits company-wide migration. Name it: *"We build and enforce the rails; each app team walks its own app across."* (Directly counters Filippo's silent-scope-absorption pattern with David.)

### Bonus: OKR KR6 is essentially MET
KR6 = "MartechKit v1 + 4 app integrations." Tattooist + FaceAI + ScreenMirroring (iOS) + iMote (Android, on merge) = **4**. AI Design via Vlad = a 5th. → Lead the David pitch and brag-doc with "KR6 delivered," then pivot to the enforcement/platform ask from a position of strength.

### Vlad → AI Design integration (updates my earlier pushback)
- My earlier concern (integrations = high cross-team interaction) is **largely neutralised**: AI Design is *his own app*, so it's solo + async — fits his constraint. Good call.
- Doubles as: onboarding to the library + a 5th reference integration + a fresh test of the integration guide and CI gate.
- **Synergy worth naming:** AI Design's portfolio tier hinges on **CAC** (kill trigger, 30 Sept). MartechKit gives cleaner attribution → better CAC data on the exact app whose fate depends on CAC. The learning task also sharpens the kill decision.
- **Caveat:** AI Design is proposed *Wind-down*. Investing integration effort in a wind-down app is fine *as a learning vehicle* (low stakes, he knows the codebase) — just don't let it grow into a feature roadmap for a dying app.

## AI DESIGN re-tiered to INVEST (2026-06-25)
- AI Design moved out of Wind-down → **Invest**. Removes my earlier "don't over-invest in a dying app" caveat entirely.
- Now a genuine strategic integration, not just a learning vehicle: an Invest app *should* have first-class attribution. MartechKit gives clean CAC/LTV on an app you're now pouring fuel into.
- NOTE: this contradicts `context/app-portfolio-framework.md` appendix (AI Design = "Wind-down with kill trigger, externals exit 30 Sept"). That doc needs updating + likely a brag/visibility moment (you changed an app's fate with data). Flag separately.

## JIRA AS THE PLATFORM TRACKER (2026-06-25)

**Decision:** Treat MartechKit as a platform → give it a Jira home. Serves (a) roadmap-by-priority, (b) visibility to David + Martech.

### Existing Jira landscape
- Per-app projects: ADIOSMAU, TTIOSMAU, FAIOSMAU, SMIOSMAU, IMANDMAU/IMIOSMAU (from config/projects.conf).
- Martech-owned: **MT** (Martech MAU), **MTGF** (MarTech Globeful), **MCS**. MT-573 lives in MT.
- **No dedicated SDK-platform project exists.**

### Recommendation — give MartechKit its OWN project (e.g. key `MTK`)
- **Why not put it in MT (Martech MAU):** MT is *Martech-owned*. Hosting the engineering platform roadmap there silently signals Martech owns the SDK — the opposite of the scope boundary you're trying to set. Where the work lives = who owns it.
- A dedicated Eng-owned project reinforces "Eng builds & owns the rails," gives David + Martech one board/roadmap to watch, and keeps app-migration work (in each app's own project) separate from platform work.
- **Caveat:** creating a Jira *project* needs admin rights — not doable via the issue API; likely a request to David/Jira admin. I can draft every epic/story now and bulk-create the instant the project exists.

### Jira ≠ the Dashboard — two layers, both needed
| | **Jira (MTK)** | **Adoption Dashboard** |
|---|---|---|
| Answers | "What are we building, in what priority?" | "Which app is on which version, adopted y/n?" |
| Layer | Work-in-flight / roadmap | State-of-the-world / adoption |
| Audience pull | Martech (roadmap), David (roadmap) | David (visibility), Martech (migration tracker #38 item 9) |
| Source | Human-maintained issues | Auto-parsed from repos/manifests |

> Don't let Jira convince David the dashboard is redundant. Jira shows *intent*; the dashboard shows *reality*. The VideoUp incident was a *reality* gap (an app silently on hand-rolled bootstrap) — Jira would never have surfaced it.

### Proposed MTK structure
- **Epics = the 3 streams:** `P0 Enforcement & Adoption`, `P1 New SDK Surface`, `P2 Identity Bridges & Cleanup`.
- **Stories = #38 items**, each linked back to GH #38 + the VideoUp incident for context. Miguel already offered to split P0 into tracked issues — converge that here.
- **Labels:** `platform:ios|android|flutter` (enforce the cross-platform contract rule), `requester:martech|eng`, `incident:videoup`.
- **Priority field** = the actual prioritisation ritual artifact with Miguel + david-leadtech (fixes the "they file faster than we deliver, no agreed order" gap).
- **A roadmap/timeline view** on MTK = what you literally show David and Martech.

## QUALITY-GATE DESIGN (2026-06-25)

### Core principle (from #38 + Victor)
**Make the wrong thing impossible, not just discouraged.** "Extra care in review is not a scalable fix." Move enforcement from human (mandatory review) → automated (CI/data). Mandatory Martech review is the *interim* gate only, until automation lands. Victor's caveat: a library can't veto app-level runtime behaviour — so it's **defense-in-depth**, not one silver bullet.

### Two failure surfaces (need different gates)
1. **SDK-side regression** — a new MartechKit version itself ships a bug → breaks ALL consumers (fan-out blast radius). *This is your original "gates for deploying new versions" ask.*
2. **App-side misuse** — an app reintroduces manual identity wiring / integrates wrong (the VideoUp case: CUID after `start()`).

### Layered gates (author-time → production)
| # | Layer / when | Gate | Catches | Owner | Priority |
|---|---|---|---|---|---|
| 1 | Design-time | Contract lives **only** in the kit (already true) | App can't break what it can't implement | Victor | Foundation ✓ |
| 2 | Kit merge | `swift test` **blocks merge** (today CI only verifies commits) | SDK regressions | Victor | **NOW** (low effort, you own it) |
| 3 | Release | Semver + changelog + **canary app** before broad rollout; deprecation policy | Bad version fanning out | Victor / you | NEXT |
| 4 | App build | CI fails on manual AF wiring (`rg` grep → later SPM build plugin) | Reintroduced manual bootstrap | App teams (your shared script) | **NOW** → rollout as apps migrate |
| 5 | Pre-submit | Codemagic blocks store upload on manual bootstrap | Last line before users | App teams | NEXT |
| 6 | Production | **NULL `customer_user_id` rate alert** + structured bootstrap logging | EVERYTHING, incl. unknown failure modes, in hours | Data / Martech | **NOW** (highest ROI safety net) |

> VideoUp shipped ~8k bad installs/day because **none of layers 2–6 existed for it** (it wasn't even on the kit). The single highest-ROI gate is **#6, the data alert** — it would have caught VideoUp in hours regardless of cause. Cheapest prevention gate is **#2**. Start with those two.

### Design tensions / decisions you own
1. **Prevention vs detection** — you can't fully prevent app misuse (Victor). Need both: shift-left checks lower probability, data alert lowers blast-radius duration. Don't pick one.
2. **Gate ownership & politics** — layers 4 & 5 touch *other teams'* CI pipelines → can't impose. Ties to the scope boundary: you ship the shared gate script + guide; each team adopts it. Layers 2, 3, 6 you (mostly) control.
3. **Who owns the data alert (#6)?** It needs BigQuery / AppsFlyer data access. Likely Martech or a data team, not Victor. Name the owner or it won't get built — and it's your most valuable gate.
4. **Cross-platform parity** — every gate must exist for iOS + Android + Flutter, or you get the exact drift #38 warns about (Swift fixed, Kotlin/Flutter still broken).

### Recommended MVP gate set (don't boil the ocean)
1. `swift test` blocks merges on MartechKit (#2) — Victor, days.
2. NULL-rate data alert (#6) — secure the data owner; the safety net that catches the unknowns.
3. Shared `verify-no-manual-martech.sh` CI script (#4) — adopted per app as it migrates.
Then layer in release canary (#3) and Codemagic pre-submit (#5).

## ACTIVE CONTRACT VERIFIER — idea (2026-06-25)

Upgrade of gate #6: instead of only alerting on NULL `customer_user_id` rate, a script **queries Amplitude + AppsFlyer + RevenueCat APIs and asserts the identity contract holds end-to-end** for the common workflow (install → first event → subscriber).

### What each API gives you
- **RevenueCat** — `GET /v1/subscribers/{app_user_id}` (secret key). Returns subscriber attributes incl. reserved `$appsflyerId`, `$amplitudeDeviceId`, `$amplitudeUserId`. → assert they're set and correct.
- **AppsFlyer** — Raw-data / Pull API (installs + in-app events reports). Rows carry `customer_user_id`, `appsflyer_id`, and customData columns (amplitude device/session id). → assert `customer_user_id` non-null and == RC app_user_id; customData populated.
- **Amplitude** — User Profile / User Activity API (key+secret). Fetch by device_id/user_id; confirm the user exists, has events, and IDs cross-reference.

### The assertions (the "most common workflow")
1. `RC.app_user_id == AF.customer_user_id`
2. `AF.customData.amplitude_device_id == Amplitude.device_id`
3. `Amplitude.device_id == RC.$amplitudeDeviceId`
4. `RC.$appsflyerId == AF.appsflyer_id`
If any fail → the joins are broken (the VideoUp class), surfaced automatically.

### Two modes
- **Reactive scan** (population): periodically sample recent real installs, compute broken-join / NULL rate. Catches real breakage, no test app needed.
- **Synthetic probe** (proactive): drive a known QA/sandbox `app_user_id` through a TestFlight/staging install, then query all three for that one user. Cleaner, controlled, runs post-release. **Recommended first build** — checking one known user across 3 APIs is far simpler than scanning the population.

### Honest caveats
- **Latency:** AppsFlyer raw data + Amplitude ingestion lag minutes→hours. So this is **monitoring / post-release check, not a PR merge gate.** RC is near-real-time.
- **Scope:** validates the *identity contract*, not business correctness of every event. Keep it to the contract that broke.
- **Access = the dependency:** needs RC secret key + AppsFlyer API token + Amplitude key/secret. These sit with **Martech / data**, not Victor. Same owner question as gate #6 — this reinforces "name the data owner."
- **Per-platform parity:** the QA user must be reproducible on iOS + Android (+ Flutter).

### Why this matters strategically
This is the promo-grade piece: novel, cross-cutting platform tooling that makes "quality" *demonstrable* (David can see a green/red contract check), feeds the **dashboard's health column**, and converts gate #6 from passive to active. Highest-signal thing in the whole gate design.

## ENGINEERING DASHBOARD — brainstorm (2026-06-25)

Vision expanded: not just MartechKit adoption → a **full Engineering Dashboard**: state of all apps/projects (what's integrated + how it's performing), **editable by all EMs**, start small and build on top.

### THE REFRAME — this is your App Portfolio Framework made LIVE
`context/app-portfolio-framework.md` already defines rows (apps) × columns (cost, revenue, health, tier, kill triggers) + a 2×2 + tiers + cadence. **The dashboard is that framework turned into a tool.** You already authored the data model. Consequence: one tool serves three audiences at once —
- **Martech** → integration/adoption columns (#38 migration tracker)
- **David** → per-app cost/value/tier (the goalkeeper cockpit)
- **All EMs** → shared app status of record

### CENTRAL DESIGN PRINCIPLE — sourced vs declared
Every column is either:
- **Auto-sourced** (from systems: repos/manifests, Jira, GitHub, Datadog, GCP, RC/AF/Amplitude) — objective, can't be faked, **stays fresh on its own**.
- **Human-entered** (EM-editable: tier, stage, notes; or PM-supplied: MRR, CAC) — subjective, needs an owner to keep current.

> Keep these visibly separate. Dashboards die when (a) data is manual and goes stale, or (b) they duplicate Jira. The fix is: **maximise auto-sourced, minimise human-entered, and make only genuinely EM-owned fields editable** (tier/status/notes — never things derivable from a system).

### Build ladder (start small → build on top)
- **v0 — Integration matrix (auto).** App × {MartechKit, Parapet, Pipelins} version + adoption + contract-verifier health. Parsed from repos. Zero human input. Already double-demanded (David + Martech). **This is the MartechKit tracker = the seed of the whole dashboard.**
- **v1 — Add auto performance/cost columns.** Crash-free rate (Datadog), cycle time / on-time (Jira+GitHub — you have `/metrics`, roadmap-status), GCP € (you have `/gcp-spend`). Aggregate existing sources; don't re-derive.
- **v2 — EM-editable layer (multi-tenant).** Each EM owns + edits their rows: tier, roadmap stage, health flag, notes. Needs shared persistence + ownership boundaries.
- **v3 — Real internal service.** DB, auth, ingestion jobs, PM/marketing data via David's air cover. The "build on top" endgame.

### Build-vs-assemble options
- **Spreadsheet / Airtable / Notion** — fastest multi-EM editing, weak at auto-parsing integrations. Good for the human layer.
- **Cowork artifact / thin web app** — auto-pulls from connectors on load (GitHub/Jira/Datadog), good for v0–v1; multi-EM editing needs shared persistence (localStorage won't cut it).
- **Internal service** — v3 endgame.
- Likely path: a script generates the **auto** matrix (v0) + a lightweight editable surface for the **human** layer; converge later.

### Blind spots / cautions
1. **Scope creep / it competes with the SDK.** "Full org dashboard, all EMs edit" = building an org-wide internal product on top of Victor-at-50% + a Q3 SDK roadmap. **Don't let the dashboard eat the SDK.** Resource it explicitly (could be a Vlad / intern / separate slice — not Victor).
2. **Schema politics.** Getting all EMs to agree column shape is political, not technical. You'll be the de-facto owner — good for promo, but it's real ongoing load. Decide if you want that hat.
3. **Don't rebuild BI you already have.** Perf may be in Datadog, cost in Tableau/GCP, delivery in Jira. Dashboard should **index/summarise/link**, not become a second data warehouse.
4. **Inherits the framework's PM-data dependency.** Value columns (MRR/CAC) need PM data → David's air cover (already an open ask in the portfolio framework). Eng columns you can fill today; PM ones you can't.
5. **Staleness = death.** The more auto-sourced, the longer it lives. Treat manual columns as a liability to minimise.

### Strategic read
Strongest promo vehicle of all the threads: owning the **engineering org's single pane of glass** is unambiguously cross-cutting, staff/lead-level visible work, and David is a ready sponsor (it's his goalkeeper cockpit). BUT it's also the biggest scope + maintenance trap. Play: **ship v0 (the MartechKit matrix) as the wedge** — it's cheap, double-demanded, and proves the pattern — then pitch the org dashboard as a *named, resourced initiative*, not something smuggled onto Victor's plate.

## ACTION POINTS (draft, to refine)

1. Authenticate GitHub connector → pull & triage #38 into Now/Next/Later. (Me/Victor)
2. Define Vlad's lane precisely + check against Face-AI evidence plan. (Me)
3. Draft quality-gate ladder v1; pick an owner. (Victor + Vlad)
4. Build lightweight dashboard tracker v1 (3 libs × apps × version × state). (Me/Vlad)
5. Identify & secure a single Martech demand counterpart. (Me)
6. Confirm Flutter approach with Catalá. (Victor)
7. Package: Q3 strategy doc + separate dashboard pitch for David; name Victor capacity + H2 conditions. (Me)

---
