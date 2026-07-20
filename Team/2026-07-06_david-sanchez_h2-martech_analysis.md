# Analysis — Filippo / David, H2 Martech (2026-07-06)

> **Scope note:** This is an M&A / Martech conversation, outside the "EM Hub / Team" project scope. Analysis produced on request; nothing written to team people-memory.

## TL;DR

Filippo opened with a proactive win (adding a second person to Martech Kit mid-month, two roadmaps + Jira board coming next week). David reframed the whole thing: **the Martech SDK is one tile in a much bigger H2 "governance" play** he wants to sell to Christian & Matellano. The real subtext of the meeting was David building his **resourcing case** — a solution architect, a clear Durban decision, and dedicated DevOps — using Signal Beacon's revenue impact ($18M processed, ~$4M/yr recovered to networks) as proof that Martech is a technical team, not "marketing guys." Filippo agreed with the direction, pushed back on vanity metrics and on the "one week a month architect" idea (says it needs someone **full-time**), and parked the web-SDK question until the app version lands.

## The two agendas in the room

```
FILIPPO's agenda                          DAVID's agenda
────────────────                          ──────────────
Unblock Martech SDK velocity        →     Reframe SDK as part of H2 governance
 • +1 person from mid-month               Build the resourcing business case
 • daily 15-min standups w/ Victor    →    • Solution architect (staff-level)
 • 2 roadmaps + Jira, ready next wk        • Durban: official % or cut him
 • most-revenue apps first                 • Dedicated DevOps (w/ Julian)
Get more authority over Victor        →    Split team: Specialists vs Engineers
 (report-line change w/ Matellano)         Sell "we ARE a technical team" upward
```

They are **aligned on direction**, but Filippo is solving a delivery problem this quarter while David is solving an org/mandate problem for H2. That gap is the thing to watch.

## Key decisions & positions

- **Martech SDK will land in all apps by end of year** (Filippo's commitment). Delivery is ~3 months behind — he expected it done by now.
- **Roadmap next week**: two timelines — (1) the SDK itself (Android + Flutter versions + additions), (2) integration into apps, sequenced highest-revenue → long tail.
- **Victor's ceiling**: Filippo is clear — Victor is right for the *mobile stack* (incl. PM'ing the Martech Kit), **not** for web / governance / architecture. Agreed by both.
- **Report lines**: Filippo & Victor are currently *peers*; Filippo is working with Matellano to gain leverage. Called out as a real blocker.
- **David's team re-org**: moving from **platform-based** split (web/app) to **role-based**: *Martech Specialists* (business-facing) vs *Martech Engineers* (infra-facing). Rationale: web & app work now bleed into each other.
- **Web SDK / governance**: **parked** by Filippo until the app version is done. David confirmed web is a "yes" long-term — but it's *governance on GCP*, not just an SDK.
- **Vanity metrics**: Filippo flagged PR count & LoC as bad metrics; David agreed and is moving to a **revenue-forward** metric (with Miguel, no figures yet).

## David's ask of Filippo (the only concrete action for you)

> "Define the scope of what Martech looks like over the next 6 months — on apps: how many apps, the ambition, who does what (Victor vs the new joiner), and how they split."

Everything else David is driving himself (the resourcing conversations with Christian/Matellano).

## Team model David is proposing

```
                        MARTECH TEAM (H2)
        ┌──────────────────────┴──────────────────────┐
   MARTECH SPECIALISTS                          MARTECH ENGINEERS
   (business-facing)                            (infra-facing)
   • sit with product / mktg / CRO              • data team / tech / devops
   • first line on attribution                  • GCP projects, ETL pipelines
     discrepancies (Amplitude vs network)       • OAuth → SSO for RevenueCat
   • web + landing, Flutter, governance         • own the "how", must review/merge
   • prompt & request changes;                  • Miguel, Alexandr(a)...
     NOT required to understand internals
        └──────────────── two parallel tracks ─────────┘
             aligned to company tracks · shared: tracking,
             attribution, post-conversion send-back, governance
                    + observability/alerts (biggest gap)
```

