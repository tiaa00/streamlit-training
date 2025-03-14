import streamlit as st

st.set_page_config(page_title="test", page_icon=":shark:", layout="wide")
st.write("Hello world!")

st.markdown("## This is the main page")
st.sidebar.write("main page")

# st.image("Dell-Logo.png", width=200)
st.sidebar.image("Dell-Logo.png", width=200)