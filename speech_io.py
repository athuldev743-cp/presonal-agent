# speech_io.py
import speech_recognition as sr
import pyttsx3
import os
import warnings

# Suppress warnings
warnings.filterwarnings("ignore")

# Apply SpeechBrain compatibility patch (if needed elsewhere in your project)
try:
    import torchaudio
    if not hasattr(torchaudio, 'list_audio_backends'):
        torchaudio.list_audio_backends = lambda: ['soundfile']
except ImportError:
    pass  # torchaudio not needed for basic speech IO

# Initialize speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Configure voice settings
try:
    voices = engine.getProperty("voices")
    if voices:
        engine.setProperty("voice", voices[0].id)  # First available voice
    engine.setProperty("rate", 180)  # Speaking speed
    engine.setProperty("volume", 0.8)  # Volume level
except Exception as e:
    print(f"Voice configuration warning: {e}")

def speak(text):
    """Convert text to speech with cleaning for better TTS"""
    print(f"🤖 Jarvis: {text}")
    
    # Clean text for better speech synthesis
    clean_text = text.replace("**", "").replace("__", "")  # Remove markdown
    clean_text = clean_text.replace('"', '').replace("'", "")  # Remove quotes
    clean_text = clean_text.replace("  ", " ")  # Remove double spaces
    clean_text = clean_text.strip()
    
    try:
        engine.say(clean_text)
        engine.runAndWait()
    except Exception as e:
        print(f"Speech error: {e}")

def listen_command(timeout=5, phrase_time_limit=5):
    """Listen for voice command with error handling"""
    try:
        with sr.Microphone() as source:
            # Adjust for ambient noise
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            print("🎧 Listening...")
            
            # Listen for audio
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            
            # Recognize speech
            text = recognizer.recognize_google(audio)
            print(f"🗣️ You said: {text}")
            return text
            
    except sr.WaitTimeoutError:
        print("⏰ Listening timed out. Please speak within 5 seconds.")
        return ""
    except sr.UnknownValueError:
        print("❓ Could not understand audio. Please try again.")
        return ""
    except sr.RequestError as e:
        print(f"🌐 Speech recognition service error: {e}")
        return ""
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")
        return ""