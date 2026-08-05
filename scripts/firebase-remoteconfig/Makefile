PYTHON ?= python3

.PHONY: help report publish setup share report-amp publish-amp share-amp

help:
	@echo "Firebase Remote Config fetch report — usage:"
	@echo "    make setup          Install Python deps (one-time)"
	@echo "    make report         Render reports/index.html"
	@echo "    make publish        Render + copy into em-hub/metrics/firebase-remoteconfig/"
	@echo "    make share          publish + HTML/MD share bundle + Cursor canvas dashboard"
	@echo "    make report-amp     report + Amplitude MAU cross-reference (fetches/user/day)"
	@echo "    make publish-amp    publish + Amplitude MAU cross-reference"
	@echo "    make share-amp      share + Amplitude MAU cross-reference"

setup:
	@$(PYTHON) -m pip install --break-system-packages -r requirements.txt

report:
	@$(PYTHON) run.py

publish:
	@$(PYTHON) run.py --publish

share:
	@$(PYTHON) run.py --publish --share

report-amp:
	@$(PYTHON) run.py --with-amplitude

publish-amp:
	@$(PYTHON) run.py --publish --with-amplitude

share-amp:
	@$(PYTHON) run.py --publish --share --with-amplitude
