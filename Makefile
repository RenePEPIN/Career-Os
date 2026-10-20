# Career OS — commandes de démarrage
# Usage : make help | make setup | make run | make test

PYTHON ?= python
VENV   := .venv

ifeq ($(OS),Windows_NT)
	SHELL := cmd.exe
	.SHELLFLAGS := /c
	BIN       := $(VENV)\Scripts
	PY        := $(BIN)\python.exe
	PIP       := $(PY) -m pip
	STREAMLIT := $(BIN)\streamlit.exe
	PYTEST    := $(BIN)\pytest.exe
	RUFF      := $(BIN)\ruff.exe
else
	BIN       := $(VENV)/bin
	PY        := $(BIN)/python
	PIP       := $(PY) -m pip
	STREAMLIT := $(BIN)/streamlit
	PYTEST    := $(BIN)/pytest
	RUFF      := $(BIN)/ruff
endif

.PHONY: help setup venv install install-dev data run test lint check-data clean

help:
	@$(PYTHON) -c "print('Career OS - commandes\n  make setup        Creer venv + deps + data seed\n  make venv         Creer le virtualenv .venv\n  make install      Installer requirements.txt\n  make install-dev  Installer pytest + ruff\n  make data         Creer data/*.json si absents\n  make run          Lancer Streamlit\n  make test         Lancer les tests\n  make lint         Verifier le code (ruff)\n  make check-data   Valider data/*.json\n  make clean        Supprimer .venv et caches')"

# --- Environnement -----------------------------------------------------------

setup: venv install install-dev data
	@$(PYTHON) -c "print('OK - pret. Lance : make run')"

venv:
	@$(PYTHON) -c "print('[venv] Creation de .venv')"
	$(PYTHON) -m venv $(VENV)

install: venv
	@$(PYTHON) -c "print('[install] Deps app')"
	$(PIP) install -r requirements.txt

install-dev: venv
	@$(PYTHON) -c "print('[install-dev] pytest + ruff')"
	$(PIP) install -r requirements-dev.txt

data:
	@$(PYTHON) -c "print('[data] Seed JSON si absents')"
	$(PYTHON) scripts/ensure_data.py

# --- App ---------------------------------------------------------------------

run:
	$(STREAMLIT) run app/main.py

# --- Qualite -----------------------------------------------------------------

test:
	$(PYTEST) -q

lint:
	$(RUFF) check app tests scripts

check-data:
	$(PY) scripts/ensure_data.py --check

# --- Nettoyage ---------------------------------------------------------------

clean:
	$(PYTHON) -c "import shutil, pathlib; [shutil.rmtree(p, ignore_errors=True) for p in map(pathlib.Path, ['.venv', '.pytest_cache', '.ruff_cache'])]; [shutil.rmtree(p, ignore_errors=True) for p in pathlib.Path('.').rglob('__pycache__')]"
