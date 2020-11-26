# ENTRY WIDGET
# Entry widget is useful to create a rectangular box that can be used to enter or display one line of text

from tkinter import *

class MyEntry:
    # constructor
    def __init__(self, root):
        self.f = Frame(root, height=350, width=500)
        
        #Let the frame will not shrink
        self.f.propagate(0)
        
        #Attach the frame to the root window
        self.f.pack()
        
        # labels
        self.l1 = Label(text='Enter user name: ')
        self.l2 = Label(text='Enter password: ')
        
        # Create Entry widget for user name
        self.e1 = Entry(self.f, width=25, fg='blue', bg='yellow', font=('Arial', 14), highlightbackground='red', highlightcolor='green', highlightthickness=2)
        
        # Create Entry widget for password. The text in the widget is replaced by stars (*)
        self.e2 = Entry(self.f, width=25, fg='blue', bg='yellow', show='*')
        
        #When user presses Enter, bind that event to display method
        self.e2.bind("<Enter>", self.display)
        
        # Place the labels and the entry widgets in the frame
        self.l1.place(x=50, y=100)
        self.e1.place(x=200, y=100)
        self.l2.place(x=50, y=150)
        self.e2.place(x=200, y=150)
        
    def display(self, event):
        #retrieve the values from entry widgets
        str1 = self.e1.get()
        str2 = self.e2.get()
        
        #Display the values using labels
        lbl = Label(text='Your name is: '+str1).place(x=50, y=200)
        lbl2 = Label(text='Your password is: '+str2).place(x=50, y=220)
        
# Create root window
root = Tk()

#Create an object to MyEntry class
mr = MyEntry(root)

#The root window handles the mouse click event
root.mainloop()