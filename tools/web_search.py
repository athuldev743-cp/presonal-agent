import wikipedia

def search_wikipedia(query: str):
    try:
        topic = query.lower().replace("tell me about", "").strip()
        summary = wikipedia.summary(topic, sentences=3)
        return summary
    except Exception:
        return "Sorry, I couldn't find information about that topic."
