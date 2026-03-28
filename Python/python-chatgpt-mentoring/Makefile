.DEFAULT_GOAL := help

PYTHON ?= python3
VENV ?= venv
PIP := $(VENV)/bin/pip
PY := $(VENV)/bin/python

.PHONY: help venv install freeze run run-class05 run-class06 run-class07 run-uvicorn run-uvicorn-class07 clone-class class06-refresh class07-refresh test lint format clean

help: ## Show available commands
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make <target>\n"} /^[a-zA-Z0-9_.-]+:.*##/ {printf "  %-14s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

##@ Setup
venv: ## Create virtual environment
	$(PYTHON) -m venv $(VENV)

install: ## Install dependencies from requirements.txt
	$(PIP) install -r requirements.txt

freeze: ## Write installed packages to requirements.txt
	$(PIP) freeze > requirements.txt

##@ Run
run: ## Run main script
	$(PY) main.py

run-class05: ## Run class_05 module
	$(PY) -m class_05.main

run-class06: ## Run class_06 module
	$(PY) -m class_06.main

run-class07: ## Run class_07 module
	$(PY) -m class_07.main

run-uvicorn: ## Run class_07 FastAPI server with uvicorn (default)
	$(PY) -m uvicorn class_07.api:app --reload

run-uvicorn-class07: ## Run class_07 FastAPI server with uvicorn
	$(PY) -m uvicorn class_07.api:app --reload

##@ Automation
clone-class: ## Clone class folder + update imports + zip (usage: make clone-class SRC=class_05 DST=class_06)
	@test -n "$(SRC)" || (echo "SRC is required, e.g. SRC=class_05" && exit 1)
	@test -n "$(DST)" || (echo "DST is required, e.g. DST=class_06" && exit 1)
	@test "$(SRC)" != "$(DST)" || (echo "SRC and DST must be different" && exit 1)
	@test -d "$(SRC)" || (echo "Source folder '$(SRC)' does not exist" && exit 1)
	rm -rf "$(DST)"
	cp -r "$(SRC)" "$(DST)"
	find "$(DST)" -type f -name "*.py" -exec sed -i "s/from $(SRC)\./from $(DST)\./g; s/import $(SRC)\./import $(DST)\./g; s/from $(SRC) import/from $(DST) import/g; s/import $(SRC)$$/import $(DST)/g" {} +
	zip -r "$(DST).zip" "$(DST)"

class06-refresh: ## Rebuild class_06 from class_05, update imports, and zip
	$(MAKE) clone-class SRC=class_05 DST=class_06

class07-refresh: ## Rebuild class_07 from class_06, update imports, and zip
	$(MAKE) clone-class SRC=class_06 DST=class_07

##@ Quality
test: ## Run tests (if present)
	$(PY) -m pytest -q

lint: ## Run Ruff linter (if installed)
	$(PY) -m ruff check .

format: ## Format with Black (if installed)
	$(PY) -m black .

##@ Cleanup
clean: ## Remove Python cache files
	find . -type d -name "__pycache__" -prune -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
