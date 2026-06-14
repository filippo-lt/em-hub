"""
M&A heartbeat data sources — one module per source, owned independently.

Each fetcher follows the same contract: return a value on success, or None on
any failure (missing access/config, network error, bad response). A fetcher
NEVER raises out — None renders downstream as `n/a (no access)`.

Re-exported here so callers can `import sources; sources.fetch_mrr(app)`.
"""

from .amplitude import fetch_mau
from .crashlytics import fetch_crash_free
from .gcp import fetch_cost
from .github import fetch_github
from .revenuecat import fetch_mrr

__all__ = [
    "fetch_mrr",        # revenuecat.py
    "fetch_mau",        # amplitude.py
    "fetch_crash_free", # crashlytics.py
    "fetch_cost",       # gcp.py
    "fetch_github",     # github.py
]
