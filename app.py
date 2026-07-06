import streamlit as st
from core.loader import load_data
from core.validator import validate_data

st.title("PURAS")

uploaded_file = st.file_uploader("Upload an Excel file")

if uploaded_file:
    df = load_data(uploaded_file)
    result = validate_data(df)

    st.write(df.head())
    st.write(result)
