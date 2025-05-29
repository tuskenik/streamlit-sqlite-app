import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="Sales Data Viewer", layout="wide")

st.title("Sales Data Table")

# Połączenie z bazą danych
conn = sqlite3.connect("sales_data.db")

# Wczytanie danych z tabeli
query = "SELECT * FROM sales"
df = pd.read_sql_query(query, conn)

# Interaktywna tabela
st.dataframe(df, use_container_width=True)

# Zamknięcie połączenia
conn.close()
