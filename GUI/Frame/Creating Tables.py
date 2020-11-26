# Creating Tables
# Table is useful to display data in form of rows and columns

from tkinter import *
class MyTable:
    def __init__(self, root):
        for i in range(total_rows):
            for j in range(total_cols):
                self.e = Entry(root, width=20, fg='green', bg='yellow', font=('Arial', 16, 'bold'))
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i] [j])
                
# take the data
lst = [(453, 'Gagan Adithya', 'Tirupati'), (445, 'Advith', 'Hyderabad'), (477, 'Ranjeet', 'Bihar')]

# find no.of rows and columns in list
total_rows = len(lst)
total_cols = len(lst[0])

# create root window
root = Tk()
mt = MyTable(root)
root.mainloop()