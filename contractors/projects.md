# Projects — Source Mapping

**Last updated:** 2026-09-08

Maps each project to its GitHub repos and Jira boards. Used by the contractor review workflow to pull metrics.

## Projects

### Tattooist

| Source | Identifier |
|--------|------------|
| GitHub Repo | https://github.com/rosseca/tattoo |
| GitHub Repo | https://github.com/rosseca/tattoo-android |
| GitHub Repo | https://github.com/leadtechcorp/tattoo_infra |
| Jira Board(s) | TTIOSMAU |

### AI Design

| Source | Identifier |
|--------|------------|
| GitHub Repo | https://github.com/rosseca/aihomedesigner |
| GitHub Repo | https://github.com/rosseca/aihomedesigner_android/ |
| GitHub Repo | https://github.com/leadtechcorp/aihomedesigner_infra |
| Jira Board(s) | ADIOSMAU |

### iMote

| Source | Identifier |
|--------|------------|
| GitHub Repo | https://github.com/rosseca/imote |
| GitHub Repo | https://github.com/rosseca/imote-android |
| Jira Board(s) | IMANDMAU |
| Jira Board(s) | IMIOSMAU |

### Face AI

| Source | Identifier |
|--------|------------|
| GitHub Repo(s) | https://github.com/rosseca/faceai_ios |
| GitHub Repo(s) | https://github.com/leadtechcorp/faceai_backend |
| Jira Board(s) | FAIOSMAU |

### Screen Mirroring

| Source | Identifier |
|--------|------------|
| GitHub Repo(s) | https://github.com/rosseca/screenmirroring |
| GitHub Repo(s) | https://github.com/leadtechcorp/screenmirroring_backend |
| Jira Board(s) | SMIOSMAU |

### ChatUltra (ChatBot)

Status: M&A — Govern-in-place — vendor transition from Helikanon; PO Ruben/Carlos.

| Source | Identifier |
|--------|------------|
| GitHub Repo | https://github.com/rosseca/chat_ai_ultra |
| GitHub Repo | https://github.com/rosseca/chat_module |
| GitHub Repo | https://github.com/rosseca/purchasing_module |
| GitHub Repo | https://github.com/rosseca/analytics_module |
| GitHub Repo | https://github.com/rosseca/chat_service |
| GitHub Repo | https://github.com/rosseca/connectinno_permission_module |
| GitHub Repo | https://github.com/rosseca/connectinno_apns_handle |
| GitHub Repo | https://github.com/rosseca/age_range_signals |
| GitHub Repo | https://github.com/rosseca/image-gen-service |
| GitHub Repo | https://github.com/rosseca/chatultra_credit_service |
| GitHub Repo | https://github.com/rosseca/cloud_token_service |
| GitHub Repo | https://github.com/rosseca/dart_firebase_admin |
| GitHub Repo | https://github.com/rosseca/flutter-sound-stream |
| Jira Board(s) | TBD — no dedicated board key yet |

Vendored forks (`dart_firebase_admin`, `flutter-sound-stream`) are listed for completeness; exclude them from commit-metric pulls.

### TraceCheck (web)

Status: Launched — Web division (formerly Truth Seeker), launched second week of August 2026.

| Source | Identifier |
|--------|------------|
| GitHub Repo | https://github.com/rosseca/tracecheck-web |
| GitHub Repo | https://github.com/rosseca/truthseeker-web-doc |
| Jira Board(s) | TBD — board exists (built out by Andrey) but key not mapped here |

<!--
How to add a new project:
1. Add a new ### section with the project name
2. List all GitHub repos (org/repo format — used with `gh` CLI)
3. List all Jira board keys (used for JQL queries)
4. Project names here must match what's used in registry.md
-->
