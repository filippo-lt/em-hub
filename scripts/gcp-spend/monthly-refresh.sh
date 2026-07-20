#!/bin/bash
# Monthly GCP spend refresh — run by launchd on the 2nd of each month
# (com.ftosetto.emhub.gcp-spend-refresh). Publishes last month's report into
# metrics/gcp-spend/ and pushes it so the "Monthly cost digest" cloud routine
# finds fresh data. Safe to run manually at any time.
set -euo pipefail

export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin"

REPO="$(cd "$(dirname "$0")/../.." && pwd)"
LOG_DIR="$REPO/scripts/gcp-spend/logs"
mkdir -p "$LOG_DIR"
exec >>"$LOG_DIR/refresh-$(date +%Y-%m).log" 2>&1

echo "=== $(date) refresh start ==="

cd "$REPO/scripts/gcp-spend"
make publish

cd "$REPO"
git pull --rebase --autostash origin main
git add metrics/gcp-spend
if git diff --cached --quiet; then
    echo "no changes to commit"
else
    git -c user.name="filippo-lt" -c user.email="filippo.tosetto@leadtech.com" \
        commit -m "Publish GCP spend report $(date -v-1m +%Y-%m)"
    git push origin main
fi

echo "=== $(date) refresh done ==="
