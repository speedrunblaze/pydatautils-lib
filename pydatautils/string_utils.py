import re

def clean_text(text):
    """Removes special characters from a string."""
    return re.sub(r'[^a-zA-Z0-9 ]', '', text)

def count_words(text):
    """Counts the number of words in a string."""
    return len(text.split())
