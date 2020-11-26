from tkinter import *

#Create root window
root = Tk()

#Create Canvas as a child to root window, background colour is dark blue
c = Canvas(root, bg='#091e42', height=700, width=1200)

#Create the house
c.create_polygon(600, 250, 700, 200, 800, 250, 800, 400, 600, 400, width=2, fill='yellow', outline='red')
c.create_line(600, 250, 800, 250, width=2, fill='red')
c.create_rectangle(650, 275, 750, 375, fill='red')

#Create 3 bushes at left side of the house
x1, y1 = 0, 350
x2, y2 = 200, 450
for i in range(3):
    c.create_arc(x1, y1, x2, y2, start=0, extent=180, fill='green')
    x1+=200
    x2+=200
    
#Create 2 bushes at right side of the house
c.create_arc(800, 350, 1000, 450, start=0, extent=180, fill='green')
c.create_arc(1000, 350, 1200, 450, start=0, extent=180, fill='green')

#Display moon image
file = PhotoImage(file='moon.png')
c.create_image(0, 0, anchor = NW, image=file)

#Display some text below the image
c.create_text(600, 600, text='My Happy Home!', font= ('Helvetica', 35, 'bold italic'), fill='magenta', activefill='orange')

#Add canvas to the root
c.pack()

#Wait for any events
root.mainloop()