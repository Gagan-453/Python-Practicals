from tkinter import *
from PIL import Image
from PIL import ImageTk

root = Tk()
width = 50
height = 50
img = Image.open("C:/Users/ADINARAYANAREDDY/Python/me.jpeg")
img = img.resize((width,height), Image.ANTIALIAS)
photoImg =  ImageTk.PhotoImage(img)

Button(root, text='    Hi I am Gagan', compound='left', bg='black', fg='white', image=photoImg, font=('Arial', 12, 'bold')).pack()


root.mainloop()