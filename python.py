# import datetime
from distutils.spawn import spawn
from operator import truediv
import os
import requests
import bs4
import pyexpat
import pyttsx3
import random
import datetime
import pyaudio
import wikipedia
import pywhatkit
import webbrowser
import speech_recognition as sr
engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice

engine.setProperty('voice', voices[0].id)
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning Sir")
    elif hour>=12 and hour<=18:
            speak("Good Afternoon Sir")      
    else:
        speak("Good Evening Sir")
    speak("I am Jarvis sir Please tell me how may i help you")  
def speak(audio):
    engine.say(audio) 
    engine.runAndWait()
def takecom():
    # Itis taking Microphone Input from user
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("recognizing..") 
        query=r.recognize_google(audio,language='en-in')
        print(f"user said {query}")            

            
    except Exception as e:
        # print(e)
        print("Say that again please !")
        return "None"      
    return query      
if __name__ == "__main__":
    wishme()
    while True:
        query=takecom().lower()
        
        
    # Logic for Executing a task 
        if'wikipedia' in query:
            speak("Searching Wikipedia")
            query=query.replace('wikipedia','')
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
      
        elif 'open youtube' in query:
            speak('Opening Youtube')
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            speak('opening google')
            webbrowser.open("google.com")
        elif 'open instagram' in query:
            speak('Opening Instagram')
            webbrowser.open('https://www.instagram.com/')
        
        elif 'what is  the current  time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strtime}")
        elif 'who are you' in query:
            speak("Jarvis is a ai assistant and have developed by Aniket joshi ")
        elif 'hello jarvis' in query:
                speak('Hello sir how may i help you')
        elif 'on youtube' in query:
            song=query.replace('on youtube','')
            pywhatkit.playonyt(query)
            speak(f"playing {query} on youtube")
        elif 'on google' or 'search' in query:
            pywhatkit.search(query)
        elif 'quit' in query:
            exit()