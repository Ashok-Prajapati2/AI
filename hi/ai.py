import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import pygame
from gtts import gTTS
import requests
from twilio.rest import Client
from youtubesearchpython import *
import vlc 
from pytube import YouTube
        

def Play(play):
       
        # customSearch = CustomSearch('movie', VideoSortOrder.uploadDate, limit = 1)
        # customSearch = CustomSearch('', VideoSortOrder.viewCount, limit=1)
        # query = "Mahabali Maharudra"
        query = play
        textSearch = query.replace(" ", "")

        customSearch = Hashtag(textSearch, limit = 1)

        results = customSearch.result()

        if results['result']:
        
        
            url = results['result'][0]['link']

            youtube = YouTube(f"{url}")
            video_stream = youtube.streams.get_highest_resolution()
            media = vlc.MediaPlayer(video_stream.url)
            media.play()
            
           
            

            # while True:
            #      pass
             
             
        else:
            print('No results found.')



  




def speak(text):
    tts = gTTS(text=text, lang='en',slow=False)
    tts.save("output.mp3")

    pygame.mixer.init()

    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
        


# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# print(voices[1].id)
# engine.setProperty('voice', voices[0].id)


# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am , Happy . Please tell me , how may I help you")       
    

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        r.adjust_for_ambient_noise(source, duration=1)
        r.energy_threshold = 30000 
        print("Listening...")
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            return query
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for the phrase to start.")
        except KeyboardInterrupt:
            print("Recognition interrupted by user.")
    
    return ''




if __name__ == "__main__":
    wishMe()
    istrue = True
    while istrue:
        
        query = takeCommand().lower()

        if 'tell me ' in query:
            speak('Searching ...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to my data")
            print(results)
            speak(results)
        
        #  close progrem 
          
        elif 'close firefox' in query:
            os.system('pkill firefox')
            
        elif 'close vs code' in query:
            os.system('pkill code')
            
        elif 'close file manager' in query:
            os.system('pkill dolphin')
            
        # -------------------------------
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'google search' in query:
             search_query = query.replace('google search', '').strip()
             search_url = f"https://www.google.com/search?q={search_query}"
             webbrowser.open(search_url)
   
            
        elif 'are you listening' in query:
           speak(f"yes, i am listening")
            
        elif 'open google' in query:
            webbrowser.open("google.com") 


        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open vs code' in query:
             os.system("code")
             speak("vs code is open")
             
        elif 'open firefox' in query:
             os.system("firefox")
             speak("Firefox is open")
        
        elif 'open file manager' in query:
            os.system("dolphin")
            speak("file manager is open")
       
          
        elif 'you shut up' in query:
            speak("sorry")
            istrue = False
            
        elif 'shut down' in query:
            os.system('init 0')
            # os.system("shutdown now")
            
        elif 'who are you' in query:
            speak("I am  personal assistant . and my owner is Ashok ")
            
        elif 'speak' in query:
            query = query.replace('speak', '').strip()
            speak(query)
            
        elif 'play' in query:
            query = query.replace('play', '').strip()
            Play(query)
            
        elif('call ashok') in query:
            account_sid = "AC84abf39b57408c683f2cd00a708cd0b0"
            auth_token = "2c60267de08e85a6e72abea2ad4e7faf"
            client = Client(account_sid, auth_token)


            call = client.calls.create(
                twiml='<Response><Say voice="male">Hello I am , Ashok . Enjoy! music </Say><Play>http://demo.twilio.com/docs/classic.mp3</Play></Response>',
                to="+919376034855",
                from_="+14307585585"
                )
            speak("Calling ashok, wait !")
