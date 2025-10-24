import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

def get_default_microphone_index():
    """Return the index of the default working microphone."""
    mic_list = sr.Microphone.list_microphone_names()
    for i, name in enumerate(mic_list):
        if "Realtek" in name or "Microphone" in name:
            return i
    # fallback
    return 0

MIC_INDEX = get_default_microphone_index()

def listen_command():
    """Listen to user via microphone and return text."""
    try:
        with sr.Microphone(device_index=MIC_INDEX) as source:
            print(f"🎧 Listening using mic index {MIC_INDEX}...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            # Wait max 5 seconds for speech to start
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
            text = recognizer.recognize_google(audio)
            print(f"🗣️ You said: {text}")
            return text
    except sr.WaitTimeoutError:
        print("❌ No speech detected, timed out.")
        return ""
    except sr.UnknownValueError:
        print("❌ Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        print("❌ Could not request results from Google Speech Recognition service.")
        return ""
    except Exception as e:
        print(f"❌ Error: {e}")
        return ""

def speak(text):
    """Speak text using pyttsx3."""
    print(f"🤖 Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()
