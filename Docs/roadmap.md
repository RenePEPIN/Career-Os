# Roadmap

Approche : petit, utile, utilisable.

## Fait

- [x] Socle projet (docs, Makefile, JSON, tests, mentor)
- [x] Seed `data/goals.json` + `data/skills.json`
- [x] Dashboard : lit JSON — skills + goals en 2 colonnes
- [x] Notice `Docs/journal-apprentissage.md`

## Prochaine étape — CRUD

1. Modifier un goal / skill depuis l’UI (écriture JSON)
2. Une feature à la fois

**DoD MVP** : goals/skills modifiables, dashboard fidèle aux JSON, zéro Docker / Postgres / API.

## Ensuite (si usage réel)

| Étape | Condition |
|-------|-----------|
| Projects | MVP utilisé ≥ 1 semaine |
| Journal temps | Besoin de suivi heures |
| SQLite / Postgres | JSON limitant |
| Documents / IA | Fondations stables + besoin clair |

## Hors scope

Auth multi-utilisateur, JWT, microservices, RAG en prod, Docker obligatoire.
