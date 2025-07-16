# helpers.py (inside utils/)
import re

def clean_title(text):
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = re.sub(r'\s+', ' ', text)     # Remove extra spaces
    return text.strip()

def convert_duration(duration_str):
    """Convert duration string (e.g. '10:32') to total seconds."""
    try:
        parts = list(map(int, duration_str.split(':')))
        if len(parts) == 2:
            return parts[0] * 60 + parts[1]
        elif len(parts) == 3:
            return parts[0] * 3600 + parts[1] * 60 + parts[2]
    except:
        return 0
