# LABEL WIDGET
# A label represents constant text that is displayed in the frame. Label can display one or more line of text that cannot be modified

#Program to display a label upon clicking a push button
from tkinter import *

class MyButtons:
    #Constructor
    def __init__(self, root):
        #Create a frame as child to root window
        self.f = Frame(root, height=350, width=500)
        
        #Let the frame not shrink
        self.f.propagate(0)
        
        #Attach the frame to root window
        self.f.pack()
        
        #Create a push button and bind it to buttonClick method
        self.b1 = Button(self.f, text='Click Me', width=15, height=2, command=self.buttonClick)
        
        #Create another button that closes the root window upon clicking
        # quit command can be used to exit the root window
        self.b2 = Button(self.f, text='Close', width=15, height=2, command=quit)
        
        #Attach buttons to the frame
        self.b1.grid(row=0, column=1)
        self.b2.grid(row=0, column=2)
        
    #The event handler method
    def buttonClick(self):
        #Create a label with some text
        self.lbl = Label(self.f, text="Welcome to Python", width=20, height=2, font=('Courier', -30, 'bold underline'), fg='blue')
        
        #Attach the label to the frame
        self.lbl.grid(row=2, column=0)

#Create root window
root = Tk()

#Create an object to MyButtons class
mb = MyButtons(root)

#The root window handles the mouse click event
root.mainloop()