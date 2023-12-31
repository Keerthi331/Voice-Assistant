#_____________________________________________________J.A.R.V.I.S________________________________________________________#py
import sys
import speech_recognition as sr
import pyttsx3
import pywhatkit as kit
import datetime
import wikipedia
import pyjokes
import webbrowser
import time
import os
import random
from requests import get
import smtplib
import psutil
import instaloader
import pyautogui
import pyaudio
import wave
from bs4 import BeautifulSoup
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from JarvisUi import Ui_JarvisUI
from pywikihow import search_wikihow
import speedtest
from pytube import YouTube

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id) 
class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
    
    def run(self):
        self.Intro()
    
    def take_Command(self):
        try:
            listener = sr.Recognizer()
            with sr.Microphone() as source:

                print('Listening....')
                listener.pause_threshold = 1
                voice = listener.listen(source,timeout=4,phrase_time_limit=7)
                print("Recognizing...")
                command1 = listener.recognize_google(voice,language='en-in')
                command1 = command1.lower()  
                if 'jarvis' in command1: 
                    command1 = command1.replace('jarvis','')
                
            return command1
        except:
            return 'None'
        
    def run_jarvis(self):
        self.wish()
        self.talk('Hello boss I am jarvis your assistant. please tell me how can i help you')
        while True:
            self.command = self.take_Command() #Every time taking command after a task is done
            print(self.command)
            if ('play a song' in self.command) or ('youtube' in self.command) or ("download a song" in self.command) or ("download song" in self.command) : 
                self.yt(self.command) 
            elif ('your age' in self.command) or ('are you single'in self.command) or ('are you there' in self.command) or ('tell me something' in self.command) or ('thank you' in self.command) or ('in your free time' in self.command) or ('i love you' in self.command) or ('can you hear me' in self.command) or ('do you ever get tired' in self.command):
                self.Fun(self.command)
            elif 'time' in self.command : 
                self.Clock_time(self.command)
            elif (('hi' in self.command) and len(self.command)==2) or ((('hai' in self.command) or ('hey' in self.command)) and len(self.command)==3) or (('hello' in self.command) and len(self.command)==5):
                self.comum(self.command)
            elif ('what can you do' in self.command) or ('your name' in self.command) or ('my name' in self.command) or ('college name' in self.command):
                self.Fun(self.command)
            elif ('joke'in self.command) or ('date' in self.command):
                self.Fun(self.command)
            elif ("college time table" in self.command) or ("schedule" in self.command):
                self.shedule() 
            elif ("today" in self.command):
                day = self.Cal_day()
                self.talk("Today is "+day)
      
            elif ("meeting" in self.command):
                self.talk("Ok sir opening meeet")
                webbrowser.open("https://meeting/")
           
            elif ('silence' in self.command) or ('silent' in self.command) or ('keep quiet' in self.command) or ('wait for' in self.command) :
                self.silenceTime(self.command)
           
            elif ('facebook' in self.command)  or ('instagram' in self.command) or ('twitter' in self.command) or ('discord' in self.command) or ('social media' in self.command):
                self.social(self.command)
            elif ('hotstar' in self.command) or ('prime' in self.command) or ('netflix' in self.command):
                self.OTT(self.command)
            elif ('online classes'in self.command):
                self.OnlineClasses(self.command)
            elif ('open teams'in self.command) or ('open stream'in self.command) or ('open sharepoint'in self.command) or('open outlook'in self.command)or('open amrita portal'in self.command)or('open octave'in self.command):
                self.college(self.command)
            elif ('wikipedia' in self.command) or ('what is meant by' in self.command) or ('tell me about' in self.command) or ('who the heck is' in self.command):
                self.B_S(self.command)
            elif ('open google'in self.command) or ('open edge'in self.command) :
                self.brows(self.command)
            elif ('open gmail'in self.command) or('open maps'in self.command) or('open calender'in self.command) or('open documents'in self.command )or('open spredsheet'in self.command) or('open images'in self.command) or('open drive'in self.command) or('open news' in self.command):
                self.Google_Apps(self.command)
            elif ('open github'in self.command):
                self.open_source(self.command)
            elif ('slides'in self.command) or ('canva'in self.command) :
                self.edit(self.command)
            elif ('open calculator'in self.command) or ('open notepad'in self.command) or ('open paint'in self.command) or ('open online classes'in self.command) or ('open discord'in self.command) or ('open ltspice'in self.command) or ('open editor'in self.command) or ('open spotify'in self.command) or ('open steam'in self.command) or ('open media player'in self.command):
                self.OpenApp(self.command)
         
            elif ('flipkart'in self.command) or ('amazon'in self.command) :
                self.shopping(self.command)
            elif ('where i am' in self.command) or ('where we are' in self.command):
                self.locaiton()
            elif ('command prompt'in self.command) :
                self.talk('Opening command prompt')
                os.system('start cmd')
            elif ('instagram profile' in self.command) or("profile on instagram" in self.command):
                self.Instagram_Pro()
            elif ('take screenshot' in self.command)or ('screenshot' in self.command) or("take a screenshot" in self.command):
                self.scshot()
            elif ("read pdf" in self.command) or ("pdf" in self.command):
                self.pdf_reader()
            elif "activate mod" in self.command:
                self.How()
            elif ("volume up" in self.command) or ("increase volume" in self.command):
                pyautogui.press("volumeup")
                self.talk('volume increased')
            elif ("volume down" in self.command) or ("decrease volume" in self.command):
                pyautogui.press("volumedown")
                self.talk('volume decreased')
            elif ("volume mute" in self.command) or ("mute the sound" in self.command) :
                pyautogui.press("volumemute")
                self.talk('volume muted')
            elif ("covid" in self.command) or  ("corona" in self.command):
                self.talk("Boss which state covid 19 status do you want to check")
                s = self.take_Command()
                self.Covid(s)
            elif 'music' in self.command:
                try:
                    music_dir ="C:\music"
                    songs = os.listdir(music_dir)
                    for song in songs:
                        if song.endswith('.mp3'):
                            os.startfile(os.path.join(music_dir, song))
                except:
                    self.talk("Boss an unexpected error occured")
            elif 'ip address' in self.command:
                ip = get('https://api.ipify.org').text
                print(f"your IP address is {ip}")
                self.talk(f"your IP address is {ip}")
            elif ('send a message' in self.command):
                self.whatsapp(self.command)
            elif "temperature" in self.command:
                self.temperature()
            elif "internet speed" in self.command:
                self.InternetSpeed()
            elif ("you can sleep" in self.command) or ("sleep now" in self.command):
                self.talk("Okay boss, I am going to sleep you can call me anytime.")
                break
            elif ("wake up" in self.command) or ("get up" in self.command):
                self.talk("boss, I am not sleeping, I am in online, what can I do for u")
            
            elif ("goodbye" in self.command) or ("get lost" in self.command):
                self.talk("Thanks for using me boss, have a good day")
                sys.exit()
            elif ('system condition' in self.command) or ('condition of the system' in self.command):
                self.talk("checking the system condition")
                self.condition()
            elif ('news' in self.command) or ("the news" in self.command) or ("todays news" in self.command):
                self.talk("Please wait boss, featching the latest news")
                self.news()
            elif ('shutdown the system' in self.command) or ('down the system' in self.command):
                self.talk("Boss shutting down the system in 10 seconds")
                time.sleep(10)
                os.system("shutdown /s /t 5")
            elif 'restart the system' in self.command:
                self.talk("Boss restarting the system in 10 seconds")
                time.sleep(10)
                os.system("shutdown /r /t 5")
            
            elif 'sleep ' in self.command:
                self.talk("Boss the system is going to sleep")
                os.system("rundll32.exe powrprof.dll, SetSuspendState 0,1,0")
            else :
                self.talk("Couldnot recogonize you , Please say again")
    def Intro(self):
        while True:
            self.permission = self.take_Command()
            print(self.permission)
            if ("wake up" in self.permission) or ("get up" in self.permission):
                self.run_jarvis()
            elif ("goodbye" in self.permission) or ("get lost" in self.permission):
                self.talk("Thanks for using me boss, have a good day")
                sys.exit()
    def talk(self,text):
        engine.say(text)
        engine.runAndWait()

    def wish(self):
        hour = int(datetime.datetime.now().hour)
        t = time.strftime("%I:%M %p")
        day = self.Cal_day()
        print(t)
        if (hour>=0) and (hour <=12) and ('AM' in t):
            self.talk(f'Good morning boss, its {day} and the time is {t}')
        elif (hour >= 12) and (hour <= 16) and ('PM' in t):
            self.talk(f"good afternoon boss, its {day} and the time is {t}")
        else:
            self.talk(f"good evening boss, its {day} and the time is {t}")

    def temperature(self):
        IP_Address = get('https://api.ipify.org').text
        url = 'https://get.geojs.io/v1/ip/geo/'+IP_Address+'.json'
        geo_reqeust = get(url)
        geo_data = geo_reqeust.json()
        city = geo_data['city']
        search = f"temperature in {city}"
        url_1 = f"https://www.google.com/search?q={search}"
        r = get(url_1)
        data = BeautifulSoup(r.text,"html.parser")
        temp = data.find("div",class_="BNeawe").text
        self.talk(f"current {search} is {temp}")

   
    def whatsapp(self,command):
        try:
            self.talk("Say the Number to send in whatsApp")
            number = self.take_Command()
            number="+91"+number
            self.talk("Say the message to send")
            message = self.take_Command()
            kit.sendwhatmsg_instantly(number, message,8,True,2)
            self.talk("message has been sent")
        except:
            print("Error occured, please try again")

   def InternetSpeed(self):
        self.talk("Wait a few seconds boss, checking your internet speed")
        st = speedtest.Speedtest()
        dl = st.download()
        dl = dl/(1000000) #converting bytes to megabytes
        up = st.upload()
        up = up/(1000000)
        print(dl,up)
        self.talk(f"Boss, we have {dl} megabytes per second downloading speed and {up} megabytes per second uploading speed")
        
    def How(self):
        self.talk("How to do mode is activated")
        while True:
            self.talk("Please tell me what you want to know")
            how = self.take_Command()
            try:
                if ("exit" in how) or("close" in how):
                    self.talk("Ok sir how to mode is closed")
                    break
                else:
                    max_result=1
                    how_to = search_wikihow(how,max_result)
                    assert len(how_to) == 1
                    how_to[0].print()
                    self.talk(how_to[0].summary)
            except Exception as e:
                self.talk("Sorry sir, I am not able to find this")

    def comum(self,command):
        print(command)
        if ('hi'in command) or('hai'in command) or ('hey'in command) or ('hello' in command) :
            self.talk("Hello boss what can I help for u")
        else :
            self.No_result_found()

    def Fun(self,command):
        print(command)
        if 'your name' in command:
            self.talk("My name is jarvis")
        elif 'my name' in command:
            self.talk("your name is P R")
        elif 'college name' in command:
            self.talk("you are studing in V.S.B. Engineering College, with batchelor in Information technology") 
        elif 'what can you do' in command:
            self.talk("I talk with you until you want to stop, I can say time, open your social media accounts,your open source accounts, open google browser,and I can also open your college websites, I can search for some thing in google and I can tell jokes")
        elif 'your age' in command:
            self.talk("I am very young that u")
        elif 'are you single' in command:
            self.talk('No, I am in a relationship with wifi')
        elif 'joke' in command:
            self.talk(pyjokes.get_joke())
        elif 'are you there' in command:
            self.talk('Yes boss I am here')
        elif 'tell me something' in command:
            self.talk('boss, I don\'t have much to say, you only tell me someting i will give you the company')
        elif 'thank you' in command:
            self.talk('boss, I am here to help you..., your welcome')
            sys.exit()
        elif 'in your free time' in self.command:
            self.talk('boss, I will be listening to all your words')
        elif 'i love you' in command:
            self.talk('I love you too boss')
        elif 'can you hear me' in command:
            self.talk('Yes Boss, I can hear you')
        elif 'do you ever get tired' in command:
            self.talk('It would be impossible to tire of our conversation')
        else :
            self.No_result_found()

    def social(self,command):
        print(command)
        if 'facebook' in command:
            self.talk('opening your facebook')
            webbrowser.open('https://www.facebook.com/')
        elif 'whatsapp' in command:
            self.talk('opening your whatsapp')
            webbrowser.open('https://web.whatsapp.com/')
        elif 'instagram' in command:
            self.talk('opening your instagram')
            webbrowser.open('https://www.instagram.com/')
        elif 'twitter' in command:
            self.talk('opening your twitter')
            webbrowser.open('https://twitter.com/Suj8_116')
        elif 'discord' in command:
            self.talk('opening your discord')
            webbrowser.open('https://discord.com/channels/@me')
        else :
            self.No_result_found()
        
    def Clock_time(self,command):
        print(command)
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        self.talk("Current time is "+time)
    
    def Cal_day(self):
        day = datetime.datetime.today().weekday() + 1
        Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',4: 'Thursday', 5: 'Friday', 6: 'Saturday',7: 'Sunday'}
        if day in Day_dict.keys():
            day_of_the_week = Day_dict[day]
            print(day_of_the_week)
        
        return day_of_the_week
    def shedule(self):
        day = self.Cal_day().lower()
        self.talk("Boss today's shedule is")
        Week = {"monday" : "Boss from 9:00 to 9:50 you have OOAD class, from 10:00 to 11:50 you have MAD class, from 12:00 to 2:00 you have brake, and today you have English lab from 2:00",
                "tuesday" : "Boss from 9:00 to 9:50 you have English class, from 10:00 to 10:50 you have break,from 11:00 to 12:50 you have ELectrical class, from 1:00 to 2:00 you have brake, and today you have MAD lab from 2:00",
                "wednesday" : "Boss today you have a full day of classes from 9:00 to 10:50 you have Data structures class, from 11:00 to 11:50 you have mechanics class, from 12:00 to 12:50 you have cultural class, from 1:00 to 2:00 you have brake, and today you have Data structures lab from 2:00",
                "thrusday" : "Boss today you have a full day of classes from 9:00 to 10:50 you have Big data Analaytics class, from 11:00 to 12:50 you have object oriented design and analysis class, from 1:00 to 2:00 you have brake, and today you have MAD lab from 2:00",
                "friday" : "Boss today you have a full day of classes from 9:00 to 9:50 you have Biology class, from 10:00 to 10:50 you have data structures class, from 11:00 to 12:50 you have Elements of computing class, from 1:00 to 2:00 you have brake, and today you have Electronics lab from 2:00",
                "saturday" : "Boss today you have a full day of classes from 9:00 to 11:50 you have maths lab, from 12:00 to 12:50 you have english class, from 1:00 to 2:00 you have brake, and today you have elements of computing lab from 2:00",
                "sunday":"Boss today is holiday but we can't say anything when they will bomb with any assisgnments"}
        if day in Week.keys():
            self.talk(Week[day])

    def college(self,command):
        print(command)
        if 'teams' in command:
            self.talk('opening your microsoft teams')
            webbrowser.open('https://teams.microsoft.com/')
        elif 'stream' in command:
            self.talk('opening your microsoft stream')
            webbrowser.open('https://web.microsoftstream.com/')
        elif 'outlook' in command:
            self.talk('opening your microsoft school outlook')
            webbrowser.open('https://outlook.office.com/mail/')
        elif 'octave' in command:
            self.talk('opening Octave online')
            webbrowser.open('https://octave-online.net/')
        else :
            self.No_result_found()
    
    def B_S(self,command):
        print(command)
        try:
            if ('wikipedia' in command):
                target1 = command.replace('search for','')
                target1 = target1.replace('in wikipedia','')
            elif('what is meant by' in command):
                target1 = command.replace("what is meant by"," ")
            elif('tell me about' in command):
                target1 = command.replace("tell me about"," ")
            elif('who the heck is' in command):
                target1 = command.replace("who the heck is"," ")
            print("searching....")
            info = wikipedia.summary(target1,5)
            print(info)
            self.talk("according to wikipedia "+info)
        except :
            self.No_result_found()
        
    def brows(self,command):
        print(command)
        if 'google' in command:
            self.talk("Boss, what should I search on google..")
            S = self.take_Command()
            webbrowser.open(f"{S}")
        elif 'edge' in command:
            self.talk('opening your Miscrosoft edge')
            os.startfile('..\\..\\MicrosoftEdge.exe')
        else :
            self.No_result_found()
    def Google_Apps(self,command):
        print(command)
        if 'gmail' in command:
            self.talk('opening your google gmail')
            webbrowser.open('https://mail.google.com/mail/')
        elif 'maps' in command:
            self.talk('opening google maps')
            webbrowser.open('https://www.google.co.in/maps/')
        elif 'news' in command:
            self.talk('opening google news')
            webbrowser.open('https://news.google.com/')
        elif 'calender' in command:
            self.talk('opening google calender')
            webbrowser.open('https://calendar.google.com/calendar/')
        elif 'photos' in command:
            self.talk('opening your google photos')
            webbrowser.open('https://photos.google.com/')
        elif 'documents' in command:
            self.talk('opening your google documents')
            webbrowser.open('https://docs.google.com/document/')
        elif 'spreadsheet' in command:
            self.talk('opening your google spreadsheet')
            webbrowser.open('https://docs.google.com/spreadsheets/')
        else :
            self.No_result_found()
            
    def yt(self,command):
        print(command)
        if 'play' in command:
            self.talk("Boss can you please say the name of the song")
            song = self.take_Command()
            if "play" in song:
                song = song.replace("play","")
            self.talk('playing '+song)
            print(f'playing {song}')
            pywhatkit.playonyt(song)
            print('playing')
        elif "download" in command:
            self.talk("Boss please enter the youtube video link which you want to download")
            link = input("Enter the YOUTUBE video link: ")
            yt=YouTube(link)
            yt.streams.get_highest_resolution().download()
            self.talk(f"Boss downloaded {yt.title} from the link you given into the main folder")
        elif 'youtube' in command:
            self.talk('opening your youtube')
            webbrowser.open('https://www.youtube.com/')
        else :
            self.No_result_found()
        
    def open_source(self,command):
        print(command)
        if 'github' in command:
            self.talk('opening your github')
            webbrowser.open('https://github.com/Ragul331')
        else :
            self.No_result_found()



    def OTT(self,command):
        print(command)
        if 'hotstar' in command:
            self.talk('opening your disney plus hotstar')
            webbrowser.open('https://www.hotstar.com/in')
        elif 'prime' in command:
            self.talk('opening your amazon prime videos')
            webbrowser.open('https://www.primevideo.com/')
        elif 'netflix' in command:
            self.talk('opening Netflix videos')
            webbrowser.open('https://www.netflix.com/')
        else :
            self.No_result_found()

    def OpenApp(self,command):
        print(command)
        if ('calculator'in command) :
            self.talk('Opening calculator')
            os.startfile('C:\\Windows\\System32\\calc.exe')
        elif ('paint'in command) :
            self.talk('Opening msPaint')
            os.startfile('c:\\Windows\\System32\\mspaint.exe')
        elif ('notepad'in command) :
            self.talk('Opening notepad')
            os.startfile('c:\\Windows\\System32\\notepad.exe')
        elif ('discord'in command) :
            self.talk('Opening discord')
            os.startfile('..\\..\\Discord.exe')
        elif ('editor'in command) :
            self.talk('Opening your Visual studio code')
            os.startfile('..\\..\\Code.exe')
        elif ('spotify'in command) :
            self.talk('Opening spotify')
            os.startfile('..\\..\\Spotify.exe')
        elif ('media player'in command) :
            self.talk('Opening VLC media player')
            os.startfile("C:\Program Files\VideoLAN\VLC\vlc.exe")
        else :
            self.No_result_found()
            
    def CloseApp(self,command):
        print(command)
        if ('calculator'in command) :
            self.talk("okay boss, closeing caliculator")
            os.system("taskkill /f /im calc.exe")
        elif ('paint'in command) :
            self.talk("okay boss, closeing mspaint")
            os.system("taskkill /f /im mspaint.exe")
        elif ('notepad'in command) :
            self.talk("okay boss, closeing notepad")
            os.system("taskkill /f /im notepad.exe")
        elif ('discord'in command) :
            self.talk("okay boss, closeing discord")
            os.system("taskkill /f /im Discord.exe")
        elif ('editor'in command) :
            self.talk("okay boss, closeing vs code")
            os.system("taskkill /f /im Code.exe")
        elif ('spotify'in command) :
            self.talk("okay boss, closeing spotify")
            os.system("taskkill /f /im Spotify.exe")
        elif ('lt spice'in command) :
            self.talk("okay boss, closeing lt spice")
            os.system("taskkill /f /im XVIIx64.exe")
        elif ('steam'in command) :
            self.talk("okay boss, closeing steam")
            os.system("taskkill /f /im steam.exe")
        elif ('media player'in command) :
            self.talk("okay boss, closeing media player")
            os.system("taskkill /f /im vlc.exe")
        else :
            self.No_result_found()

    def shopping(self,command):
        print(command)
        if 'flipkart' in command:
            self.talk('Opening flipkart online shopping website')
            webbrowser.open("https://www.flipkart.com/")
        elif 'amazon' in command:
            self.talk('Opening amazon online shopping website')
            webbrowser.open("https://www.amazon.in/")
        else :
            self.No_result_found()

    def silenceTime(self,command):
        print(command)
        x=0
        if ('10' in command) or ('ten' in command):x=600
        elif '1' in command or ('one' in command):x=60
        elif '2' in command or ('two' in command):x=120
        elif '3' in command or ('three' in command):x=180
        elif '4' in command or ('four' in command):x=240
        elif '5' in command or ('five' in command):x=300
        elif '6' in command or ('six' in command):x=360
        elif '7' in command or ('seven' in command):x=420
        elif '8' in command or ('eight' in command):x=480
        elif '9' in command or ('nine' in command):x=540
        self.silence(x)
        
    def silence(self,k):
        t = k
        s = "Ok boss I will be silent for "+str(int(t/60))+" minutes"
        self.talk(s)
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
        self.talk("Boss "+str(k/60)+" minutes over")

    def SendEmail(self,to,content):
        print(content)
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login("pasupathyeaswaran331@gmail.com","fgcxeeqmqpycstrv")
        server.sendmail("pasupathyeaswaran331@gmail.com","pradhiveragul@gmail.com",content)
        server.close()
        
    def locaiton(self):
        self.talk("Wait boss, let me check")
        try:
            IP_Address = get('https://api.ipify.org').text
            print(IP_Address)
            url = 'https://get.geojs.io/v1/ip/geo/'+IP_Address+'.json'
            print(url)
            geo_reqeust = get(url)
            geo_data = geo_reqeust.json()
            city = geo_data['city']
            state = geo_data['region']
            country = geo_data['country']
            tZ = geo_data['timezone']
            longitude = geo_data['longitude']
            latidute = geo_data['latitude']
            org = geo_data['organization_name']
            print(city+" "+state+" "+country+" "+tZ+" "+longitude+" "+latidute+" "+org)
            self.talk(f"Boss i am not sure, but i think we are in {city} city of {state} state of {country} country")
            self.talk(f"and boss, we are in {tZ} timezone the latitude os our location is {latidute}, and the longitude of our location is {longitude}, and we are using {org}\'s network ")
        except Exception as e:
            self.talk("Sorry boss, due to network issue i am not able to find where we are.")
            pass

    def Instagram_Pro(self):
        self.talk("Boss please enter the user name of Instagram: ")
        name = input("Enter username here: ")
        webbrowser.open(f"www.instagram.com/{name}")
        time.sleep(5)
        self.talk("Boss would you like to download the profile picture of this account.")
        cond = self.take_Command()
        if('download' in cond):
            mod = instaloader.Instaloader()
            mod.download_profile(name,profile_pic_only=True)
            self.talk("I am done boss, profile picture is saved in your main folder. ")
        else:
            pass

    def scshot(self):
        self.talk("Boss, please tell me the name for this screenshot file")
        name = self.take_Command()
        self.talk("Please boss hold the screen for few seconds, I am taking screenshot")
        time.sleep(3)
        img = pyautogui.screenshot()
        img.save(f"{name}.png")
        self.talk("I am done boss, the screenshot is saved in main folder.")

    def news(self):
        MAIN_URL_= "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=a16e64b0f48d436f8aa6c2693b57e4ba"
        MAIN_PAGE_ = get(MAIN_URL_).json()
        articles = MAIN_PAGE_["articles"]
        headings=[]
        seq = ['first'] #If you need more than ten you can extend it in the list
        for ar in articles:
            headings.append(ar['title'])
        for i in range(len(seq)):
            print(f"todays  news is: {headings[i]}")
            self.talk(f"todays news is: {headings[i]}")
        self.talk("Boss I am done, I have read most of the latest news")

    def condition(self):
        usage = str(psutil.cpu_percent())
        self.talk("CPU is at"+usage+" percentage")
        battray = psutil.sensors_battery()
        percentage = battray.percent
        self.talk(f"Boss our system have {percentage} percentage Battery")
        if percentage >=75:
            self.talk(f"Boss we could have enough charging to continue our work")
        elif percentage >=40 and percentage <=75:
            self.talk(f"Boss we should connect out system to charging point to charge our battery")
        elif percentage >=15 and percentage <=30:
            self.talk(f"Boss we don't have enough power to work, please connect to charging")
        else:
            self.talk(f"Boss we have very low power, please connect to charging otherwise the system will shutdown very soon")
        
    def No_result_found(self):
        self.talk('Boss I couldn\'t understand, could you please say it again.')        

