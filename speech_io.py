import re
import pyttsx3  # or whichever TTS you use

engine = pyttsx3.init()

def speak(text):
    clean_text = clean_for_speech(text)
    engine.say(clean_text)
    engine.runAndWait()

def clean_for_speech(text):
    """
    Makes AI responses sound natural — removes punctuation and symbols.
    """
    # Remove URLs and slashes
    text = re.sub(r"http\S+|www\S+|/|\\", " ", text)
    # Replace punctuation with natural pauses
    text = text.replace(".", "").replace(",", "").replace(":", "")
    text = text.replace(";", "").replace("-", " ").replace("_", " ")
    text = text.replace("(", "").replace(")", "")
    # Remove emojis and symbols
    text = re.sub(r"[^\w\s]", "", text)
    # Compact multiple spaces
    text = re.sub(r"\s+", " ", text)
    return text.strip()
