# Arranging Widgets in a Frame
# Arranging widgets in a frame is called 'layout management'
# There are three types of layout management: Pack layout manager, Grid layout manager, Place layout manager

# PACK LAYOUT MANAGER
# This manager uses pack() method
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
        self.b1 = Label(self.f, text='Hi', width=len('Hi'), height=1, bg='yellow')
        self.b2 = Label(self.f, text='Hi', width=len('Hi'), height=1, bg='yellow')
        self.b3 = Label(self.f, text='Wurd', width=len('Wurd'), height=1, bg='yellow')
        self.b4 = Label(self.f, text='Hi', width=len('Hi'), height=1, bg='yellow')
        self.b5 = Label(self.f, text='Hi', width=len('Hi'), height=1, bg='yellow')
        self.b6 = Label(self.f, text='Wurd', width=len('Wurd'), height=1, bg='yellow')
        self.b7 = Label(self.f, text='Hi', width=len('Hi'), height=1, bg='yellow')
        self.b8 = Label(self.f, text='Hi', width=len('Hi'), height=1, bg='yellow')
        self.b9 = Label(self.f, text='Wurd', width=len('Wurd'), height=1, bg='yellow')
        self.b10 = Label(self.f, text='Hi', width=len('Hi'), height=1, bg='yellow')
        self.b11 = Label(self.f, text='Hi', width=len('Hi'), height=1, bg='yellow')
        self.b12 = Label(self.f, text='Wurd', width=len('Wurd'), height=1, bg='yellow')
        

        #Attach buttons to the frame
# 'fill' can be 'X' (represents that the widget should occupy the frame horizontally), 'Y' (represents that the widget should occupy the frame vertically), 'BOTH' (represents that the widget should occupy in both the directions), 'NONE' (represents that the widget should be displayed as it is)
# 'padx' represents the number of spaces in pixels to be left at the left and right of the button, 'pady' represents the number of spaces in pixels to be left around (up and down) of the button
#  'side' is used to place the widgets side by side, side can be 'RIGHT', 'LEFT', 'BOTTOM', 'TOP'(Default value is top)
        self.b1.pack(anchor=NW, side=TOP, fill=Y, padx=10, pady=10) #Align towards right, Occupy vertically, space on x-axis 10 px, on y-axis 50 px
        self.b2.pack(anchor=NE, side=TOP,fill=Y, padx=10, pady=10) #Align towards left, Occupy horizontally, space on x-axis = 70 px, space on y-axis = 40 px
        self.b3.pack(anchor=NW, side=TOP, fill=Y) #Align towards bottom, Occupy horizontally, no space outside the widget
        self.b4.pack(anchor=NW, side=TOP, fill=Y, padx=10, pady=10) #Align towards right, Occupy vertically, space on x-axis 10 px, on y-axis 50 px
        self.b5.pack(anchor=NE, side=TOP,fill=Y, padx=10, pady=10) #Align towards left, Occupy horizontally, space on x-axis = 70 px, space on y-axis = 40 px
        self.b6.pack(anchor=NW, side=TOP, fill=Y)
        self.b1.pack(anchor=NW, side=TOP, fill=Y, padx=10, pady=10) #Align towards right, Occupy vertically, space on x-axis 10 px, on y-axis 50 px
        self.b7.pack(anchor=NE, side=TOP,fill=Y, padx=10, pady=10) #Align towards left, Occupy horizontally, space on x-axis = 70 px, space on y-axis = 40 px
        self.b8.pack(anchor=NW, side=TOP, fill=Y)
        self.b1.pack(anchor=NW, side=TOP, fill=Y, padx=10, pady=10) #Align towards right, Occupy vertically, space on x-axis 10 px, on y-axis 50 px
        self.b9.pack(anchor=NE, side=TOP,fill=Y, padx=10, pady=10) #Align towards left, Occupy horizontally, space on x-axis = 70 px, space on y-axis = 40 px
        self.b10.pack(anchor=NW, side=TOP, fill=Y)
        self.b11.pack(anchor=NW, side=TOP, fill=Y, padx=10, pady=10) #Align towards right, Occupy vertically, space on x-axis 10 px, on y-axis 50 px
        self.b12.pack(anchor=NE, side=TOP,fill=Y, padx=10, pady=10) #Align towards left, Occupy horizontally, space on x-axis = 70 px, space on y-axis = 40 px
        
        
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

