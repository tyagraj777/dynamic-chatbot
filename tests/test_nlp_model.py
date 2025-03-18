from backend.models.nlp_model import predict_intent

def test_predict_intent():
    assert predict_intent("Tell me about your products") == "product"
    assert predict_intent("I need support for my server") == "support"
