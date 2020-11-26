# Creating text using Canvas
from tkinter import * 
#Create a root window
root = Tk()

# var c is Canvas class object
# root is the name of the parent window, bg is background colour, height is the height of the window and width is the breadth of window, cursor represents the shape of the cursor in the canvas
c = Canvas(root, bg = 'green', height = 700, width = 1200, cursor = 'hand2')

# create_text() function can used to create text in Canvas

fnt = ('Times', 40, 'bold') # 'Times' font, size = 40(indicates the font size in points) , Option = bold
fnt = ('Arial', -40, 'bold italic underline') # 'Arial' font, size = 40(indicates the font size in pixels) , Options = bold, italic, underline (These are optional)

# (500, 100) represents the location in Pixels of where the text should be written, text represents the text to be written, font represents, fill represents the colour and activefill represents the colour which should be changed when the cursor is on the text
id = c.create_text(500, 100, text = "My Canvas", font = fnt, fill='yellow',  activefill = 'orange')

#Once the Canvas is created, it should be added to the root window. Then only it will be visible. This is done using pack() method
c.pack()
#Wait for any events
root.mainloop()