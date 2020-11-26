# Container CANVAS
# Container is a space that displays the output to the user
#Canvas container is generally used to draw shapes like lines, curves, arcs, circles

from tkinter import *
root = Tk() #Root window

#Create Canvas as a child to root window
c = Canvas(root, bg = 'green', height = 700, width = 1200, cursor = 'star')

#Create a line in the Canvas
id = c.create_line(50, 50, 200, 50, 200, 150, width = 4, fill='white')

#Create a oval in the Canvas
id = c.create_oval(10, 100, 400, 300, width = 5, fill='yellow', outline = 'red', activefill = 'green')

#Create a polygon in theCanvas
id = c.create_polygon(10, 10, 200, 200, 300, 200, width = 3, fill='white', outline = 'red', smooth = 1, activefill = 'green')

#Create a rectangle in the Canvas
id = c.create_rectangle(500, 200, 700, 600, width = 3, fill='grey', outline = 'red', activefill = 'lightblue')

#Create some text in the Canvas
fnt = ('Arial', -40, 'bold italic underline')
id = c.create_text(500, 100, text = "My Canvas",font = fnt, fill='yellow',  activefill = 'orange')

#add canvas to the root window
c.pack()

#Wait for any events
root.mainloop()
