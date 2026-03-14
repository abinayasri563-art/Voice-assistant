import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import datetime

# initialize speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        command = r.recognize_google(audio)
        print("User said:", command)
    except:
        speak("Sorry, I didn't understand.")
        return "none"

    return command.lower()

def assistant():
    speak("Hello, I am your voice assistant. How can I help you?")

    while True:
        command = take_command()

        if "time" in command:
            time = datetime.datetime.now().strftime("%H:%M")
            speak("The time is " + time)

        elif "wikipedia" in command:
            speak("Searching Wikipedia")
            command = command.replace("wikipedia", "")
            result = wikipedia.summary(command, sentences=2)
            speak(result)

        elif "open youtube" in command:
            webbrowser.open("https://youtube.com")

        elif "open google" in command:
            webbrowser.open("https://google.com")

        elif "exit" in command:
            speak("Goodbye!")
            break

assistant()