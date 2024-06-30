import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening.....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "alexa" in command:
                command = command.replace("alexa","")
                print("\n") 
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command+"\n")
    if "play" in command:
        song = command.replace("play","")
        talk("playing"+song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        talk("Current time is " + time)
    elif "who is" in command or "information" in command:
        person = command.replace("who is","")
        info = wikipedia.summary(person,1)
        print("[ "+info+" ]")
        talk("information"+info)
    elif "who am i" in command:
        talk("you are a person\nBut for me you are a god")
    elif "date" in command:
        print("No")
        talk("No")
    elif "what are you doing" in command:
        print("I am helping you")
        talk("I am helping you")
    elif "where are you" in command:
        print("In front of you")
        talk("In front of you")
    elif "are you single" in command or "do you have boyfriend" in command:
        print("I am in relationship with wifi")
        talk("I am in relationship with wifi")
    elif "joke" in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
    elif "ok bye" in command or "go" in command:
        talk("Ok bye sir")
        quit()
    else:
        talk("I can't understand \nPlease say it again.")

while True:
    run_alexa()