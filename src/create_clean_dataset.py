import pandas as pd

print("=" * 60)
print("CREATING CLEAN DATASET")
print("=" * 60)

chunks = pd.read_csv(
    "data/raw/rows.csv",
    chunksize=100000,
    low_memory=False
)

clean_data = []

for chunk in chunks:

    # Keep only rows with complaint text
    chunk = chunk.dropna(subset=["Consumer complaint narrative"])

    # Keep only required columns
    chunk = chunk[
        [
            "Consumer complaint narrative",
            "Product"
        ]
    ]

    clean_data.append(chunk)

    total = sum(len(x) for x in clean_data)

    print(f"Collected {total} complaints...")

    if total >= 50000:
        break

df = pd.concat(clean_data)

df = df.head(50000)

df.to_csv(
    "data/processed/clean_complaints.csv",
    index=False
)

print("\nDataset Saved Successfully!")

print("\nShape:")
print(df.shape)

print("\nCategories:")
print(df["Product"].value_counts())