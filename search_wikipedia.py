# search_wikipedia.py
import wikipedia

def search_wikipedia(query, speak):
    """Search Wikipedia and return summary."""
    try:
        speak("Searching Wikipedia...")
        results = wikipedia.summary(query, sentences=2)
        speak(f"According to Wikipedia, {results}")
    except wikipedia.exceptions.DisambiguationError as e:
        speak("Multiple results found. Please be more specific.")
    except wikipedia.exceptions.PageError:
        speak("No Wikipedia page found for this search.")
