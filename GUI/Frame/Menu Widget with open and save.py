# A GUI program to display a menu and also to open a file and save it through the file dialog box
from tkinter import *
from tkinter import filedialog # This is a sub module of tkinter and can be used to save and open files

class MyMenu:
    def __init__(self, root):
        # create a menubar
        self.menubar = Menu(root)
        
        # attach the menubar to the root window
        root.config(menu=self.menubar)
        
        # create file menu
        self.filemenu = Menu(root, tearoff=0)
        
        # create menu items in the file menu
        # Add options and bind it to donothing() method
        self.filemenu.add_command(label="New", command=self.donothing)
        
        self.filemenu.add_command(label="Open", command=self.open_file) 
        self.filemenu.add_command(label="Save", command=self.save_file)
        
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
    
    # method for opening a file and display its contents in a text box
    def open_file(self):
        # open a file dialog box and accept the file name
# filedialog module gives a method askopenfile() to open files, filetypes represents the files to be read, when the user selects the file from the dialog box, it is available in filename variable
        self.filename = filedialog.askopenfilename(parent=root, title='Select a file', filetypes=(("Python files", "*.py"), ("All files", ".")))
        
        # if cancel button is not clicked in the dialog box
        if self.filename != None:
            # open the file in read mode
            f = open(self.filename, 'r')
            # read the contents of the file
            contents = f.read()
            
            # create a text box and add it to root window
            self.t = Text(root, width=80, height=20, wrap=WORD)
            self.t.pack()
            
            # insert the file contents into the text box
            self.t.insert(1.0, contents)
            
            # close the file
            f.close()
            
    # method to save a file that is already in the text box
    def save_file(self):
        # open a file dialog box and type a file name
        # 'defaultextension' option specifies the extension type when we do not mention any
        self.filename = filedialog.asksaveasfilename(parent=root, defaultextension='.txt')
        # if cancel button is not clicked in the dialog box
        if self.filename != None:
            # open the file in write mode
            f = open(self.filename, 'w')
            
            # get the contents of the text box
            contents = str(self.t.get(1.0, END))
            
            # store the file contents into the file
            f.write(contents)
            
            # close the file
            f.close()
    
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