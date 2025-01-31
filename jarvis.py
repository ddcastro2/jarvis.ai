#The function that lets Jarvis speak
from speak import speak
#The frunction that elicits the provess of Jarvis analyzing what is being said (speech recognition)
from take_command import take_command
#The function that has Jarvis greet the user
from wish_me import wish_me
#The function that has Jarvis tell the time
from tell_time import tell_time
#The function that has Jarvis to tell the date
from tell_date import tell_date
#The function that lets Jarvis open wikipedia
from search_wikipedia import search_wikipedia
#The function that lets Jarvis open a website
from open_website import open_website
#The function that lets Jarvis send an email
from send_email import send_email
#The function that lets Jarvis do a fgorecast
from get_weather import get_weather
#The function that lets Jarvis take a screenshot
from take_screenshot import take_screenshot
#The functiuon that has Jarvis say a joke(s)
from tell_joke import tell_joke
#The function that stores information of the email's username and password

from email_credentials import EMAIL, PASSWORD
if __name__ == "__main__":
    wish_me(speak)
    while True:
        command = take_command()
        if "time" in command:
            tell_time(speak)
        elif "date" in command:
            tell_date(speak)
        elif "wikipedia" in command:
            search_wikipedia(command.replace("wikipedia", ""), speak)
        elif "open youtube" in command:
            open_website("youtube")
        elif "open google" in command:
            open_website("google")
        elif "send email" in command:
            speak("What should I say?")
            content = take_command()
            speak("Whom should I send it to?")
            recipient = input("Enter recipient email: ")  # Input for demo purposes
            send_email(recipient, content, speak)
        elif "weather" in command:
            get_weather(speak)
        elif "joke" in command:
            tell_joke(speak)
        elif "screenshot" in command:
            take_screenshot(speak)
        elif "exit" in command:
            speak("Goodbye!")
            break
        else:
            speak("I'm not sure how to do that yet.")
