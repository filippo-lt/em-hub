# MTSDK restructure, part 2 — App Integrations epic

Follows on from `RUN.md` (already applied: MTSDK-47 epic + MTSDK-48→54 stories + MTSDK-10 re-parented).

All dry-run by default. Nothing is written until `--commit`.

```bash
cd ~/scripts
J=~/Projects/em-hub/projects/martech-sdk/jira
```

---

## Step 5 — Create the App Integrations epic

```bash
PROJECT_KEY=MTSDK ISSUETYPE_ID=10000 ./jira-create-story.sh $J/05-epic-app-integrations.json
PROJECT_KEY=MTSDK ISSUETYPE_ID=10000 ./jira-create-story.sh $J/05-epic-app-integrations.json --commit
```

**Note the key** (expected `MTSDK-55`).

## Step 6 — Substitute, then create the 2 verification stories

```bash
sed -i '' "s/__EPIC2__/MTSDK-55/g" $J/06-stories-app-integrations.json $J/08-relations-app-integrations.json

PROJECT_KEY=MTSDK ISSUETYPE_ID=10001 ./jira-create-story.sh $J/06-stories-app-integrations.json
PROJECT_KEY=MTSDK ISSUETYPE_ID=10001 ./jira-create-story.sh $J/06-stories-app-integrations.json --commit
```

**Note both keys** (expected `MTSDK-56` = Verify iOS, `MTSDK-57` = Verify Android).

```bash
sed -i '' "s/__VERIFY_IOS__/MTSDK-56/g;s/__VERIFY_ANDROID__/MTSDK-57/g" $J/08-relations-app-integrations.json
```

## Step 7 — Rewrite MTSDK-52 / 53 / 54 as integration-only stories

```bash
./jira-update-story.sh $J/07-updates-pilot.json
./jira-update-story.sh $J/07-updates-pilot.json --commit
```

## Step 8 — Re-parent the pilots + wire the dependencies

```bash
./jira-relate.sh $J/08-relations-app-integrations.json
./jira-relate.sh $J/08-relations-app-integrations.json --commit
```

## Step 9 — Reframe MTSDK-10 as the spike that runs first

```bash
./jira-update-story.sh $J/09-updates-spike.json
./jira-update-story.sh $J/09-updates-spike.json --commit
```

---

## The dependency graph this produces

Verified as a clean DAG — no cycles. Roots (blocked by nothing): **MTSDK-10**, MTSDK-25, MTSDK-34, MTSDK-37.

```
MTSDK-10  (spike — runs FIRST, blocked by nothing)
   │
   ├──► MTSDK-52  Integrate AI Design (iOS)   ─┐
   │                    ↕ relates to           │
   ├──► MTSDK-48/49/50  Harnesses             ─┤  parallel, mutually informing
   │                                           │
   │                                           ├──► MTSDK-56  Verify AI Design (iOS) ──► MTSDK-54  Playbook
   │                                           └──► MTSDK-51  Wire into CI
   │
   └──► MTSDK-53  Integrate AI Design (Android)  ──► MTSDK-57  Verify (Android)
            ▲                                            ▲
        MTSDK-25 (parity)                        MTSDK-34 / MTSDK-37 (DI)
```

`MTSDK-52 relates to MTSDK-48/49/50` — deliberately **Relates**, not **Blocks**. They run concurrently and iterate against each other. A `Blocks` link in either direction would serialise work that shouldn't be serialised.

## Epics after this

**MTSDK-55 · App Integrations** — priority #1, now visible at epic level
MTSDK-52 (integrate iOS) · MTSDK-56 (verify iOS) · MTSDK-53 (integrate Android) · MTSDK-57 (verify Android) · MTSDK-54 (playbook)

**MTSDK-47 · Integration Confidence** — the tooling
MTSDK-10 (spike) · MTSDK-48/49/50 (harnesses) · MTSDK-51 (CI)

**MTSDK-2 · Developer Experience** — SDK changes that prevent misuse
MTSDK-9 · MTSDK-12 · MTSDK-21

## Sequencing rationale

**MTSDK-10 runs first and blocks both the harnesses and the integrations.** The spike decides *how* verification works, and that decision changes *what a verifiable integration looks like*. If the answer is SDK-boundary assertion rather than vendor API read-back, a host app needs a debug flavour, a test transport seam and an injectable graph. Integrating before knowing that means retrofitting it after.

**The spike does not need AI Design.** Its core unknowns — Amplitude Export API ingestion latency, AppsFlyer Pull API availability, whether debug traffic is queryable at all — are properties of the vendor platforms, not of the Martech SDK. They can be measured today against any of the six apps already emitting to Amplitude. The end-to-end prototype needs a debug build that emits *through* Martech: a sample app or a minimal harness app.

**Open prerequisite:** if no SDK sample app exists, standing one up is a real cost hiding inside MTSDK-10. Its first acceptance criterion now forces that to be named in the first hour rather than discovered in week two.

## Not automated

MTSDK-24 — Filippo is handling it by hand.
