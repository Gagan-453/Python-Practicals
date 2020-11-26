# Creating Polygon using Canvas
from tkinter import * 
#Create a root window
root = Tk()

# var c is Canvas class object
# root is the name of the parent window, bg is background colour, height is the height of the window and width is the breadth of window, cursor represents the shape of the cursor in the canvas
c = Canvas(root, bg = 'green', height = 700, width = 1200, cursor = 'umbrella')

# create_polygon() function can used to create polygon

# (10, 10, 200, 200, 300, 200) are pixels and the polygon is created using the points (10, 10), (200, 200), (300, 200) and then the last point is connected to the 1st point
# Width specifies the width of the line, fill specifies the colour of the line, outline specifies the colour of the border, activefill represents the colour to be filled when the mouse is placed on the oval
# smooth can become 1 or 0. If 0, it indicates a polygon with sharp edges and 1 indicates a polygon with smooth edges
id = c.create_polygon(10, 10, 200, 200, 300, 200, width = 3, fill='green', outline = 'red', smooth = 1, activefill = 'green')

#Once the Canvas is created, it should be added to the root window. Then only it will be visible. This is done using pack() method
c.pack()
#Wait for any events
root.mainloop()

