# Données

## État actuel

Persistance MVP en place : `data/skills.json` et `data/goals.json` (seed via `make data`).

L’UI (`app/main.py`) n’écrit / ne lit pas encore ces fichiers — prochain chantier, pas une absence de modèle.

Schéma réel = celui du seed (champs minimaux).

## skills.json

```json
[
  {
    "id": "s1",
    "name": "Python Fundamentals",
    "level": 80,
    "target_level": 100
  }
]
```

`level` / `target_level` : entier 0–100.

## goals.json

```json
[
  {
    "id": "g1",
    "title": "CV mis à jour",
    "status": "completed"
  }
]
```

Statuts : `pending` | `in_progress` | `completed` | `cancelled`.

## Commandes

```text
make data         # créer le seed si absent
make check-data   # valider
make test         # smoke tests
```

## Non retenu pour l’instant

PostgreSQL, UUID, soft delete, tables users / projects / formations / documents / journal / applications, champs `priority` / `created_at` (ajoutables plus tard si besoin).
