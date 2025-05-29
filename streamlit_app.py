import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="Sales Data App", layout="wide")

# Sidebar - nawigacja
view = st.sidebar.radio("Wybierz widok:", ["Tabela", "git add streamlit_app.pyWykres"])

# Połączenie z bazą danych SQLite
conn = sqlite3.connect("sales_data.db")
df = pd.read_sql_query("SELECT * FROM sales", conn)

# Widok 1: tabela danych
if view == "Tabela":
    st.title("Tabela danych sprzedażowych")
    st.dataframe(df, use_container_width=True)

# Widok 2: wykres
elif view == "Wykres":
    st.title("Wizualizacja danych sprzedażowych")

    # Przykład: zsumowana sprzedaż wg regionu (dostosuj do kolumn w Twoim CSV)
    if "Region" in df.columns and "Total Revenue" in df.columns:
        chart_data = df.groupby("Region")["Total Revenue"].sum().reset_index()
        chart_data = chart_data.sort_values(by="Total Revenue", ascending=False)

        st.bar_chart(chart_data, x="Region", y="Total Revenue", use_container_width=True)
    else:
        st.warning("Nie znaleziono odpowiednich kolumn do utworzenia wykresu.")

# Zamknij połączenie z bazą
conn.close()
