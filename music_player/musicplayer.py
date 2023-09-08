import tkinter as tk
from tkinter import *
from playsound import playsound
from pygame import mixer
import time
from PIL import Image, ImageTk

mixer.init()


r = tk.Tk()
r.title("Music player")
var = StringVar()


e = tk.Entry(r, width=25)
name = e.get()

path = "music_player/images/Faasle.jpeg"
image = Image.open(path)
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(r, image=photo)
image_label.pack()


def image(e):
    img = ImageTk.PhotoImage(Image.open(f"music_player/images/{e.get()}.jpeg"))
    image_label.configure(image=img)
    image_label.image = img


# Label(r, text=f"{e.get()}")


def play():
    mixer.music.load(f"music_player\music\{e.get().title()}.mp3")
    mixer.music.play()


Play = tk.Button(r, text="Play", width=25, command=lambda: [play(), image(e)])
Pause = tk.Button(r, text="Pause", width=25, command=mixer.music.stop)


e.pack()
Play.pack()
Pause.pack()
# image_label.pack()

r.mainloop()
