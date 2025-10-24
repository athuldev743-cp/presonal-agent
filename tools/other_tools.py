# other_tools.py

import os
import webbrowser

def open_website(url: str):
    """
    Opens a website in the default browser.
    """
    if not url.startswith("http"):
        url = "https://" + url
    try:
        webbrowser.open(url)
        return f"Opened {url} in your browser."
    except Exception:
        return "Sorry, I couldn't open the website."

def play_music(file_path: str):
    """
    Plays a local music file.
    """
    try:
        os.startfile(file_path)  # Windows only; use subprocess for cross-platform
        return f"Playing music: {file_path}"
    except Exception:
        return "Sorry, I couldn't play the music."

def shutdown_pc():
    """
    Shuts down the PC.
    """
    try:
        os.system("shutdown /s /t 5")  # Windows
        return "Shutting down in 5 seconds..."
    except Exception:
        return "Sorry, I couldn't shut down your PC."

def say_joke():
    """
    Returns a random joke.
    """
    jokes = [
        "Why did the computer go to the doctor? Because it caught a virus!",
        "Why was the math book sad? Because it had too many problems!",
        "Why don’t programmers like nature? It has too many bugs!"
    ]
    import random
    return random.choice(jokes)
