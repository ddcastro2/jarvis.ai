# take_command.py
import speech_recognition as sr

def take_command():
    """Listen to user command via microphone and convert to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except Exception as e:
        print("Sorry, could not understand. Say that again please.")
        return "None"
    return query.lower()
