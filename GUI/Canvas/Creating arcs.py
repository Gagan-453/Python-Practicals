#Creating arcs using Canvas
from tkinter import *
#Create a root window
root = Tk()

# var c is Canvas class object
# root is the name of the parent window, bg is background colour, height is the height of the window and width is the breadth of window, cursor represents the shape of the cursor in the canvas
c = Canvas(root, bg='lightblue', height=700, width=1200, cursor='arrow')

# create_arc() function can used to create arcs, chords, pie slice

# The arc is created in the rectangular space defined by the coordinates (100, 100) and (400, 300)
#The width of the arc will be 3 pixels, This arc will start at an angle 270 degrees and extend for another 180 degrees (refer to that book for more understanding), style can be 'arc' or 'chord' or 'pie slice;
id = c.create_arc(100, 100, 400, 300, width=3, start=270, extent=180, outline='red', style='arc')
id = c.create_arc(500, 100, 800, 300, width=3, start=90, extent=180, outline='red', style='arc')
id = c.create_arc(100, 400, 400, 700, width=3, start=0, extent=180, outline='red', style='arc')
id = c.create_arc(500, 400, 800, 600, width=3, start=180, extent=180, outline='red', style='arc')
id = c.create_arc(900, 400, 1200, 600, width=3, start=90, extent=90, outline='red', style='arc')
c.pack()
root.mainloop()