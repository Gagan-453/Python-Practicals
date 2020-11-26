# Creating Oval using Canvas
from tkinter import * 
#Create a root window
root = Tk()

# var c is Canvas class object
# root is the name of the parent window, bg is background colour, height is the height of the window and width is the breadth of window, cursor represents the shape of the cursor in the canvas
c = Canvas(root, bg = 'green', height = 700, width = 1200, cursor = 'star')

# create_oval() function can used to create oval or circle

# (100, 100, 400, 300) are pixels, which creates an oval in the rectangular area defined by the top left coordinates (100, 100) and bottom lower coordinates (400, 300)
# (100, 100) represents 100 pixels from the top left corner and 100 pixels to down from that point, this is where an oval is made
# (400, 300) represents 400 pixels from top left corner and 300 pixels down from that point(400 pixels from top left corner), these are measurements of the oval
# Width specifies the width of the line, fill specifies the colour of the line, outline specifies the colour of the border, activefill represents the colour to be filled when the mouse is placed on the oval
id = c.create_oval(100, 100, 400, 300, width = 5, fill='yellow', outline = 'red', activefill = 'green')

#Once the Canvas is created, it should be added to the root window. Then only it will be visible. This is done using pack() method
c.pack()

root.mainloop()