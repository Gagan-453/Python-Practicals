#Colours and fonts

#Program to know all available font families
from tkinter import *
from tkinter import font #all fonts are available in tkinter.font module inside tkinter module
#Create root window
root = Tk()

#Get all supported font families
list_fonts = list(font.families())
print(list_fonts) #Display them

#Colours in tkinter can be displayed directly by mentioning their names as: blue, lightblue, red, black, white, cyan, etc...
#Colours can also be represented in hexadecimals number format like #000000 represents black, #ff0000 represents red, #000fff000 represents puregreen

#ALL STANDARD COLOURS TABLE IS SAVED IN G DRIVE!