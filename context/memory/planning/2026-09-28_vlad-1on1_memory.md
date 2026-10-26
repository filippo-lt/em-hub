# Planning memory — Vlad 1:1, 2026-09-28

```
[2026-09-28] [planning] - TraceCheck will have ZERO developers for ~1.5 weeks in November: Andrey leaves 30 Oct, Vlad (sole dev from then) is on leave in November. Coverage options: David's web-developer offer (answer owed w/c 28 Sep), the external hire won't be proficient by then.
[2026-09-28] [planning] - MartechKit has a structural dependency problem: declared dependencies (TikTok, Firebase) enter the app's package resolution even when not linked; AI Design (Ads Global wrapper → TikTok) cannot resolve. Firebase works only by version-range accident. Vlad's fix: split into separate packages per dependency in a monorepo — weeks, not months. Integration in AI Design paused; if Tattooist has the same issue, Victor drops everything.
[2026-09-28] [planning] - MartechKit needs an issue triage process with an SLA (~48h) for adopting apps; no owner named yet — should be Victor (owner), not Vlad (user).
[2026-09-28] [planning] - Security: one whitebook for AI Design + Face AI + The Twist, with an epic of fix tickets done by the team. ISO trial run in December → personal data must be masked/hashed; every stored data point reviewed with Miguel, "just in case" = removed.
[2026-09-28] [planning] - TraceCheck ~$50K/month revenue (late Sep 2026), growing. Open product question: a results URL with a phone number auto-runs a paid lookup without confirmation.
```
