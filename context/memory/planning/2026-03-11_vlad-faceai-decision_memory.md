# Memory — Vlad Face AI Rebuild Decision (2026-03-11)

```
[2026-03-11] [planning] - Decided: Vlad rebuilds Face AI from scratch, full feature parity with today's store version; current external team stays in place and continues on the live app until cutover
[2026-03-11] [planning] - Staff Engineer (Sergio) providing baseline repo with architecture rules and workflow — Vlad's role shifts from "create rules" to "validate and feed back"; this de-risks the timeline significantly
[2026-03-11] [planning] - Cutover strategy: same bundle ID, future version; preserves store ratings/reviews; rebuild replaces live app only after QA gate passes
[2026-03-11] [planning] - Timeline pressure accepted as genuine measurement, not a promise — first rebuild is the learning investment; the ratio between first and second rebuild is the metric that proves scalability to David
[2026-03-11] [planning] - Two hypotheses being tested: (1) speed — rebuild vs original build timeline for David's savings narrative; (2) model viability — can one SE with AI produce production-quality output independently
[2026-03-11] [planning] - Priority stack if Vlad needs scope relief: cut company-wide rule shaping first, then reduce ceremony attendance — protect build time above all else
[2026-03-11] [planning] - Vlad should follow Staff Engineer baseline and log disagreements, not deviate mid-build; debrief on rule friction after the rebuild completes
[2026-03-11] [planning] - Need to define before build starts: (1) feedback channel from Vlad to Staff Engineer, (2) who QAs the rebuild before cutover, (3) baseline number for how long original Face AI took to build
[2026-03-11] [planning] - Frame to David: "Staff Engineers set the patterns, Software Engineers execute with AI" — this is the scalable story, not just a one-off POC
```
