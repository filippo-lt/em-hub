# Parapet Presentation — Draft Script

> Estimated delivery: ~15-18 minutes
> Pace: conversational, not rushed. Pause after key points.

---

## Slide 1 — Cover (~30 sec)

> "Thanks everyone for joining. Today I want to walk you through Parapet — what it is, what it does, and how it fits into a broader shift in how we build across the portfolio.
>
> This isn't a feature demo or a technical deep-dive. It's about a strategic change: moving from apps that each solve the same problems independently, to a portfolio that shares infrastructure."

---

## Slide 2 — Same Problem, Solved 10 Times (~1.5 min)

> "Let me start with a pattern that everyone in this room has experienced.
>
> Every app that needs quotas, usage limits, subscription handling, or device authentication builds it from scratch. Different implementations, different bugs, no shared foundation.
>
> When a new app needs something that already exists in another app — say, quota management — the answer is always: 'build it again.' New sprint, new tickets, new bugs to find.
>
> We've solved the same problem at least ten times across the portfolio. And every time we solve it again, we're not just spending engineering time — we're spending *your* time. Product teams wait on custom development for capabilities that already exist somewhere else in the company.
>
> That's the problem. Now let's talk about the fix."

---

## Slide 3 — Build Once, Integrate Everywhere (~1.5 min)

> "The shift is simple: instead of each app building everything from scratch, we build shared components that any app can plug into.
>
> Cloud services plus client libraries. Build it once, maintain it in one place, and every app that integrates gets the same capability — tested, maintained, and improving over time.
>
> Parapet is the first shared component. It's live today. But it's not the only one — AI Gateway, TVFoundationSDK, MartechSDK are all following the same pattern.
>
> What you're looking at here is the beginning of a platform. Not every app needs every component — and that's fine. The point is: when you need it, it's there. You don't start from zero."

---

## Slide 4 — What Parapet Handles (~2 min)

> "So what does Parapet actually do? Four things.
>
> **First, device authentication.** It verifies that real users are on real devices. This is App Check — it protects your backend from abuse and automated attacks.
>
> **Second, quota management.** It tracks feature usage limits per user and resets them automatically — daily, weekly, monthly, or on the billing cycle. You configure the rules; Parapet enforces them.
>
> **Third, a token and credit system.** Persistent credits that users buy through in-app purchase. They don't reset — they persist until consumed. This is independent of subscriptions, so it works for free users and paying users alike. The backend decides what costs how much, giving you full flexibility for A/B testing pricing models.
>
> **Fourth, subscription sync.** RevenueCat integration is handled automatically. When a user's subscription changes, Parapet updates their quotas and entitlements in real time. No webhook plumbing, no state management — it just works.
>
> All of this is multi-tenant — one system, all apps. It works across iOS, Android, and Flutter today. Web support is architecturally ready; we're looking for the first web app to integrate."

---

## Slide 5 — Configure, Don't Code (~2 min)

