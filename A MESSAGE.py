import time
import speech_recognition as sr
import pyttsx3
from playsound import playsound
 

engine = pyttsx3.init() 
voice = engine.getProperty('voices') 
engine.setProperty('voice', voice[1].id) #changing voice to index 1 for male voice or 0 for female
engine.setProperty("rate",160)
engine.runAndWait()

def Speak(audio):
   
    engine.say(audio)
    engine.runAndWait()
    print("Unknown: ", audio)

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You: {query}\n")
        
       
    except Exception as e:
        print(e)
        return "None"
    return

Speak("HELLO!!, you are i the WORLD OF DANGER. SO BE AWARE AND BRAVE, THEIR IS ONLY 1 percent chance to survive this world. after completing a period of surviving you are able to come back to you home.\n\n GOOD LUCK!!!")
Speak("Now,This message will automatically destroy in 3 seconds")

def countdown(n):
    if n> 0:
        playsound("Beep.mp3")
        time.sleep(1)
        Speak(n)
        countdown(n-1)
    else:
        print("BLAST!!!")
countdown(3)