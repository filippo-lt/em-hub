#!/bin/bash
# email-audit — find everywhere an email address is used before disabling it.
#
# Usage:
#   scripts/email-audit/run.sh <email>
#   scripts/email-audit/run.sh ciklum@ext.leadtech.com
#
# Checks (all read-only):
#   1. GitHub code search across configured orgs
#   2. GitHub commit-author search per repo
#   3. Local git history across ~/Apps repos
#   4. GCP IAM bindings across all accessible projects
#   5. Jira assignee/watcher JQL search
#   6. This repo's config/ and docs
#
# Output: outputs/email-audit/<date>_<slug>.md
set -euo pipefail

readonly EMAIL="${1:-}"
if [[ -z "$EMAIL" ]]; then
  echo "Usage: $0 <email>" >&2
  exit 1
fi

readonly REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
readonly SLUG="$(echo "$EMAIL" | tr '@.' '__')"
readonly DATE="$(date +%Y-%m-%d)"
readonly OUT_DIR="$REPO_ROOT/outputs/email-audit"
readonly REPORT="$OUT_DIR/${DATE}_${SLUG}.md"
readonly WORKSPACE="${WORKSPACE:-$HOME/Apps}"

# GitHub orgs to scan (from config/repos.conf — rosseca + leadtechcorp)
readonly GH_ORGS=("rosseca" "leadtechcorp")

mkdir -p "$OUT_DIR"

# --- helpers -----------------------------------------------------------------

_log() { echo "$@" | tee -a "$REPORT"; }
_h1()  { _log ""; _log "# $1"; }
_h2()  { _log ""; _log "## $1"; }
_ok()  { _log "- ✓ $1"; }
_none(){ _log "- (none found) $1"; }
_warn(){ _log "- ⚠️  $1"; }

# --- start report ------------------------------------------------------------
cat > "$REPORT" <<EOF
# Email audit: \`$EMAIL\`

Generated: $(date)
Run by: scripts/email-audit/run.sh

All checks are read-only (GET / search). Manual checklist appended at the end.
EOF

_h1 "1. GitHub — code search"
for org in "${GH_ORGS[@]}"; do
  _h2 "org: $org"
  if results=$(gh search code "$EMAIL" --owner "$org" --json repository,path,textMatches \
        --limit 200 2>&1); then
    count=$(echo "$results" | jq 'length' 2>/dev/null || echo "0")
    if [[ "$count" -gt 0 ]]; then
      _ok "$count matches in $org"
      echo "$results" | jq -r '.[] | "  - \(.repository) : \(.path)"' | tee -a "$REPORT"
    else
      _none "in $org code search"
    fi
  else
    _warn "GitHub code search failed for $org: $results"
  fi
done

_h1 "2. GitHub — commit author search"
for org in "${GH_ORGS[@]}"; do
  _h2 "org: $org"
  repos=$(gh repo list "$org" --limit 300 --json name -q '.[].name' 2>/dev/null || echo "")
  if [[ -z "$repos" ]]; then
    _warn "could not list repos for $org"
    continue
  fi
  found_any=false
  for repo in $repos; do
    if commits=$(gh api "repos/$org/$repo/commits?author=$EMAIL&per_page=5" \
          -q 'length' 2>/dev/null) && [[ "$commits" -gt 0 ]]; then
      _ok "$commits commits by author in $org/$repo"
      found_any=true
    fi
  done
  $found_any || _none "commits by author in $org"
done

_h1 "3. Local git history (~/Apps)"
if [[ -d "$WORKSPACE" ]]; then
  found_any=false
  while IFS= read -r repo; do
    if [[ -d "$repo/.git" ]]; then
      if count=$(git -C "$repo" log --all --author="$EMAIL" --oneline 2>/dev/null | wc -l | tr -d ' '); then
        if [[ "$count" -gt 0 ]]; then
          _ok "$count commits in ${repo#$WORKSPACE/}"
          git -C "$repo" log --all --author="$EMAIL" --oneline -5 2>/dev/null \
            | sed 's/^/    /' | tee -a "$REPORT"
          found_any=true
        fi
      fi
    fi
  done < <(find "$WORKSPACE" -maxdepth 2 -type d 2>/dev/null)
  $found_any || _none "commits by author in local repos"
