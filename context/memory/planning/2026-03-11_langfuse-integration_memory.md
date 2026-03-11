# Memory — Langfuse Integration Review — 2026-03-11

```
[2026-03-11] [planning] - Langfuse integration document reviewed for FaceAI; three blockers before implementation: resource sizing undefined, data governance for production images undecided, Cloud vs Self-Hosted deployment not chosen
[2026-03-11] [planning] - Recommended sequencing: FaceAI first (Python, single provider, doc already written), Tattooist second (same Gemini/Firestore but Node.js runtime + serverless flushing caveat), AI Design third (multiple providers, hardcoded prompts, two-service arch — most effort)
[2026-03-11] [planning] - Decision needed: start on Langfuse Cloud for FaceAI proof of concept vs wait for self-hosted infra — Cloud unblocks the backend dev immediately; migrate to self-hosted when onboarding second app
[2026-03-11] [planning] - Decision needed: restricted evaluation approach (dev/staging images only) vs production feedback loop — recommend starting restricted for compliance safety; production loop can be enabled later
[2026-03-11] [planning] - Tattooist integration is viable but not a copy-paste — Node.js SDK (not Python), Cloud Functions need synchronous flush before return, and prompt assembly is more complex (4 Firestore sources vs single filter config)
[2026-03-11] [planning] - AI Design is the hardest to onboard — FAL.AI and Stability have no native Langfuse integration (manual spans needed), prompts are hardcoded in code (not Firestore), and tracing must span Node.js gateway + Python AI service
[2026-03-11] [planning] - Langfuse self-hosted as shared platform is the right long-term play — one instance serves all three apps; per-app marginal cost decreases after first deployment; aligns with existing GCP/K8s infra
[2026-03-11] [planning] - Mobile work required to unblock FaceAI integration: X-Session-Id and X-Request-Id headers per request, plus user feedback (like/dislike) wired to send request ID back for trace-level scoring
```
