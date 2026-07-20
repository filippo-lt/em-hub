# MTSDK restructure — run book

All four steps are **dry-run by default**. Nothing is written until you add `--commit`.

Run these on your Mac (the sandbox has no network route to `leadtech.atlassian.net`).

```bash
cd ~/scripts
J=~/Projects/em-hub/projects/martech-sdk/jira
```

---

## Step 1 — Create the Integration Confidence epic

MTSDK's Epic issue type is `10000` (the script defaults to TSMAU's, which is wrong for this project).

```bash
PROJECT_KEY=MTSDK ISSUETYPE_ID=10000 ./jira-create-story.sh $J/01-epic-integration-confidence.json
PROJECT_KEY=MTSDK ISSUETYPE_ID=10000 ./jira-create-story.sh $J/01-epic-integration-confidence.json --commit
```

**Note the key it prints** (expected: `MTSDK-43`). Steps 2 and 4 need it.

## Step 2 — Substitute the epic key, then create the 7 stories

Story issue type is `10001`.

```bash
sed -i '' "s/__EPIC__/MTSDK-43/g" $J/02-stories-integration-confidence.json $J/04-relations.json   # use the real key

PROJECT_KEY=MTSDK ISSUETYPE_ID=10001 ./jira-create-story.sh $J/02-stories-integration-confidence.json
PROJECT_KEY=MTSDK ISSUETYPE_ID=10001 ./jira-create-story.sh $J/02-stories-integration-confidence.json --commit
```

## Step 3 — Narrow MTSDK-2, reframe MTSDK-10 as a go/no-go spike

```bash
./jira-update-story.sh $J/03-updates.json
./jira-update-story.sh $J/03-updates.json --commit
```

## Step 4 — Links and re-parent

```bash
./jira-relate.sh $J/04-relations.json
./jira-relate.sh $J/04-relations.json --commit
```

---

## What Step 4 does

| Op | Effect |
|---|---|
| `MTSDK-25 blocks MTSDK-3` | Flutter can't start until parity lands |
| `MTSDK-9 / MTSDK-12 block MTSDK-6` | Misuse-prevention spikes mutate the public init surface — the bridge must not bind to a surface that's about to change |
| `MTSDK-34 / MTSDK-37 block MTSDK-6` | DI + testability are prerequisites for the bridge and for Android assertions |
| re-parent `MTSDK-10` | Moves the identity spike into the new epic |

## Not automated — MTSDK-24

**Filippo is handling MTSDK-24 by hand.** No script touches it.

For the record: MTSDK-24 ("Bring Martech Pack and Martech Kit to feature Parity") duplicates the whole of MTSDK-25. It has no *Won't Do* resolution available — its only closing transition is `Mark as done` → `Done`, which would book it as completed work in a burn-up. Hence: manual.

The dependency it was standing in for is now explicit via the `MTSDK-25 blocks MTSDK-3` link created in Step 4, so nothing is lost by closing it however you see fit.

## Caveats

**No Acceptance Criteria field exists on MTSDK.** `jira-create-story.sh` expects `customfield_15530` (TSMAU-only). Acceptance criteria are folded into the description as a bulleted section instead. Don't add an `acceptance_criteria` key to these specs — it would send a field that doesn't exist and the create would 400.

**Don't set `workgroup`** for the same reason (`customfield_15575` doesn't exist here either).

## Rollback

Links are individually removable in the Jira UI. Re-parenting MTSDK-10 is reversible (set parent back to MTSDK-2). The 7 created stories would need deleting by hand. There is no scripted undo — which is why every step is dry-run first.

Nothing in these four steps closes, deletes, or resolves an existing issue. The only mutations to pre-existing issues are: MTSDK-2 (summary + description), MTSDK-10 (summary + description + parent), and new links on MTSDK-3 / MTSDK-6 / MTSDK-9 / MTSDK-12 / MTSDK-25 / MTSDK-34 / MTSDK-37.
