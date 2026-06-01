# MartechKit Presentation — Talking Points

> Duration: ~15-20 min + Q&A
> Audience: Mixed — POs, PMs, product leadership + SEs, EMs, Staff Engineer, Technical Director
> Presenters: **Filippo (EM)** — high-level / strategy · **Victor Jalencas (Staff Engineer)** — technical
> Split: Filippo slides 1-4 + 9-10 · Victor slides 5-8 · Handoffs at 4→5 and 8→9

---

## Key Messages to Land

1. **We integrate the same Martech tools 10 times** — Amplitude, RevenueCat, AppsFlyer re-wired from scratch in every app. (Filippo)
2. **The cost is in the data and the speed** — mis-tracked events break cross-app analysis; Martech waits on per-app engineering. (Filippo)
3. **One library, single point of implementation** — vendors live behind MartechKit; changes ship as a version bump. (Filippo)
4. **It's a facade, not a rewrite** — one clean app-facing API; vendor specifics hidden inside. (Victor)
5. **The shared event dictionary is the real unlock** — same events, same schema, everywhere → trustworthy cross-app analytics. (Victor)
6. **It's live and validated** — iOS v1.0 running, proven in 3 pilot apps. (Victor)
7. **Clear road to full coverage** — iOS rollout now, Android + Flutter in parallel. (Filippo)
8. **Part of one shared-components platform** — alongside Parapet, AI Gateway, TVFoundationSDK. Repeatable pattern, not a one-off. (Filippo)

---

## Presenter Split & Handoffs

- **Filippo opens** (slides 1-4): frame the problem, the cost, and the strategic shift.
- **Handoff 4→5:** "That's the why and the what. Victor built this end-to-end — he'll take you through how it actually works."
- **Victor** (slides 5-8): the facade, the event dictionary, integration model, and live status / pilots.
- **Handoff 8→9:** "That's where the technology stands today. Filippo will take you through where it goes from here."
- **Filippo closes** (slides 9-10): roadmap to full coverage, platform context, credit to Victor, Q&A.

---

## Audience-Specific Angles

### For POs / PMs
- Every app will track the **same events the same way** — cross-app product analysis finally becomes reliable
- Martech experiments stop waiting on **per-app engineering tickets**
- New vendor or new tracked event reaches every app as a **version bump**, not a project

### For Technical Director / Staff / EMs
- Facade pattern: vendor churn (SDK upgrades, swaps) is **contained in the library**, not spread across app codebases
- Event schema is **enforced by the library**, not by each developer's memory — fewer mis-tracked events
- Lower cognitive load: developers integrate **one API**, not three vendor SDKs

### For David specifically
- Hits the Q2 OKR on **component presentations** (Parapet, MartechKit, AI Gateway)
- Reinforces the **shared-components / "build once" strategy** — efficiency and savings narrative
- Another proof point that **one Staff Engineer can deliver portfolio-wide infrastructure** end-to-end

---

## Potential Questions & Answers

| Question | Answer | Best answered by |
|----------|--------|------------------|
| "How long does integration take per app?" | Lightweight — add the library + config. The three pilots are the reference point; Victor can give the real numbers. | Victor |
| "What happens when a vendor ships a breaking SDK update?" | We absorb it inside MartechKit once and ship a version bump; apps update a dependency instead of each fixing it. | Victor |
| "Can an app still use a vendor feature MartechKit doesn't expose yet?" | The facade exposes what's standardised; anything missing is a quick addition to the library, kept consistent for everyone. | Victor |
| "Who owns and maintains MartechKit?" | It's a shared library — one owner maintains it, every app benefits. | Filippo |
| "What about apps already wired to these vendors directly?" | They migrate to MartechKit during iOS rollout; the event dictionary is what makes their data comparable to everyone else's. | Filippo |
| "Why not just write a shared events doc instead of a library?" | A doc drifts the moment it's written. The library enforces the schema in code — that's the difference between consistent data and hoping for it. | Victor |
| "When do Android and Flutter land?" | In parallel with the iOS rollout. Full portfolio coverage once both ship. | Filippo |

---

## Credit (slide 10 — Filippo)

- **Victor Jalencas** — designed and built MartechKit end-to-end, including the three pilot integrations.
- **David Sanchez and his team** — shaped the initiative and provided the context that made it possible.
