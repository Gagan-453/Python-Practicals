#We can display an image with the help of create_image function
from tkinter import *
#Create a root window
root = Tk()

#Create Canvas as a child to root window
c = Canvas(root, bg='white', height=700, width=1200)

#Copy images into files
file1 = PhotoImage(file="Peacock.png")
file2 = PhotoImage(file='Screenshot (40).png')

#The image is displayed relative to the point represented by the coordinates (500, 200)
#The image can be placed in any direction from this point indicated by anchor (8 Directions - NW, N, NE, E, SE, S, SW, W, CENTER)
#Image to be displayed is file1 and 'activeimage' is the image to be shown when the cursor is placed on the image
id = c.create_image(500,200, anchor=NE, image=file1, activeimage=file2)

#Create some text
id = c.create_text(800, 500, text='This is a thrilling photo', font=('Helvetica', 30, 'bold underline'), fill='blue')

#Add canvas to the root
c.pack()

#Wait for any events
root.mainloop()