"""Smoke tests : les fichiers JSON MVP existent et sont valides."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"


def test_data_dir_exists():
    assert DATA.is_dir(), "Créer le dossier data/ (voir Docs/guide-demarrage.md étape 2)"


def test_skills_json_valid():
    path = DATA / "skills.json"
    assert path.is_file(), "Créer data/skills.json"
    skills = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(skills, list) and len(skills) > 0
    for s in skills:
        assert "id" in s and "name" in s and "level" in s
        assert 0 <= int(s["level"]) <= 100


def test_goals_json_valid():
    path = DATA / "goals.json"
    assert path.is_file(), "Créer data/goals.json"
    goals = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(goals, list) and len(goals) > 0
    allowed = {"pending", "in_progress", "completed", "cancelled"}
    for g in goals:
        assert "id" in g and "title" in g and "status" in g
        assert g["status"] in allowed
