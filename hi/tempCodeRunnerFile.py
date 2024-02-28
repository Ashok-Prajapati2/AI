import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pygame
from gtts import gTTS
import vlc
from pytube import YouTube
from twilio.rest import Client
import subprocess
from youtubesearchpython import Hashtag ,VideosSearch



class PersonalAssistant:
    def __init__(self):
        self.engine = pyttsx3.init("espeak")
        self.voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", self.voices[5].id)
        self.pygame_initialized = False

    def initialize_pygame(self):
        if not self.pygame_initialized:
            pygame.mixer.init()
            self.pygame_initialized = True

    def speak(self, text):
        self.initialize_pygame()
        tts = gTTS(text=text, lang="en", slow=False)
        tts.save("output.mp3")

        pygame.mixer.music.load("output.mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    
    # def __init__(self):
    #     self.engine = pyttsx3.init("")
    #     self.voices = self.engine.getProperty("voices")
    #     self.engine.setProperty("voice", self.voices[16].id)
    #     self.pygame_initialized = False

    # def initialize_pygame(self):
    #     if not self.pygame_initialized:
    #         pygame.mixer.init()
    #         self.pygame_initialized = True

    # def speak(self, audio):
    #     self.engine.setProperty("rate", 120)
    #     self.initialize_pygame()
    #     self.engine.say(audio)
    #     self.engine.runAndWait()

    def wish_me(self):
        hour = int(datetime.datetime.now().hour)
        if 0 <= hour < 12:
            self.speak("Good Morning!")
        elif 12 <= hour < 18:
            self.speak("Good Afternoon!")
        else:
            self.speak("Good Evening!")

        self.speak("I am, Happy. Please tell me, how may I help you")

    def take_command(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Adjusting for ambient noise... Please wait.")
            r.adjust_for_ambient_noise(source, duration=1)
            r.energy_threshold = 30000
            print("Listening...")
            try:
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
                print("Recognizing...")
                query = r.recognize_google(audio, language="en-in")
                print(f"User said: {query}\n")
                return query.lower()
            except sr.UnknownValueError:
                print("Sorry, I couldn't understand what you said.")
            except sr.RequestError as e:
                print(
                    f"Could not request results from Google Speech Recognition service; {e}"
                )
            except sr.WaitTimeoutError:
                print("Listening timed out while waiting for the phrase to start.")
            except KeyboardInterrupt:
                print("Recognition interrupted by user.")

        return ""

    def search_wikipedia(self, query):
        self.speak("Searching ...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        self.speak("According to my data")
        print(results)
        self.speak(results)

    def open_web_browser(self, url):
        webbrowser.open(url)
        
    def run_system(self, query):
        command = [query]
        subprocess.call(command , shell=True)
    def play_video(self, query):
        # text_search = query.replace(" ", "")
        # custom_search = Hashtag(text_search, limit=1)
        custom_search = VideosSearch(query, limit=1)
        results = custom_search.result()

        if results["result"]:
            url = results["result"][0]["link"]
            youtube = YouTube(url)
            video_stream = youtube.streams.get_highest_resolution()
            
            webbrowser.open(video_stream.url)
            # media = vlc.MediaPlayer(video_stream.url)
            # media.play()
        else:
            print("No results found.")

    def call_ashok(self):
        account_sid = "AC84abf39b57408c683f2cd00a708cd0b0"
        auth_token = "2c60267de08e85a6e72abea2ad4e7faf"
        client = Client(account_sid, auth_token)

        call = client.calls.create(
            twiml='<Response><Say voice="male">Hello I am , Ashok . Enjoy! music </Say><Play>http://demo.twilio.com/docs/classic.mp3</Play></Response>',
            to="+919376034855",
            from_="+14307585585",
        )
        self.speak("Calling Ashok, wait!")

    def execute_command(self, query):

        if "tell me " in query:
            self.search_wikipedia(query)

        elif "close firefox" in query:
            os.system("pkill firefox")

        elif "close vs code" in query:
            os.system("pkill code")

        elif "close file manager" in query:
            os.system("pkill dolphin")
            
        elif "stop video" in query:
            os.system("pkill firefox")

        # - ------------------------------``

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "google search" in query:
            search_query = query.replace("google search", "").strip()
            search_url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open(search_url)

        elif "are you listening" in query:
            self.speak(f"yes, i am listening")
            

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            self.speak(f"Sir, the time is {strTime}")

        elif "open vs code" in query:
            os.system("code")
            self.speak("vs code is open")
            

        elif "open firefox" in query:
            os.system("firefox")
            self.speak("Firefox is open")

        elif "open file manager" in query:
            os.system("dolphin")
            self.speak("file manager is open")



        elif "shut down" in query:
            os.system("poweroff")
            # os.system("shutdown now")

        elif "who are you" in query:
            self.speak("I am  personal assistant . and my owner is Ashok ")

        elif "speak" in query:
            query = query.replace("speak", "").strip()
            self.speak(query)

        elif "play" in query:
            query = query.replace("play","").strip()
            self.play_video(query)

        elif ("call ashok") in query:
            self.call_ashok()
            
        elif "run system" in query:
            query = query.replace("run system", "").strip()
            self.run_system(query)
    def run(self):
        self.wish_me()
        is_true = True
        while is_true:
            query = self.take_command()
            if "you shut up" in query:
                self.speak("sorry")
                is_true = False
            elif query:
                self.execute_command(query)


if __name__ == "__main__":
    assistant = PersonalAssistant()
    assistant.run()
