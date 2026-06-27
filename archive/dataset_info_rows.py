import pandas as pd

print("=" * 60)
print("CONSUMER COMPLAINT DATASET")
print("=" * 60)

# Read only first 50,000 rows (fast)
df = pd.read_csv(
    "data/raw/rows.csv",
    nrows=50000,
    low_memory=False
)

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nData Types:")
print(df.dtypes)