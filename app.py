import streamlit as st
import os

# Get the directory where app.py is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Path to index.html inside the same repo
html_path = os.path.join(BASE_DIR, "index.html")

# Read file
with open(html_path, "r", encoding="utf-8") as f:
    html_code = f.read()

# Render HTML
st.components.v1.html(html_code, height=800, scrolling=True)
