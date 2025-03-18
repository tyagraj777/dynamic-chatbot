from transformers import pipeline

classifier = pipeline("zero-shot-classification")

def predict_intent(text):
    intents = ["account", "support", "devops", "product", "services", "media"]
    result = classifier(text, intents)
    return result['labels'][0]