startExecution = MainThread()
class Main(QMainWindow):
    cpath =""
    
    def __init__(self,path):
        self.cpath = path
        super().__init__()
        self.ui = Ui_JarvisUI(path=current_path)
        self.ui.setupUi(self)
        self.ui.pushButton_4.clicked.connect(self.startTask)
        self.ui.pushButton_3.clicked.connect(self.close)
    
    def startTask(self):
        self.ui.movie = QtGui.QMovie(rf"{self.cpath}\UI\ironman1.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(rf"{self.cpath}\UI\ringJar.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(rf"{self.cpath}\UI\circle.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(rf"{self.cpath}\UI\lines1.gif")
        self.ui.label_7.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(rf"{self.cpath}\UI\ironman3.gif")
        self.ui.label_8.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(rf"{self.cpath}\UI\circle.gif")
        self.ui.label_9.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(rf"{self.cpath}\UI\powersource.gif")
        self.ui.label_12.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(rf"{self.cpath}\UI\powersource.gif")
        self.ui.label_13.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(rf"{self.cpath}\UI\ironman3_flipped.gif")
        self.ui.label_16.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(rf"{self.cpath}\UI\Sujith.gif")
        self.ui.label_17.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()
    
    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)

current_path = os.getcwd()
app = QApplication(sys.argv)
jarvis = Main(path=current_path)
jarvis.show()
exit(app.exec_())
