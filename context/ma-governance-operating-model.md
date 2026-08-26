# M&A Governance Operating Model — v1

**Owner:** Filippo (EM, Mobile App Unit)
**Author date:** 2026-06-07
**Status:** Draft — for Q3. Operationalises the App Portfolio Framework for the M&A apps.
**Relation to other docs:**
- Parent framework: `context/app-portfolio-framework.md` (the 2×2, tiers, cadence)
- Portfolio state: `config/ma-apps.conf` (the live app list — posture, studio, source ids; see `config/ma-apps.conf.example`). `context/m-and-a-status.md` is now a June-2026 historical record, not the live list.
- Live heartbeat: `templates/ma-portfolio-tracker.md` (one row per app — the monthly review)
- Per-app decision doc: `templates/app-scorecard-template.md`
- Per-app technical evidence: `templates/ma-app-technical-scorecard.md`

**Shared decision vocabulary (all artifacts speak these four verbs):**
**Govern-in-place** (studio delivers, we govern) · **Remediate** (time-boxed internal SE fix) · **Rebuild** (greenfield/new-app track, internal SE) · **Sunset** (wind down). Posture = where an app sits now; a scorecard recommends a move between them.

**Artifact flow:** Tracker (always) → app flags 🔴 or hits a trigger date → refresh its Scorecard to make the call → if Remediate/Rebuild/takeover is on the table, run the Technical Audit for evidence → decision logged → tracker row updates. Govern-in-place apps mostly just live in the tracker.

---

## The problem this solves

David asked me to *establish control* over the M&A mess but has not funded *takeover* of the apps (ChatUltra externals delayed ~1 month). Those are two different things, and collapsing them is the trap — it leaves me with responsibility and no authority.

**The resolution:** separate **control** from **takeover**.

- **Control** = visibility, gates, decision rhythm. The goalkeeper role David already gave me (12 May). Deliverable now, with **zero new resources**.
- **Takeover** = moving an app's execution onto our resources. A funded decision, *gated* on business case + resourcing per the portfolio framework.

I govern all 5 apps from week one. I take over execution only when an app is resourced and scored worth it. Until then, an app runs on its current studio and I own its *governance*, not its *delivery*.

---

## Operating principle

> I govern apps I don't develop through **gates, visibility, and decision rhythm — not code.** Control is owning the points where money, releases, and commitments get decided. This is the standard external-studio vendor-governance model.

Operational footprint: **~3 hours/week of manager work** — one spreadsheet, one automated release check, two studio calls, a monthly slot with David, and a few one-page decision memos. No code. It is *my* work, not Andrey's or Vlad's — it does not consume their delivery capacity.

---

## Roles & accountability boundary

