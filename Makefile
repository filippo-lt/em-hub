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
	@echo "  GCP spend report"
	@echo "    make gcp-spend [MONTH=YYYY-MM]   Run the report (default: $(LAST_MONTH))"
	@echo "    make gcp-spend-open              Open the most recently generated report"
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
	@latest=$$(ls -1 scripts/gcp-spend/reports/[0-9]*.html 2>/dev/null | sort | tail -1); \
	if [ -z "$$latest" ]; then \
	  echo "No reports found. Run: make gcp-spend"; exit 1; \
	fi; \
	echo "Opening $$latest"; \
	if command -v open >/dev/null 2>&1; then open "$$latest"; \
	elif command -v xdg-open >/dev/null 2>&1; then xdg-open "$$latest"; \
	else echo "Neither 'open' nor 'xdg-open' found. Path: $$latest"; \
	fi
