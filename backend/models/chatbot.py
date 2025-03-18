import random

class Chatbot:
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base
        self.default_responses = [
            "I'm not sure I understand. Could you please elaborate?",
            "That's interesting! Can you tell me more?",
            "I'm here to help! Can you provide more details?",
            "Hmm, I might need more information to assist you better."
        ]
        self.greeting_responses = [
            "Hello! How can I assist you today?",
            "Hi there! What can I do for you?",
            "Welcome! How can I help you today?"
        ]
        self.farewell_responses = [
            "Goodbye! Feel free to chat with me again.",
            "See you soon! Let me know if you have more questions.",
            "Take care! I'm here if you need me again."
        ]

    def get_response(self, user_input, contact_info=None):
        """Main method to generate a response based on user input."""
        user_input = user_input.lower()

        # 1. Greeting
        if any(word in user_input for word in ["hi", "hello", "hey", "greetings"]):
            return random.choice(self.greeting_responses)

        # 2. Farewell
        elif any(word in user_input for word in ["bye", "goodbye", "see you"]):
            return random.choice(self.farewell_responses)

        # 3. Account Info
        elif "account" in user_input:
            return self.knowledge_base.get("account_info", "You can access your account details by logging in to your dashboard.")

        # 4. Troubleshooting
        elif "issue" in user_input or "problem" in user_input or "troubleshoot" in user_input:
            return self.knowledge_base.get("troubleshooting", "Please describe your issue in more detail, and I'll try to help!")

        # 5. Product Information
        elif "product" in user_input or "plan" in user_input:
            return self.knowledge_base.get("products", "We offer a variety of products. Would you like to know about any specific one?")

        # 6. Services
        elif "service" in user_input:
            return self.knowledge_base.get("services", "Our services include web hosting, domain registration, and more.")

        # 7. FAQs
        elif "faq" in user_input or "common question" in user_input:
            return self.knowledge_base.get("faqs", "You can find answers to common questions on our FAQ page.")

        # 8. Media Updates
        elif "news" in user_input or "updates" in user_input:
            return self.knowledge_base.get("media_updates", "Check out our media section for the latest updates.")

        # 9. About the Company
        elif "about" in user_input or "company" in user_input:
            return self.knowledge_base.get("about", "We are a leading provider in cloud services, dedicated to helping businesses grow.")

        # 10. Customer Support
        elif "support" in user_input or "help" in user_input:
            return "You can reach out to our support team at support@example.com for assistance."

        # 11. Collect Contact Info
        elif "contact" in user_input or "email" in user_input or "phone" in user_input:
            return "Please provide your email and mobile number for better assistance."

        # 12. Basic Small Talk
        elif "how are you" in user_input:
            return "I'm just a bot, but I'm here to help you!"

        elif "thank you" in user_input or "thanks" in user_input:
            return "You're welcome! 😊"

        elif "what's your name" in user_input:
            return "I'm Jr., your chatbot assistant."

        # 13. Fallback for Unrecognized Inputs
        else:
            return random.choice(self.default_responses)
