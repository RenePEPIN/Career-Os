# Décisions

Trace des choix figés. Éviter de changer sans raison écrite ici.

---

## 2026-10-20 — Projet Career OS

Application personnelle : goals, skills, progression vers AI Engineer. Un utilisateur.

---

## 2026-10-20 — Streamlit

UI en Streamlit pour aller vite en Python. Pas d’objectif frontend React sur ce projet. Réévaluable si multi-utilisateur un jour.

---

## 2026-10-20 — IA en dernier

Pas d’assistant IA / RAG tant que données + usage quotidien ne sont pas stables.

---

## 2026-10-20 — Docs dans le dépôt

Le dépôt Git est la source officielle (pas Notion / OneNote dispersés).

---

## 2026-10-20 — Simplification MVP (alignement code / docs)

**Problème** : docs décrivaient Feature First + service/repository + PostgreSQL + FastAPI + 10 versions, alors que le code est un seul fichier Streamlit hardcodé.

**Décision** :

- MVP = Streamlit + JSON + Dashboard / Goals / Skills
- Pas de couches service/repository tant que la logique tient dans les pages
- Postgres, API, auth, documents, RAG = reportés, conditionnés à un besoin réel
- Roadmap réduite à des étapes conditionnelles, pas une V1–V10 figée

---

## 2026-10-20 — Mentor Cursor

Règle `.cursor/rules/mentor-mvp.mdc` : une tâche à la fois, pas de code complet à la place de l’utilisateur, anti sur-engineering.

---

## 2026-10-20 — Cohérence avant code UI

**Décision** : UI hardcodée + JSON seed = état de départ validé (pas une dette cachée).  
Docs, guide, archi et roadmap décrivent cet état. Checklist : `Docs/coherence.md`.

**Décision** : pas de split `dashboard.py` / `goals.py` / `skills.py` tant que `main.py` reste lisible.

---

## Principe

Concevoir avant d’étendre. Construire petit. Documenter l’état réel, pas l’état rêvé.
