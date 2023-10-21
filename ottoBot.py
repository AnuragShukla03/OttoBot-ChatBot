import sys
import time
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser as wb
import pywhatkit
import os
import random
import pyautogui as pyauto

# ChatGPTAPIKey="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"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty(voices, voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    dt = int(datetime.datetime.now().hour)
    if dt >= 0 and dt < 12:
        speak("Good Morning!")

    elif dt >= 12 and dt < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am ethan hunt sir.")
    speak("please tell me how i may help you")


def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print("User said: ", query)
        except:
            
            return "None"

        return query



if __name__ == "__main__":  
    wishMe()
    while True:
        query = command().lower()

        if 'wikipedia'and 'who is'and 'tell me about' in query:
            speak("searching on wikipedia...")
            query = query.replace("wikipedia who is tell me about", " ")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            speak("please wait")
            query = query.replace("youtube", " ")
            speak("your song is ready")
            pywhatkit.playonyt(query)

        elif 'on google' in query:
            query = query.replace("on google", " ")
            wb.get().open("http://www.google.com/search?q="+query)

        elif 'play music' in query:
            music_dir="C:\\Users\\Brain Box\\Music\\music"
            song=os.listdir(music_dir)
            n=len(song)
            r=random.randrange(0,n)
            os.startfile(os.path.join(music_dir,song[r]))
        
        elif 'open vs code' in query:
            code_dir="C:\\Users\\Brain Box\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_dir)

        elif 'minimise' in query:
           speak("okay sir") 
           pyauto.click(1771,16)

        elif 'close' in query:
            speak("okay sir")
            pyauto.click(1899,27)  
        
        elif 'volume up' and 'increase volume' in query:
            speak("okay sir")
            pyauto.press('volumeup')

        elif 'volume down' and 'decrease volume' in query:
            speak("okay sir")
            pyauto.press('volumedown')
             
        elif 'volume mute' in query:
            speak("okay sir")
            pyauto.press('volumemute')

        elif 'pause' and 'stop music' in query:
            speak("Okay sir")
            pyauto.press('volumedown')
            time.sleep(0.5)
            pyauto.click(299,131)
        
        elif 'time' in query:
            now = datetime.datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(current_time)
            speak(f"the current time is {current_time}")
        
        elif 'quit'and 'exit' in query:
            speak("okay sir hope use me again")
            sys.exit()



        
        

            
            

