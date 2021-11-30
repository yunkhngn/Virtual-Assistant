#please make a playing music from youtube function

from tkinter import *
import pytube
import pytube.extract

screen = Tk()
screen.title("Music Player")
screen.geometry("400x100")
screen.resizable(0,0)

def searchForLink():
    link = entry.get()
    yt = pytube.YouTube(link)
    videos = yt.streams.all()
    for i in videos:
        print(i)

def play_music():
    link = inputMusicName.get()
    yt = pytube.YouTube(link)
    videos = yt.streams.all()
    for i in videos:
        print(i)
    videos.get_audio_only()
    videos.download("./")

nowPlaying = Label(screen, text="Now Playing: ")
nowPlaying.pack()

inputMusicName = Entry(screen)
inputMusicName.pack()

playButton = Button(screen, text="Play", width=10, command=play_music)
playButton.pack()

screen.mainloop()