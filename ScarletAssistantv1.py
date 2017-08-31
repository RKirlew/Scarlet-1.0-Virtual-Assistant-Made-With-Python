import pyttsx
import webbrowser
import random,os
import speech_recognition as sr
from time import sleep
from selenium import webdriver
import wikipedia
from time import strftime
import time,sys
import datetime

engine=pyttsx.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
r=sr.Recognizer()
booting=['Scarlet Assistant version 1.0 has begun','Scarlet Assistant at your service','Currently starting Scarlet Virtual Assistant']
greetings=["hello","hello there","Hi,I am Scarlet","What is up user","Greetings human","Your wish is my command","Hello user","Hello user,what would you like to do"] #Possible responses to user greetings
userGreet=["hello","hi","start","hey"]
closing=['Shutting down','Closing Scarlet Assistant','Have a nice day']
musical=["What are we watching today","Are gonna to sing some karaoke","Listening to some music today","Good thing I have my dancing module in","My favorite youtuber is Shane Dawson"]
engine.say(random.choice(booting))
engine.runAndWait()
def greeting(data):
        engine.say(random.choice(greetings))
        engine.runAndWait()
        
def search(data):
    driver=webdriver.Chrome()
    driver.get("http://google.com/search?q="+data.split("search",1)[1])
    wordSearch=data.split("search",1)[1]
    sentence=wikipedia.summary(wordSearch, sentences=4)
    engine.say(sentence)
    engine.runAndWait()
   
    
    

def youtube(data):
    driver=webdriver.Chrome()
    driver.get("http://youtube.com")
    engine.say(random.choice(musical))
    engine.runAndWait()
    sleep(2)
def time(data):
    current=strftime("%I:%M")
    engine.say("The current time is "+current)
    engine.runAndWait()

def tDate(date):
    dateT=strftime("%B:%d:%A:%Y")
    engine.say("Today's date is "+dateT)
    engine.runAndWait()
def Gmail(data):
        engine.say("Opening Email Client")
        engine.runAndWait
        webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://gmail.com")
def Amazon(data):
        engine.say("Opening Amazon to purchase "+data.split('buy',1)[1])
        engine.runAndWait
        webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://www.amazon.com/s/field-keywords=",data.split('buy',1)[1]) 
       


while True:        
    with sr.Microphone() as source:
        sleep(1)
        print("Say something then wait.")
        audio=r.listen(source)
        sleep(1)
   
    
    try:
       data = r.recognize_google(audio)
       print("You said:"+data)
       if data=='hello':
            greeting(data)
       if 'search'in data:
           engine.say("Opening web browser to search for "+data.split("search",1)[1])
           engine.runAndWait()
           search(data)
       if 'YouTube' in data:
           youtube(data)
       if 'time' in data:
           time(data)
       if 'date' in data:
            tDate(data)
       if data=='shut down':
           engine.say(random.choice(closing))
           engine.runAndWait()
           sys.exit()
       if 'thank you' in data:
           engine.say("You are welcome")
           engine.runAndWait()
       if data=='scarlet':
               engine.say("Yes, I am here")
       if data=='email':
               Gmail(data)
       if 'buy' in data:
               Amazon(data)
               
    except sr.UnknownValueError:
            sleep (2)
            engine.say("Google Speech Recognition could not understand what you were trying to say")
            engine.runAndWait()
    except sr.RequestError as e:
           print("Could not request results from Google Speech Recoginition Service;{0}".format(e))
    
