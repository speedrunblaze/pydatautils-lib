import json

def save_json(data, filename):
    """Saves a dictionary to a JSON file."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def load_json(filename):
    """Loads a JSON file and returns a dictionary."""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
