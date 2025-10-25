# agent.py - FIXED FOR DEPLOYMENT
import os
from dotenv import load_dotenv

# Load environment variables first
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OpenAI API key not found in environment variables")

# Import OpenAI with compatibility handling
try:
    from openai import OpenAI
    # Initialize with minimal parameters to avoid proxies issue
    client = OpenAI(api_key=OPENAI_API_KEY)
except TypeError as e:
    # Fallback for version compatibility
    if "proxies" in str(e):
        import openai
        openai.api_key = OPENAI_API_KEY
        client = None
        OPENAI_OLD_VERSION = True
    else:
        raise
else:
    OPENAI_OLD_VERSION = False

# Import tools with error handling
try:
    from tools import calculator, web_search, health, weather, other_tools
    TOOLS_AVAILABLE = True
except ImportError:
    TOOLS_AVAILABLE = False

# Import memory with error handling  
try:
    from memory.memory import conversation_memory, remember, recall
    MEMORY_AVAILABLE = True
except ImportError:
    MEMORY_AVAILABLE = False
    # Fallback memory
    conversation_memory = []
    def remember(command: str, response: str):
        conversation_memory.append((command, response))
    def recall(query: str):
        return "Memory system unavailable"

def process_command(command: str):
    cmd = command.lower()

    # === Predefined Tools ===
    if TOOLS_AVAILABLE:
        if "calculate" in cmd:
            response = calculator.calculate(command)
            if MEMORY_AVAILABLE:
                remember(command, response)
            return response

        elif "tell me about" in cmd:
            response = web_search.search_wikipedia(command)
            if MEMORY_AVAILABLE:
                remember(command, response)
            return response

        elif "heart rate" in cmd:
            try:
                rate = int(cmd.split()[-1])
                response = health.check_heart_rate(rate)
            except:
                response = "Please provide the heart rate as a number."
            if MEMORY_AVAILABLE:
                remember(command, response)
            return response

        elif "weather" in cmd:
            response = weather.get_weather(command)
            if MEMORY_AVAILABLE:
                remember(command, response)
            return response

        elif "open" in cmd and ".com" in cmd:
            response = other_tools.open_website(command.split("open")[-1].strip())
            if MEMORY_AVAILABLE:
                remember(command, response)
            return response

        elif "joke" in cmd:
            response = other_tools.say_joke()
            if MEMORY_AVAILABLE:
                remember(command, response)
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

    elif "recall" in cmd and MEMORY_AVAILABLE:
        query = command.replace("recall", "").strip()
        response = recall(query)
        return response

    # === Chat with OpenAI ===
    else:
        messages = []
        
        # Add conversation history if available
        if MEMORY_AVAILABLE and conversation_memory:
            recent_memory = conversation_memory[-10:]
            for i, (user_cmd, resp) in enumerate(recent_memory):
                if i % 2 == 0:
                    messages.append({"role": "user", "content": user_cmd})
                else:
                    messages.append({"role": "assistant", "content": resp})
        
        # Add system message for context
        system_message = {
            "role": "system", 
            "content": "You are JARVIS, a helpful AI assistant created by Athul Dev. Be concise, professional, and helpful. Respond in a natural speaking style."
        }
        messages.insert(0, system_message)
        
        # Add current command
        messages.append({"role": "user", "content": command})

        try:
            if OPENAI_OLD_VERSION:
                # Old version (v0.x)
                import openai
                response_obj = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=messages,
                    max_tokens=150,
                    temperature=0.7,
                )
                response = response_obj.choices[0].message.content
            else:
                # New version (v1.x+)
                response_obj = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=messages,
                    max_tokens=150,
                    temperature=0.7,
                )
                response = response_obj.choices[0].message.content

            # Clean up response
            response = response.replace("**", "").replace("__", "")
            response = response.replace('"', '').replace("'", "")
            response = ' '.join(response.split())
            
        except Exception as e:
            response = f"I encountered an error: {str(e)}"

        if MEMORY_AVAILABLE:
            remember(command, response)
        return response