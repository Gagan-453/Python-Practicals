# CHECKBUTTON WIDGET
# Check button widget or check boxes are useful for the user to select one or more options from available group of options
# The buttons are displayed in the form of square shaped boxes. When a check button is selected, a tick mark is displayed on the button

from tkinter import *

class Mycheck:
    # constructor
    def __init__(self, root):
        # create a frame as child to root window
        self.f = Frame(root, height=400, width=500)
        
        #Let the frame will not shrink
        self.f.propagate(0)
        
        #Attach frame to the root window
        self.f.pack()
        
        # Create IntVar class variables
        # The class 'IntVar' is useful to know the state of the check button, whether it is clicked or not
        # This 'IntVar' returns 0 if the button is not clicked, if the button is clicked it returns 1
        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()
        
        #Create check buttons and bind them to display method
# 'text' represents the text to be displayed after the check button, 'variable' represents an object of IntVar() class, command represents the method to be called when the user clicks the button
        self.c1 = Checkbutton(self.f, bg='yellow', fg='green', font=('Georgia', 20, 'underline'), text='Java', variable=self.var1, command=self.display)
        self.c2 = Checkbutton(self.f, text='Python', variable=self.var2, command=self.display)
        self.c3 = Checkbutton(self.f, text='.NET', variable=self.var3, command=self.display)
        
        #Attach check boxes to the frame
        self.c1.place(x=50, y=100)
        self.c2.place(x=200, y=100)
        self.c3.place(x=350, y=100)
        
    def display(self):
        #retrieve the control variable values
        x = self.var1.get()
        y = self.var2.get()
        z = self.var3.get()
        
        #String is initially empty
        str = ' '
        
        # Catch user choice
        if x == 1:
            str+='Java '
        if y == 1:
            str+='Python '
        if z == 1:
            str+='.NET '
            
        #Display the user selection as a label
        lbl = Label(self.f, text=str, fg='blue').place(x=50, y=150, width=200, height=20)
        
# Create a root window
root = Tk()

#Create an object of Mycheck class
mc = Mycheck(root)

#The root window handles the mouse click event
root.mainloop()