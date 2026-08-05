# MTSDK — MartechKit correctness epic (audit P0s)

Applied 2026-07-28. Source drafts: `martech-kit/audit/jira-drafts/`, reviewed and amended by
Filippo before creation. Backlog: `martech-kit/audit/2026-07-28-consolidated-backlog.md`.

| Key | Type | Summary | Priority |
|---|---|---|---|
| MTSDK-88 | Epic | MartechKit correctness: the defects blocking further integrations | Critical |
| MTSDK-89 | Story | TikTok: confirm and fix the silent initialisation failure | Critical |
| MTSDK-90 | Story | ATT: stop recording an unanswered prompt as answered, and make requestATT() safe to call twice | Critical |
| MTSDK-91 | Story | AppsFlyer: never fail to start silently, and remove the banned identity fallback | Critical |
| MTSDK-92 | Story | Bootstrap: one configuration, a readiness signal, and no crash for early events | Critical |
| MTSDK-93 | Story | Make the tests that guard the identity contract able to fail | Critical |
| MTSDK-94 | Story | Integration guide: make the documented path actually work | Major |
| MTSDK-95 | Story | Meta: set the advertiser flags from the ATT answer, not from each app | Major |

All eight assigned to Vladyslav Krut. Epic start 2026-07-28, due 2026-08-11.

MTSDK-95 came later and from a different source — MT-1193, not the audit — via
`31-story-meta-att-flags.json`, created the same way with `parent` already set to MTSDK-88.
**Timing:** the three apps in MT-1193 (Ereasy, Photo up, Video up) confirmed their own per-app
fix on 2026-07-28, the same day. Coordinate or the work happens twice.

## What was run

```bash
cd ~/scripts
J=~/Projects/em-hub/projects/martech-sdk/jira

# 1. Epic (dry run first, then commit) — created MTSDK-88
PROJECT_KEY=MTSDK ISSUETYPE_ID=10000 ./jira-create-story.sh $J/29-epic-martechkit-correctness.json
PROJECT_KEY=MTSDK ISSUETYPE_ID=10000 ./jira-create-story.sh $J/29-epic-martechkit-correctness.json --commit

# 2. Substitute the epic key into the story spec
sed -i '' "s/__EPIC__/MTSDK-88/g" $J/30-stories-martechkit-correctness.json

# 3. Stories — created MTSDK-89 … MTSDK-94
PROJECT_KEY=MTSDK ISSUETYPE_ID=10001 ./jira-create-story.sh $J/30-stories-martechkit-correctness.json
PROJECT_KEY=MTSDK ISSUETYPE_ID=10001 ./jira-create-story.sh $J/30-stories-martechkit-correctness.json --commit
```

Assignee and dates were set by a follow-up `PUT /rest/api/3/issue/{key}` — neither
`jira-create-story.sh` nor `jira-update-story.sh` supports those fields.

**MTSDK field ids discovered 2026-07-28** (both issuetype 10000 and 10001):

| Field | Id |
|---|---|
| Start date | `customfield_11010` |
| Due date | `duedate` |
| Assignee | `assignee` (account id) |
| Sprint | `customfield_10007` |
| Extra Assignees | `customfield_10402` |

Vladyslav Krut's account id is `712020:94e99e48-a403-48da-8819-051babe6b2d5`. Note there are
three people named Vladyslav assignable on MTSDK — match on `vladyslav.krut@leadtech.com`, not
on first name.

## Not done

- **No links created.** Worth adding: MTSDK-88 blocks MTSDK-52 (AI Design integration) and
  MTSDK-56 (verify iOS); MTSDK-93 feeds MTSDK-10. Remember the direction — "A blocks B" is
  `inwardIssue: A, outwardIssue: B` — and read the graph back afterwards.
- **No sprint assigned**, and backlog rank is drag-order only (not settable via API), so the
  seven sit at the bottom of the backlog until moved by hand.
- All seven are in status **Pending**; nothing was transitioned.
- The audit's P1/P2 findings are not ticketed and remain in the backlog document.
