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
        self.b1 = Button(self.f, text='Red', width=15, height=2, relief=FLAT, command= lambda: self.buttonClick(1))
        self.b2 = Button(self.f, text='Green', width=15, height=2, relief=GROOVE, command= lambda: self.buttonClick(2))
        self.b3 = Button(self.f, text='Blue', width=15, height=2, command= lambda: self.buttonClick(3))
        
# Command option does not allow to pass arguments to the method, to pass arguments we can use 'lambda' expression
        #Attach buttons to the frame
        self.b1.pack()
        self.b2.pack()
        self.b3.pack()
    
    #Method to be called when the Button is clicked
    def buttonClick(self, num):
        #Set background color of the frame depending on the button clicked
        #"bg" is the option of the frame f, to set background colour of the frame, we can write:
        if num==1:
            self.f["bg"] = 'red'
            print('You have chosen Red')
        if num==2:
            self.f["bg"] = 'green'
            print('You have chosen Green')
        if num==3:
            self.f["bg"] = 'blue'
            print('You have chosen Blue')
# Length and height can also be changed like 'self.f["height"] = 500  #500 is new height
            
#Create root window
root = Tk()
#Create an object to MyButton class
mb = MyButton(root)

#The root window handles the mouse click event
root.mainloop()