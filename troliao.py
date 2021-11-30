from tkinter import *
from time import strftime, sleep

COLOR = "#0f0f0f"
TEXTCOLOR = "white"
AGENTNAME = "Siri Phake"

screen = Tk()
screen.title(AGENTNAME + " - Virtual Agent")
screen.geometry("350x667")
screen.resizable(0, 0)
screen.config(bg=COLOR)

Avatar = PhotoImage(file="agent.png")

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

def agentResponse():
    global agentFrame, agentAvatar, agentTime, agentNameChat, agentChatBox
    agentFrame = Frame(chatbox, width=500, height=50, bg=COLOR)
    agentFrame.pack(side=TOP)

    agentAvatar = Label(agentFrame, image=Avatar, bg=COLOR)
    agentAvatar.grid(row=0, column=0, padx=0, pady=(10,0))

    agentTime = Label(agentFrame, text=strftime('%H:%M') , font=("segoe ui light", 10), bg=COLOR, fg=TEXTCOLOR)
    agentTime.grid(row=0, column=2, padx=50, pady=10)

    agentNameChat = Label(agentFrame, text=AGENTNAME, font=("segoe ui",7), bg=COLOR, fg=TEXTCOLOR)
    agentNameChat.grid(row=1, column=0)

    agentChatBox = Label(agentFrame, text="Hello, my name is " + AGENTNAME + ".", font=("segoe ui", 10), wraplength=500, justify=LEFT, bg=COLOR, fg=TEXTCOLOR)
    agentChatBox.grid(row=0, column=1, padx=(10,0), pady=10)

def agentChat():
    agentResponse()

def agentVoice():
    agentResponse()

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
