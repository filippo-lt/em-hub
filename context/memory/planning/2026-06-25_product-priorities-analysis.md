# Analysis — Product priorities & roadmap churn

**Source:** Bi-Weekly Managers Apps Sync, 2026-06-25 (Granola transcript)
**Present:** Filippo, Andre Montenegro, David Matellano, David Català (Dcatala), Aramos, Yuri
**Type:** Pattern analysis — keep for the families/roadmap discussion in Q3

## What this was really about
On the surface, "priorities keep changing." The substance: **David Matellano** advancing a
diagnosis and a structural fix, while the other managers supply evidence the current model is
broken. Three managers describing the same disease from different apps.

## The evidence on the table
- **Andre (photo/video family):** video web handed to him by Jorge & Dmitro as *the* highest
  priority ("deliver by July") — then he realises the following Tuesday they hadn't even pitched
  it to Christian yet. Something is labelled "top priority" before the decider knows it exists.
- **Filippo (me):** last week's launches changes only partly matched the morning 1:1 — video
  priority and removing the EDC website lined up, but "easy web" appeared from outside my scope,
  and the one-product-at-a-time agreement has quietly become 3–4 products.
- **David Català:** sharpest case. Translator Go Android was top priority because Christian asked,
  then paused since Friday pending a marketing "is it worth it" check — after ~3–4 weeks of dev.
  Same on Fax: launched Android, then campaigns paused on a budget cut. Calls Translator "the
  worst app in the portfolio" business-wise; marketing doesn't know how to sell it.

## David Matellano's core insight (strong — adopt the language)
Reframes the problem economically: **changes are free.** Free for the PMs (no investment to
define them) and free for the POs. When a change costs the requester nothing, you get an
unbounded number of them. The written roadmap's value isn't planning per se — it's that it
**imposes a cost on changing your mind**: "if I have something written I can fight the changes;
if not, I can't."

## Second mechanism: the broken feedback loop
The churn is a ~5-day latency loop. A priority is set, the PM talks to peers and Christian over
days, and by the time it loops back it has changed (Mon "web is #1" → Thu not anymore).
Filippo's ask to product was the right lever: **shorten the loop** — "don't go five days without
talking to Christian."
- Variant raised by **Filippo**: the Sergio↔Christian relay mismatch — they met and aligned in
  person, but what Sergio relayed afterward wasn't what was agreed with Christian. David
  Matellano's honest take: "that's how startups work, I don't know how to solve it." He thinks the
  information-fidelity problem is partly unfixable; the change-frequency problem is the one he's
  attacking.

## The proposed fix: families + written bi-weekly + strict ranking
- **Families model (David Matellano's structural bet):** collapse many app-level conversations
  into one PM per family as single point of contact. Clean accountability chain: PO follows PM,
  PM follows Christian. Photo/video family already operates at this maturity (existence proof).
- **Bi-weekly written confirmation:** the cost-imposing ritual — "still the priorities? changing?"
- **Strict ranking (no two apps at the same priority):** removes the hiding place where
  everything is "high."
- **"This company moves by written"** — people change their minds, forget, get messy; the doc is
  the anchor.

## Where the tension is (unresolved — keep honest)
- **David Català's pushback:** the 3-month roadmap they *did* run produced no measurable revenue
  impact, at least on his apps. David Matellano half-conceded: "you're right, but at least we had
  a process to develop and deliver — right now we have neither impact nor process."
- So the honest framing: families/written-cadence buys **predictability and reduced thrash, not
  necessarily revenue.** Hold the team to that distinction so "the roadmap didn't work" doesn't
  get re-litigated in six months.

## Tooling: keep it dumb
- **Andre:** resisted Jira/epics — "I want one-two-three-four-five, the things that cannot fail";
  a slide is fine.
- **David Matellano:** "we're not even mature enough for spreadsheets, let alone Jira."
- Both land on light-weight. The failure is the conversation layer, not the tool — a ranked slide
  reviewed on a cadence is the minimum viable artifact. Reaching for heavier tooling would treat
  the symptom.

## Risks to watch
- **No owner, no date on the families rollout** — "I'll start with families in Q3" is aspiration.
- **The escalation chat (David Matellano + Christian + PM) is masking the problem** — a lifesaver
  but not scalable; danger is it works just well enough that the structural fix never gets built.
- **Christian is the single point of failure in both models** — families reorganises inputs but
  doesn't fix the output gate if his availability is the real bottleneck.
- **Mini-product sprawl** (video captions, PDF merges, web screenshots) compounds the ranking
  surface — discipline must land *before* the catalogue explodes.

## Net read
The diagnosis (changes are free) and the loop-latency observation are genuinely strong — adopt
the language. The families + written-cadence fix is reasonable and the right weight of tool. The
thing to keep honest is David Català's gap: process predictability ≠ revenue impact, and the last
roadmap proved it. If backing families, back it as a **thrash-reduction mechanism with a named
owner and a date**, not as a revenue lever.
