import streamlit as st

# Page config (optional)
st.set_page_config(page_title="Hello World", layout="centered")

# Center the text using markdown and HTML
st.markdown(
    """
    <h1 style='text-align: center;'>Hello, World!</h1>
    """,
    unsafe_allow_html=True
)
