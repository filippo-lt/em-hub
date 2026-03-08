#!/usr/bin/env bash
set -euo pipefail

# =============================================================================
# gh-metrics.sh — Collect GitHub metrics for external developers in parallel
#
# Usage:
#   gh-metrics.sh --start YYYY-MM-DD --end YYYY-MM-DD [--dev "Name"] [--project "Name"]
#
# Reads contractors/registry.md and contractors/projects.md to determine scope,
# then queries GitHub API in parallel. Outputs structured JSON.
# =============================================================================

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
HUB_ROOT="$SCRIPT_DIR/.."
REGISTRY="$HUB_ROOT/contractors/registry.md"
PROJECTS_FILE="$HUB_ROOT/contractors/projects.md"
MAX_PARALLEL=4

START=""
END=""
FILTER_DEV=""
FILTER_PROJECT=""
OUTPUT_PATH=""

# --- Helpers ----------------------------------------------------------------

usage() {
  cat <<EOF
Usage: $(basename "$0") --start YYYY-MM-DD --end YYYY-MM-DD [OPTIONS]

Options:
  --start DATE       Start date (required)
  --end DATE         End date (required)
  --dev "Name"       Filter to a single developer
  --project "Name"   Filter to a project
  --output PATH      Override output file path
  -h, --help         Show this help

Output: contractors/reports/{start}_to_{end}_gh-metrics.json
EOF
  exit 1
}

log()   { echo "[gh-metrics] $*" >&2; }
warn()  { echo "[WARN] $*" >&2; }
error() { echo "[ERROR] $*" >&2; }

# Normalize a string for comparison: lowercase, remove spaces
normalize() {
  echo "$1" | tr '[:upper:]' '[:lower:]' | tr -d ' '
}

# --- Argument Parsing -------------------------------------------------------

while [[ $# -gt 0 ]]; do
  case "$1" in
    --start)   START="$2"; shift 2 ;;
    --end)     END="$2"; shift 2 ;;
    --dev)     FILTER_DEV="$2"; shift 2 ;;
    --project) FILTER_PROJECT="$2"; shift 2 ;;
    --output)  OUTPUT_PATH="$2"; shift 2 ;;
    -h|--help) usage ;;
    *) echo "Unknown option: $1"; usage ;;
  esac
done

if [[ -z "$START" || -z "$END" ]]; then
  echo "Error: --start and --end are required."
  usage
fi

if ! [[ "$START" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]] || ! [[ "$END" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]]; then
  echo "Error: dates must be YYYY-MM-DD format."
  exit 1
fi

if [[ -z "$OUTPUT_PATH" ]]; then
  OUTPUT_PATH="$HUB_ROOT/contractors/reports/${START}_to_${END}_gh-metrics.json"
fi

# --- Prerequisites ----------------------------------------------------------

for cmd in gh jq; do
  if ! command -v "$cmd" &>/dev/null; then
    echo "Error: '$cmd' is required but not installed."
    exit 1
  fi
done

if ! gh auth status &>/dev/null; then
  echo "Error: 'gh' is not authenticated. Run 'gh auth login' first."
  exit 1
fi

# --- Temp directory ---------------------------------------------------------

TMP=$(mktemp -d)
mkdir -p "$TMP/results"
trap 'rm -rf "$TMP"' EXIT

# --- Parse Registry ---------------------------------------------------------

log "Parsing registry: $REGISTRY"

