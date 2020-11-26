# PLACE LAYOUT MANAGER
# Place layout manager uses place() method to arrange widgets
#The place() method takes x and y coordinates of the widget along with width and height of the window where the widget has to be displayed

from tkinter import *

class MyButton:
    #Constructor
    def __init__(self, root):
        #Create a frame as child to root window
        self.f = Frame(root, height=400, width=500)
        
        #Let the frame will not shrink
        self.f.propagate(0)
        
        #Attach the frame to root window
        self.f.pack()
        
    #Create 3 push buttons and bind them to buttonClick method and pass a number
        self.b1 = Button(self.f, text='Red', command= lambda: self.buttonClick(1))
        self.b2 = Button(self.f, text='Green', width=15, height=2, command= lambda: self.buttonClick(2))
        self.b3 = Button(self.f, text='Blue', width=15, height=2, command= lambda: self.buttonClick(3))
        
        #Attach buttons to the frame
        self.b1.place(x=20, y=30, width=100, height=50) #Display at (20, 30), coordinates in the window 100 px width and 50 px height
        self.b2.place(x = 20, y = 100, width=100, height=50) # Display at (20, 100)
        self.b3.place(x=200, y=100, width=100, height=50) #Display at (200, 100)
    
    #Method to be called when the Button is clicked
    def buttonClick(self, num):
        #Set background color of the frame depending on the button clicked
        if num==1:
            self.f["bg"] = 'red'
            print('You have chosen Red')
        if num==2:
            self.f["bg"] = 'green'
            print('You have chosen Green')
        if num==3:
            self.f["bg"] = 'blue'
            print('You have chosen Blue')
            
#Create root window
root = Tk()
#Create an object to MyButton class
mb = MyButton(root)

#The root window handles the mouse click event
root.mainloop()