- **I own the PM relationship.** I am the single integration point between Product (direction, business case, revenue data) and Engineering (studios, delivery, quality). I source revenue/usage data myself — no air-cover dependency.
- **I report to David / give him visibility.** He does not run the relationships; he gets the state of things and backs escalation.
- **Product owns the kill/continue decision.** I supply the engineering evidence and recommendation. (Forcing mechanism in Phase 5 so Product indecision doesn't become my cost.)

**Boundary — to be stated in writing:**
> "I own M&A governance — visibility, tiers, gates, decisions, studio relationships and the PM interface. I do **not** own delivery on apps I am not resourced to develop. I am accountable for governance, not for delivery on unfunded apps."

If this line isn't explicit and on the record, it silently blurs into "Filippo owns M&A outcomes" — the trap reasserting itself.

---

## The phases

### Phase 0 — Access (foundation)

Cannot govern what I can't see. Per app, get **read** access to: repo (`github.com/rosseca/...`), Amplitude (usage), RevenueCat (revenue/MRR), Firebase/Crashlytics (crashes), App Store Connect / Play Console (the store), AI cost dashboards, CI/CD status.

**Action:** in the `M&A Apps Tech Overview` sheet, add a "Access? Y/N" column. The N's are the **week-one ask to David — logins, not headcount.**

### Phase 1 — Tracker (the heartbeat)

One row per app in the **Portfolio Tracker** (`templates/ma-portfolio-tracker.md`; live [Google Sheet](https://docs.google.com/spreadsheets/d/1edO2XOHpxBTTqRDk9tfjegO0sZ485O4q0XORSbg4prE/edit), build source `context/app-portfolio/ma-portfolio-tracker.xlsx`) — the column spec and automation notes live there, not duplicated here. I touch only the judgment fields (Posture, Studio, Release health, Next decision, Flag), which rarely change.

**Single source of truth = History.** The Tracker is a live snapshot; behind it sits an append-only **History** sheet — one row per app per weekly run. The numeric columns (Cost, MRR, MAU, crash-free %) *derive* their latest value from History, so I only ever append; the snapshot updates itself. Cadence: **capture weekly, review monthly.** Evolution surfaces three ways — Δ arrows on the snapshot, a Trends chart sheet, and threshold evidence ("3 of last 5 failed") for the QA wedge and the Phase-5 memo. Build sequence: v1 validate columns → v1.5 History + derived snapshot + deltas + charts (current, on sample data) → v2 automate the weekly append.

**Star metric: crash-free %.** Objective, automatable, the exact thing the studios fail at. Triple duty — health (tracker), release gate (Phase 2), QA evidence (QA Tier 3).

### Phase 2 — Release control (automated, exception-based)

**Do not watch PRs.** That's reviewing their development — wrong altitude, no time, not my code. Govern the **release event**, not the code. Two pieces:

1. **Awareness (passive):** notification when a build hits the store or a release tag is cut → posts to `#ma-releases`. I don't watch; it pings me.
2. **The gate (automated, not human):** a release must clear an automated floor before shipping —
   - crash-free % above threshold
   - **smoke test: app launches without crashing** (catches "crashes on open" — the studios' worst failure)
   - secret scan (GitHub secret scanning — no hardcoded keys)
   - consent/CMP present

   Green posts ✅ automatically. **I only look when it's red.** That's the answer to "I don't have time" — exception-based, not review-based.

The automated floor *is* the gate, and (see QA) it's also the politically bulletproof thin end of the quality mandate.

**The floor is infrastructure, not a tracker column.** A blocking gate is always green by definition — anything that fails never ships — so mirroring it in the tracker carries zero information. The tracker's **Release health** column instead measures what the gate is blind to: **delivery autonomy** — how cleanly the studio got live. 🟢 shipped clean & alone · 🟡 friction / multiple attempts · 🔴 needed heavy help. Fed by CI gate-bounce count (objective, keeps the political shield) + the studio-call help read (subjective). This is the leading indicator of studio health and the Helikanon concentration risk — a studio that needs heavy help on every release is a hidden takeover cost made visible.

### Phase 3 — Studio calls (relationship + intel)

Two 30-min biweekly calls (Helikanon — 4/5 apps; TurboCat — PDF). Fixed agenda: what shipped, what's next 2 weeks, blockers, this period's crash/cost numbers. Running notes doc.

**Framing (political):** *not* oversight — that trips the "we're independent" defense. Frame as **value to them**: one point of contact company-side, faster unblocking, fewer conflicting asks. Make them want the call → control without a mandate fight.

**The advantage I extract:**
- **Intel** — what is Product asking them *directly*, around me? (I own the PM interface; a studio tasked behind me is a leak to catch.)
- **Early risk signal** — what's fragile, what's about to slip.
- **Relationship capital** — a person to call for an urgent fix, not a ticket.
- **Concentration read** — is Helikanon a genuine single point of failure across its 4 apps? Name it on the scorecard as a tracked risk with a "what if they walk" note.

> Open: the specific politics around the two studios still need mapping to sharpen the call shape.

### Phase 4 — Monthly review with David

30 min inside the existing 1:1. Screen-share the scorecard; per app: cost, revenue, tier, recommendation. He says yes/no; I log decisions.

Purpose: **inform + bank air cover for enforcement.** When a studio repeatedly fails the quality floor, the monthly review is where David has already seen the pattern — so escalation isn't a surprise and carries his weight.

### Phase 5 — Decision log (Product decides, I supply evidence)

Half-page memo per change, engineering data → recommendation. Product owns the call. **Forcing mechanism so Product indecision doesn't become my cost:**

> "Engineering recommends [sunset / remediate / maintain] based on [crash-free %, MRR trend, cost]. **Requesting Product decision by [date]. Absent a decision by then, default is wind-down to maintenance-only.**"

Converts non-decision into a decision, and puts me on record: if Product keeps a crashing app alive against the evidence, that's documented as their call. (Same principle as the SE role: where Product won't direct in time, engineering acts to keep things moving — applied at portfolio level.)

---

## QA — the teeth of the model

QA is **not a separate phase — it's the enforcement layer of Phase 2.** A release gate with no quality bar behind it is theater. Current state: no real internal QA team; 2hr/week exploratory session per app; bugs reported but no "seal" — blocked politically ("studios are independent"). Reality: studios ship apps that crash on open.

Mandate quality **without winning the independence fight head-on**, in three tiers, leading with the one politics can't touch:

**Tier 1 — Automated floor (no humans, no politics).** Crash-free threshold + launches-without-crashing smoke test + secret scan + consent present. Objective, so the independence argument can't apply — there's no human judgment to resent. "Independent" ≠ "allowed to ship a build that crashes on open"; that's a defect, not a quality opinion. **This is the wedge.**

**Tier 2 — Repurpose the 2hr/week exploratory session.** Change the *output*: instead of a bug list into a void, produce a go / critical-issues signal on the app's core journeys, landing on the scorecard. Same 2 hours → documented quality state instead of ignored bugs.

**Tier 3 — Formal QA sign-off mandate (the contested one).** Don't fight for this first. Build Tier 1 + 2, accumulate data ("3 of last 5 Helikanon releases failed the floor; here's the crash spike and revenue dip"), then the mandate proposes itself — independence can't be defended against evidence of crashes hitting revenue. **Evidence-first, mandate-second.**

**Resourcing:** automation carries the floor (scales without headcount); spend scarce human QA only where automation can't reach (UX, critical journeys). Don't ask for QA headcount up front — prove the floor catches the worst, then the headcount ask is evidence-backed.

---

## What governance produces across the 5 apps (zero new resource)

Governance doesn't just hold the line — it **shrinks the problem**, which is the real answer to resource starvation.

| App | Action via governance | Resource need |
|---|---|---|
| **ChatUltra** (P1, acceptable, revenue) | Govern in place — Helikanon develops; I own scorecard + release/audit gate + standing "fund takeover when ready" proposal | None |
| **PDF Editor** (P2, bad codebase, GDPR) | Business-case-by-hard-date gate; TurboCat minimal maintenance until then; sunset if no case | None |
| **Step Counter** (P2, Android native) | Score → likely Maintain; low touch | None |
| **Truth Seeker** (P3, Apple-blocked, pre-launch) | Drive **sunset** — easiest kill (no users to lose) | None |
| **Music Player** (P3, sunset candidate) | Execute **sunset**; reclaim capacity | None |

5 apps I'm "not resourced to own" → 2–3 that actually matter. David's ChatUltra delay matters far less once Truth Seeker and Music Player are dead and PDF is gated.

---

## The resource reframe

Stop asking David for externals (expensive, keeps getting denied). Governance needs only the **cheap things he can't reasonably refuse**:

1. **Access** — the logins from Phase 0.
2. **Data** — since I own the PM relationship, I gather MRR/MAU/CAC myself; no air-cover ask needed.

Walk into the Friday 1:1 asking for *logins*, not headcount → likely a yes, which finally breaks the month-long stall.

---

## Week-one stand-up sequence

- **Mon** — Build the access checklist from the inventory sheet; fire off login requests. Drop the two studio calls + the monthly David scorecard slot on the calendar.
- **Tue–Wed** — Write the one-page release-floor checklist; post the "no release without ✅" rule to the studios. Draft the Music Player + Truth Seeker sunset memos (the two easy wins — portfolio drops 5→3 in week one).
- **Thu** — First Helikanon call. Pull whatever metrics I already have access to into the scorecard.
- **Fri** — Bring David two things: the two sunset memos to sign, and the one ask — **logins/access** (not externals).

By Friday: two apps on the path to dead, three visible and gated, studios know there's a sign-off rule, David has signed actual decisions. That's control — built with meetings and a spreadsheet, not resources.

---

## Risks / what could break

- **Governance without teeth → accountant.** Every scorecard row must terminate in a decision right, not a description. The gates are what make it control.
- **Accountability boundary stays verbal → blurs into "owns M&A outcomes."** Get it in writing (see Roles).
- **Helikanon concentration (4/5).** Governing in place means depending on one studio. Track as a named risk with a "what if they walk" contingency; don't fix now, don't be surprised later.
- **Product won't decide.** The Phase 5 default-action mechanism is the mitigation.
- **The independence-politics fight on QA.** Mitigated by leading with the objective Tier 1 floor and deferring the Tier 3 mandate until evidence forces it.
- **Personal failure mode:** building this and under-presenting it / chasing moving goalposts instead of forcing one decision. Antidote: engineer the evidence (the scorecard + crash data), then the asks write themselves. Bring the artifact to the room.
