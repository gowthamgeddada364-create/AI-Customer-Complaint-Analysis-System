from flask import Flask, render_template, request
import joblib
import re
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.ner import extract_entities
from src.auto_reply import generate_reply

app = Flask(__name__)

# Load trained model and vectorizer
model = joblib.load("models/trained/classifier.pkl")
vectorizer = joblib.load("models/trained/vectorizer.pkl")


# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Prediction
@app.route("/predict", methods=["POST"])
def predict():

    # Get complaint
    complaint = request.form["complaint"].strip()

    # -----------------------------
    # Input Validation
    # -----------------------------

    if not complaint:
        return render_template(
            "index.html",
            error="Please enter a customer complaint."
        )

    if len(complaint) < 10:
        return render_template(
            "index.html",
            error="Please enter at least 10 characters."
        )

    if complaint.replace(" ", "").isdigit():
        return render_template(
            "index.html",
            error="Complaint cannot contain only numbers."
        )

    if not re.search(r"[A-Za-z]", complaint):
        return render_template(
            "index.html",
            error="Please enter meaningful text."
        )

    # Convert to TF-IDF
    vector = vectorizer.transform([complaint])

    # Predict
    prediction = model.predict(vector)[0]

    probabilities = model.predict_proba(vector)[0]

    confidence = round(max(probabilities) * 100, 2)

    # Confidence Threshold
    if confidence < 40:
     return render_template(
        "index.html",
          error_title="Unable to Classify Complaint",
        error_reason="The complaint doesn't appear to match any of our supported financial complaint categories.",
        suggestions=[
            "Credit Card",
            "Checking or Savings Account",
            "Mortgage",
            "Student Loan",
            "Vehicle Loan",
            "Debt Collection",
            "Money Transfer",
            "Payday Loan",
            "Credit Report"
        ]
    )

    classes = model.classes_

    top3 = sorted(
        zip(classes, probabilities),
        key=lambda x: x[1],
        reverse=True
    )[:3]

    top3 = [
        (category, round(probability * 100, 2))
        for category, probability in top3
    ]
    # Extract Named Entities
    entities = extract_entities(complaint)

    # Generate AI Reply
    reply = generate_reply(prediction,entities)

    return render_template(
        "index.html",
        complaint=complaint,
        prediction=prediction,
        confidence=confidence,
        top3=top3,
        entities=entities,
        reply=reply
        
    
    )


if __name__ == "__main__":
    app.run(debug=True)