from tkinter import *
from time import strftime
import pyttsx3
import requests
import speech_recognition as sr

COLOR = "#0f0f0f"
TEXTCOLOR = "white"
AGENTNAME = "Siri Phake"
USERNAME = "Khoa"

#please make a function to get username and dump it into a txt file and make it as USERNAME
def getUserName():
    global USERNAME

    getname = Tk()
    getname.title("Get your name")
    getname.geometry("300x100")
    getname.config(bg=COLOR)

    nameLabel = Label(getname, text="Please enter your name:", bg=COLOR, fg=TEXTCOLOR)
    nameLabel.grid(row=0, column=0, padx=10, pady=10)

    nameEntry = Entry(getname, width=30)
    nameEntry.grid(row=1, column=0, padx=10, pady=10)

    submit = Button(getname, text="Submit", command=lambda: getname.destroy())
    submit.grid(row=2, column=0, padx=10, pady=10)

    USERNAME = nameEntry.get()  
    file = open("name.txt", "w")
    file.write(USERNAME)
    file.close()
    getname.lift()
    getname.attributes('-topmost', True)
def checkUserName():
    global USERNAME
    with open("name.txt", "r") as f:
        USERNAME = f.read()
    if USERNAME == "":
        getUserName()

screen = Tk()
screen.title(AGENTNAME + " - Virtual Agent")
screen.geometry("350x667")
screen.resizable(0, 0)
screen.config(bg=COLOR)
screen.lift()
screen.attributes('-topmost', True)

Avatar = PhotoImage(file="agent.png")
UserAvatar = PhotoImage(file="user.png")

def getLocation():
    url = "http://ipinfo.io/"
    response = requests.get(url)
    data = response.json()
    city = data["city"]
    return city

def getWeather():
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + getLocation() + "&appid=b1b35bba8b434a28a0be2a3e1071ae5b"
    response = requests.get(url)
    data = response.json()
    weather = data["weather"][0]["main"]
    return('Currently '+ weather + " and " + str(round(data["main"]["temp"]-273,1)) + '°C in ' + getLocation())

def agentThinkingToResponse():
    userNeed = textEntry.get().lower()
    if userNeed == "":
        agentChatBox.config(text="Please enter a valid request.")
        return "Please enter a valid request."
    elif "time" in userNeed:
        agentChatBox.config(text="The time is " + strftime('%H:%M'))
        return "The time is " + strftime('%H:%M')
    elif "date" in userNeed:
        agentChatBox.config(text="The date is " + strftime('%A, %d %B, %Y'))
        return "The date is " + strftime('%A, %d %B, %Y')
    elif "weather" in userNeed:
        agentChatBox.config(text=getWeather())
        return getWeather()
    elif "location" in userNeed:
        agentChatBox.config(text=getLocation())
        return getLocation()
    elif "how are you" in userNeed:
        agentChatBox.config(text="I am fine, thanks for asking.")
        return "I am fine, thanks for asking."
    elif "who are" or 'name' in userNeed:
        agentChatBox.config(text="I am a virtual agent named " + AGENTNAME + " coded by Khoa Nguyen.")
        return "I am a virtual agent named " + AGENTNAME + " coded by Khoa Nguyen."    
    else:
        agentChatBox.config(text="I don't know what you mean.")
        return "I don't know what you mean."

def textToSpeech():   
    agentsay = agentThinkingToResponse()
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 145)   
    engine.say(agentsay)
    engine.runAndWait()
    engine.stop()
    

def time(): 
    string = strftime('%H:%M') 
    timeClock.config(text = string) 
    timeClock.after(1000, time)
def currentDate():
    #get the name of the day
    global string
    string = strftime('%A, %d %B, %Y')
    date.config(text = string)
    date.after(1000, currentDate)

def welcome():
    welcomeFrame = Frame(chatbox, width=500, height=50, bg=COLOR)
    welcomeFrame.pack(side=TOP)

    welcome = Label(welcomeFrame, text="Hello, my name is " + AGENTNAME + ".\nHow can I help you?", font=("segoe ui", 10), wraplength=500, justify=LEFT, bg=COLOR, fg=TEXTCOLOR)
    welcome.grid(row=0, column=1, padx=(10,0), pady=10)
    agentAvatarLabel = Label(welcomeFrame, image=Avatar, bg=COLOR)
    agentAvatarLabel.grid(row=0, column=0, padx=0, pady=(10,0))

    agentSpeakTime = Label(welcomeFrame, text=strftime('%H:%M'), font=("segoe ui light", 10), bg=COLOR, fg=TEXTCOLOR)
    agentSpeakTime.grid(row=0, column=2, padx=50, pady=10)

    agentName = Label(welcomeFrame, text=AGENTNAME, font=("segoe ui",7), bg=COLOR, fg=TEXTCOLOR)
    agentName.grid(row=1, column=0)

    # checkUserName()
