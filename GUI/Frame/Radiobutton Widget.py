# RADIOBUTTON WIDGET
# A Radio Button is similar to Check button but it is useful to select only one option from a group of available options

from tkinter import *

class Myradio:
    # constructor
    def __init__(self, root):
        self.f = Frame(root, height=350, width=500)
        
        #Let the frame will not shrink
        self.f.propagate(0)
        
        #Attach the frame to the root window
        self.f.pack()
        
        #Create IntVar class variable
        self.var = IntVar()
        
        # create radio buttons and bind them to display method
        # 'value' option represents a value that is set to the IntVar object when the radiobutton is clicked (Here 1 is set to the Intvar object)
        self.r1 = Radiobutton(self.f, bg='yellow', fg='green', font=('Georgia', 20, 'underline'), text='Male', variable=self.var, value=1, command=self.display)
        
        self.r2 = Radiobutton(self.f, text='Female', variable=self.var, value=2, command=self.display)
        
        #Attach radio buttons to the frame
        self.r1.place(x=50, y=100)
        self.r2.place(x=200, y=100)
        
    def display(self):
        #retrieve the control variable value
        x = self.var.get()
        
        #String is initially empty
        str = ' '
        
        #Catch user choice
        if x == 1:
            str+='You selected: Male'
        if x == 2:
            str+='You selected: Female'
            
        #Display the user selection as a label
        lbl = Label(text=str, fg='blue').place(x=50, y=150, width=200, height=20)
        
# Create root window
root = Tk()

#Create an object to Myradio class
mr = Myradio(root)

#The root window handles the mouse click event
root.mainloop()