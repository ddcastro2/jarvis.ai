# tell_date.py
import datetime

def tell_date(speak):
    """Fetch current date."""
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    speak(f"Today's date is {date}")
