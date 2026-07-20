# M&A Transition-Readiness Checklist

**Owner:** Filippo · **Created:** 2026-07-03
**Purpose:** One repeatable checklist to make every M&A app safe to keep, park, or wind down — before the studios (Helikanon, TurboCat) exit end-July. Complements the `M&A – Apps Tech Overview` sheet and the per-app scorecards; this is the *transition* layer, not the tech audit.

> The exit deadline is the forcing function. The single biggest risk isn't the code — it's **credentials and knowledge walking out the door with the studios.** Everything below is organised so nothing critical leaves un-transferred.

---

## 1. Disposition map

| App | Platform | Studio | Disposition | Governance posture (4-verb) | Transition mode |
|-----|----------|--------|-------------|------------------------------|-----------------|
| **ChatUltra** | Flutter (+Python BE) | Helikanon | **KEEP** (critical path) | **Govern-in-place** (new studio + Vlad lead) | Handover → new external team + Vlad lead |
| **Truth Seeker** | Flutter → **web** | Internal | **KEEP (web)** | **Rebuild** (greenfield web, internal SE) | Native = dead; internal (Andrey + Oscar QA) |
| **PDF Editor** | Flutter | TurboCat | **PARK** (after July ad fix) | **Sunset** (default; revive → Govern-in-place) | Freeze + minimal maintenance |
| **Step Counter** | Android native | Helikanon | **PARK / HOLD** | **Govern-in-place** (low-touch; gate → Sunset) | Minor fixes → hold, gated on ad-model |
| **Screen Mirroring** | (existing unit) | — | **PARK** | **Govern-in-place** (paused, internal) | Andrey resumes when marketing frees |
| **Music Player** | Android native | Helikanon | **WIND-DOWN** | **Sunset** | Effectively dead (~2–3 mo untouched) |

Three modes, three depths of checklist: **KEEP** = full handover; **PARK** = freeze safely + revive criteria; **WIND-DOWN** = capture, secure, and let die.

### Disposition vocabulary — reconciled with the governance model

The transition modes above (**KEEP / PARK / WIND-DOWN**) are **not** the same axis as the governance operating model's four verbs (**Govern-in-place / Remediate / Rebuild / Sunset**). They answer different questions, and both are needed:

- **Transition mode** = *what happens to the app through the studio exit* — the exit-window action.
- **Governance posture** = *how we own and deliver the app afterward* — the four-verb vocabulary the rest of the M&A system speaks (see `context/ma-governance-operating-model.md`).

The mapping is deliberately **not 1:1** — the same mode can land in different postures:

| Transition mode | Lands in posture(s) | Apps |
|-----------------|---------------------|------|
| **KEEP** | **Govern-in-place** *or* **Rebuild** | ChatUltra → Govern-in-place; Truth Seeker → Rebuild |
| **PARK** | **Govern-in-place (held)** *or* **Sunset** — *deferred*; a revive/kill trigger decides | Step Counter, Screen Mirroring → Govern-in-place; PDF Editor → Sunset (default) |
| **WIND-DOWN** | **Sunset** | Music Player |

Two notes: **Remediate** currently holds no app — it stays available for a KEEP app that needs a time-boxed internal SE fix instead of external delivery. And **PARK maps to a *deferred* posture**: the table shows the default trajectory, but the revive trigger flips it up and the release gate can drop it to Sunset (§H owns those triggers).

---

## 2. The checklist (apply per app)

### A. Disposition & decision
- [ ] Disposition confirmed with a named decision-maker and date
- [ ] Review/revive date set (for Park) or sunset date (for Wind-down)
- [ ] Written and shared with Product (no verbal-only dispositions)

### B. People & knowledge *(the exit-critical section)*
- [ ] Exiting studio devs named, with last working day **and access-revocation date** (the two often differ — the access date is the real risk trigger; ties to §D/§4)
- [ ] New owner named (internal dev / external team / advisor) — or explicitly "no owner while parked"
- [ ] **KT / handover overlap** booked (paid window; who ↔ who; what artifacts)
- [ ] Architecture note + build/release runbook captured *from the exiting devs* (not reconstructed later)
- [ ] "How to build, sign, and ship" documented for each platform
- [ ] List of tribal-knowledge landmines captured (the "only X knows this" items)

### C. Code & repos
- [ ] Full repos list recorded
- [ ] Tech stack + platforms recorded per app (iOS / Android / Backend / Web; framework — Flutter vs native; key third-party SDKs)
- [ ] Repo ownership/admin transferred off studio accounts
- [ ] Build state green or known-red per platform (BE / Android / iOS / Web) — link the scorecard row

