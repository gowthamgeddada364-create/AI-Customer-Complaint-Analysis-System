import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

print("=" * 60)
print("TRAINING CUSTOMER COMPLAINT CLASSIFIER")
print("=" * 60)

# Load processed dataset
df = pd.read_csv("data/processed/preprocessed_complaints.csv")

# Features and Labels
X = df["clean_text"]
y = df["Product"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print(f"\nTraining Samples : {len(X_train)}")
print(f"Testing Samples  : {len(X_test)}")

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer(
    max_features=10000,
    ngram_range=(1,2)
)

X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

# Train Model
model = LogisticRegression(
    max_iter=1000,
    random_state=42
)

print("\nTraining Model...")

model.fit(X_train, y_train)

print("Training Completed!")

# Prediction
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print(f"\nAccuracy : {accuracy*100:.2f}%")

print("\nClassification Report:\n")
print(classification_report(y_test, predictions))

# Save Model
joblib.dump(model, "models/trained/classifier.pkl")
joblib.dump(vectorizer, "models/trained/vectorizer.pkl")

print("\nModel Saved Successfully!")
print("classifier.pkl")
print("vectorizer.pkl")