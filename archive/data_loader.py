import pandas as pd

print("=" * 60)
print("CUSTOMER SUPPORT DATASET")
print("=" * 60)

df = pd.read_csv(
    "data/raw/twcs.csv",
    usecols=["tweet_id", "author_id", "inbound", "text"],
    nrows=10000
)

print("\nOriginal Dataset Shape:")
print(df.shape)

# Keep only customer messages
customer_df = df[df["inbound"] == True]

print("\nCustomer Messages Only:")
print(customer_df.shape)

print("\nFirst 10 Customer Messages:")
print(customer_df["text"].head(10))

print("\nMissing Values:")
print(customer_df.isnull().sum())