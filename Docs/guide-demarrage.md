# Guide de démarrage — Career OS

Maquette de référence : [`Docs/images/Designer.png`](images/Designer.png) (« Mon Parcours »).

**Cœur MVP (uniquement ça pour l’instant)** : bloc *Progression globale* (skills + %) + bloc *Mes étapes clés* (goals).  
Sidebar complète, calendrier, projets, candidatures, ressources = **plus tard**.

Une seule tâche à la fois. Termine une étape avant la suivante.

---

## Étape 1 — Initialisation de l’environnement

### 1.1 Ouvre le projet dans Cursor

Dossier : `d:\Career-Os`

### 1.2 Setup en une commande (recommandé)

Terminal Cursor, à la racine du projet :

```powershell
cd d:\Career-Os
make setup
```

Cela crée `.venv`, installe Streamlit + pytest/ruff, et seed `data/*.json` si absents.

Commandes utiles ensuite :

| Commande | Rôle |
|----------|------|
| `make run` | Lancer l’app |
| `make test` | Tests smoke JSON |
| `make lint` | Ruff |
| `make help` | Liste des cibles |

### 1.3 Variante manuelle (sans make)

```powershell
cd d:\Career-Os
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt -r requirements-dev.txt
python scripts/ensure_data.py
```

Si scripts PowerShell bloqués : `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`

**Fin de l’étape 1** : `make setup` OK. Ne code rien d’autre.

---

## Étape 2 — Stockage minimal (JSON)

Pas de PostgreSQL. Deux fichiers locaux = source de vérité MVP.

Si tu as fait `make setup`, les fichiers existent déjà. Sinon :

```powershell
make data
```

Ou à la main : `python scripts/ensure_data.py`

Fichiers : `data/skills.json`, `data/goals.json`  
Statuts goals : `pending` | `in_progress` | `completed` | `cancelled`

Vérifier :

```powershell
make check-data
make test
```

**Fin de l’étape 2** : JSON OK + `make test` vert. Pas d’UI encore.

---

## Étape 3 — Brancher l’UI sur le JSON (cœur MVP)

Objectif : afficher **progression skills** + **étapes clés** depuis `data/` (cœur maquette).

**Mode mentor** (règle `.cursor/rules/mentor-mvp.mdc`) : une micro-tâche à la fois, pas de fichier entier collé.  
Exemple d’ordre (chaque ligne = une session mentor) :

1. Importer `json` + `Path` et définir `DATA_DIR` vers le dossier `data/`
2. Écrire une petite fonction qui charge un fichier JSON
3. Charger `skills` et afficher les barres `st.progress`
4. Charger `goals` et afficher la liste d’étapes
5. (Optionnel) moyenne des levels → métrique « progression globale »

Hors scope maintenant : sidebar, CRUD, calendrier, projets, candidatures, CSS thème.

**Fin de l’étape 3** : `make run` montre les données de `data/*.json` (plus le hardcode).

---

## Étape 4 — Tester en local

```powershell
make run
```

### Checklist

1. Skills du JSON visibles (ex. Python Fundamentals ~80 %)
2. Goals du JSON visibles (CV / CEP completed, PTP in_progress)
3. Modifier un `level` dans `data/skills.json` → reload → le % change

Arrêt : `Ctrl+C`.

---

## Ensuite

**CRUD Goals** (écriture JSON), une feature à la fois — `Docs/roadmap.md`.

## Référence maquette → MVP

| Zone maquette | Dans ce guide |
|---------------|---------------|
| Progression globale + skills | Oui (étape 3) |
| Mes étapes clés | Oui (étape 3) |
| Cartes PTP / Formation / Objectif / Motivation | Non |
| Calendrier | Non |
| Projets / Candidatures / Ressources | Non |
| Sidebar complète | Non |