## The business case David is building (his leverage upward)

- **$18M processed** through the tool; **~500k lines of code**, ~305k (≈60%) owned by *non-developers* — by mid-March, commit ownership flipped to non-IT.
- **~$4M/yr recovered to networks** from two Signal Beacon features:
  - Web→app click-ID recovery (AppsFlyer gap): ~600k signals sent back → run-rate proxy **$1.15M**, est. **$2.3M** in extra revenue routed to networks.
  - Web-attribution click recovery (Durban-drafted): **$1.7M/yr**.
- **How they ship without traditional devs**: Cursor scans the codebase every Monday (critical bugs, RBAC, SQL-injection), dependabots bump versions, 6–7 CI tests per PR (code quality, conventional-commit, CRM impact, terraform), auto-release + UI release layer, Confluence architecture hub (not yet automated). Google's own team told them Signal Beacon could be sold **B2B**.

## The resourcing asks (what he wants from Christian/Matellano)

1. **Solution architect** (staff-level, not a full staff engineer in his framing) — to call infra shots (Cloud SQL vs datastore, etc.) *before* they build each new tool. Rationale: having Durban early is exactly why Signal Beacon got this far. **Filippo disagrees on sizing** → says the moving-parts count means **full-time**, not "one week a month."
2. **A clear Durban decision** — official % (50 / 30 / 0). Current on/off gives the team "false hope" of becoming Durban. If no Durban, he'd hire an architect from market and keep Durban as backup.
3. **Dedicated DevOps** (working with Julian) rather than depending on central DevOps that lacks capacity.
- Headwind: company is in **cost-reduction mode**; he'll wait until Christian is back from summer and lead with the "we behave as a technical team" evidence.

## Risks & watch-items

- **Delivery vs mandate mismatch**: Filippo's fix (one of his engineers, temporarily) is explicitly *not permanent*. David is planning as if Martech is becoming a standing technical org. If Filippo's person is pulled after unblocking, the SDK integration could stall again.
- **Single-person knowledge risk**: "very few people know everything Martech-related." Durban is a bus factor; David himself flags the team is chasing "become Durban."
- **Report-line ambiguity (Victor)**: until resolved with Matellano, Filippo has limited ability to enforce priority.
- **AppsFlyer monopoly**: mobile "signal independence" depends on replacing AppsFlyer, whose investors include Google/Meta/Unity — David admits this will be "a nightmare." App-to-app / web-to-app send-back is blocked on it.
- **"Signature" decision-making**: David's own concern (Kubernetes-vs-Cloud-Run example) — people making architecture choices to leave a mark. Filippo agreed to steer away from that; relevant when the architect is hired.
- **Apps' brownfield base**: Filippo was blunt — apps can't replicate Signal Beacon's AI-driven workflow because the code is bad and untested; every push breaks something. This is the root of the "can't give Martech push permission" friction. **Thursday EM + Matellano meeting** is meant to resolve it.

## Open questions to close

1. Who is the second engineer joining Martech Kit mid-month, and for how long?
2. Firm answer on Durban's allocation — does Filippo have any say / dependency here?
3. Does the Thursday EM meeting unblock Martech's push permissions on apps?
4. Web governance-on-GCP plan from Google/Durban — get the doc David offered to send.

## Suggested next steps for Filippo

- Deliver the **two roadmaps + Jira board** next week (committed).
- Write the **6-month Martech app scope** David asked for: app count, ambition, Victor vs new-joiner split — this is the one deliverable he's owed.
- Land the **report-line change** with Matellano before over-committing Victor.
- Grab David's **all-flows diagram** and web-governance-on-GCP doc (you said you want to show the flow diagram to your team).
- Keep the **web SDK parked** but on the radar for the *next* conversation.
