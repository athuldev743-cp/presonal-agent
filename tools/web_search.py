# web_search.py
import wikipedia

def search_wikipedia(query: str):
    topic = query.lower().replace("tell me about", "").strip()
    try:
        summary = wikipedia.summary(topic, sentences=3)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Multiple results found for '{topic}', please be more specific: {e.options[:5]}"
    except wikipedia.exceptions.PageError:
        return f"Sorry, I couldn't find information about '{topic}'."
    except Exception:
        return "Sorry, an error occurred while searching Wikipedia."
