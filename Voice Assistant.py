import speech_recognition as sr
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0])
recognizer = sr.Recognizer()

def cmd():

    while True:

        with sr.Microphone() as source:
            print("Clearing background voices. Please wait.")
            recognizer.adjust_for_ambient_noise(source)
            print("Ask me anything")
            recorded_audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(recorded_audio)
            print("Your message:", format(command))
        except Exception as e:
            print(e)


        if 'play' in command:
            b = 'Opening YouTube'
            engine.say(b)
            engine.runAndWait()
            pywhatkit.playonyt(command)

        if 'exit' in command:
            exit()

cmd()