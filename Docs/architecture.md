# Architecture

## Vue d'ensemble

Career OS est un système personnel de pilotage de carrière conçu selon une architecture modulaire, évolutive et maintenable.

L'objectif est de séparer clairement :

- l'interface utilisateur ;
- la logique métier ;
- l'accès aux données ;
- les services techniques.

Chaque module métier est autonome et responsable d'un domaine fonctionnel précis.

---

# Architecture cible

```text
Career OS

┌─────────────────────┐
│      Streamlit      │
│   Interface UI      │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│      Services       │
│    Logique métier   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│    Repositories     │
│   Accès données     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│     PostgreSQL      │
│    Persistance      │
└─────────────────────┘
```

---

# Architecture du dépôt

```text
career-os/
│
├── app/
│   │
│   ├── main.py
│   │
│   ├── dashboard/
│   ├── goals/
│   ├── skills/
│   ├── projects/
│   ├── formations/
│   ├── documents/
│   ├── journal/
│   └── settings/
│
├── database/
│
├── tests/
│
├── docs/
│
├── requirements.txt
│
├── .env.example
│
├── .gitignore
│
└── README.md
```

---

# Organisation des modules

L'architecture adopte une approche **Feature First**.

Chaque fonctionnalité possède son propre dossier.

Exemple :

```text
goals/
│
├── page.py
├── models.py
├── service.py
├── repository.py
└── tests.py
```

Cette organisation permet :

- une meilleure lisibilité ;
- une maintenance simplifiée ;
- une évolution indépendante des fonctionnalités.

---

# Modules métier

## Dashboard

Responsabilités :

- Vue synthétique de l'application
- Statistiques globales
- Progression des compétences
- Objectifs prioritaires

---

## Goals

Responsabilités :

- Création des objectifs
- Suivi des objectifs
- Priorisation
- État d'avancement

Exemples :

- Dossier PTP
- Admission AI Engineer
- Certification Docker

---

## Skills

Responsabilités :

- Gestion des compétences
- Évaluation du niveau
- Historique de progression

Exemples :

- Python
- SQL
- FastAPI
- Docker
- Machine Learning
- RAG

---

## Projects

Responsabilités :

- Gestion du portfolio
- Suivi d'avancement
- Documentation technique

Exemples :

- Career OS
- Assistant BIM IA
- Analyseur de CV

---

## Formations

Responsabilités :

- Parcours de formation
- Certifications
- Objectifs pédagogiques

Exemples :

- OpenClassrooms
- Certifications Azure
- Autoformation

---

## Documents

Responsabilités :

- Stockage documentaire
- Classement
- Recherche

Exemples :

- CV
- Diplômes
- Dossier PTP
- Certificats

---

## Journal

Responsabilités :

- Historique des apprentissages
- Suivi du temps investi
- Retours d'expérience

---

# Architecture technique

## Présentation

Le projet sera développé en plusieurs phases.

---

## Version 1

```text
Python
+
Streamlit
+
Fichiers JSON
```

Objectif :

- Développement rapide
- Validation des concepts
- Maîtrise de l'architecture métier

---

## Version 2

```text
Python
+
Streamlit
+
PostgreSQL
+
SQLAlchemy
```

Objectif :

- Persistance des données
- Modélisation relationnelle

---

## Version 3

```text
FastAPI
+
Streamlit
+
PostgreSQL
```

Objectif :

- Séparation Frontend / Backend
- API REST

---

## Version 4

```text
FastAPI
+
PostgreSQL
+
RAG
+
LLM
```

Objectif :

- Assistant IA
- Recherche documentaire intelligente

---

# Principes d'architecture

## Single Responsibility

Chaque module possède une seule responsabilité.

Exemple :

```text
Skills
=
gestion des compétences
```

et rien d'autre.

---

## Separation of Concerns

Séparation stricte entre :

```text
UI
Business
Persistence
Infrastructure
```

---

## Simplicité

Privilégier :

```text
Solution simple
```

avant :

```text
Solution complexe
```

---

## Évolutivité

Toute fonctionnalité doit pouvoir être :

- modifiée ;
- remplacée ;
- supprimée ;

sans impacter les autres modules.

---

# Flux de données

```text
Utilisateur

    ▼

Page Streamlit

    ▼

Service

    ▼

Repository

    ▼

PostgreSQL

    ▼

Repository

    ▼

Service

    ▼

Page Streamlit

    ▼

Utilisateur
```

---

# Gestion des erreurs

Principe :

- jamais de logique métier dans l'interface ;
- gestion centralisée des erreurs ;
- messages explicites.

Types d'erreurs :

```text
ValidationError

NotFoundError

DatabaseError

BusinessRuleError
```

---

# Tests

Les tests concernent principalement :

```text
Services métiers
```

et non les composants visuels.

Priorité :

- GoalService
- SkillService
- ProjectService

---

# Documentation

Toute décision importante doit être documentée.

Dossier :

```text
docs/
│
├── vision.md
├── roadmap.md
├── architecture.md
├── decisions.md
├── database.md
└── changelog.md
```

---

# Principe directeur

> Construire comme un projet BIM.
>
> Concevoir avant de développer.
>
> Visualiser avant de coder.
>
> Structurer avant d'étendre.