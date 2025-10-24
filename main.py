from speech_io import listen_command, speak
from agent import process_command

def main():
    speak("Hi sir,  How can I help you today?")
    
    while True:
        # Listen to user command
        command = listen_command()
        if not command:
            continue

        command_lower = command.lower()

        # Exit condition
        if command_lower in ["exit", "quit"]:
            speak("Goodbye, sir.")
            break

        # Send everything else to agent.py → handles tools, memory, Claude
        response = process_command(command)
        speak(response)

if __name__ == "__main__":
    main()
