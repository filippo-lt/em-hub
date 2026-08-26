# Coaching plan — Vlad: closed loop → technical leverage

**Opened:** 2026-08-24 · **Last updated:** 2026-08-24 (post-1:1) · **Review:** Dec 2026
**Visual version:** https://claude.ai/code/artifact/fc7066c5-f86b-4882-9e4f-ac5c73c69b04

---

## The reframe

Filippo's starting description was "arrogance toward other developers." That word still doesn't fit — **zero complaints, zero incidents**, and in the 24 Aug 1:1 Vlad was careful and generous about an engineer whose work he couldn't evaluate. Against a profile documenting a standing bias to *under-trust* Vlad (anchored March 2026, one recorded wrong read on 8 May), reaching for a character label would be a mistake.

But the **behaviour** got much better evidenced on 24 Aug — see E4 and E5. The diagnosis sharpened rather than softened: **the pattern is not disdain for other engineers, it is an inability to route work through them.** Coach the routing. Never coach the disdain — it isn't there.

**So the plan coaches the capability, not the trait:**

> ~~You come across as arrogant to other developers.~~
> → **You're a closed loop. Everything goes in and comes out through you. That's a ceiling, and you're leaning toward the track where it binds hardest.**

Same behaviour, same intervention. One is a verdict he can only accept or reject; the other is a gap he can close.

---

## Evidence held (all already in em-hub notes)

| | What | Source | Weight |
|---|---|---|---|
| **E1** | Victor's explanations *"very broad — sometimes barely touch the information I was looking for"*; did **not** feel he needed more from him | 20 Jul memory | **Strongest.** Note records knowledge transfer happened "on Vlad's terms and stayed shallow" — reinforced the SDK bus-factor + outdated-docs gap. The only item with a recorded downstream consequence |
| **E2** | Over-called five audit items later rejected by consensus, against a Staff Engineer's code | 28 Jul memory (Filippo's own review note, **not** Vlad's words) | Calibration, not malice. A second reader catches all five. He didn't use one |
| **E3** | Doesn't like being the smartest in the room — *"it gives me ego problems"* | 20 Jul memory | The original entry point. He named the discomfort first. ⚠️ **Not transcript-verbatim** — the note mixes his words with Filippo's conjugation. Paraphrase it back, don't quote it |
| **E4** | *"I contacted him and I offered the help and he accepted my help. **So I finished the pull request, basically.**"* — on Damien's TikTok fix. Asked if the contribution was valuable: *"It's like, yes"*, then ~90 seconds re-explaining his own work before landing on "yes, it was valuable" | 24 Aug transcript, narrated unprompted | 🔴 **STRONGEST.** This week, named engineer, his own account. Damien found and fixed the bug correctly — Vlad said so. What Vlad did was take over its *delivery*. The option that never appeared in his account, or Filippo's, was **leave the PR with Damien and review him through the extra work** |
| **E5** | *"I keep it in the repo as well. It's not been held and protected… if you ask AI to debug a very specific issue, it will go and read through sources and will find possible root causes."* | 24 Aug transcript, answering "centralise or spread?" | **The loop describing itself.** Translation: *the knowledge is available to anyone as good at extracting it as I am.* Sincere, not defensive — he genuinely isn't hoarding. He can't see the difference between *documented somewhere* and *transferred to someone* |

**Counter-evidence, kept deliberately in view:** in the same meeting Vlad's read on Viacheslav (Android, work he can't easily evaluate) was careful and generous — *"I think this list is honest… every single item needs to be run through a non-biased agent asked to verify."* And on the Martech contract: *"let's make it look like it was their decision and not ours"* — political sophistication, not arrogance.

---

## Phases

**Phase 0 — Seed · 24 Aug · ✅ done, differently**
Filippo didn't use the July opener. Off the back of the ATT deep-dive he asked *"should this knowledge be centralised in one or two people, or should we spread it?"* — the same thread, arrived at from the work rather than from a feedback frame. **Better than the planned opener.** Vlad answered with E5. Filippo accepted it and pivoted to "let's write a simple document", stopping one question short.

⚠️ **Do not count this as delivered.** A thread was opened and closed. Phase 1 still has to happen — but it now has much stronger material to open with.

**Phase 1 — Get his self-diagnosis first · weeks of 31 Aug & 7 Sep**
One 20-minute conversation, he talks more than Filippo. Test whether the read survives contact with his.
- **Open with this, not the July quote:** *"If Damien had to debug an attribution bug next week without you — would he get there?"* Concrete, unarguable, drawn from a PR he worked on this week. He'll answer honestly.
- Then: name the last three times another engineer changed his mind technically. If he can't reach three, that *is* the conversation.
- Give **E4** as a system observation, not a fault: *"you finished Damien's PR yourself. What would it have taken to have him finish it instead — and was that worth the extra week?"* E1 (Victor) is the backup if he waves E4 off.
- Name the track: at senior+ technical, the measure stops being the quality of his answers and becomes the quality of everyone's around him.
- **Contract it.** If he says no, that's a different and more useful problem.

**Phase 2 — Change the environment, not the person · Sep–Oct**
The five moves below. Sequence: **M1 first** — it's the only one he genuinely can't self-serve past on the timeline. Don't announce them as coaching; they're the work.