parse_registry() {
  # Extract table rows (lines starting with |), skip header and separator
  local line_num=0
  while IFS= read -r line; do
    # Only process lines that look like table data rows (start with |, contain data)
    [[ "$line" =~ ^\| ]] || continue
    # Skip header row and separator row
    line_num=$((line_num + 1))
    [[ $line_num -le 2 ]] && continue
    # Skip HTML comments
    [[ "$line" =~ ^\<\!-- ]] && continue

    # Parse fields (awk with | delimiter, trim whitespace)
    local name vendor skills projects username active
    name=$(echo "$line" | awk -F'|' '{gsub(/^[ \t]+|[ \t]+$/, "", $2); print $2}')
    vendor=$(echo "$line" | awk -F'|' '{gsub(/^[ \t]+|[ \t]+$/, "", $3); print $3}')
    skills=$(echo "$line" | awk -F'|' '{gsub(/^[ \t]+|[ \t]+$/, "", $4); print $4}')
    projects=$(echo "$line" | awk -F'|' '{gsub(/^[ \t]+|[ \t]+$/, "", $5); print $5}')
    username=$(echo "$line" | awk -F'|' '{gsub(/^[ \t]+|[ \t]+$/, "", $6); print $6}')
    active=$(echo "$line" | awk -F'|' '{gsub(/^[ \t]+|[ \t]+$/, "", $8); print $8}')

    # Skip inactive devs
    [[ "$(normalize "$active")" == "yes" ]] || continue
    # Skip empty rows
    [[ -n "$name" ]] || continue

    # Apply filters
    if [[ -n "$FILTER_DEV" ]]; then
      [[ "$(normalize "$name")" == "$(normalize "$FILTER_DEV")" ]] || continue
    fi
    if [[ -n "$FILTER_PROJECT" ]]; then
      local match=false
      IFS=',' read -ra proj_list <<< "$projects"
      for p in "${proj_list[@]}"; do
        p=$(echo "$p" | xargs) # trim
        if [[ "$(normalize "$p")" == "$(normalize "$FILTER_PROJECT")" ]]; then
          match=true
          break
        fi
      done
      [[ "$match" == "true" ]] || continue
    fi

    # Output: tab-separated
    printf '%s\t%s\t%s\t%s\t%s\n' "$name" "$vendor" "$skills" "$projects" "$username"
  done < "$REGISTRY"
}

parse_registry > "$TMP/developers.tsv"

dev_count=$(wc -l < "$TMP/developers.tsv" | tr -d ' ')
if [[ "$dev_count" -eq 0 ]]; then
  warn "No developers matched the filters."
  # Write empty JSON
  jq -n --arg start "$START" --arg end "$END" --arg gen "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
    '{period: {start: $start, end: $end}, generated: $gen, developers: []}' > "$OUTPUT_PATH"
  log "Empty report saved to: $OUTPUT_PATH"
  exit 0
fi
log "Found $dev_count developer(s)"

# --- Parse Projects ---------------------------------------------------------

log "Parsing projects: $PROJECTS_FILE"

