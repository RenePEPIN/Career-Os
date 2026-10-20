# Database

## Objectif

La base de données est le référentiel unique de Career OS.

Elle permet de centraliser :

- les objectifs ;
- les compétences ;
- les projets ;
- les formations ;
- les documents ;
- le journal d'apprentissage ;
- les candidatures.

L'objectif est de conserver un historique fiable et cohérent de l'évolution professionnelle.

---

# Choix techniques

## Version 1

Stockage temporaire :

```text
JSON
```

Objectif :

- développement rapide ;
- validation du modèle métier.

---

## Version 2

Migration vers :

```text
PostgreSQL
```

Objectif :

- persistance ;
- relations ;
- intégrité des données ;
- évolutivité.

---

# Conventions

## Clé primaire

Toutes les tables possèdent :

```text
id
```

Type :

```text
UUID
```

---

## Audit

Toutes les tables possèdent :

```text
created_at
updated_at
```

---

## Suppression

Aucune suppression physique.

Utilisation :

```text
is_active
```

ou

```text
deleted_at
```

selon les besoins futurs.

---

# Diagramme métier

```text
User
 │
 ├── Goals
 │
 ├── Skills
 │
 ├── Projects
 │
 ├── Formations
 │
 ├── Documents
 │
 ├── Journal Entries
 │
 └── Applications
```

---

# Table users

## Description

Utilisateur principal du système.

## Colonnes

```text
id
email
first_name
last_name
created_at
updated_at
```

## Exemple

```text
id: uuid
email: rene@example.com
first_name: Rene
last_name: Pepin
```

---

# Table goals

## Description

Gestion des objectifs personnels et professionnels.

## Colonnes

```text
id
title
description
status
priority
target_date
created_at
updated_at
```

## Statuts

```text
pending
in_progress
completed
cancelled
```

## Priorités

```text
low
medium
high
critical
```

## Exemple

```text
Titre :
Obtenir le financement PTP

Statut :
in_progress
```

---

# Table skills

## Description

Suivi des compétences techniques et métier.

## Colonnes

```text
id
name
category
level
target_level
notes
created_at
updated_at
```

## Catégories

```text
Programming

Database

AI

Cloud

DevOps

Soft Skills
```

## Niveaux

Échelle :

```text
0 à 100
```

## Exemple

```text
Python

Niveau actuel : 70

Objectif : 90
```

---

# Table projects

## Description

Portfolio de projets.

## Colonnes

```text
id
name
description
status
github_url
start_date
end_date
created_at
updated_at
```

## Statuts

```text
planned
active
completed
archived
```

## Exemple

```text
Career OS

Status :
active
```

---

# Table project_skills

## Description

Relation entre projets et compétences.

## Colonnes

```text
project_id
skill_id
```

## Exemple

```text
Career OS
  ├── Python
  ├── Streamlit
  └── PostgreSQL
```

---

# Table formations

## Description

Suivi des formations.

## Colonnes

```text
id
name
provider
status
start_date
end_date
cost
notes
created_at
updated_at
```

## Statuts

```text
planned
in_progress
completed
cancelled
```

## Exemple

```text
AI Engineer

Provider :
OpenClassrooms
```

---

# Table documents

## Description

Gestion documentaire.

## Colonnes

```text
id
name
file_path
file_type
category
description
created_at
updated_at
```

## Catégories

```text
CV

Diploma

Certification

PTP

Administrative

Technical
```

## Exemple

```text
Bachelor_Python.pdf

Category :
Diploma
```

---

# Table journal_entries

## Description

Historique d'apprentissage.

## Colonnes

```text
id
date
title
content
hours_spent
created_at
updated_at
```

## Exemple

```text
Date :
20/10/2026

Sujet :
FastAPI

Temps :
2 heures
```

---

# Table applications

## Description

Suivi des candidatures.

## Colonnes

```text
id
company
job_title
status
application_date
response_date
notes
created_at
updated_at
```

## Statuts

```text
draft

sent

interview

accepted

rejected
```

## Exemple

```text
Company :
Capgemini

Position :
AI Engineer Junior
```

---

# Futures tables

## certifications

```text
id
name
provider
date_obtained
expiration_date
```

---

## learning_resources

```text
id
title
type
url
status
```

Types :

```text
book
course
video
article
```

---

## ai_conversations

Historique des échanges avec l'assistant IA.

```text
id
question
answer
created_at
```

---

# Règles métier

## Objectifs

- Un objectif possède toujours un statut.
- Un objectif terminé ne peut pas être modifié sans réouverture.

---

## Compétences

- Le niveau doit être compris entre 0 et 100.
- La progression est historisée.

---

## Projets

- Un projet doit avoir un statut.
- Un projet terminé conserve son historique.

---

## Journal

- Une entrée est liée à une seule date.
- Le temps investi doit être positif.

---

# Principes de conception

## Source unique de vérité

Chaque donnée n'existe qu'à un seul endroit.

---

## Historisation

Conserver l'historique plutôt que remplacer l'information.

---

## Simplicité

Privilégier un schéma simple et compréhensible.

---

## Évolutivité

Le modèle doit pouvoir accueillir :

- plusieurs utilisateurs ;
- un assistant IA ;
- des statistiques avancées ;
- des intégrations externes.

---

# Vision cible

```text
Career OS

Users
│
├── Goals
├── Skills
├── Projects
├── Formations
├── Documents
├── Journal Entries
└── Applications
```

La base de données doit rester simple, cohérente et suffisamment robuste pour accompagner plusieurs années d'évolution du projet.