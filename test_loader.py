from core.loader import DataLoader
from core.validator import DataValidator

loader = DataLoader("PURAS_Synthetic_Insurance_Dataset.xlsx")

datasets = loader.load()

print(loader.summary())

validator = DataValidator(datasets)

report = validator.validate()

print(report)
