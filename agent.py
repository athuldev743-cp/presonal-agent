# agent.py - MINIMAL WORKING VERSION
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OpenAI API key not found in environment variables")

# Initialize OpenAI
from openai import OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)

# Simple memory system
conversation_memory = []

def remember(command: str, response: str):
    conversation_memory.append((command, response))
    if len(conversation_memory) > 20:
        conversation_memory.pop(0)

def recall(query: str):
    for cmd, resp in conversation_memory:
        if query.lower() in cmd.lower():
            return resp
    return "I don't recall anything about that."

def process_command(command: str):
    cmd = command.lower()

    # === Identity & Creator Awareness ===
    if "who created you" in cmd or "your creator" in cmd:
        return "I was created by Mr. Athul Dev, my brilliant creator and mentor."

    elif "who are you" in cmd or "what is your name" in cmd:
        return "I am JARVIS, your personal AI assistant created by Mr. Athul Dev."

    elif "your purpose" in cmd or "what can you do" in cmd:
        return "My purpose is to assist you with calculations, web searches, health monitoring, weather information, and general tasks to make your life easier."

    elif "who am i" in cmd:
        return "You are Mr. Athul Dev, my creator and the person I'm dedicated to serving."

    elif "recall" in cmd:
        query = command.replace("recall", "").strip()
        return recall(query)

    # === Chat with OpenAI ===
    else:
        messages = []
        
        # Add conversation history
        if conversation_memory:
            recent_memory = conversation_memory[-6:]  # Last 3 conversations
            for user_cmd, resp in recent_memory:
                messages.append({"role": "user", "content": user_cmd})
                messages.append({"role": "assistant", "content": resp})
        
        # Add system message
        messages.insert(0, {
            "role": "system", 
            "content": "You are JARVIS, a helpful AI assistant created by Athul Dev. Be concise, professional, and helpful. Keep responses under 200 characters."
        })
        
        # Add current command
        messages.append({"role": "user", "content": command})

        try:
            response_obj = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=150,
                temperature=0.7,
            )
            response = response_obj.choices[0].message.content

            # Clean response for consistency
            response = response.replace("**", "").replace("__", "")
            response = ' '.join(response.split())
            
        except Exception as e:
            response = f"I encountered an error: {str(e)}"

        remember(command, response)
        return response