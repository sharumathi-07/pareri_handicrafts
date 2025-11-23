import streamlit as st
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
page = st.sidebar.selectbox(
    "Choose Page",
    ["Home (index.html)", "Products (product.html)"]
)
if page == "Home (index.html)":
    html_path = os.path.join(BASE_DIR, "index.html")
    css_path = os.path.join(BASE_DIR, "style.css")
else:
    html_path = os.path.join(BASE_DIR, "product.html")
    css_path = os.path.join(BASE_DIR, "style1.css")
html_code = read_file(html_path)
css_code = f"<style>{read_file(css_path)}</style>"
final_html = css_code + html_code
st.components.v1.html(final_html, height=6000, scrolling=True, width=None)