def userWrite():
    global textEntry
    userFrame = Frame(chatbox, width=500, height=50, bg=COLOR)
    userFrame.pack(side=TOP, fill=X)

    userAvatar = Label(userFrame, image=UserAvatar, bg=COLOR)
    userAvatar.grid(row=0, column=0, padx=0, pady=(10,0))

    userTime = Label(userFrame, text=strftime('%H:%M') , font=("segoe ui light", 10), bg=COLOR, fg=TEXTCOLOR)
    userTime.grid(row=0, column=2, padx=(50,0), pady=10)

    userNameChat = Label(userFrame, text=USERNAME, font=("segoe ui",7), bg=COLOR, fg=TEXTCOLOR)
    userNameChat.grid(row=1, column=0)

    userChatBox = Label(userFrame, text=textEntry.get() + ".", font=("segoe ui", 10), wraplength=160, justify=LEFT, bg=COLOR, fg=TEXTCOLOR)
    userChatBox.grid(row=0, column=1, padx=(10,0), pady=10,sticky=E)
    
def agentResponse():
    global agentFrame, agentAvatar, agentTime, agentNameChat, agentChatBox
    agentFrame = Frame(chatbox, width=500, height=50, bg=COLOR)
    agentFrame.pack(side=TOP, fill=X)

    agentAvatar = Label(agentFrame, image=Avatar, bg=COLOR)
    agentAvatar.grid(row=0, column=0, padx=0, pady=(10,0))

    agentTime = Label(agentFrame, text=strftime('%H:%M') , font=("segoe ui light", 10), bg=COLOR, fg=TEXTCOLOR)
    agentTime.grid(row=0, column=2, padx=(50,0), pady=10)

    agentNameChat = Label(agentFrame, text=AGENTNAME, font=("segoe ui",7), bg=COLOR, fg=TEXTCOLOR)
    agentNameChat.grid(row=1, column=0)

    agentChatBox = Label(agentFrame, text="" + AGENTNAME + ".", font=("segoe ui", 10), wraplength=160, justify=LEFT, bg=COLOR, fg=TEXTCOLOR)
    agentChatBox.grid(row=0, column=1, padx=(10,0), pady=10)
    agentThinkingToResponse()
    # textToSpeech()

def agentChat():
    userWrite()
    agentResponse()

speech = sr.Recognizer()

def userSay():
    with sr.Microphone() as source:
        print("Say something!")
    audio = speech.listen(source)
    try:
        text = speech.recognize_google(audio)
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def agentVoice():
    userNeed = userSay()
    userWrite()
    agentResponse()
    textToSpeech()
    
string = 0

displayTime = Frame(screen, width=375, height=50, bg='#0a0a0a')
displayTime.pack(side=TOP, fill=X)

timeClock = Label(displayTime, text="10:00", font=("segoe ui light", 10), bg='#0a0a0a', fg=TEXTCOLOR)
timeClock.pack(side=LEFT)

date = Label(displayTime, text="", font=("segoe ui light", 10), bg='#0a0a0a', fg=TEXTCOLOR)
date.pack(side=RIGHT)

title = Label(screen, text=AGENTNAME + " - Virtual Agent", font=("segoe ui bold", 15), bg=COLOR, fg=TEXTCOLOR)
title.pack(fill=X)

chatbox = Frame(screen, width=500, height=400, bg=COLOR)
chatbox.pack(fill=X, padx=20)

textMessage = Frame(screen, bg=COLOR)
textMessage.pack(fill=X, side=BOTTOM, padx=20, pady=(10,30))

textEntry = Entry(textMessage, width=28, bg='white', fg='black', relief=FLAT, font=("segoe ui", 11))
textEntry.grid(row=0, column=0, columnspan=2)

enterButton = Button(textMessage, text="Enter", bg=COLOR, fg=TEXTCOLOR, relief=FLAT, bd = 1, command=agentChat)
enterButton.grid(row=0, column=2, padx=(4,0))

textVoice = Button(textMessage, text="Voice", bg=COLOR, fg=TEXTCOLOR, relief=FLAT, bd = 1, command=agentVoice)
textVoice.grid(row=0, column=3, padx=(4,0))

welcome()
time()
currentDate()
screen.mainloop()
