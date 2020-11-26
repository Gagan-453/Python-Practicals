# SPINBOX WIDGET
# Spinbox widget allows the user to select values from a given set of values
# Spinbox appears as a long rectangle attached with arrowheads pointing towards up and down, the user can click on arrowheads to see the next value or previous value


from tkinter import *

class MySpinbox:
    # constructor
    def __init__(self, root):
        self.f = Frame(root, height=350, width=500)
        
        #Let the frame will not shrink
        self.f.propagate(0)
        
        #Attach the frame to the root window
        self.f.pack()
        
        # These are control variables for spinboxes
        self.val1 = IntVar()
        self.val2 = StringVar()
        
        # Create Spinbox with numbers 5 to 15
        # option 'from_' represents the starting of the range, 'to' represents the ending of range, 'textvariable' shows the control vaariable.i.e val1 that is created as an object of IntVar class
        self.s1 = Spinbox(self.f, from_= 5, to=15, textvariable=self.val1, width=15, fg='black', bg='LightGreen', font=('Arial', 14, 'bold'))
        
        # Create Spinbox with a tuple of strings
        # The fixed strings that are displayed in the spin box are mentioned in 'values' option as a tuple, the 'textvariable' option indicates the control variable value 'val2' that is created as an object of StringVar class
        self.s2 = Spinbox(self.f, values=('Hyderabad', 'Tirupati', 'Bangalore', 'Delhi'), textvariable=self.val2, width=15, fg='blue', bg='yellow', font=('Arial', 14, 'bold italic'))
        
        # Create a button and bind it with display() method
        self.b = Button(self.f, text='Get values from spin boxes', command=self.display)
        
        # Place the spin boxes and button widgets in the frame
        self.s1.place(x=50, y=50)
        self.s2.place(x=50, y=100)
        self.b.place(x=50, y=150)
        
    def display(self):
        #retrieve the values from spin box widgets
        a = self.val1.get()
        s = self.val2.get()
        
        #Display the values using labels
        lbl = Label(text='Selected value is: '+str(a)).place(x=50, y=200)
        lbl2 = Label(text='Selected city is: '+s).place(x=50, y=220)
        
# Create root window
root = Tk()

#Create an object to MySpinbox class
mr = MySpinbox(root)

#The root window handles the mouse click event
root.mainloop()