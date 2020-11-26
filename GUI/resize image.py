from tkinter import *
import tkinter
import tkinter.messagebox
from PIL import Image
from PIL import ImageTk

master = Tk()
 
def callback():
    print("click!")

width = 50
height = 50
img = Image.open("C:/Users/ADINARAYANAREDDY/Python/Bird.png")
img = img.resize((width,height), Image.ANTIALIAS)
photoImg =  ImageTk.PhotoImage(img)
b = Button(master,image=photoImg, command=callback, width=50)
b.pack()
mainloop()