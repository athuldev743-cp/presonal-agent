conversation_memory = []

def remember(command, response):
    conversation_memory.append((command, response))
    if len(conversation_memory) > 50:
        conversation_memory.pop(0)
    return "I’ll remember that for this session."

def recall(query):
    for user_cmd, response in reversed(conversation_memory):
        if query.lower() in user_cmd.lower() or query.lower() in response.lower():
            return f"You said earlier: '{user_cmd}', and I replied: '{response}'"
    return "I can’t recall anything about that in this session."
