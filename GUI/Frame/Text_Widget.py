# TEXT WIDGET
# Text widget is similar to Label and Message widgets but Text widget has several options and can display multiple lines of text using different fonts and colours

from tkinter import *

class MyText:
    #Constructor
    def __init__(self):
        root = Tk()
        root.minsize(300, 200)
        #Create a text widget with 200 chars widthe and 10 lines height
# 'wrap' specifies where to cut the line, wrap=CHAR (represents that any line that is too long will be broken at any character, wrap=WORD (breaks the line in the widget after the last word fits in the line, wrap=NONE (will not wrap the lines)
        self.t = Text(root, width=20, height=10, font=('Verdana', 14, 'bold'), fg='blue', bg='yellow', wrap=WORD, undo=5)
        
        #Insert some text into the text widget
        #this can be done using insert() method
# 'END' represents that the text is added at the end of the previous text, we can use 'CURRENT' to represent that the text is added at the current cursor position
        self.t.insert(END, 'Text Widget\nThis text is inserted into the text widget.\n This is the second line\n This is the third line\n')
        
        #Attach text to the root
        self.t.pack(side=LEFT)
        
        #Show image in the text widget
#We can display an image like a photo using image_create() method
        self.img = PhotoImage(file=r'C:\Users\ADINARAYANAREDDY\Python\GUI\Frame\Bird.png')
        self.t.image_create(END, image=self.img)
        
        #create a tag with the name 'Gagan'
#It is possible to mark some of the text as a tag and provide different colours and font for that text
        #For this we should specify the tag using tag_add() method
        
        #Here the tag name is 'Gagan', '1.0' represents that the tag should start from 1st line 0th charcter, '1.11' represents that the tag should continue upto 1st line 11th character
        self.t.tag_add('Gagan', '1.0', '1.11')
        
        #Apply colours, font to tag 'Gagan'
        # this can be done using tag_config() method
        self.t.tag_config('Gagan', background='red', foreground='white', font=('Lucida console', 20, 'bold italic'))
        
        #Create a Scrollbar widget to move the text vertically
        self.s = Scrollbar(root, orient=VERTICAL, command=self.t.yview)
        
        #attach the scroll bar to the Text widget
        self.t.configure(yscrollcommand=self.s.set)
        
        #attach the scroll bar to the root window
        self.s.pack(side=RIGHT, fill=Y)
        
#Create root window


#Create an object to MyText class
if __name__ == '__main__':
    mt = MyText()

#The root window handles the mouse click event
