#Button Widget

from tkinter import *

#Method to be called when the button is clicked
def ButtonClick(self):
    print('You have clicked me')
    
# Create root window
root = Tk()

#Create Frame as child to root window
f = Frame(root, height=200, width=300)

#Let the frame will not shrink
f.propagate(0)

#Attach the frame to the root window
f.pack()

file = PhotoImage(file='new.png')
#Create a push button as child to Frame
b = Button(f, image=file, text='Mybutton', width=75, height=80, bg='yellow', fg='blue', activebackground='green', activeforeground='red')
# 'b' is the object of the Button class, 'f' represents the frame for which the button is created as a child, means the button is shown in the frame
# 'width' represents the width in pixels, 'height' represents the height of the button in pixels
# 'bg' represents the foreground colour and 'fg' represents the background colour of the button, 'activebackground' represents the background colour when the button is clicked, 'activeforeground' represents the foreground colour when the button is clicked

#Attach button to the frame
b.pack()

#Bind the left mouse button with the method to be called
b.bind("<Button-1>", ButtonClick)

#The root window handles the mouse click event
root.mainloop()

