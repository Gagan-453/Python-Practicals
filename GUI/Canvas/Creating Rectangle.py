# Creating Oval using Canvas
from tkinter import * 
#Create a root window
root = Tk()

# var c is Canvas class object
# root is the name of the parent window, bg is background colour, height is the height of the window and width is the breadth of window, cursor represents the shape of the cursor in the canvas
c = Canvas(root, bg = 'green', height = 700, width = 1200, cursor = 'hand1')

# create_rectangle() function can used to create rectangle or a square

# The rectangle will be formed with the top left coordinate at (500, 200) pixels and the lower bottom coordinate at (700, 600)
# First point is created at (500, 200) pixels, the second point is at (700, 600) pixels. These two alternate points are joined like a rectangle
# Width specifies the width of the line, fill specifies the colour of the line, outline specifies the colour of the border, activefill represents the colour to be filled when the mouse is placed on the oval
id = c.create_rectangle(500, 200, 700, 600, width = 3, fill='green', outline = 'red', activefill = 'lightblue')

#Once the Canvas is created, it should be added to the root window. Then only it will be visible. This is done using pack() method
c.pack()
#Wait for any events
root.mainloop()


