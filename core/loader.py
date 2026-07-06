"""
===========================================================
PURAS - Prime Underwriting Risk Analytics System
Module: loader.py

Description:
    Handles loading of all datasets from a single Excel
    workbook exported from SLAMS.

Author:
    PURAS Development Team
===========================================================
"""

from pathlib import Path
import pandas as pd

# ==========================================================
# Required worksheets
# ==========================================================

REQUIRED_SHEETS = [
    "Clients",
    "Policies",
    "Claims",
    "Agencies",
    "Underwriters",
    "Renewals",
    "Claim_Payments"
]

class DataLoader:

    def __init__(self, file):
        self.file = file
        self.data = {}

    def load(self):

        excel = pd.ExcelFile(self.file)

        missing = [
            sheet for sheet in REQUIRED_SHEETS
            if sheet not in excel.sheet_names
        ]

        if missing:
            raise ValueError(f"Missing worksheets: {missing}")

        for sheet in REQUIRED_SHEETS:
            self.data[sheet] = pd.read_excel(excel, sheet_name=sheet)

        return self.data

    def summary(self):

        summary = []

        for sheet, df in self.data.items():

            summary.append({
                "Dataset": sheet,
                "Rows": len(df),
                "Columns": len(df.columns)
            })

        return pd.DataFrame(summary)