else
  _warn "workspace dir not found: $WORKSPACE"
fi

_h1 "4. GCP — IAM bindings"
if command -v gcloud >/dev/null 2>&1; then
  found_any=false
  while IFS= read -r proj; do
    [[ -z "$proj" ]] && continue
    if bindings=$(gcloud projects get-iam-policy "$proj" \
          --flatten="bindings[].members" \
          --filter="bindings.members:\"$EMAIL\"" \
          --format="value(bindings.role)" 2>/dev/null); then
      if [[ -n "$bindings" ]]; then
        _ok "project \`$proj\`:"
        echo "$bindings" | sed 's/^/    /' | tee -a "$REPORT"
        found_any=true
      fi
    fi
  done < <(gcloud projects list --format="value(projectId)" 2>/dev/null)
  $found_any || _none "IAM bindings in any project"
else
  _warn "gcloud not installed"
fi

_h1 "5. Jira — assignee / watcher"
if [[ -f "$HOME/.config/jira/.env" ]]; then
  # shellcheck disable=SC1090
  source "$HOME/.config/jira/.env"
  for field in assignee watcher; do
    jql="$field = \"$EMAIL\""
    if resp=$(curl -s -u "$JIRA_EMAIL:$JIRA_API_TOKEN" \
          -H "Content-Type: application/json" \
          -X POST "$JIRA_BASE_URL/rest/api/3/search" \
          -d "{\"jql\":\"$jql\",\"maxResults\":50,\"fields\":[\"summary\",\"status\"]}" 2>/dev/null); then
      total=$(echo "$resp" | jq -r '.total // 0' 2>/dev/null || echo "0")
      if [[ "$total" -gt 0 ]]; then
        _ok "$total issues with $field = $EMAIL"
        echo "$resp" | jq -r '.issues[] | "    \(.key): \(.fields.summary)"' 2>/dev/null | tee -a "$REPORT"
      else
        _none "issues with $field = $EMAIL"
      fi
    else
      _warn "Jira $field query failed"
    fi
  done
else
  _warn "Jira creds not found at ~/.config/jira/.env"
fi

_h1 "6. This repo — config & docs"
if hits=$(rg -l --hidden "$EMAIL" "$REPO_ROOT" \
      --glob '!outputs/**' --glob '!.git/**' 2>/dev/null); then
  if [[ -n "$hits" ]]; then
    while IFS= read -r f; do
      _ok "${f#$REPO_ROOT/}"
      rg -n "$EMAIL" "$f" 2>/dev/null | sed 's/^/    /' | tee -a "$REPORT"
    done <<< "$hits"
  else
    _none "references in this repo"
  fi
fi

_h1 "Manual checks (not automatable)"
cat <<'EOF' | tee -a "$REPORT"
- [ ] App Store Connect — Users & Access
- [ ] Google Play Console — user list
- [ ] Apple Developer Team — member list
- [ ] PagerDuty / Opsgenie — on-call schedules & escalation policies
- [ ] Slack — app config & webhook owners
- [ ] Google Chat — space membership & webhook senders
- [ ] Codemagic — team members & notification recipients (web UI)
- [ ] Firebase App Distribution — testers/admins
- [ ] Vendor portals (Ciklum) — confirm they don't rely on it on their side
- [ ] Procurement / PO systems — billing contact
- [ ] SSO / Google Workspace — confirm identity type & cascade effects
- [ ] Long-lived API tokens tied to the identity (per-service audit)
- [ ] Calendar ownership & meeting organizer transfer
- [ ] SSL certificate notification recipients
- [ ] DNS / domain registrar technical contact
EOF

_log ""
_log "---"
_log "Report saved to: \`$REPORT\`"
echo ""
echo "Done. Report: $REPORT"
