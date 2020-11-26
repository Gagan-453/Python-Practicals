# MESSAGE WIDGET
# messages are generally used to display multiple lines of text whereas label is used to display a single line of text

#Program to display a message in the frame
from tkinter import *

class MyMessage:
    #Constructor
    def __init__(self, root):
        #Create a frame as child to root window
        self.f = Frame(root, height=350, width=500, bg='yellow')
        
        #Let the frame not shrink
        self.f.propagate(0)
        
        #Attach the frame to the root window
        self.f.pack()
        
        #Create a Message widget with some text
        self.msg = Message(self.f, text='This is a message that has more than one line of text.', width=200, font=('Roman', 20, 'bold italic'), fg='dark goldenrod')
        
        #Attach message to the frame
        self.msg.pack(side=LEFT)
        
#Create a root window
root = Tk()

#Create an object to MyMessage class
mb = MyMessage(root)

#the root window handles the mouse click event
root.mainloop()