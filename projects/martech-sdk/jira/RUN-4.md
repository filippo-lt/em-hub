# Run 4 — Android diagnostics (2026-09-10)

Brings Vladyslav Krut's iOS diagnostics work (API, event ledger, debug screen, JSON export;
martech-kit main 2026-07-24 → 09-01) to MartechPack.

| Key | Type | Summary |
|---|---|---|
| MTSDK-140 | Epic | Android: check from inside the app that marketing tracking is working |
| MTSDK-141 | Story | Developers can read the SDK's setup status in code and in the logs |
| MTSDK-142 | Story | Keep a list of the events the app tried to send, and whether each one went out |
| MTSDK-143 | Story | A debug screen testers can open inside a test build |
| MTSDK-144 | Story | Report a startup that failed or only partly worked, instead of staying silent |
| MTSDK-145 | Story | Integration guide: add the debug screen and explain it for QA |
| MTSDK-146 | Story | Try the debug screen in iMote before other apps rely on it |

All Major, assigned to Viacheslav Lypchenko (`712020:60fdd21c-4b16-41f5-8e5c-df947b00ef5e`),
component `MartechPack - Android`, status Pending. No sprint, no dates.

## Files

- `32-epic-android-diagnostics.json` — epic (created)
- `35-update-mtsdk140.json` — epic correction: Android *does* have a consent step; status words
  aligned to "waiting for consent / not healthy"; sequencing says Android matches today's iOS first
- `34-stories-android-diagnostics.json` — stories, created with `__S1__..__S6__` placeholders
- `37-update-story-keys.json` — same descriptions with real keys filled in
- `33-relations-android-diagnostics.json` — epic links
- `36-relations-android-diagnostics-stories.json` — story links

## Link graph (read back and matched intent)

```
MTSDK-104 ─blocks→ 140, 141, 142, 146
MTSDK-112 ─blocks→ 142
141, 142 ─blocks→ 143
143 ─blocks→ 145, 146, 144
145 ─blocks→ 146, 144
MTSDK-137, MTSDK-138 ─blocks→ 144
140 ─blocks→ MTSDK-53, MTSDK-57
140 relates MTSDK-137, MTSDK-138;  146 relates MTSDK-50
```

## Notes

- A story for "events tracked before setup are lost" was requested and **not created**: MTSDK-112
  already covers it and `fix/MTSDK-112` (in review) buffers 250 events and flushes in order, as iOS.
- Comprehension check ran four rounds; round-4 findings (cross-ticket blockers, epic vs story
  wording) were fixed without a fifth run.
- MTSDK-144's failure trigger ("first launch with no network") is today's documented Android
  behaviour; iOS MTSDK-138 is still moving there — re-check when it closes.
- CLAUDE.md is stale: MTSDK-34/37 (Android DI graph) are Done, and Android is now Slava's.
