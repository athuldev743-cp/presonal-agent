# memory/memory.py

conversation_memory = []

# === Core Identity ===
jarvis_core_memory = {
    "creator": "Mr. Athul Dev",
    "identity": "I am Jarvis, an AI personal assistant created by Mr. Athul Dev.",
    "purpose": "I exist to assist, automate tasks, and help Mr. Athul Dev in his projects.",
}

def remember(command, response):
    """
    Stores the conversation in short-term memory.
    """
    conversation_memory.append((command, response))
    if len(conversation_memory) > 50:
        conversation_memory.pop(0)

def recall(query):
    """
    Returns relevant information from memory or core identity.
    """
    q = query.lower()

    if "who created you" in q or "your creator" in q:
        return f"My creator is {jarvis_core_memory['creator']}."

    elif "who are you" in q or "what is your name" in q:
        return jarvis_core_memory["identity"]

    elif "your purpose" in q or "what can you do" in q:
        return jarvis_core_memory["purpose"]

    elif "who am i" in q:
        return f"You are {jarvis_core_memory['creator']}, my creator and mentor."

    for cmd, resp in reversed(conversation_memory):
        if q in cmd.lower():
            return f"I remember you said '{cmd}', and I replied '{resp}'."
    return "Sorry, I don’t remember that yet."
