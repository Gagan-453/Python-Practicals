# FRAME Container
#a frame is similar to canvas that represents a rectangular area where some text or widgets can be displayed

from tkinter import *

#Create root window
root = Tk()

#Give a title for root window
root.title('Gagan\'s frame')

#Create a frame as child to root window
f = Frame(root, height=400, width=500, bg='yellow', cursor='cross')
# f is the object of Frame class
# The options 'height' and 'width' represent the height and width of the frame in pixels
# 'bg' represents the back ground colour to be displayed and 'cursor' indicates the type of the cursor to be displayed in the frame

#Attach the frame to the root window
f.pack()

#Let the root window wait for any events
root.mainloop()


# WIDGETS
#A widget is a GUI component that is displayed on the screen and can perform a task as desired by the user

#To create widget suppose Button widget, we can create an object of the Button class as:
# b = Button(f, text='My Button') # 'f' is frame object to which the button is added, 'My Button is the text that is displayed on the button

#When the user interacts with a widget, he will generate an event, these events should be handled by writing functions or routines, these are called event handlers
# Event handler example:
#def ButtonClick(self):
#    print('You have clicked me') #This message should be displayed when the user clicks on Button 'My Button'

# When user clicks on the button, that clicking event should be linked with the 'event handler' function
# This is done using bind() method
#Example for bind():
# b.bind('<Button-1>, ButtonClick) # 'b' represents the push button and <Button-1> indicates the left mouse button, linked to the function ButtonClick()
