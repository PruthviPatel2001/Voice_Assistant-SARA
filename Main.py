import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os

from googlesearch import search

engine = pyttsx3.init('sapi5')  # to take voice given by window API
voices = engine.getProperty("voices")

engine.setProperty('voice', voices[1].id)  # voice of sara


def speak(audio):  # function which help to speak our voice assistance
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon!!")

    else:
        speak("Good Evening!!")
    print("  I am Sara .. Always ready to help you..")
    speak("  I am Sara .. Always ready to help you..")


def takecommand():
    '''
    it takes input through microphone form users
    and returns string output
    :return:'''

    r = sr.Recognizer()
    with sr.Microphone() as source:

        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')  # google web speech api
        print(f"user said:{query}\n")

    except Exception as e:

        print("sorry! didn't get you , speak again please..")
        return "None"
    return query




if __name__ == '__main__':
    wishme()

    if 1:

        query = takecommand().lower()  #This variable store command that you give

        if 'wikipedia' in query:

            speak('searching wikipedia..')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'google' in query:

            speak('searching on google..')

            query = query.replace("google", "")

            for j in search(query, tld="co.in", num=10, stop=10, pause=2):
                print(j)


        elif "open youtube" in query:
            webbrowser.open("youtube.com")


        elif "open google" in query:
            webbrowser.open("google.com")


        elif "open outlook" in query:
            webbrowser.open("outlook.com")

        elif"open facebook" in query:
            webbrowser.open("facebook.com")

        elif "open instagram" in query:
            webbrowser.open("instagram.com")



        elif "play music" in query:

            music_dir = "F:\song"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))




        elif "the time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strtime)
            speak(f"sir, the time is {strtime}")


        elif "open pycharm" in query:

            codePath = "E:\\Softwares\\PyCharm 2020.1\\bin\\pycharm64.exe"
            os.startfile(codePath)


        elif "open vs code" in query:

            codePath = "G:\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif"bye sara" in query:
            exit()
