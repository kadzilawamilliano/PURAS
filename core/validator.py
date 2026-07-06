"""
===========================================================
PURAS - Prime Underwriting Risk Analytics System
Module: validator.py

Description:
    Performs data quality validation checks.

Author:
    PURAS Development Team
===========================================================
"""

import pandas as pd


class DataValidator:

    def __init__(self, datasets):

        self.datasets = datasets

        self.report = []

    # ------------------------------------------------------
    # Missing Values
    # ------------------------------------------------------

    def check_missing_values(self):

        for name, df in self.datasets.items():

            missing = df.isnull().sum().sum()

            self.report.append({
                "Dataset": name,
                "Check": "Missing Values",
                "Result": int(missing)
            })

    # ------------------------------------------------------
    # Duplicate Records
    # ------------------------------------------------------

    def check_duplicates(self):

        key_columns = {
            "Policies": "Policy_Number",
            "Claims": "Claim_Number",
            "Clients": "Client_ID",
            "Agencies": "Agency_ID",
            "Underwriters": "Underwriter_ID"
        }

        for dataset, column in key_columns.items():

            if dataset in self.datasets:

                df = self.datasets[dataset]

                duplicates = df.duplicated(
                    subset=[column]
                ).sum()

                self.report.append({

                    "Dataset": dataset,

                    "Check": f"Duplicate {column}",

                    "Result": int(duplicates)

                })

    # ------------------------------------------------------
    # Negative Values
    # ------------------------------------------------------

    def check_negative_values(self):

        numeric_checks = {

            "Policies": [
                "Premium",
                "Sum_Insured"
            ],

            "Claims": [
                "Claim_Amount"
            ]

        }

        for dataset, columns in numeric_checks.items():

            if dataset not in self.datasets:
                continue

            df = self.datasets[dataset]

            for column in columns:

                if column not in df.columns:
                    continue

                negatives = (df[column] < 0).sum()

                self.report.append({

                    "Dataset": dataset,

                    "Check": f"Negative {column}",

                    "Result": int(negatives)

                })

    # ------------------------------------------------------
    # Generate Report
    # ------------------------------------------------------

    def validate(self):

        self.check_missing_values()

        self.check_duplicates()

        self.check_negative_values()

        return pd.DataFrame(self.report)
