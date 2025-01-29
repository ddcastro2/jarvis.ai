import pyttsx3 #pip install pyttsx3 == it is used to convert text to speech
import datetime
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is:")
    speak(date)
    speak(month)
    speak(year)

def greeting ():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <12:
        speak("Good morning, Sir!")
    elif hour >= 12 and hour <18:
        speak("Good afternoon Sir!")
    elif hour >= 18 and hour <24:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")\

def wishme():
    speak("Welcome Back Sir")
    time()
    date()
    greeting()
    speak("Jarvis at your service, please tell me how I can help you?")

def takeCommandCMD():
    query = input("please tell me how I can help you?\n")
    return query

if __name__ == "_main_":
    wishme()
    while True:
        query = takeCommandCMD().lower()
        if 'time' in query:
            time()
        elif 'date' in query:
            date()