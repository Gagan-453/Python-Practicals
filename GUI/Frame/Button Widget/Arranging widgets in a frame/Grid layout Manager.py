# GRID LAYOUT MANAGER
# Grid layout manager uses grid() method to arrange widgets in a two-dimensional table that contains rows and columns

# A python program to create three push buttons and change the background of the frame according to the button clicked by the user

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
        self.b1 = Button(self.f, text='Red', width=15, height=2, command= lambda: self.buttonClick(1))
        self.b2 = Button(self.f, text='Green', width=15, height=2, command= lambda: self.buttonClick(2))
        self.b3 = Button(self.f, text='Blue', width=15, height=2, command= lambda: self.buttonClick(3))
        
        #Attach buttons to the frame
# The position of a widget is defined by a row and column number, the size of the table is determined by the grid layout manager depending on the widgets size
        self.b1.grid(row=0, column=0, padx=100, pady=15) #Display in 0th row and 0th column with sapces around
        self.b2.grid(row=1, column=2, padx=10, pady=15) #Display in 1st row and 2nd column with spaces around
        self.b3.grid(row=2, column=0) #Display in 2nd row and 0th column with no spaces around
    
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
