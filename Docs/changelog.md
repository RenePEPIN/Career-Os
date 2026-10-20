# Changelog

## 2026-10-20 — MVP lecture JSON

- `app/main.py` : skills + goals depuis `data/`, layout 2 colonnes
- Makefile, tests, seed, docs simplifiées, règle mentor, notice d’apprentissage

## 2026-10-20 — Journal d’apprentissage

- Ajout `Docs/journal-apprentissage.md` (premières notes : socle, Streamlit, DATA_DIR)

## 2026-10-20 — Reset UI

- Suppression de `app/main.py` (hardcode) pour recommencer le dashboard depuis zéro

## 2026-10-20 — Cohérence globale OK

- Checklist `Docs/coherence.md` : tous les statuts OK
- Archi / roadmap / database / guide / README alignés sur seed JSON + UI hardcodée volontaire
- Guide étape 3 = micro-tâches (compatible mentor)
- Suppression cache parasite ; ignore `pytest-cache-files-*/`

## 2026-10-20 — Makefile de démarrage

- Ajout `Makefile` : setup, run, test, lint, data, clean
- `requirements-dev.txt` (pytest, ruff)
- `scripts/ensure_data.py` + `tests/test_data.py`

## 2026-10-20 — Guide de démarrage

- Ajout `Docs/guide-demarrage.md` (4 étapes) calé sur la maquette `Designer.png`
- Cœur MVP : progression skills + étapes clés (reste de la maquette hors scope)

## 2026-10-20 — Alignement docs / réalité

- Docs réécrites pour coller au code actuel (prototype Streamlit hardcodé)
- Suppression des engagements prématurés : Feature First complet, Postgres, FastAPI, soft delete, auth, RAG
- Roadmap MVP : JSON + Goals + Skills + Dashboard
- `requirements.txt` réduit à Streamlit (suppression du dump Jupyter non utilisé)
