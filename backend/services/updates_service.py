import json

def share_updates():
    with open("data/dynamic_data.json", "r") as file:
        data = json.load(file)
    return data.get("media_updates", "No updates available at the moment.")
