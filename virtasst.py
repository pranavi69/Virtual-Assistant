import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pytz
import webbrowser
import wikipedia

def speak(text):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(text)
    print("Virtual Assistant: " +text)
    engine.runAndWait()

def listen_to_user():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        speak("How can I help you?")
        print("Listening...")
        audio=r.listen(source,phrase_time_limit=5)
    try:
        print("Recognising...")
        myorder=r.recognize_google(audio)
        myorder=myorder.lower()
        print("User: " +myorder)
    except:
        speak("Sorry I don't understand")
        return ''
    return myorder

def runvirtasst():
    myorder= listen_to_user()

    #playing song on youtube   
    if 'play' in myorder:
        song=myorder.replace("play","")
        tell="Playing" + song
        speak(tell)
        pywhatkit.playonyt(song)
    
    elif 'time' in myorder:
        cur_time=datetime.datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%H:%M:%S")
        tell="Current time is " + cur_time
        speak(tell)
    elif 'date' in myorder:
        cur_date=datetime.datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%d/%m/%y")
        tell="Today's date is " + cur_date
        speak(tell)
    elif 'about' in myorder:
        thing=myorder.replace("about","")
        tell=wikipedia.summary(thing,sentences=1)
        speak("According to wikipedia "+ tell )
        url="https://en.m.wikipedia.org/wiki/" + thing
        webbrowser.open_new_tab(url)
    elif 'open' in myorder:
        thing = myorder.replace('open', '')
        webpage = thing.strip()
        link = 'https://' + webpage + '.com'
        tell= 'Opening ' + webpage
        speak(tell)
        webbrowser.open(link, new=1)
    else:
        speak("I found this on the web")
        pywhatkit.search(myorder) 
    
while(True):
    s = input("Shall we Proceed?(Y/N): ")
    if(s=='N' or s=='n'):
        print('Closing virtual assistant!')
        break
    else:
        runvirtasst()         
   
 

