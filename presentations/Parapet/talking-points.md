# Parapet Presentation — Talking Points

> Date: Friday, April 10, 2026
> Duration: ~15-20 min + Q&A
> Audience: POs, PMs, CPMO, COO, Technical Director, team leads, advisors, Christian, David

---

## Key Messages to Land

1. **This is live, not a pitch** — Parapet is running in production (Photo Up, Face AI). Credibility first.
2. **Build Once, Integrate Everywhere** — the portfolio shares infrastructure instead of each app reinventing the wheel.
3. **Product teams gain autonomy** — Control Center lets POs/support configure quotas, view users, debug — no engineering ticket needed.
4. **Integration is lightweight** — days, not weeks. Client libraries for iOS, Android, Flutter. Developers integrate an API, not a domain.
5. **Tokens unlock new monetisation** — any app can offer consumable credits out of the box, no custom development.
6. **AI-assisted development proof point** — built in 2 days by 1 engineer with AI. This is how we build going forward.
7. **Parapet is the first of many** — shared components strategy (AI Gateway, TVFoundationSDK, MartechSDK) compounds across the portfolio.
8. **Invitational, not mandated** — no rollout plan, no forced timeline. "Ready when you are."

---

## Audience-Specific Angles

### For POs / PMs
- You can configure quotas and tokens **without filing an engineering ticket**
- Changes take effect **immediately** — no sprint, no deploy
- Token system opens **new monetisation paths** with zero dev effort
- You can debug user issues yourself via Control Center

### For Technical Director / COO
- Eliminates redundant development across the portfolio
- Compounds: each new shared component saves weeks per app
- AI-assisted development model = faster delivery with smaller teams
- Aligns with contractor reduction — build infrastructure, not headcount

### For David specifically
- Hits Q2 OKR: component presentations (Parapet, MartechKit, AI Gateway)
- Supports the €700K-1M savings narrative through efficiency
- Demonstrates the AI-assisted development model he wants to scale

---

## Potential Questions & Answers

| Question | Answer |
|----------|--------|
| "What if Parapet goes down?" | Multi-region, auto-scaling. Client libraries have offline fallback — apps degrade gracefully, never crash. |
| "How long does integration actually take?" | Photo Up and Face AI both integrated in under a week. Expect 3-5 days for a typical app. |
| "Who maintains it?" | My team. It's a shared service — one team maintains, all apps benefit. |
| "Can we customise quota logic per app?" | Yes — fully configurable per app, per feature through Control Center. Different apps can have completely different quota models. |
| "What about web apps?" | Architecture is web-ready. Looking for the first web app to integrate — the API layer is platform-agnostic. |
| "Is this adding a dependency / single point of failure?" | It's replacing N independent implementations with one maintained, tested, monitored service. The risk profile is better, not worse. |
| "How does this relate to AI Gateway / other components?" | Same pattern: cloud service + client libraries, multi-tenant, configure-don't-code. Parapet is the proof point. |
| "What if a PO breaks something in Control Center?" | Guardrails are built in — validation on inputs, audit log on changes. No destructive operations exposed. |

---

## Things to Avoid

- Don't get pulled into architecture / technical deep-dives — offer a follow-up session instead
- Don't promise specific integration timelines for apps you haven't scoped
- Don't position this as mandatory — the "ready when you are" framing is deliberate and strategic
- Don't oversell the AI angle — "changed the economics" not "AI wrote everything"
- Don't compare to specific past failures or call out teams who built things from scratch
