# STORY 1 — iMote

**Jira project:** `IMIOSMAU`
**Issue type:** User Story
**Priority:** Critical
**Summary:** `Confirm whether deviceInfo has any consumer, then remove or reduce the write`
**Epic:** `[Security] Protect iMote Firestore device and rating data`

---

## Context

This story decides the shape of the fix. It must complete before the rules story ships.

`deviceInfo` is written by the iOS app on every TV connection at
`iMote/Core/BaseVC/BaseVC + Extensions.swift:165`. The write is not gated by any
feature flag — `shouldShowDeviceInfo` only controls whether a row appears in Settings.
Each write mints a fresh random document id, so a new document is created on every
single connection rather than updating one per device. That is why the collection
reached ~14,600 documents.

The payload is the entire `TVConnectableDeviceModel`, JSON-serialised into a single
string field (`iMote/Module/ConnectToDevice/Model/ConnectToDeviceModel.swift:50`):

```
id, address, friendlyName, tvDisplayName, modelName, modelNumber, manufacturer,
modelDescription, commandURL, lastKnownIPAddress, lastSeenOnWifi, lastConnected,
lastDetection, serviceType, osType, port, deviceType, manufacturerURL, modelURL,
serialNumber, type
```

**No code in either the iOS or the Android app reads this collection back.** A
repository-wide search found writes only. That does not prove nobody reads it — a
BigQuery export, a scheduled report, a support workflow or a habit of opening the
Firebase console would not appear in the codebase.

## Provenance

These findings were produced through an AI-assisted review of the application code,
cross-referenced against the non-destructive Firebase permission probe recorded in
ADO-1570. They must be validated by the technical owner before implementation.
Contact: filippo.tosetto@leadtech.com

## Technical guidance

1. Ask the iMote PO, and the growth/analytics owner, one question: does anything read
   `deviceInfo`? Name the person who answered and record the answer on this ticket.
   Do not skip this step on the assumption that write-only means unused — connected TV
   make and model is plausibly valuable product data for a remote-control app.

2. **If there is no consumer:** remove the write from both platforms. The collection then
   receives no new documents and can be closed server-only in Story 2. Delete or archive
   the existing ~14,600 documents (and whatever `imote-prod` holds) as part of that
   change, since they are personal data with no purpose.

3. **If there is a consumer:** do not keep the current payload. What a product consumer
   would need is `modelName`, `modelNumber` and `manufacturer`. What is being written
   additionally includes `lastSeenOnWifi` (the home Wi-Fi network name),
   `lastKnownIPAddress`, `serialNumber` and `friendlyName` / `tvDisplayName` (a
   user-chosen label, frequently a person's name or a room). Those four categories are
   personal data and are not required for device-compatibility reporting.

   Replace the Firestore write with an analytics event carrying model, model number and
   manufacturer only. Telemetry belongs in Analytics, not in a queryable user-data
   collection. If the consumer specifically needs a Firestore document, the write must
   move behind a backend endpoint so the collection can still be closed to clients.

4. Apply the same change to Android if an equivalent write exists there. Android's
   Firestore surface could not be fully confirmed from source because
   `google-services.json` is gitignored; verify directly.

## Validation

- Search both codebases and confirm no remaining client write to `deviceInfo`.
- Confirm with the named owner that removing (or reducing) the write breaks no downstream
  report or process.
- Exercise TV connection on both platforms and confirm connection, pairing and casting
  are unaffected. Firestore is not on the casting path — pairing is local-network
  SSDP/DIAL/WebSocket — so no functional regression is expected.

## Acceptance criteria

- A named owner has answered whether `deviceInfo` has a consumer, and the answer is
  recorded on this ticket.
- Either the client write is removed on both platforms, or the payload no longer contains
  Wi-Fi SSID, LAN IP address, serial number or user-set device name.
- Existing `deviceInfo` documents in `imote-dev` and `imote-prod` are deleted or archived
  where the write was removed.
- TV connection and casting verified working on both platforms.
