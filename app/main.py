import streamlit as st

st.set_page_config(
    page_title="Career OS",
    layout="wide"
)

st.title("Career OS")

st.subheader("Objectif")
st.write("Devenir AI Engineer")

st.subheader("Compétences")

st.progress(70, text="Python")
st.progress(40, text="SQL")
st.progress(20, text="FastAPI")

st.subheader("Objectifs")

st.checkbox("CV terminé", value=True)
st.checkbox("RDV CEP effectué", value=True)
st.checkbox("Documentation terminée", value=True)
st.checkbox("Dossier PTP", value=False)