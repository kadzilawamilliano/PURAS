import streamlit as st
from core.loader import DataLoader
from core.validator import DataValidator

st.title("PURAS")

file = st.file_uploader("Upload SLAMS Excel Workbook", type=["xlsx"])

if file is not None:
    # Save uploaded file temporarily
    with open("temp.xlsx", "wb") as f:
        f.write(file.getbuffer())

    # Load datasets
    loader = DataLoader("temp.xlsx")
    datasets = loader.load()

    st.subheader("Dataset Summary")
    st.dataframe(loader.summary())

    # Validate datasets
    validator = DataValidator(datasets)
    report = validator.validate()

    st.subheader("Validation Report")
    st.dataframe(report)
