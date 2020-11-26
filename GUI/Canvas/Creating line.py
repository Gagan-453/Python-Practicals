# Creating lines using Canvas
from tkinter import * #Import module
#Create a root window
root = Tk()

# var c is Canvas class object
# root is the name of the parent window, bg is background colour, height is the height of the window and width is the breadth of window, cursor represents the shape of the cursor in the canvas
c = Canvas(root, bg = 'green', height = 700, width = 1200, cursor = 'pencil')

# create_line() function can used to create lines

# 50, 50, 200, 50, 200, 150 are pixels where this creates a line with connecting the points (50, 50), (200, 50) and (200,150)
# (50, 50) represents 50 pixels from the top left corner and 50 pixels to down from that point, this will be the a point of line
# (200, 50) represents 200 pixels from top left corner and 50 pixels down from that point (200 pixels from top left corner), this is 2nd point
# (200, 150) represents 200 pixels from top left corner and 150 pixels down from that point (200 pixels from top left corner), this is 3rd point
# These 3 points are joined
# Width specifies the width of the line, fill specifies the colour of the line
id = c.create_line(50, 50, 200, 50, 200, 150, width = 4, fill='white')

#Once the Canvas is created, it should be added to the root window. Then only it will be visible. This is done using pack() method
c.pack()
#Wait for any events
root.mainloop()