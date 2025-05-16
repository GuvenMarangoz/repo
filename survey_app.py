import streamlit as st
import pandas as pd
import sqlite3
from datetime import datetime

# SQLite setup
conn = sqlite3.connect("survey_responses.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS responses (
    timestamp TEXT,
    team TEXT,
    data_collected TEXT,
    data_goals TEXT,
    current_blockers TEXT,
    needs_now TEXT,
    tools_wanted TEXT,
    time_wasters TEXT,
    time_saved_use TEXT
)
""")
conn.commit()

st.title("Global R&D Digitalization Survey")

st.write("Please fill in the survey below. It takes ~3–5 minutes.")

team = st.text_input("Your R&D Team or Department:")

data_collected = st.text_area("1. What types of data do you currently collect (if any)? (e.g. Excel, devices, lab systems)")

data_goals = st.text_area("2. What do you wish you could do with that data? (e.g. trends, analysis, monitoring)")

current_blockers = st.text_area("3. What currently prevents you from doing this? (e.g. lack of tools, time, structure)")

needs_now = st.text_area("4. What would help you most right now? (e.g. dashboard, clean data, prediction tools)")

tools_wanted = st.text_area("5. What digital tools or training do you wish you had? (e.g. Python, Minitab, SPC, Industry 4.0)")

time_wasters = st.text_area("6. Are there any repetitive or time-consuming tasks you’d like to reduce via digitalization?")

time_saved_use = st.text_area("→ If time were saved, how would you use it? (e.g. learning, analysis, creativity)")

if st.button("Submit"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("""
        INSERT INTO responses VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (timestamp, team, data_collected, data_goals, current_blockers, needs_now, tools_wanted, time_wasters, time_saved_use))
    conn.commit()
    st.success("Thank you! Your response has been recorded.")

