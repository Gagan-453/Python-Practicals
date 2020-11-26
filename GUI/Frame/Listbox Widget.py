# LISTBOX WIDGET
# It is useful to display a list of items, so that he can select one or more items

from tkinter import *

class ListBox:
    def __init__(self, root):
        self.f = Frame(root, width=700, height=400)

        #Let the frame will not shrink
        self.f.propagate(0)
        
        # Attach the frame to the root window
        self.f.pack()
        
        # Create a label
        self.lbl = Label(self.f, text='Click one or more universities below:', font=('Calibri 14'))
        self.lbl.place(x=50, y=50)
        
        #Create List box with university names
        # 'fg' option represents the colour of the text in the list box, 'bg' represents the back ground colour, 'height' represents the height of the list box, 'selectmode' option represents to select single or multiple items from the box
        # 'selectmode' can be 'BROWSE', 'SINGLE', 'MULTIPLE', 'EXTENDED'
        self.lb = Listbox(self.f, font='Arial 12 bold', fg='green', bg='yellow', height=10, selectmode=MULTIPLE)
        self.lb.place(x=50, y=100)
        
        #Using for loop, insert items into list box
        for i in ["Standford University", "Oxford University", "Texas A&M University", "Cambridge University", "University of California"]:
            self.lb.insert(END, i) #We can insert items into list box using insert() method
            
        # Bind the ListboxSelect event to on_select() method
        self.lb.bind('<<ListboxSelect>>', self.on_select)
        
        # Create a text box to display selected items
        self.t = Text(self.f, width=40, height=6, wrap=WORD)
        self.t.place(x=300, y=100)
        
    def on_select(self, event):
        #Create an empty list
        self.lst = [ ]
        
        #Know the indexes of the selected items
        # We can know the selected items in the list box using curselection() method
        indexes = self.lb.curselection()
        
        # Retrieve the items names depending on indexes
        # Append the items names to the list
        # We can get the selected items from indexes using get(index) method
        for i in indexes:
            self.lst.append(self.lb.get(i))
        
        # Delete the previous content of the text box
        self.t.delete(0.0, END)
        
        # Insert the new contents into the text box
        self.t.insert(0.0, self.lst)
        
# Create root window
root = Tk()

# title for the root window
root.title("List box")

# Create object to ListBox class
obj = ListBox(root)

# Handle any events
root.mainloop()