parse_projects() {
  local current_project=""
  while IFS= read -r line; do
    # Detect project headers: ### ProjectName
    if [[ "$line" =~ ^###[[:space:]]+(.+)$ ]]; then
      current_project="${BASH_REMATCH[1]}"
      current_project=$(echo "$current_project" | xargs) # trim
      continue
    fi
    # Detect GitHub repo rows (match both "GitHub Repo" and "GitHub Repo(s)")
    if [[ -n "$current_project" ]] && echo "$line" | grep -qi "github repo"; then
      local url
      url=$(echo "$line" | awk -F'|' '{gsub(/^[ \t]+|[ \t]+$/, "", $3); print $3}')
      # Strip https://github.com/ prefix and trailing slash
      local owner_repo
      owner_repo=$(echo "$url" | sed 's|https://github.com/||' | sed 's|/$||')
      [[ -n "$owner_repo" ]] || continue
      printf '%s\t%s\n' "$current_project" "$owner_repo"
    fi
  done < "$PROJECTS_FILE"
}

parse_projects > "$TMP/project_repos.tsv"
log "Found $(wc -l < "$TMP/project_repos.tsv" | tr -d ' ') project-repo mapping(s)"

# --- Build Work Matrix ------------------------------------------------------

log "Building work matrix..."

build_work_matrix() {
  while IFS=$'\t' read -r name vendor skills projects username; do
    # Split comma-separated projects
    IFS=',' read -ra proj_list <<< "$projects"
    for proj in "${proj_list[@]}"; do
      proj=$(echo "$proj" | xargs) # trim
      local norm_proj
      norm_proj=$(normalize "$proj")

      # Find repos for this project (normalized comparison)
      local found=false
      while IFS=$'\t' read -r p_name p_repo; do
        if [[ "$(normalize "$p_name")" == "$norm_proj" ]]; then
          printf '%s\t%s\t%s\t%s\t%s\t%s\n' "$name" "$username" "$vendor" "$skills" "$proj" "$p_repo"
          found=true
        fi
      done < "$TMP/project_repos.tsv"

      if [[ "$found" == "false" ]]; then
        warn "Project '$proj' for dev '$name' not found in projects.md"
      fi
    done
  done < "$TMP/developers.tsv"
}

build_work_matrix > "$TMP/work_items.tsv"

work_count=$(wc -l < "$TMP/work_items.tsv" | tr -d ' ')
log "Work items: $work_count (dev x repo pairs)"

if [[ "$work_count" -eq 0 ]]; then
  warn "No work items to process (no dev-repo pairs found)."
  exit 1
fi

# --- Collect Metrics (per dev x repo pair) ----------------------------------

collect_one() {
  local username="$1" owner_repo="$2" start="$3" end="$4" outfile="$5"

  local commits=0 prs_json="[]" reviews_count=0

  # 1. Commits
  commits=$(gh api "/repos/${owner_repo}/commits?author=${username}&since=${start}T00:00:00Z&until=${end}T23:59:59Z&per_page=100" \
    --paginate 2>/dev/null | jq -s 'add | length' 2>/dev/null) || commits=0
  [[ "$commits" =~ ^[0-9]+$ ]] || commits=0

  # 2. PRs merged
  prs_json=$(gh pr list --repo "${owner_repo}" --author "${username}" --state merged \
    --search "merged:${start}..${end}" --limit 200 \
    --json number,additions,deletions,createdAt,mergedAt 2>/dev/null) || prs_json="[]"
  # Validate JSON
  echo "$prs_json" | jq empty 2>/dev/null || prs_json="[]"

  # 3. PR reviews (PRs reviewed by this user, excluding their own)
  reviews_count=$(gh api "/search/issues?q=type:pr+repo:${owner_repo}+reviewed-by:${username}+merged:${start}..${end}+-author:${username}&per_page=1" \
    2>/dev/null | jq '.total_count // 0' 2>/dev/null) || reviews_count=0
  [[ "$reviews_count" =~ ^[0-9]+$ ]] || reviews_count=0

  # 4. Compute derived metrics and write result
  echo "$prs_json" | jq \
    --argjson commits "$commits" \
    --argjson reviews "$reviews_count" \
    '{
      commits: $commits,
      prs_merged_count: length,
      prs_merged: [.[] | {number, additions, deletions, createdAt, mergedAt}],
      prs_reviewed: $reviews,
      avg_pr_size: (if length > 0 then ([.[] | .additions + .deletions] | add / length | . * 10 | round / 10) else 0 end),
      avg_time_to_merge_hours: (if length > 0 then
        ([.[] |
          ((.mergedAt | gsub("\\.[0-9]+Z$"; "Z") | strptime("%Y-%m-%dT%H:%M:%SZ") | mktime) -
           (.createdAt | gsub("\\.[0-9]+Z$"; "Z") | strptime("%Y-%m-%dT%H:%M:%SZ") | mktime)) / 3600
        ] | add / length | . * 10 | round / 10)
        else 0 end)
    }' > "$outfile" 2>/dev/null

  # If jq failed, write a fallback
  if [[ ! -s "$outfile" ]]; then
    echo '{"commits":0,"prs_merged_count":0,"prs_merged":[],"prs_reviewed":0,"avg_pr_size":0,"avg_time_to_merge_hours":0,"error":"jq computation failed"}' > "$outfile"
  fi
}

log "Collecting GitHub metrics (max $MAX_PARALLEL parallel)..."

running=0
while IFS=$'\t' read -r name username vendor skills project owner_repo; do
  safe_repo=$(echo "$owner_repo" | sed 's|/|__|')
  outfile="$TMP/results/${username}__${safe_repo}.json"

  log "  -> $username @ $owner_repo"
  collect_one "$username" "$owner_repo" "$START" "$END" "$outfile" &
  running=$((running + 1))

  # Throttle: if we've hit max parallel, wait for one to finish
  if [[ "$running" -ge "$MAX_PARALLEL" ]]; then
    wait -n 2>/dev/null || wait  # wait -n is bash 4.3+; fall back to wait-all
    running=$((running - 1))
  fi
done < "$TMP/work_items.tsv"
wait  # wait for remaining background jobs

log "Collection complete. Assembling JSON..."

# --- Assemble JSON ----------------------------------------------------------

assemble_json() {
  local developers_json="[]"

  # Get unique developers (by username — but a username could appear for multiple devs)
  # Use the developers.tsv which has one row per dev
  while IFS=$'\t' read -r name vendor skills projects username; do
    # Build the repos object for this developer
    local repos_json="{}"

    # Find all result files for this username
    for result_file in "$TMP/results/${username}"__*.json; do
      [[ -f "$result_file" ]] || continue
      # Extract owner/repo from filename: username__owner__repo.json
      local basename_file
      basename_file=$(basename "$result_file" .json)
      # Remove username__ prefix (username + __ = username__)
      local repo_part="${basename_file#${username}__}"
      # The repo was stored as owner__repo, convert first __ back to /
      local owner_repo
      owner_repo=$(echo "$repo_part" | sed 's/__/\//')

      local repo_data
      repo_data=$(cat "$result_file" 2>/dev/null || echo '{}')
      # Validate JSON before using it
      if ! echo "$repo_data" | jq empty 2>/dev/null; then
        repo_data='{"commits":0,"prs_merged_count":0,"prs_merged":[],"prs_reviewed":0,"avg_pr_size":0,"avg_time_to_merge_hours":0,"error":"invalid json in result file"}'
      fi

      repos_json=$(echo "$repos_json" | jq --arg repo "$owner_repo" --argjson data "$repo_data" '. + {($repo): $data}')
    done

    # Build projects array from comma-separated string
    local projects_json
    projects_json=$(echo "$projects" | tr ',' '\n' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//' | jq -R . | jq -s .)

    # Compute totals across all repos
    local totals
    totals=$(echo "$repos_json" | jq '
      to_entries | map(.value) |
      {
        total_commits: (map(.commits) | add // 0),
        total_prs_merged: (map(.prs_merged_count) | add // 0),
        total_prs_reviewed: (map(.prs_reviewed) | add // 0),
        total_avg_pr_size: (if (map(select(.prs_merged_count > 0)) | length) > 0
          then (map(select(.prs_merged_count > 0) | .avg_pr_size * .prs_merged_count) | add) /
               (map(select(.prs_merged_count > 0) | .prs_merged_count) | add) | . * 10 | round / 10
          else 0 end),
        total_avg_ttm_hours: (if (map(select(.prs_merged_count > 0)) | length) > 0
          then (map(select(.prs_merged_count > 0) | .avg_time_to_merge_hours * .prs_merged_count) | add) /
               (map(select(.prs_merged_count > 0) | .prs_merged_count) | add) | . * 10 | round / 10
          else 0 end)
      }
    ')

    # Build developer object
    local dev_json
    dev_json=$(jq -n \
      --arg name "$name" \
      --arg username "$username" \
      --arg vendor "$vendor" \
      --arg skills "$skills" \
      --argjson projects "$projects_json" \
      --argjson repos "$repos_json" \
      --argjson totals "$totals" \
      '{
        name: $name,
        github_username: $username,
        vendor: $vendor,
        skills: $skills,
        projects: $projects,
        totals: $totals,
        repos: $repos
      }')

    developers_json=$(echo "$developers_json" | jq --argjson dev "$dev_json" '. + [$dev]')
  done < "$TMP/developers.tsv"

  # Final envelope
  jq -n \
    --arg start "$START" \
    --arg end "$END" \
    --arg generated "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
    --argjson developers "$developers_json" \
    '{
      period: { start: $start, end: $end },
      generated: $generated,
      developers: $developers
    }'
}

assemble_json > "$OUTPUT_PATH"

# --- Summary ----------------------------------------------------------------

log "Report saved to: $OUTPUT_PATH"
log "Developers: $dev_count"
log "Repo pairs queried: $work_count"

# Count errors
error_count=$(find "$TMP/results" -name '*.json' -exec grep -l '"error"' {} \; 2>/dev/null | wc -l | tr -d ' ')
if [[ "$error_count" -gt 0 ]]; then
  warn "$error_count repo pair(s) had errors — check the JSON for details"
fi

log "Done."
