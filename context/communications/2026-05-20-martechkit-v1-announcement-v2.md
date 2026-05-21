**To:** Product team (POs, PMs, product leadership) + Engineering team (SEs, EMs, Staff Engineer, Technical Director)
**Channel:** Email
**Subject:** MartechKit v1.0 (iOS) released — unified Martech SDK now live

---

Hi everyone,

I'm writing to introduce **MartechKit**, a shared library that unifies our third-party Martech tooling and is now available for integration across the iOS portfolio.

**What it does**

MartechKit consolidates the third-party tools we rely on: Amplitude, RevenueCat, AppsFlyer, and others, behind a single library:

- **Single point of implementation.** Martech changes ship as a library version bump, no per-app re-implementation.
- **Standardisation across the portfolio.** All apps integrate third party libraries the same way, removing drift and inconsistencies.
- **Shared event dictionary.** Every app tracks the same events with the same schema. This sharply reduces mis-tracked events and makes cross-app product analysis possible.
- **Lower cognitive load for engineers.** Vendor specifics live inside the SDK, not in app code.
- **Faster experimentation for Marketing/Martech.** The Martech team iterates without being bottlenecked on per-app engineering.

**Integration**

MartechKit handles vendor SDKs, configuration, and event plumbing; developers integrate a single libreary instead of wiring each vendor from scratch. What used to be portfolio-wide tickets becomes a version bump.

**Where we are**

MartechKit v1.0 for native iOS is live today, validated in three pilot apps. Next:

1. Roll out across the rest of the native iOS portfolio.
2. Android version of the library, in parallel.
3. Flutter version of the library, in parallel.

Once Android and Flutter land, we have full portfolio coverage.

**Credit**

MartechKit was designed and built end-to-end by **Victor Jalencas**, one of our Staff Engineers, over the last few weeks, including the integration in the three pilot apps. Thank you, Victor.

Thanks also to **David Sanchez and his team** for shaping the initiative and sharing the context that made it possible.


Please forward this email to anyone in your area who may find it relevant. Happy to answer any questions.

Best,
Filippo
