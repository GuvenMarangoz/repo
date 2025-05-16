import streamlit as st
import sqlite3
import pandas as pd

# Connect to your SQLite database
conn = sqlite3.connect("survey_responses.db")
cursor = conn.cursor()

st.title("Digitalization Survey App")

menu = ["Take Survey", "View Responses"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Take Survey":
    st.subheader("Please fill out the survey")
    # your survey form here...

elif choice == "View Responses":
    st.subheader("Survey Responses")

    try:
        df = pd.read_sql_query("SELECT * FROM responses", conn)
        st.dataframe(df)
    except Exception as e:
        st.warning("No responses found or table missing.")
        st.error(str(e))