#Graphical User Interface
#We should create space to display Graphical Output. This space is called Root Window

#Program to create a root window
from tkinter import * #Import all components from tkinter
root = Tk() #Create the root window
#Wait and watch for any events that may take place in the root window
root.mainloop()

#Program to create root window with some options
from tkinter import *
root = Tk() #Create top level window or root window 
root.title("Gagan") #Set window Title
root.geometry("400x300") #Set window size
root.wm_iconbitmap('image.ico') #Set window icon
root.mainloop() #display window and wait for any events