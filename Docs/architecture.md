# Architecture

## État réel (figé avant démarrage MVP UI)

```text
career-os/
├── app/
│   └── main.py              # Streamlit — lit skills + goals (2 colonnes)
├── data/
│   ├── goals.json
│   └── skills.json
├── scripts/
│   └── ensure_data.py
├── tests/
│   └── test_data.py
├── Docs/
├── .cursor/rules/
│   └── mentor-mvp.mdc
├── Makefile
├── requirements.txt
├── requirements-dev.txt
└── README.md
```

Pas de service/repository, pas de Postgres, pas d’API.

**Fait** : lecture JSON + affichage maquette (skills | goals).  
**Ensuite** : CRUD (écriture JSON depuis l’UI).

## Cible MVP (simple)

Rester sur **un seul** `app/main.py` tant que ça tient. Pas de sur-découpage.

## Stack

| Phase | Stack |
|-------|--------|
| Maintenant | Python + Streamlit + JSON (lecture OK) |
| Ensuite | Écriture JSON (CRUD) |
| Plus tard (si besoin) | SQLite/Postgres → FastAPI → RAG |

## Flux cible

```text
Utilisateur → main.py (Streamlit) → data/*.json → affichage
```

## Principes

1. Simplicité avant abstraction
2. Un fichier tant que c’est clair
3. Docs = état réel
