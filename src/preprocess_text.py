import pandas as pd
import spacy

print("=" * 60)
print("TEXT PREPROCESSING")
print("=" * 60)

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Load dataset
df = pd.read_csv("data/processed/clean_complaints.csv")


def clean_text(text):
    doc = nlp(str(text).lower())

    tokens = []

    for token in doc:

        # Remove stopwords, punctuation, spaces
        if token.is_stop:
            continue

        if token.is_punct:
            continue

        if token.is_space:
            continue

        # Keep only alphabetic words
        if not token.is_alpha:
            continue

        # Convert to base form (lemma)
        tokens.append(token.lemma_)

    return " ".join(tokens)


print("\nCleaning complaints...")

# Create a new cleaned text column
df["clean_text"] = df["Consumer complaint narrative"].apply(clean_text)

# Save cleaned dataset
df.to_csv(
    "data/processed/preprocessed_complaints.csv",
    index=False
)

print("\n✅ Preprocessing Completed!")

print("\nShape:")
print(df.shape)

print("\nOriginal Complaint:\n")
print(df["Consumer complaint narrative"].iloc[0][:500])

print("\nCleaned Complaint:\n")
print(df["clean_text"].iloc[0][:500])