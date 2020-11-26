#SCROLLBAR WIDGET
# Scrollbar widget is useful to scroll the text in another widget

from tkinter import *

class MyScrollbar:
    #constructor
    def __init__(self, root):
        #Create a text widget with 70 chars width and 15 lines height
        self.t = Text(root, width=70, height=15, wrap=NONE)
        
        #Insert some text into the text widget
        for i in range(50):
            self.t.insert(END, "This is some text ")
            
        #Attach the text widget to root window at the top
        self.t.pack(side=TOP, fill=X)
            
        #Create a horizontal scroll bar and attach it to Text widget
# 'orient' represents whether it is a horizontal scroll bar or vertical scroll bar, the method 'xview' is executed on the object 't'
        self.h = Scrollbar(root, orient=HORIZONTAL, command=self.t.xview)
# After the scroll bar is created it should be attached to the text widget or listbox widget, 'xscrollcommand' calls the set() method of horizontal scrollbar, we can use 'yscrollbar' to call the set() method of vertical scroll bar
        #Attach text widget to the horizontal scroll bar
        self.t.configure(xscrollcommand=self.h.set)
        
        #Attach scroll bar to root window at the bottom
        self.h.pack(side=BOTTOM, fill=X)
        
#Create root window
root = Tk()

#Create an object to MyScrollbar class
ms = MyScrollbar(root)

#The root window handles the mouse click event
root.mainloop()