#Same output as Button Widget.py without using bind() method
#Using command method instead of bind() method


from tkinter import *
class MyButton:
    #Constructor
    def __init__(self, root):
        #Create a frame as child to root window
        self.f = Frame(root, height=200, width=300)
        #Let the frame will not shrink
        self.f.propagate(0)
        
        #Attach the frame to root window
        self.f.pack()
        
        #Create a push button as child to frame and bind it to buttonClick method
        self.b = Button(self.f, text = 'My Button', width=15, height=2, bg='yellow', fg='blue', activebackground='green', activeforeground='red', command=self.buttonClick)
        
        #Attach button to frame
        self.b.pack()
        
    #Method to be called when the button is clicked
    def buttonClick(self):
        print('You have clicked me')
            
#Create root window
root = Tk()

#Create an object to MyButton class
mb = MyButton(root)

#The root window handles the mouse click event