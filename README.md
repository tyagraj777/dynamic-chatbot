# dynamic-chatbot
Here's a detailed project structure and implementation guide for the advanced chatbot that dynamically learns from six input links, adapts to company information, and handles customer interactions. (WIP)

# Dynamic Chatbot (Jr.)

A chatbot that dynamically learns from six provided input links and handles customer queries for cloud hosting services.

## 🚀 Features
- Dynamic learning from company data (FAQs, Products, Services, etc.)
- Basic intent recognition with NLP.
- Handles greetings, collects user info, and redirects to support channels.
- Shares product updates.

## 📂 Folder Structure
- `backend/`: Backend logic (Flask, NLP, Scraper).
- `frontend/`: Simple frontend UI.
- `data/`: Stores dynamically learned data.
- `tests/`: Unit tests for the project.
- `config/`: Configuration settings.

![Screenshot 2024-11-25 224354-folder](https://github.com/user-attachments/assets/90a54f25-455e-4c1d-a3ad-796179307f78)


## ⚙️ Setup Instructions
1. **Clone the repository**:
    ```bash
    git clone <repo-link>
    cd dynamic-chatbot
    ```

2. **Set up the virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r backend/requirements.txt
    ```

4. **Initialize Learning**:
    ```bash
    curl -X POST http://127.0.0.1:5000/initialize -H "Content-Type: application/json" \
    -d '{"home": "https://example.com", "faqs": "https://example.com/faqs", "products": "https://example.com/products", "services": "https://example.com/services", "about": "https://example.com/about", "medi
a_updates": "https://example.com/media"}'
    ```

5. **Run the Application**:
    ```bash
    python backend/app.py
    ```

6. **Open `frontend/index.html`** to interact with the chatbot.

## ✅ Testing
- Run tests using `pytest`:
    ```bash
    pytest tests/
    ```

---

This setup ensures a **fully functional, dynamically learning chatbot** tailored for hosting companies. Let me know if you'd like to enhance it with more features like multilingual support or AI-driven inten
t analysis. 🚀
