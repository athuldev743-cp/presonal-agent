# memory/memory.py
# Simple in-session memory using a list of past interactions

conversation_memory = []  # Stores tuples: (user_command, assistant_response)

def remember(command, response):
    """
    Store command and response in memory.
    """
    conversation_memory.append((command, response))
    if len(conversation_memory) > 50:  # prevent infinite growth
        conversation_memory.pop(0)
    return "I’ll remember that for this session."

def recall(query):
    """
    Search memory for a query using simple keyword matching.
    """
    for user_cmd, response in reversed(conversation_memory):
        if query.lower() in user_cmd.lower() or query.lower() in response.lower():
            return f"You said earlier: '{user_cmd}', and I replied: '{response}'"
    return "I can’t recall anything about that in this session."
