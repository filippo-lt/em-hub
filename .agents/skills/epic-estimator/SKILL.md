---
name: epic-estimator
description: "Estimate a Jira epic end-to-end: fetch, validate, decompose into work items, produce a person-week estimate table, refine with the user, and post the approved estimate back to Jira. Use when the user says things like 'estimate epic', 'estimate TATA-123', 'decompose epic', 'break down epic', or mentions an epic key (e.g. TATA-456) in the context of estimation."
user_invocable: true
---

# Epic Estimator

End-to-end Jira epic estimation workflow. Fetches the epic, validates it has the minimum required content, decomposes it into work items with person-week estimates, refines with the user, and posts the approved estimate back to Jira.

---

## Trigger

Activate when the user mentions an epic key (e.g. `TATA-123`) in an estimation context, or says:
- "estimate epic"
- "estimate TATA-123"
- "decompose epic"
- "break down epic"

---

## State to Track

Keep these in memory across the conversation:

- `epic_key` — e.g. `TATA-123`
- `epic_json` — raw output from `jira-fetch.sh`
- `gate_result` — PASS or REJECT + details
- `estimate_table` — current estimate markdown
- `approved` — boolean, starts `false`

---

## Phase 1 — Fetch Epic

Run:

```bash
~/scripts/jira-fetch.sh <epic_key>
```

Store the output as `epic_json`. If the script errors or returns non-200, report the error and stop.

---

## Phase 2 — Gate (Validate Epic Completeness)

Validate the epic has all five required sections. Look for content, not headings — apply reasonable inference. Each section can appear anywhere in `description` or `acceptance_criteria`.

| Section | What counts as sufficient |
|---|---|
| **Overview** | At least 1 sentence describing what the feature/change is |
| **Business Goal** | Why this is being built — a metric, user outcome, or strategic reason |
| **Problem Statement** | The specific problem or gap being addressed |
| **Scope** | At least one explicit statement of what is IN scope (out-of-scope is a bonus) |
| **Success Criteria** | A measurable or verifiable outcome — not just "feature is done" |

### If any section is missing → REJECT

Output exactly this format and **stop**. Do not proceed to estimation. Do not list sections that passed. Do not add suggestions beyond what's listed.

```markdown
## Epic <KEY>: <Title> — REJECTED ❌

This epic cannot be estimated. The following required sections are missing or incomplete:

- ❌ **<Section name>**: <One sentence: what was found and what is needed>
- ❌ **<Section name>**: <One sentence: what was found and what is needed>

Please update the epic in Jira and re-submit.
```

Do not proceed until the user re-submits with an updated epic. Never skip the gate, even if the user says "just estimate it".

### If all sections pass → continue silently

No commentary needed. Proceed to Phase 3.

---

## Phase 3 — Load Configuration

Run:

```bash
cat ~/.config/epic-estimator/taxonomy.yml
cat ~/.config/epic-estimator/calibration-notes.md
ls ~/.config/epic-estimator/projects/
cat ~/.config/epic-estimator/projects/<project-name>.yml
cat ~/.config/epic-estimator/history/<project-name>-history.yml  # if exists
```

Determine project name from the `epic_key` prefix (e.g. `TATA` → `tattooist.yml`). Bundle all loaded config as `config_bundle`.

---

## Phase 4 — Estimate

### Step 4.1 — Scan relevant codebase areas

Using repo paths from `project_config.yml`, scan local repos:

```bash
find <repo_path> -type f -name "*.swift" | head -50   # adjust extension per repo type
```

Focus only on:
- Top-level directory structure (architecture overview)
- Files/modules directly related to the epic's feature area
- Shared modules likely to be impacted

**Do NOT read every file. Always fetch the latest changes from remote and checkout the develop branch.**

If a relevant area is unclear or not found, note it — use a range estimate for that item instead of a point estimate.

### Step 4.2 — Decompose into work items

Map the epic's work onto categories from `taxonomy.yml` (plus any `additional_categories` in the project config).

Each work item must be:
- Assignable to a single developer or discipline
- Independently deliverable
- Mapped to exactly one taxonomy category

**Merge iOS and Android** into a single `Mobile UI` line item (per calibration rules). Skip categories with no applicable work — only include what the epic actually requires.

### Step 4.3 — Estimate each item

For each work item:

1. Start from `typical_range` in `taxonomy.yml`
2. Adjust based on observed codebase complexity
3. Apply any matching multipliers from `calibration-notes.md`
4. Cross-reference `history.yml` for similar past items in this project
5. Consider team composition from `project_config.yml` (a team of 1 backend dev affects parallelism assumptions)
6. If `external_partner.enabled = true` in project config:
   - Apply `handoff_overhead_weeks` if explicitly set
   - Otherwise, flag timezone/communication delta as a Risk item

**Constraints:**
- Minimum per item: 0.5 person-week
- Granularity: 0.5 increments only
- Prefer conservative over optimistic
- Use ranges (e.g. `1.0–1.5`) when confidence is low

**Exclude:** PM overhead, meetings, ceremonies, waiting time.

### Step 4.4 — Output the estimate table

