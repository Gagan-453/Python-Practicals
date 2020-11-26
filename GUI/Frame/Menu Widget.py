# MENU WIDGET
# Menu represents a group of items or options for the user to select from.

from tkinter import *

class MyMenu:
    def __init__(self, root):
        # Create a menubar
        self.menubar = Menu(root)
        
        # attach the menubar to the root window
        root.config(menu=self.menubar)
        
        # create file menu
        # 'tearoff' can be 0 or 1
        self.filemenu = Menu(root, tearoff=0)
        
        # create menu items in the file menu
        # Add options and bind it to donothing() method
        self.filemenu.add_command(label="New", command=self.donothing)
        self.filemenu.add_command(label="Open", command=self.donothing)
        self.filemenu.add_command(label="Save", command=self.donothing)
        
        # add a horizontal line as separator
        # This creates a separator after the 3 options "New", "Open", "Save"
        self.filemenu.add_separator()
        
        # create another menu item below the separator
        self.filemenu.add_command(label='Exit', command=root.destroy)
        
        # add the file menu with a name "file" to the menubar
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        
        # create edit menu
        self.editmenu = Menu(root, tearoff=0)
        
        # create menu items in edit menu
        self.editmenu.add_command(label="Cut", command=self.donothing)
        self.editmenu.add_command(label="Copy", command=self.donothing)
        self.editmenu.add_command(label="Paste", command=self.donothing)
        
        # add the edit menu with a name 'Edit' to the menubar
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)
        
    def donothing(self):
        pass
    
# create root window
root = Tk()

# title for the root window
root.title("A Menu Example...")

# Create object to MyMenu class
obj = MyMenu(root)

# define the size of the root window
root.geometry('600x500')

# handle any events
root.mainloop()