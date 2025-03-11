import speech_recognition as sr
import webbrowser
import pyttsx3 
import musiclibrary
import requests
from openai import OpenAI
# recognizer is class in speech recognition module which identifies the text
recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "168943f98b2a47f4ad1dda4a4c2b5a32" #this is free api u can get your own free api from from news api key which provide free apis 
# these above and below are bydefault in pyttsx3 module
def speak(text) :
    engine.say(text)
    engine.runAndWait()


def aiProcess(command) :
    client = OpenAI(api_key = "openai-api-key-and it is paid")
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role" : "system", "content" : "You are a virtual Assistant named jarvis  skilled in general tasks like Alexa and Google"},
        {"role" : "user", "content": command}
    ]
    )
    
    return completion.choices[0].message.content

def processCommand(c) :
    if "open google" in c.lower() :
        webbrowser.open("http://google.com")
    elif "open facebook" in c.lower() :
        webbrowser.open("http://facebook.com")
    elif "open youtube" in c.lower() :
        webbrowser.open("http://youtube.com")
    elif "open linkedin" in c.lower() :
        webbrowser.open("http://linkedin.com")
    elif c.lower().startswith("play") :
        song = c.lower().split(" ")[1]
        # suppose we have play march 
        # split converts play march into list -> ['play', 'march']
        # and then[1] we selected the first argument of list
        link = musiclibrary.music[song] 
        webbrowser.open(link)
    elif "news" in c.lower() :
        r = requests.get("https://newsapi.org/v2/everything?q=apple&from=2025-03-10&to=2025-03-10&sortBy=popularity&apiKey=168943f98b2a47f4ad1dda4a4c2b5a32")
        
        if r.status_code == 200 :
            # parse the json response
            data = r.json()
            # /extract the articles
            articles = data.get('articles', [])
            
            for article in articles :
                speak(article['title'])
    else :
        # let openai handle the request
        output = aiProcess(c)
        speak(output)
    
    
        
if __name__ == "__main__" :
        speak("Initializing Jarvis....")
        # below code is taken from github template
        while True :
            # Listen for the wake word Jarvis
            # obtain audio from the microphone
            r = sr.Recognizer()
            # recognize speech using google
            print("Recgnizning....")
            try :
                with sr.Microphone() as source :
                    print("Listening...")
                    audio = r.listen(source, timeout=2, phrase_time_limit=1)
                word = r.recognize_google(audio)
                if(word.lower() == "jarvis") :
                    speak("Ya")
                    # Listen for command
                    with sr.Microphone() as source :
                        print("Jarvis Active")
                        audio = r.listen(source)
                        command = r.recognize_google(audio)
                        processCommand(command)
                        
                        
            except Exception as e :
                print("error ; {0}".format(e))