**Phase 3 — Close the loop with real signal · Oct–Nov**
- Ask Andre, Dmitri, Damien one narrow question each: *"how easy is it to change Vlad's mind?"* — never "is Vlad arrogant", never sourced back to him.
- Score the measures against baseline.
- One piece of specific evidenced feedback — by now a progress update on something he agreed to, not a surprise.

**Phase 4 — Fold into the ladder · Dec**
He froze the career conversation in July pending the rephrased path. When it reopens, this is already part of it, not a new complaint bolted on. **If he's moved, say so and stop coaching it** — unended coaching becomes nagging.

---

## The five structural moves

| # | Move | Why it works on this trait |
|---|---|---|
| **M1** | **Make Dmitri his Android route.** Run the Vlad ↔ Dmitri intro — **still open as of 24 Aug**, carried since July. (Confirm what Dmitri actually owns first — notes only say "Android parity") | He said "I need to learn a bit about how Android works" and reflexively designs iOS-only. **The one domain where self-serving isn't available on the timeline.** The environment does the work |
| **M2** | 🔴 **Give Damien a call that actually wins — now the most urgent move.** Filippo promised twice on 24 Aug to "find a way" to get Damien's time, with no mechanism. This *is* the mechanism: name one area where Damien's judgement is final | E4 happened this week. Right now other engineers are *pre-shrunk* around Vlad — Filippo himself scoped Damien as "feedback voice, not architecture decision-maker". If nobody outside ever holds authority, the closed loop is structurally correct behaviour, not a flaw. Vlad's own words: *"I don't really see how you get more of his time without him actually doing stuff"* — he can't picture the mode, so design it for him |
| **M3** | **No solo audits.** Any register or audit gets a named second reader before it circulates. Applies to Filippo too | Directly fixes E2. All five over-calls are what a second reader catches in 20 minutes. As craft policy it costs no ego to accept |
| **M4** | **Score his integration guide by adoption.** Success = another dev integrates without asking Vlad a question | Moves "done" from *my work is correct* to *someone else succeeded*. Cheapest possible rehearsal of leverage, on work he already owns |
| **M5** | **Make him teach how he works with AI.** One session for the other devs — prompting, review discipline, where he does and doesn't trust the output | Don't hang this on the AI-SE pilot; **that plan is parked.** Hang it on the fact that he's the strongest AI-assisted engineer in the group and nobody can copy him. Forces him to meet other engineers at their level, and converts "smartest in the room" from private discomfort into public asset |

---

## Measures (set baseline Sep, re-score Nov)

- Does he cite another engineer's input in a design decision? — *baseline ~0 · target ≥2/month unprompted*
- Does he route others toward help or absorb it? — *baseline Jul: declined a PO hand-off ("I can share it") · target: connects people to the right owner*
- Over-call rate on his next written audit — *baseline Jul: 5 rejected · target ≤1, with a named second reader*
- Did he learn Android **through** Dmitri or around him? — *baseline Jul: planned to self-serve · target: can name what Dmitri taught him*
- Did his integration guide unblock someone without him? — *baseline Aug: two guides, both outdated · target: one clean integration, zero questions*
- Peer read Oct (Andre/Dmitri/Damien): "how easy is it to change Vlad's mind?"

---

## Four ways this goes wrong

1. **You might still be wrong about the size of it.** E4 and E5 made the *behaviour* solid — but zero complaints and zero incidents still means nobody has been hurt by it. Coach it as a capability ceiling, never as a problem others are suffering. Say "I might be wrong about this" out loud in Phase 1; it costs nothing and it's true. Phase 3 peer data settles it.
2. **The under-trust bias is the loudest thing in the room.** Documented since May with one recorded misread. "He's arrogant" is exactly the shape of errors already made about this person. Before each session: what did he *do*, versus what did I infer?
3. **The social cost is real, not a preference.** He left the Developer Advisor role in three days because interaction demands were unsustainable. Never prescribe *more* interaction — prescribe *higher-yield* interaction and cut something else to pay for it. **Keep his meeting count flat or falling throughout.** Getting this wrong doesn't give a slightly worse outcome; it gives the March flameout again.
4. **Don't run this during a crunch.** If Phase 1 collides with a delivery fire, delay it. A coaching thread opened under pressure reads as blame for the pressure.

**🛑 Kill switch.** If by end of Phase 1 his self-read shows genuine awareness and no peer reports friction — **stop, and write down that you stopped.** His Viacheslav read on 24 Aug is exactly the kind of signal that should make you consider pulling it. Coaching a trait nobody has experienced is how a good manager turns a strong engineer into a defensive one. This plan needs an exit that isn't "he improved."

---

## Not on 24 Aug (kept for the Phase 1 conversation)

- ✕ Don't use "arrogant", "ego", "how you come across" — except paraphrasing his own July line.
- ✕ Don't deliver the audit-citation feedback. Audit landed 28 Jul, four weeks ago, first conversation since. Retire it as standalone feedback; it survives as E2 inside the real conversation later.
- ✕ Don't stack it on the status update. Status first, seed last, five minutes.
- ✕ Don't let him agree too fast. "Yeah you're right" in the first minute means he's managing you.

**One sentence:** coach him from the smartest person in the room to the person who makes the room smarter — because he's leaning technical-track and this is its actual ceiling, not because anybody complained. Nobody has.