### D. Credentials, keys & secrets *(rotate before access is revoked)*
- [ ] Signing certs / keystores located and re-owned; App Store + Play Console access transferred
- [ ] Third-party keys inventoried: AppsFlyer, RevenueCat, Amplitude, Firebase, Crashlytics, Superwall
- [ ] **Secrets committed to git identified and ROTATED** (see §4 — ChatUltra & PDF Editor both flagged)
- [ ] Cloud project ownership (GCP / GAE / Cloud Run) + billing re-assigned off studio
- [ ] Service accounts / API keys rotated at the access-revocation date (from §B — not necessarily the last working day)

### E. CI/CD & infrastructure
- [ ] CI/CD pipelines owned by an internal account; a non-studio person can run a build
- [ ] Backend hosting owner + cost owner named (esp. ChatUltra Python services)
- [ ] Domains / DNS ownership confirmed (esp. Truth Seeker web)

### F. Product & roadmap
- [ ] PO / PM owner named
- [ ] Roadmap state: committed work vs frozen, written down
- [ ] Marketing / UA status: running, paused, or gated (PDF ads; Step Counter ad-model)

### G. Monitoring, support & incidents
- [ ] Crash reporting + attribution health owner named
- [ ] Who responds to a P1 while the app is parked — named, with expected response time / hours of coverage, or explicitly "no coverage"
- [ ] Support/escalation path after the studio is gone

### H. Revive / sunset criteria
- [ ] **Park:** the trigger that reactivates it, the trigger that kills it, and who decides
- [ ] Explicit "transition complete" definition **per app** — Keep = owner live + KT done; Park = frozen safely + revive criteria set; Wind-down = captured, secured, sunset dated
- [ ] Store presence + data retention while parked (keep listing / pull / delete) decided

---

## 3. Per-app readiness matrix

| Dimension | ChatUltra (KEEP) | Truth Seeker (KEEP-web) | PDF Editor (PARK) | Step Counter (PARK) | Screen Mirroring (PARK) | Music Player (WIND-DOWN) |
|-----------|------------------|-------------------------|-------------------|---------------------|-------------------------|--------------------------|
| **Posture (4-verb)** | Govern-in-place | Rebuild | Sunset (default) | Govern-in-place (low-touch) | Govern-in-place (paused) | Sunset |
| Exiting devs | Helikanon (held for KT) | — (internal) | Maxim Panasenko, Valeriy Knyazev | Helikanon (Mesut, Serkan?) | — | Helikanon |
| New owner | New external team + **Vlad lead** | Andrey (+ Oscar QA) | none (parked) | none | Andrey (later) | none |
| KT overlap | **Required — protect paid window** | n/a | short/none | short | n/a | capture-then-cut |
| Keys to rotate | **3 Firebase svc-acct keys in git** | unknown — audit | **2 hardcoded prod API keys** | unknown — audit | unknown — audit | unknown — audit |
| Hosting/BE | Python svcs on GAE/Cloud Run | web hosting TBD | — | — | — | — |
| PO / roadmap | Ruben (preferred, open) | internal | frozen after ad fix | gated on ad-model | frozen | none |
| Revive / kill | "transition complete" = team live + KT done | web release ~early Aug | revive if marketing #s justify | gated on ad-model decision | when marketing frees | sunset candidate |

`unknown` = needs a repo/inventory audit before the studio leaves. Fill from the `M&A – Apps Tech Overview` sheet.

---

## 4. Critical path — do these BEFORE the studios lose access (end-July)

1. **Rotate the committed secrets now, not at handover.** ChatUltra has **3 Firebase service-account private keys committed in git** across BE repos; PDF Editor has **2 hardcoded prod API keys** + user files uploading to public hosts. The moment studio access is revoked those credentials are compromised-by-default — rotate and re-own them while the exiting devs can still help identify every place they're used.
2. **Confirm the named exit scope** (Mesut Güngör, Serkan Dağlıoğlu on Helikanon's on-hold apps) *before* anyone is pulled — your explicit lever.
3. **Lock the ChatUltra KT overlap.** Sergio's email reframed the fallback as "pause or alternatives"; protect a short paid Helikanon handover so a revenue app isn't cut cold.
4. **Capture knowledge from every exiting dev** (architecture + build/release runbook) — this is the one thing that can't be redone after they're gone.
5. **Transfer repo, store, cloud, and pipeline ownership** off studio accounts for all six apps.

---

## 5. How to use this
Run §2 per app, fastest-decaying items first (People, then Credentials). The KEEP apps need all eight sections; PARK apps need A, B, C, D, G, H; WIND-DOWN needs B (capture), D (secure), H (sunset). Walk Product through §3 + §4 to align on ownership and timeline.
