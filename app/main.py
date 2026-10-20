import streamlit as st
from pathlib import Path
import json

DATA_DIR = Path(__file__).parent.parent / "data"

st.set_page_config(
    page_title="Mon Parcours",
    page_icon=":briefcase:",
    layout="wide"
)
st.title("Mon Parcours")

col1, col2 = st.columns(2)
with col1:
    skills = json.load((DATA_DIR / "skills.json").open(encoding="utf-8"))
    st.subheader("Mes compétences")
    for s in skills:
        st.progress(s["level"] /100, text=f"{s['name']} {s['level']}%")
with col2:
    goals = json.load((DATA_DIR / "goals.json").open(encoding="utf-8"))
    st.subheader("Mes étapes clés")
    for g in goals:
        st.write(f"{g['title']} - {g['status']}")