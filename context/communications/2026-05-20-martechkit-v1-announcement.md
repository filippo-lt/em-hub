**To:** Product team (POs, PMs, product leadership) + Engineering team (SEs, EMs, Staff Engineer, Technical Director)
**Channel:** Email
**Subject:** MartechKit v1.0 (iOS) released — unified Martech SDK now live

---

Hi all,

I want to share an update on an initiative that has shipped today and that will meaningfully change how we work with our martech stack across the portfolio.

**What is MartechKit**

MartechKit is the first deliverable of a broader Martech SDK initiative. The goal is to consolidate all the third-party martech tools we depend on: Amplitude, RevenueCat, AppsFlyer, and others; behind a single library that each app integrates once.

**Why this matters**

Changing any martech implementation across our app portfolio has historically been one of the pin points in our workflows. Every change required per-app tickets, per-developer context, and a deep understanding of each vendor's specifics.

MartechKit changes that in a few concrete ways:

- **Single point of implementation.** When a change in one of the third party libraries is needed, developers bump the library version and get the change for free, no per-app re-implementation.
- **Standardisation across the portfolio.** All apps consume third party libraries the same way, removing drift and inconsistencies.
- **Shared event dictionary.** Every app tracks the same events with the same schema. This sharply reduces mistracked events and, for the first time, makes cross-app product analysis possible.
- **Lower cognitive load for engineers.** Developers no longer need to understand the specifics of each third party service, those concerns live inside the SDK.
- **Faster experimentation for Marketing/Martech.** The Martech team can iterate without being bottlenecked on per-app engineering work.
- **Development cost savings.** What used to be portfolio-wide tickets becomes a version bump.

**Credit where it's due**

This work was designed and built end-to-end by **Victor Jalencas**, one of our Staff Engineers, over the last few weeks, including the integration in the three pilot apps. Thank you, Victor.

A big thank-you also goes to David Sanchez and his team, who helped shape the initiative and shared the context and nuance of the broader Martech landscape that made this possible.

**Next steps**

- **Today:** MartechKit v1.0 for native iOS is released.
- **In parallel, starting now:**
  1. Roll out MartechKit across the rest of the native iOS portfolio.
  2. Build the Android version of the library.
  3. Build the Flutter version of the library.

Once Android and Flutter land, we will have full portfolio coverage and the benefits above compound across every app we ship.

Happy to answer any questions.

Best,
Filippo
