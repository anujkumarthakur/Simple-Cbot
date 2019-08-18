import pyttsx3
import datetime
import speech_recognition as sr
engin=pyttsx3.init('sapi5')
voices=engin.getProperty('voices')
engin.setProperty('voice',voices[0].id)

def speak(audio):
    engin.say(audio)
    engin.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("Good morinig sir")
    elif hour>12 and hour<=18:
        speak("Good After Noon Sir")
    else:
        speak("Good Evening Sir")
def takecommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listenin")
        r.phrase_threshold=1
        audio=r.listen(source)
        try:
            print("Recogination")
            query=r.recognize_google(audio,language='an-in')
            print(f"user-said:{query}\n")
        except Exception as e:
            print("say agin plz..")
            return "None"
        return query
if __name__ =="__main__":
    #speak("Anuj is a bad boy")
    #wishme()
    takecommand()
