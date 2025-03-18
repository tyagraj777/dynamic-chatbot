import json

def handle_query(user_input):
    with open("data/dynamic_data.json", "r") as file:
        data = json.load(file)

    for key, content in data.items():
        if user_input.lower() in content.lower():
            return f"I found some relevant information in the {key} section."
    return "I’m sorry, I couldn’t find information on that topic. Redirecting you to a support channel."
