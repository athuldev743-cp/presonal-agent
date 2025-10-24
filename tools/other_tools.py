# other_tools.py
import os
import webbrowser
import subprocess
import platform
import random

def open_website(url: str):
    if not url.startswith("http"):
        url = "https://" + url
    try:
        webbrowser.open(url)
        return f"Opened {url} in your browser."
    except Exception:
        return "Sorry, I couldn't open the website."

def play_music(file_path: str):
    try:
        if platform.system() == "Windows":
            os.startfile(file_path)
        elif platform.system() == "Darwin":  # macOS
            subprocess.run(["open", file_path])
        else:  # Linux
            subprocess.run(["xdg-open", file_path])
        return f"Playing music: {file_path}"
    except Exception:
        return "Sorry, I couldn't play the music."

def shutdown_pc():
    try:
        if platform.system() == "Windows":
            os.system("shutdown /s /t 5")
        elif platform.system() == "Darwin":
            os.system("sudo shutdown -h now")
        else:
            os.system("shutdown now")
        return "Shutting down..."
    except Exception:
        return "Sorry, I couldn't shut down your PC."

def say_joke():
    jokes = [
        "Why did the computer go to the doctor? Because it caught a virus!",
        "Why was the math book sad? Because it had too many problems!",
        "Why don’t programmers like nature? It has too many bugs!"
    ]
    return random.choice(jokes)
