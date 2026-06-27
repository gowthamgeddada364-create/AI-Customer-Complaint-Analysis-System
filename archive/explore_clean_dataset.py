import pandas as pd

print("=" * 60)
print("CLEAN DATASET EXPLORATION")
print("=" * 60)

# Load cleaned dataset
df = pd.read_csv("data/processed/clean_complaints.csv")

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nCategories:")
print(df["Product"].value_counts())

print("\nNumber of Categories:")
print(df["Product"].nunique())

print("\nSample Complaints:\n")

for category in df["Product"].unique():
    print("=" * 60)
    print(category)
    print("=" * 60)

    sample = df[df["Product"] == category]["Consumer complaint narrative"].iloc[0]
    print(sample[:500])  # Show first 500 characters
    print()