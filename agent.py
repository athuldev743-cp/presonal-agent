# agent.py - FIXED VERSION
import os
from dotenv import load_dotenv
from openai import OpenAI
from tools import calculator, web_search, health, weather, other_tools
from memory.memory import conversation_memory, remember, recall

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OpenAI API key not found in environment variables")

# FIX: Initialize OpenAI client with minimal parameters
try:
    client = OpenAI(api_key=OPENAI_API_KEY)
except TypeError:
    # Fallback for version compatibility
    client = OpenAI(api_key=OPENAI_API_KEY, base_url="https://api.openai.com/v1")

def process_command(command: str):
    cmd = command.lower()

    # === Predefined Tools ===
    if "calculate" in cmd:
        response = calculator.calculate(command)
        remember(command, response)
        return response

    elif "tell me about" in cmd:
        response = web_search.search_wikipedia(command)
        remember(command, response)
        return response

    elif "heart rate" in cmd:
        try:
            rate = int(cmd.split()[-1])
            response = health.check_heart_rate(rate)
        except:
            response = "Please provide the heart rate as a number."
        remember(command, response)
        return response

    elif "weather" in cmd:
        response = weather.get_weather(command)
        remember(command, response)
        return response

    elif "open" in cmd and ".com" in cmd:
        response = other_tools.open_website(command.split("open")[-1].strip())
        remember(command, response)
        return response

    elif "play music" in cmd:
        response = other_tools.play_music("music.mp3")
        remember(command, response)
        return response

    elif "shutdown" in cmd:
        response = other_tools.shutdown_pc()
        remember(command, response)
        return response

    elif "joke" in cmd:
        response = other_tools.say_joke()
        remember(command, response)
        return response

    elif "recall" in cmd:
        query = command.replace("recall", "").strip()
        response = recall(query)
        return response

    # === Identity & Creator Awareness ===
    elif "who created you" in cmd or "your creator" in cmd:
        return "I was created by Mr. Athul Dev, my brilliant creator and mentor."

    elif "who are you" in cmd or "what is your name" in cmd:
        return "I am JARVIS, your personal AI assistant created by Mr. Athul Dev."

    elif "your purpose" in cmd or "what can you do" in cmd:
        return "My purpose is to assist you with calculations, web searches, health monitoring, weather information, and general tasks to make your life easier."

    elif "who am i" in cmd:
        return "You are Mr. Athul Dev, my creator and the person I'm dedicated to serving."

    # === Chat with OpenAI ===
    else:
        messages = []
        
        # Add conversation history if available
        if conversation_memory:
            recent_memory = conversation_memory[-10:]
            for i, (user_cmd, resp) in enumerate(recent_memory):
                if i % 2 == 0:
                    messages.append({"role": "user", "content": user_cmd})
                else:
                    messages.append({"role": "assistant", "content": resp})
        
        # Add system message for context
        system_message = {
            "role": "system", 
            "content": "You are JARVIS, a helpful AI assistant created by Athul Dev. Be concise, professional, and helpful. Respond in a natural speaking style suitable for text-to-speech."
        }
        messages.insert(0, system_message)
        
        # Add current command
        messages.append({"role": "user", "content": command})

        try:
            response_obj = client.chat.completions.create(
                model="gpt-3.5-turbo",  # Using gpt-3.5-turbo for better compatibility
                messages=messages,
                max_tokens=150,
                temperature=0.7,
            )
            response = response_obj.choices[0].message.content

            # Clean up for natural speech
            response = response.replace("**", "").replace("__", "")
            response = response.replace('"', '').replace("'", "")
            response = ' '.join(response.split())
            
        except Exception as e:
            response = f"I encountered an error while processing your request: {str(e)}"

        remember(command, response)
        return response