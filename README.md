# Career OS

Tableau de bord personnel pour piloter une reconversion vers AI Engineer : objectifs, compétences, progression.

## État actuel (cohérent)

| Élément | État |
|---------|------|
| `data/*.json` | Seed prêt + tests OK |
| `app/main.py` | Lit `data/*.json` — skills + goals en 2 colonnes |
| Docs / Makefile / mentor | Alignés — voir [Docs/coherence.md](Docs/coherence.md) |

## Stack MVP

- Python 3 + Streamlit
- Persistance : JSON locaux
- Plus tard si besoin : Postgres / FastAPI / IA

## Lancer

```powershell
make setup    # venv + deps + data seed
make test     # smoke tests
make run      # Streamlit
```

`make help` pour le reste.

## Démarrer le développement MVP

1. Vérifier [Docs/coherence.md](Docs/coherence.md) = tout OK  
2. Suivre le mentor Cursor + [Docs/guide-demarrage.md](Docs/guide-demarrage.md) (étape 3+)  
3. Maquette : [Docs/images/Designer.png](Docs/images/Designer.png)

## Docs

| Fichier | Contenu |
|---------|---------|
| [Docs/coherence.md](Docs/coherence.md) | Checklist alignement |
| [Docs/guide-demarrage.md](Docs/guide-demarrage.md) | Setup + branchement UI |
| [Docs/vision.md](Docs/vision.md) | Mission |
| [Docs/architecture.md](Docs/architecture.md) | Structure |
| [Docs/roadmap.md](Docs/roadmap.md) | Étapes |
| [Docs/database.md](Docs/database.md) | Schéma JSON |
| [Docs/decisions.md](Docs/decisions.md) | Décisions |
| [Docs/changelog.md](Docs/changelog.md) | Historique |
| [Docs/journal-apprentissage.md](Docs/journal-apprentissage.md) | Notice de fabrication / cours |
