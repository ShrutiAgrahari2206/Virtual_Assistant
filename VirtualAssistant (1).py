import datetime
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import os
import random
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate', 150)
# print(type(engine))
# print(engine)

def speak(msg): #to speak. Text to Speech
    engine.say(msg)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    # minute= int(datetime.datetime.now().minute)
    if (hour>=0 and hour<12):
        speak("Good Morning Boss!")     #Text to Speech
    elif(hour>=12 and hour<18):
        speak("Good Afternoon Boss")
    else:
        speak("Good Evening Boss")
    speak("How may I help you?")

def takeCommand(): #it takes microphone input from the user and return the string output
     r=sr.Recognizer()    #recogniser class helps in recognising the audio
     with sr.Microphone() as source:
         print("Listening...")
         r.pause_threshold = 0.5 #it refers to the amount of time gap after which the audio is supposed to be complete
         r.energy_threshold =300
         audio=r.listen(source) #digitaldata of whatsoever hs been spoken will be stored in audio
     try:
      print("Recognising...")
      query=r.recognize_google(audio,language="en-in")
      print("User Said:",query)
     except Exception as e:
      print("Say that again please!")
      return "None"
     return query
wishMe()
#while True:
if 1:
    query = takeCommand().lower()             #query="search covid19 on wikipedia"
    #logic for executing tasks based on query
    if 'wikipedia' in query:                 #wikipedia is a keyword. If user doesnt say that, it will not work.
        speak("Searching Wikipedia")
        query=query.replace("wikipedia", "")    #query="search covid19 on"
        results=wikipedia.summary(query, sentences=1)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif 'youtube' in query:
        webbrowser.open("youtube.com")
    elif 'facebook' in query:
        webbrowser.open("fb.com")
    elif 'stack overflow' in query:
        webbrowser.open("stackoverflow.com")
    elif 'google' in query:
        query=query.replace("google","")
        query=query.replace("search","")
        webbrowser.open(f"https://google.com/search?q={query}"  )
    elif (('music' in query) or ("song" in query)):
        music_dir= 'D:\\OldSongs' #\\ slash is to escape the character
        songs=os.listdir(music_dir)  #listdir is used to enlist all the songs of mentioned directory
        print(songs)
        song=random.choice(songs)
        os.startfile(os.path.join(music_dir,song)) #song[0] will play the first song. using random module, song can be shuffled
    elif 'time' in query:
        time=datetime.datetime.now().strftime("%H:%M")
        speak("sir, the time is")
        speak(time)
        print(time)
    elif ('sleep' in query) or ("so jao" in query):
        print("Thank you")
        speak("Thank you")
        exit()


