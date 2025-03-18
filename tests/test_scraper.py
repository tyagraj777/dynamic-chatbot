from backend.models.scraper import dynamic_learning
import os
import json

def test_dynamic_learning():
    test_data = {
        "home": "https://example.com/home"
    }
    dynamic_learning(test_data)
    assert os.path.exists("data/dynamic_data.json")
    with open("data/dynamic_data.json", "r") as file:
        data = json.load(file)
        assert "home" in data
