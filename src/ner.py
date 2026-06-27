import spacy

nlp = spacy.load("en_core_web_sm")

# Friendly names
LABELS = {
    "ORG": "🏢 Organization",
    "PERSON": "👤 Person",
    "GPE": "📍 Location",
    "DATE": "📅 Date",
    "MONEY": "💰 Money",
}


def extract_entities(text):

    doc = nlp(text)

    entities = []

    for ent in doc.ents:

        label = LABELS.get(ent.label_, ent.label_)

        entities.append((ent.text, label))

    return entities