# EPIC — iMote

 https://leadtech.atlassian.net/browse/IMIOSMAU-1568
 

**Jira project:** `IMIOSMAU` (see open question on platform split)
**Issue type:** Epic
**Priority:** Critical
**Summary:** `[Security] Protect iMote Firestore device and rating data`
**Parent:** ADO-1570 (link as *relates to*)

---

## Executive summary

iMote's follow-up to the cross-app Security initiative ADO-1570.

iMote's Firebase project allows a fresh anonymous app identity to list `deviceInfo`, a
collection that records every TV a user connects to. ADO-1570 reports approximately
14,600 documents in `imote-dev/deviceInfo`, confirmed HTTP 200 with anonymous
authentication on 2026-08-24.

Each document holds the full connected-device record: TV serial number, last known LAN
IP address, the Wi-Fi network name the device was last seen on, the user's own name for
the device, plus make, model and timestamps. An attacker could automate anonymous
sign-in and bulk-download the collection, producing a map of household TVs — device
names, home network names and hardware serials — without knowing any customer or
document ID. This is personal data under GDPR Art. 4(1) even though no account,
email or payment identifier is stored.

Two facts raise this above its document count.

**`imote-dev` is not a test project.** The `Dev` and `DevRelease` build configurations
point at `imote-dev` and ship to TestFlight under the production bundle id
`imote.tv.remote.control`, and to the Saucelabs device farm. The 14,600 documents are
real users, real TVs and real home networks.

**`imote-prod` was never probed.** It is absent from ADO-1570's affected list in both
the production and dev sections. It is a real Firebase project, it is the target of
every App Store build, and it runs identical client code writing the same collections.
Its exposure is therefore unknown rather than closed. Before June 2026 the build
configuration selected Prod for every non-Debug build, so pre-June TestFlight traffic
also wrote to `imote-prod`; its document count is structurally likely to exceed dev's.

Nothing in either the iOS or the Android app ever reads `deviceInfo` back. It is
write-only telemetry. The first question is therefore not how to secure it but whether
it needs to be collected at all.

## Expected outcome

- Confirmed whether any consumer outside the app reads `deviceInfo`, with a named owner
  for the answer.
- If it has no consumer: the write is removed from both platforms and the collection
  becomes server-only.
- If it has a consumer: the payload is reduced to what that consumer actually needs, and
  the four personal-data fields (Wi-Fi SSID, LAN IP, serial number, user-set device
  name) are dropped regardless.
- `deviceInfo` cannot be listed or read by mobile or anonymous clients.
- `rateApp` submission continues to work on both platforms and becomes create-only.
- Firestore rules are stored in source control with a deploy path, on both `imote-dev`
  and `imote-prod`.

## Scope note

`rateApp` is a live user-facing flow and is not a candidate for removal. It is also not
the collection ADO-1570 probed, so its anonymous create path is not in conflict with the
parent's acceptance criteria. It is included here because any rules change touches it.

## Out of scope — raised separately

- `imote-prod` has never been probed. Requesting that probe is tracked outside this epic.
- The Realtime Database path `signaling/{roomID}` has no rules file in either repo and
  was not covered by ADO-1570, which is Firestore-only.
- Android's `google-services.json` is gitignored, so Android's GCP project ids could not
  be confirmed from source.