Present **only** this markdown block (no preamble, no methodology, no closing remarks):

```markdown
## Epic <KEY>: <Title>

| Working Block | Description | Estimate (Person-Week) |
|---|---|---|
| <Category> | <What will be built — one line> | X.X |
| <Category> | <What will be built — one line> | X.X |
| **Total** | | **X.X weeks** |

**Assumptions:**
- <assumption> (max 3, one line each)

**Risks:**
- <risk description> (+X.Xw if realized) (max 3)
```

Then add:

```
---
Reply **approve** to post this to Jira, or ask for adjustments.
```

Store the table as `estimate_table`. Set `approved = false`. **Do NOT write to Jira yet.**

---

## Phase 5 — Refinement Loop

While `approved = false`:

- **If the user requests changes** (split items, adjust estimates, add context): apply the requested changes to `estimate_table` directly. Do not restart the full analysis — only modify the affected items. Re-present the updated table with the approval prompt.
- **If the user replies with an approval word** (`approve`, `yes`, `confirm`, `lgtm`): set `approved = true` and proceed to Phase 6.

If the user provides a **new epic key** mid-conversation, reset all state and restart from Phase 1.

---

## Phase 6 — Write to Jira

**Precondition:** `approved = true`. Never run this phase autonomously.

### Step 6.1 — Load credentials

```bash
source ~/.config/epic-estimator/.env
# Expects: JIRA_BASE_URL, JIRA_EMAIL, JIRA_API_TOKEN
```

If the file is missing or any variable is empty, report the error and stop. Do not attempt to prompt for credentials.

### Step 6.2 — Fetch current description

```bash
curl -s \
  -H "Authorization: Basic $(echo -n "$JIRA_EMAIL:$JIRA_API_TOKEN" | base64)" \
  -H "Content-Type: application/json" \
  "$JIRA_BASE_URL/rest/api/3/issue/<epic_key>?fields=description" \
  -o /tmp/jira-current-description.json
```

Parse `/tmp/jira-current-description.json` to extract the existing ADF document from `.fields.description`.

- If `description` is `null` or missing, treat it as an empty ADF doc: `{ "type": "doc", "version": 1, "content": [] }`
- If the fetch fails (non-200), report the error and stop

### Step 6.3 — Convert estimate to ADF and merge

Convert `estimate_table` into an ADF block. Use this structure:

```json
[
  { "type": "rule" },
  {
    "type": "paragraph",
    "content": [
      { "type": "text", "text": "Estimation (auto-generated)", "marks": [{ "type": "strong" }] }
    ]
  },
  {
    "type": "table",
    "attrs": { "isNumberColumnEnabled": false, "layout": "default" },
    "content": [
      {
        "type": "tableRow",
        "content": [
          { "type": "tableHeader", "content": [{ "type": "paragraph", "content": [{ "type": "text", "text": "Working Block" }] }] },
          { "type": "tableHeader", "content": [{ "type": "paragraph", "content": [{ "type": "text", "text": "Description" }] }] },
          { "type": "tableHeader", "content": [{ "type": "paragraph", "content": [{ "type": "text", "text": "Estimate (Person-Week)" }] }] }
        ]
      }
      // ... one tableRow per work item, plus totals row
    ]
  },
  {
    "type": "paragraph",
    "content": [{ "type": "text", "text": "Assumptions: ..." }]
  },
  {
    "type": "paragraph",
    "content": [{ "type": "text", "text": "Risks: ..." }]
  }
]
```

The leading `rule` node acts as a visual divider between the original description and the estimate.

**Append** these ADF nodes to the end of the existing description's `content` array to produce the merged ADF document.

### Step 6.4 — Write updated description

```bash
curl -s -o /tmp/jira-write-response.json -w "%{http_code}" \
  -X PUT \
  -H "Authorization: Basic $(echo -n "$JIRA_EMAIL:$JIRA_API_TOKEN" | base64)" \
  -H "Content-Type: application/json" \
  -d '{ "fields": { "description": <MERGED_ADF_DOC> } }' \
  "$JIRA_BASE_URL/rest/api/3/issue/<epic_key>"
```

Capture the HTTP status code.

### Step 6.5 — Report

**On success (HTTP 204):**
```
✅ Estimate appended to <epic_key> description in Jira.
```

**On failure:**
```
❌ Failed to update Jira description. HTTP <status_code>.
Response: <contents of /tmp/jira-write-response.json>
```

Do not retry automatically. Report the failure and let the user decide next steps.

---

## Hard Rules

- **Never write to Jira before `approved = true`.**
- **Never skip the Gate** — even if the user says "just estimate it".
- **Never fabricate epic content** — always fetch from Jira first.
- **Only ever modify the `description` field via PUT** — never POST comments, never touch any other field (summary, status, assignee, etc.).
- **Always fetch the current description first and append** — never overwrite the full description from scratch.
- **Never store or log credentials** beyond the current session.
- **If `epic_key` doesn't match the project's `jira_project_key`**, warn the user before writing.
- **If the user provides a new epic key mid-conversation, reset all state and restart from Phase 1.**
