"""
M&A heartbeat data sources — one module per source, owned independently.

Each fetcher follows the same contract: return a value on success, or None on
any failure (missing access/config, network error, bad response). A fetcher
NEVER raises out — None renders downstream as `n/a (no access)`.

Cost + MAU are NOT fetched directly here — they come from the gcp-spend report
(the single source of truth, with per-app attribution + the $/MAU caveat) via
gcp_spend.py. Re-exported so callers can `import sources; sources.fetch_mrr(app)`.
"""

from .crashlytics import fetch_crash_free
from .gcp_spend import fetch_cost, fetch_mau
from .github import fetch_github
from .revenuecat import fetch_mrr

__all__ = [
    "fetch_mrr",        # revenuecat.py
    "fetch_mau",        # gcp_spend.py  (canonical, from the gcp-spend report)
    "fetch_crash_free", # crashlytics.py
    "fetch_cost",       # gcp_spend.py  (canonical, from the gcp-spend report)
    "fetch_github",     # github.py
]
