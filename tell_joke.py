# tell_joke.py
import random

def tell_joke(speak):
    """Tell a random joke."""
    jokes = [
        "Why don’t programmers like nature? It has too many bugs!",
        "Why do Java developers wear glasses? Because they don’t see sharp!",
        "Why was the JavaScript developer sad? Because he didn’t know how to 'null' his feelings."
    ]
    speak(random.choice(jokes))  # Randomly select a joke from the list
