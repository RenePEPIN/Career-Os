"""Crée data/*.json seed si absents, ou valide (--check)."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

SKILLS = [
    {"id": "s1", "name": "Python Fundamentals", "level": 80, "target_level": 100},
    {"id": "s2", "name": "SQL & Databases", "level": 70, "target_level": 100},
    {"id": "s3", "name": "Web Development", "level": 60, "target_level": 100},
    {"id": "s4", "name": "Machine Learning", "level": 40, "target_level": 100},
    {"id": "s5", "name": "Generative AI & LLM", "level": 30, "target_level": 100},
]

GOALS = [
    {"id": "g1", "title": "CV mis à jour", "status": "completed"},
    {"id": "g2", "title": "RDV CEP", "status": "completed"},
    {"id": "g3", "title": "Dossier PTP", "status": "in_progress"},
    {"id": "g4", "title": "Réponse Transitions Pro", "status": "pending"},
    {"id": "g5", "title": "Début formation AI Engineer", "status": "pending"},
]

ALLOWED_STATUS = {"pending", "in_progress", "completed", "cancelled"}


def write_seed(path: Path, payload: list) -> None:
    if path.exists():
        print(f"OK  {path.name} (déjà présent)")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"NEW {path.name}")


def check_skills(path: Path) -> None:
    skills = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(skills, list) and skills, "skills.json vide"
    for s in skills:
        assert "id" in s and "name" in s and "level" in s
        assert 0 <= int(s["level"]) <= 100


def check_goals(path: Path) -> None:
    goals = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(goals, list) and goals, "goals.json vide"
    for g in goals:
        assert "id" in g and "title" in g and "status" in g
        assert g["status"] in ALLOWED_STATUS


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Valider sans créer")
    args = parser.parse_args()

    skills_path = DATA / "skills.json"
    goals_path = DATA / "goals.json"

    if args.check:
        if not skills_path.is_file() or not goals_path.is_file():
            print("ERREUR: data/skills.json ou data/goals.json manquant", file=sys.stderr)
            return 1
        check_skills(skills_path)
        check_goals(goals_path)
        print("OK data/*.json valides")
        return 0

    write_seed(skills_path, SKILLS)
    write_seed(goals_path, GOALS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
