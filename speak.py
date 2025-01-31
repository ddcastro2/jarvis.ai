# speak.py
import pyttsx3

def speak(audio):
    """Convert text to speech."""
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()
