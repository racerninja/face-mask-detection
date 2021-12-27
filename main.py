from tkinter import *
from pytube import YouTube
import time

def download_video():
    url =YouTube(str(link.get()))
    g = variable.get()

    if g == "144p":
        video = url.streams.first()
    elif g == "Audio Only(HD)":
        video = url.streams.get_audio_only()
    else:
        video = url.streams.get_highest_resolution()
    video.download()

    label = Label(root, text = "       DOWNLOADED         ", font = "arial 15 bold", bg = "pink")
    label.place(x= 130, y= 250)

    def next_label():
        label["text"] = "Ready for next Download"

    label.after(1000, next_label)

root = Tk()
root.geometry("500x500")
root.resizable(0,0)
root.title("GreenSauce- YouTube Video Downloader")
root.configure(background = "pink")

#------------------------------------------------------------------------------------
Label(root,text = "YouTube Video Downloader", font ="arial 20 bold", bg = "pink").place(x= 70,y= 60)
link = StringVar()

Label(root, text = "Enter the yt link here: ", font = "arial 15 bold", bg = "pink").place(x= 150 , y = 120)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 200)

#------------------------------------------------------------------------------------

options = ["144p","720p","Audio Only(HD)"]
variable = StringVar(root)
variable.set(options[0])
OptionMenu(root, variable, *options).place(x=400,y=250)

Button(root,text = "DOWNLOAD", font = "arial 15 bold" ,bg = "black",fg = "white", padx = 2, command = download_video).place(x=180 ,y = 350)

root.mainloop()
