import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="Sales Data App", layout="wide")

# Sidebar - nawigacja
view = st.sidebar.radio("Wybierz widok:", ["Tabela", "Wykres"])

# Połączenie z bazą danych SQLite
conn = sqlite3.connect("sales_data.db")
df = pd.read_sql_query("SELECT * FROM sales", conn)



# Widok 1: tabela danych
if view == "Tabela":
    st.title("Tabela danych sprzedażowych")
    st.dataframe(df, use_container_width=True)

# Widok 2: wykres



elif view == "Wykres":
    st.title("Sprzedaż wg linii produktów")

    # Sprawdź czy kolumny istnieją
    if "PRODUCTLINE" in df.columns and "SALES" in df.columns:
        sales_by_product = df.groupby("PRODUCTLINE")["SALES"].sum().reset_index()
        sales_by_product = sales_by_product.sort_values(by="SALES", ascending=False)

        st.bar_chart(sales_by_product, x="PRODUCTLINE", y="SALES", use_container_width=True)
    else:
        st.warning("Brakuje kolumn PRODUCTLINE lub SALES.")

# Zamknij połączenie z bazą
conn.close()
