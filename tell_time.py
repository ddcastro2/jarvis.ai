# tell_time.py
import datetime

def tell_time(speak):
    """Fetch current time."""
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The time is {time}")