> "This is the part I think will matter most to the product people in the room.
>
> Parapet comes with a Control Center — a web dashboard where product and support teams can manage everything directly.
>
> You can set and change quota limits per app, per feature. You can configure reset schedules. You can look up any user and see their quota state, their token balance, their subscription status — in real time.
>
> And here's the key part: **changes take effect immediately.** No sprint. No deploy. No waiting for the next release.
>
> If you want to change the daily limit on a feature from 5 to 10 — you change it. It's live. If support needs to debug why a user ran out of credits — they look it up. No engineering ticket needed.
>
> [If doing live demo: Let me show you what that looks like…]
>
> [If showing screenshots: Here's what the dashboard looks like in practice…]"

---

## Slide 6 — Tokens: Now Available to Every App (~1.5 min)

> "I want to spend a moment on tokens specifically, because this is a capability that opens up new monetisation for the whole portfolio.
>
> Some apps already use consumable credits — but each one built its own implementation. With Parapet, any app can offer token packs out of the box. No custom development.
>
> Here's how they differ from quotas: quotas reset — daily, weekly, monthly. They limit usage. Tokens don't reset. They persist until consumed. They're independent of subscriptions, so any user — free or paid — can buy and use them.
>
> Think of quotas as guardrails: '5 AI edits per day.' Think of tokens as currency: 'Buy 100 credits for premium filters.'
>
> The backend decides what costs how much, so you have full flexibility to experiment with pricing. And because it's all handled through Parapet, rolling this out to a new app is configuration, not development."

---

## Slide 7 — Fraction of the Time, Fraction of the Complexity (~1.5 min)

> "Integration time is dramatically reduced. What used to take weeks is now days.
>
> But the bigger win isn't just speed — it's complexity.
>
> Without Parapet, a developer integrating quotas or tokens needs to understand RevenueCat webhooks, subscription state management, quota reset scheduling, device attestation, billing cycle handling, token accounting, error recovery. That's a lot of domain knowledge for every developer on every app.
>
> With Parapet, they integrate an API. That's it. The domain complexity lives in Parapet, not scattered across every app's codebase.
>
> Client libraries ship for iOS, Android, and Flutter. Plug in and go. We're talking days of integration, not weeks of domain learning."

---

## Slide 8 — Already Live (~1 min)

> "This is not a proposal. Parapet is running in production today.
>
> Photo Up — live, quota management active. Face AI — live, quota management active. Two more apps are already planned for integration.
>
> The integrations went smoothly. The system is stable. The Control Center is being used by product and QA teams.
>
> This is the foundation we're building on — proven, not promised."

---

## Slide 9 — Ready When You Are (~1.5 min)

> "So here's the offer.
>
> Parapet is built, proven, and available. Any app in the portfolio can integrate. Here's what you get:
>
> Quota management — configure limits and resets without a sprint. Token system — offer consumable credits from day one. Subscription sync — RevenueCat handled automatically. Control Center access — product and support can self-serve immediately.
>
> Integration is lightweight: a few days of engineering work.
>
> There's no rollout plan. No mandated timeline. When your product team is ready to move, we're ready to support. Come talk to us."

---

## Slide 10 — Built in 2 Days with AI (~1.5 min)

> "One more thing I want to share, because I think it matters for how we think about building going forward.
>
> Parapet — the cloud services, the client libraries, the Control Center — was built in 2 days by a single engineer working with AI.
>
> I want to be clear about what that means. AI didn't write everything. AI handled the scaffolding — the API boilerplate, the client libraries, the dashboard UI, the integration tests. The engineer made the decisions that matter: the architecture, the security model, the multi-tenancy design, the domain logic.
>
> What changed is the economics. What used to require a team and a quarter now requires focus and the right tools.
>
> Parapet is a shared component *and* a proof point. The same approach — AI handling the scaffolding, engineers handling the judgment — applies to everything we build next."

---

## Slide 11 — The Platform (~1.5 min)

> "Zooming out.
>
> Parapet is the first shared component, but it's not the only one. Four are already in motion:
>
> Parapet — live. Quota, auth, tokens.
> AI Gateway — centralised AI access across apps. In progress.
> TVFoundationSDK — shared TV platform capabilities. In progress.
> MartechSDK — shared marketing tech for the portfolio. In progress.
>
> Each one follows the same model: cloud service plus client libraries, multi-tenant, configure-don't-code.
>
> Not every app needs every component — and that's by design. But each component we build saves weeks per app and compounds across the portfolio. The more we share, the faster every team moves."

---

## Slide 12 — The Bigger Picture (~1 min)

> "This is where it all fits together.
>
> What you're looking at is the portfolio architecture we're building toward. Shared services across infrastructure, identity, monetisation, AI, martech — with every app plugging into the pieces it needs.
>
> Parapet is one piece. But it's the proof that the model works: build once, maintain in one place, integrate everywhere.
>
> We're not building a collection of apps anymore. We're building a portfolio."

---

## Slide 13 — Close (~30 sec)

> "That's Parapet. I'm happy to take questions.
>
> If you want to explore integration for your app, come find me or anyone on my team. The Control Center is live — I can get you access today.
>
> Thanks, everyone."

---

## Notes for Delivery

- **Pacing:** Don't rush slides 4-6 (the "what it does" section). This is where POs/PMs get their value. Give them time to absorb.
- **Energy shift:** Slides 2-3 set the problem/vision. Slides 4-9 are the substance. Slide 10 is the surprise moment — let it land. Slides 11-12 are the strategic close.
- **Live demo vs screenshots:** If doing a live demo on slide 5, rehearse it. Keep it to 2-3 actions max (configure a quota, look up a user, change a limit). If anything could go wrong, use screenshots instead.
- **Q&A management:** If questions go deep technical, offer a follow-up session: "Great question — let's set up a deeper session for that. For today I want to keep it at the strategic level."
- **David's presence:** He's seen this material. He'll likely reinforce key points. Let him — it strengthens the message when the boss backs it publicly.
- **Christian's presence:** Keep it outcome-focused. Savings, speed, platform thinking. Don't get lost in implementation details.
