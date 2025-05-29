import streamlit as st
from modules import quality_analysis, compliance_analysis, ai_readiness
from utils.data_loader import load_data

st.set_page_config(page_title="Data Governance & AI Readiness Dashboard", layout="wide")

st.title("📊 Data Governance & AI Readiness Dashboard")

# Wczytaj dane
data = load_data('data/sample_sales_data.csv')

# Sidebar
st.sidebar.title("📌 Wybierz analizę")
analysis_type = st.sidebar.radio("Etap analizy:", ["1️⃣ Jakość danych", "2️⃣ Zgodność z AI Act", "3️⃣ Przygotowanie do AI"])

# Główna sekcja
if analysis_type == "1️⃣ Jakość danych":
    quality_analysis.run(data)
elif analysis_type == "2️⃣ Zgodność z AI Act":
    compliance_analysis.run(data)
elif analysis_type == "3️⃣ Przygotowanie do AI":
    ai_readiness.run(data)