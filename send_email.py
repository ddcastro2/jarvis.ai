# send_email.py
import smtplib
from email_credentials import EMAIL, PASSWORD
  # Don't forget to import your credentials

def send_email(to, content, speak):
    """Send an email using stored credentials in `secrets.py`."""
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.sendmail(EMAIL, to, content)
        server.close()
        speak("Email has been sent successfully!")
    except Exception as e:
        speak("Sorry, I was unable to send the email.")
