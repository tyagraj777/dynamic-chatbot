from flask import Flask, request, jsonify, send_from_directory
from models.scraper import dynamic_learning
from models.chatbot import Chatbot
import os

# ------------------------------
# Initialize Flask App
# ------------------------------
app = Flask(__name__, static_folder="../frontend", static_url_path="")

# ------------------------------
# Dynamic Initialization
# ------------------------------
input_links = {
    "home": "https://www.sqlite.org/index.html",
    "faqs": "https://www.sqlite.org/faq.html",
    "products": "https://www.sqlite.org/prosupport.html",
    "services": "https://www.sqlite.org/purchase/index.html",
    "about": "https://www.sqlite.org/about.html",
    "media": "https://www.sqlite.org/news.html"
}

# Dynamically learn from the input links
learned_data = dynamic_learning(input_links)

# Initialize chatbot with learned data
chatbot = Chatbot(learned_data)

# ------------------------------
# Serve Frontend Files
# ------------------------------
@app.route('/')
def serve_index():
    """Serve the main chatbot UI."""
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static_files(path):
    """Serve static frontend files like JS, CSS."""
    return send_from_directory(app.static_folder, path)

# ------------------------------
# Chatbot API Endpoint
# ------------------------------
@app.route('/chat', methods=['POST'])
def chat():
    """Handle incoming chatbot messages."""
    user_input = request.json.get("message")
    user_contact = request.json.get("contact", {})

    # Process the query with the chatbot
    response = chatbot.get_response(user_input, user_contact)

    return jsonify({"response": response})

# ------------------------------
# Run Flask App
# ------------------------------
