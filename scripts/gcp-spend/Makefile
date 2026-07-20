PYTHON ?= python3

ifeq ($(shell uname),Darwin)
LAST_MONTH := $(shell date -v-1m +%Y-%m)
else
LAST_MONTH := $(shell date -d "last month" +%Y-%m)
endif

MONTH ?= $(LAST_MONTH)

.PHONY: help report publish setup

help:
	@echo "GCP spend report (vendored, headless) — usage:"
	@echo "    make setup                     Install Python deps (one-time per environment)"
	@echo "    make report [MONTH=YYYY-MM]    Render dashboard + focal month (default: $(LAST_MONTH))"
	@echo "    make publish [MONTH=YYYY-MM]   Render + copy into em-hub/metrics/gcp-spend/"
	@echo ""
	@echo "Auth is non-interactive: a service-account key at secrets/gcp-sa-key.json"
	@echo "(pointed to by GCP_SA_KEY_FILE in .env). See SETUP-HEADLESS.md."

setup:
	@$(PYTHON) -m pip install --break-system-packages -r requirements.txt

report:
	@$(PYTHON) run.py --month $(MONTH)

publish:
	@$(PYTHON) run.py --month $(MONTH) --publish
