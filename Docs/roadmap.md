# Roadmap

## Vision générale

Career OS est développé progressivement selon une approche incrémentale.

Chaque version doit être :

- Utilisable
- Maintenable
- Documentée
- Testée
- Évolutive

L'objectif n'est pas seulement de construire une application, mais également de progresser vers le métier d'AI Engineer en appliquant de bonnes pratiques d'ingénierie logicielle.

---

# V1 — MVP : Visualisation et Suivi

## Objectif

Créer une première version exploitable permettant de piloter la reconversion professionnelle.

## Fonctionnalités

### Dashboard

- Progression globale
- Objectif principal
- Compétences clés
- Projets actifs

### Goals

CRUD complet :

- Créer un objectif
- Modifier un objectif
- Supprimer un objectif
- Marquer comme terminé

### Skills

CRUD complet :

- Ajouter une compétence
- Évaluer un niveau
- Suivre la progression

## Compétences travaillées

- Python
- Streamlit
- Git
- GitHub
- Architecture de projet

## Livrable

Première version utilisable localement.

---

# V2 — Gestion des Projets

## Objectif

Centraliser les projets personnels et professionnels.

## Fonctionnalités

### Projects

CRUD complet :

- Nom
- Description
- Statut
- Technologies
- Lien GitHub

### Dashboard Projet

- Nombre de projets
- Projets actifs
- Projets terminés

## Compétences travaillées

- Organisation métier
- Modélisation de données
- Refactoring

## Livrable

Portfolio centralisé.

---

# V3 — Journal d'Apprentissage

## Objectif

Conserver l'historique des apprentissages.

## Fonctionnalités

### Journal

- Date
- Temps investi
- Sujet étudié
- Difficultés rencontrées
- Notes personnelles

### Statistiques

- Temps total d'apprentissage
- Répartition par compétence
- Suivi hebdomadaire

## Compétences travaillées

- Manipulation de données
- Reporting
- Gestion d'état

## Livrable

Historique complet de progression.

---

# V4 — Base de Données

## Objectif

Remplacer les données statiques par une base relationnelle.

## Évolutions

Migration vers :

- PostgreSQL
- SQLAlchemy

Création des premières tables :

- goals
- skills
- projects
- journal_entries

## Compétences travaillées

- SQL
- PostgreSQL
- Modélisation relationnelle
- ORM

## Livrable

Données persistantes.

---

# V5 — API Backend

## Objectif

Séparer la logique métier de l'interface utilisateur.

## Fonctionnalités

API REST :

- Goals
- Skills
- Projects
- Journal

## Stack

- FastAPI
- Pydantic
- PostgreSQL

## Compétences travaillées

- REST
- Validation de données
- Architecture Backend

## Livrable

Backend autonome.

---

# V6 — Qualité Logicielle

## Objectif

Réduire les régressions et la dette technique.

## Fonctionnalités

Mise en place de :

- Pytest
- Couverture de tests
- Linting
- Formatage automatique

## Outils

- Pytest
- Ruff
- Black

## Livrable

Pipeline de qualité minimale.

---

# V7 — Authentification

## Objectif

Préparer une utilisation multi-utilisateur.

## Fonctionnalités

- Inscription
- Connexion
- Déconnexion
- Profil utilisateur

## Technologies

- JWT
- FastAPI

## Livrable

Gestion sécurisée des comptes.

---

# V8 — Gestion Documentaire

## Objectif

Centraliser tous les documents importants.

## Fonctionnalités

### Documents

- Upload
- Téléchargement
- Classement
- Recherche

### Types

- CV
- Diplômes
- Dossier PTP
- Certificats
- Ressources techniques

## Livrable

Bibliothèque documentaire personnelle.

---

# V9 — Intelligence Artificielle

## Objectif

Créer un assistant personnel de recherche.

## Fonctionnalités

Recherche dans :

- Documents
- Journal
- Projets
- Objectifs

## Questions possibles

- Quels projets utilisent FastAPI ?
- Combien d'heures ai-je consacré à Python ?
- Quels objectifs sont en retard ?

## Technologies

- Ollama
- LangChain
- ChromaDB

## Compétences travaillées

- RAG
- Embeddings
- LLM

## Livrable

Assistant IA intégré.

---

# V10 — Career OS 1.0

## Objectif

Première version complète utilisée quotidiennement.

## Modules

- Dashboard
- Goals
- Skills
- Projects
- Journal
- Documents
- Formations
- Assistant IA

## Résultat attendu

Career OS devient :

- Un système de pilotage de carrière
- Un gestionnaire documentaire
- Un portfolio technique
- Un support d'apprentissage
- Un laboratoire de compétences AI Engineer

---

# Feuille de Route Carrière

## 2026

- Remise à niveau Python
- Dossier PTP
- Career OS V1 à V3

## 2027

- Formation AI Engineer
- Career OS V4 à V6

## 2028

- Premier poste Python / IA
- Career OS V7

## 2029

- Consolidation de l'expertise
- Career OS V8 à V9

## 2030

- Lancement activité indépendante
- Career OS 1.0 stable

---

# Principe Directeur

> Construire petit.
>
> Construire utile.
>
> Construire propre.
>
> Améliorer continuellement.