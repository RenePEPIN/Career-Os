# Notice Career OS

Comme une notice de meuble : une étape = un bloc.  
Format : **Quoi** → **Pourquoi** → **Comment tester** → **Piège**.

---

## 1. Lancer l’environnement

**Quoi**  
À la racine du projet : `make setup`

**Pourquoi**  
Crée le venv, installe Streamlit / pytest, prépare `data/`.

**Comment tester**  
`make test` → 3 passed.

**Piège**  
Lancer les commandes depuis `d:\Career-Os`, pas depuis un sous-dossier.

---

## 2. Afficher une page Streamlit vide

**Quoi**  
Créer `app/main.py` avec :
- `import streamlit as st`
- `st.set_page_config(page_title="Career OS", layout="wide")`
- `st.title("Mon Parcours")`

**Pourquoi**  
Vérifier que l’app s’ouvre dans le navigateur avant d’ajouter de la logique.

**Comment tester**  
`make run` → titre « Mon Parcours » visible.

**Piège**  
Écrire `set_page_config` (avec des `_`). Pas `set_pageconfig`.

---

## 3. Pointer vers le dossier des données

**Quoi**  
Ajouter :
`DATA_DIR = Path(__file__).resolve().parent.parent / "data"`  
(il faut `from pathlib import Path`)

**Pourquoi**  
Les JSON sont dans `data/` à la racine, pas dans `app/`.

**Comment tester**  
`st.write(DATA_DIR)` → le chemin finit par `\Career-Os\data`. Puis enlever le `st.write`.

**Piège**  
Un seul `.parent` → tu pointes vers `app/data` (mauvais dossier).

---

## 4. Afficher les compétences ✓

**Quoi**  
`import json`, charger `skills.json`, `st.subheader("Mes compétences")` **avant** le `for`, puis  
`st.progress(s["level"] / 100, text=f"{s['name']} {s['level']}%")`

**Pourquoi**  
Le JSON pilote l’écran : changer un `level` change la barre au reload.  
`text=f"..."` = libellé ; `{s['name']}` et `{s['level']}` sont remplacés par les valeurs du dictionnaire.

**Comment tester**  
`make run` → barres = contenu de `data/skills.json`. Modifier un level → reload → barre à jour.

**Piège**  
- `st.progress` attend 0.0–1.0 → diviser par 100.  
- Oublier `encoding="utf-8"` peut casser les accents sous Windows.

---

## 5. Afficher les étapes clés ✓

**Quoi**  
Charger `goals.json`, boucle `for g in goals` avec  
`st.write(f"{g['title']} - {g['status']}")`

**Pourquoi**  
Afficher les jalons (CV, CEP, PTP…) depuis le JSON, comme pour les skills.

**Comment tester**  
`make run` → 5 lignes ; CV/CEP = `completed`, PTP = `in_progress`.

**Piège**  
- `DATA_DIR` pas `DATA.DIR` (sinon NameError).  
- `st.subheader` **avant** le `for` (sinon le titre se répète à chaque goal).  
- Recharger la page après chaque modif du JSON.

---

## 6. Deux colonnes (maquette) ✓

**Quoi**  
`col1, col2 = st.columns(2)` puis `with col1:` (skills) et `with col2:` (goals).

**Pourquoi**  
Sur la maquette, progression et étapes sont côte à côte ; `layout="wide"` donne de la place.

**Comment tester**  
`make run` → compétences à gauche, étapes à droite.

**Piège**  
Indentation : tout le contenu d’une colonne doit être indenté sous le `with`.
