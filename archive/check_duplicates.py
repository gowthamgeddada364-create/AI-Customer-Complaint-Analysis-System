import pandas as pd

df = pd.read_csv("data/raw/customer_support_tickets_200k.csv")

duplicates = (
    df.groupby("issue_description")["category"]
      .nunique()
      .sort_values(ascending=False)
)

print("Complaints with multiple categories:")
print(duplicates[duplicates > 1].head(20))