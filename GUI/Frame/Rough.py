from tkinter import *
import Text_Widget
root = Tk()
f = Frame(root, width=500, height=400)
f.pack()

def open_window():
    root.destroy()
    Text_Widget.MyText()
    
b = Button(f, text='Open', width=15, command=open_window)
b.pack()
