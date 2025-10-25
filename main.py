# main.py
from speech_io import listen_command, speak
from agent import process_command

def main():
    speak("Welcome back, Mr. Athul Dev. I’m online and ready to assist you.")

    while True:
        command = listen_command()
        if not command:
            continue

        cmd_lower = command.lower()
        if cmd_lower in ["exit", "quit", "bye"]:
            speak("Goodbye, Mr. Athul Dev. Take care.")
            break

        response = process_command(command)
        speak(response)

if __name__ == "__main__":
    main()
