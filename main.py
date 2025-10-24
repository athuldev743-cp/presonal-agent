# main.py
from speech_io import listen_command, speak
from agent import process_command

def main():
    speak("Hi sir, How can I help you today?")
    
    while True:
        command = listen_command()
        if not command:
            continue

        cmd_lower = command.lower()
        if cmd_lower in ["exit", "quit"]:
            speak("Goodbye, sir.")
            break

        response = process_command(command)
        speak(response)

if __name__ == "__main__":
    main()
