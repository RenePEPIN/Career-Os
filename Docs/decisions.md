
# Décisions Architecture

Ce document recense les principales décisions prises pour le projet Career OS.

L'objectif est de garder une trace des choix réalisés et de leur justification afin d'éviter les hésitations ou les changements inutiles en cours de développement.

---

# 20/10/2026

## Création du projet Career OS

### Décision

Créer une application personnelle permettant de suivre :

- mes objectifs ;
- mes compétences ;
- mes formations ;
- mes projets ;
- mes candidatures ;
- ma progression vers le métier d'AI Engineer.

### Motivation

J'ai besoin de visualiser les choses pour les comprendre et les piloter.

Career OS doit devenir mon tableau de bord personnel de carrière.

---

# 20/10/2026

## Utilisation de Streamlit

### Décision

Construire l'interface avec Streamlit.

### Motivation

Je souhaite me concentrer sur :

- Python ;
- la logique métier ;
- l'architecture ;
- les bases de données.

Je connais déjà React mais ce projet n'a pas pour objectif de progresser en frontend.

Streamlit permet de créer rapidement des interfaces visuelles et fonctionnelles.

### Réévaluation

Le choix pourra être revu plus tard si le projet devient une véritable application multi-utilisateur.

---

# 20/10/2026

## Architecture Feature First

### Décision

Organiser le projet par fonctionnalités.

### Exemple

```text
goals
skills
projects
documents
journal
```

### Motivation

Cette organisation est plus simple à comprendre et à maintenir qu'une séparation par couches techniques.

---

# 20/10/2026

## Développement progressif

### Décision

Développer les fonctionnalités une par une.

### Ordre

1. Dashboard
2. Goals
3. Skills
4. Projects
5. Journal
6. Documents
7. IA

### Motivation

Terminer chaque module avant de passer au suivant.

Éviter l'accumulation de fonctionnalités incomplètes.

---

# 20/10/2026

## IA en dernier

### Décision

Ne pas intégrer d'intelligence artificielle immédiatement.

### Motivation

Une bonne application repose d'abord sur :

- une architecture claire ;
- des données fiables ;
- une logique métier solide.

L'IA viendra enrichir l'application lorsque les fondations seront stables.

---

# 20/10/2026

## PostgreSQL comme base cible

### Décision

Utiliser PostgreSQL à terme.

### Motivation

Acquérir une expérience proche des environnements professionnels.

### Phase de démarrage

Les premières versions pourront utiliser :

- JSON
- SQLite

afin d'accélérer le développement.

---

# 20/10/2026

## Documentation dans le dépôt

### Décision

Conserver toute la documentation dans le projet.

### Motivation

Éviter d'avoir :

- des notes dans OneNote ;
- des notes dans Obsidian ;
- des notes dans Notion ;
- des informations dispersées.

Le dépôt Git devient la source officielle du projet.

---

# Principe directeur

Construire Career OS comme un projet BIM :

1. Comprendre le besoin.
2. Dessiner la solution.
3. Structurer les données.
4. Développer.
5. Améliorer.

Ne jamais construire sans vision d'ensemble.

