# em-hub Makefile — convenience wrappers for repo tools.
#
# Default target prints help. Add new tools as their own .PHONY targets below.

PYTHON ?= python3

# "Last completed calendar month" in YYYY-MM. Tries BSD date (macOS) first,
# falls back to GNU date (Linux). Used as the default for `make gcp-spend`.
LAST_MONTH := $(shell date -v-1m +%Y-%m 2>/dev/null || date -d "last month" +%Y-%m)
MONTH ?= $(LAST_MONTH)

.PHONY: help gcp-spend gcp-spend-setup gcp-spend-open

# ── Default ───────────────────────────────────────────────────────────────
help:
	@echo "em-hub — make targets"
	@echo ""
	@echo "  GCP spend reports"
	@echo "    make gcp-spend [MONTH=YYYY-MM]   Generate dashboard + focal month (default: $(LAST_MONTH))"
	@echo "    make gcp-spend-open              Open the dashboard"
	@echo "    make gcp-spend-setup             One-time: install deps + ADC login"
	@echo ""

# ── GCP spend ─────────────────────────────────────────────────────────────
gcp-spend:
	@$(PYTHON) scripts/gcp-spend/run.py --month $(MONTH)

gcp-spend-setup:
	@$(PYTHON) -m pip install -r scripts/gcp-spend/requirements.txt
	@echo ""
	@echo "Now authorize Application Default Credentials (browser will open):"
	@gcloud auth application-default login

gcp-spend-open:
	@dash=scripts/gcp-spend/reports/index.html; \
	if [ ! -f "$$dash" ]; then \
	  echo "Dashboard not found. Run: make gcp-spend"; exit 1; \
	fi; \
	echo "Opening $$dash"; \
	if command -v open >/dev/null 2>&1; then open "$$dash"; \
	elif command -v xdg-open >/dev/null 2>&1; then xdg-open "$$dash"; \
	else echo "Neither 'open' nor 'xdg-open' found. Path: $$dash"; \
	fi
