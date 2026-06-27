import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/customer_support_tickets_200k.csv")

print("=" * 60)
print("CUSTOMER SUPPORT DATASET EXPLORATION")
print("=" * 60)

print("\nDataset Shape:")
print(df.shape)

print("\nUnique Categories:")
print(df["category"].unique())

print("\nNumber of Categories:")
print(df["category"].nunique())

print("\nTickets Per Category:")
print(df["category"].value_counts())

print("\nSample Complaints:")

for category in df["category"].unique():
    print(f"\n===== {category} =====")
    print(df[df["category"] == category]["issue_description"].iloc[0])