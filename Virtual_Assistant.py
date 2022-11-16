import pyttsx3                              #pip install pyttsx3
import speech_recognition as sr             #pip install speechRecognition
import datetime
import wikipedia                            #pip install wikipedia
import webbrowser
import os
import smtplib
# import time
# from plyer import notification

source = pyttsx3.init('sapi5') #sapi5, for  windows and nsss for mac, espeak for every other platform
voices = source.getProperty('voices')
# print(voices[1].id) '''checking for voices present in system'''
source.setProperty('voice', voices[1].id)


def speak(audio):
    source.say(audio)
    source.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("hello , I am quinn, what do want my help with")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        speak("I did not recognize that, can you  please repeat what you just said...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('abc1977@gmail.com', 'abc')
    server.sendmail('abc1977@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching on Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open blogger' in query:
            webbrowser.open("blogger.com")   


        elif 'play music' in query:
            music_dir = 'A:\audio files'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\ASUS\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            # "C:\Users\ASUS\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(codePath)

        elif 'email to kunaal' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "abc1977@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry! I am unable to send this email")
