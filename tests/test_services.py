from backend.services.greeting_service import greet
from backend.services.input_service import collect_info
from backend.services.updates_service import share_updates

def test_greet():
    assert greet() == "Hello! Welcome to Jr. Support. How can I assist you today?"

def test_collect_info():
    assert collect_info("my email is test@example.com") == "Thank you for providing your contact details. How may I assist you further?"

def test_share_updates():
    assert "No updates available" not in share_updates()
