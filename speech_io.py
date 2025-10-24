import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty("rate", 160)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # Choose a voice

def speak(text):
    print(f"🤖 Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

def listen_command(timeout=5, phrase_time_limit=5):
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("🎧 Listening...")
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            text = recognizer.recognize_google(audio)
            print(f"🗣️ You said: {text}")
            return text
    except sr.WaitTimeoutError:
        print("❌ Listening timed out. Please speak faster.")
        return ""
    except sr.UnknownValueError:
        print("❌ Could not understand audio.")
        return ""
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return ""
