from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class operation:
    def __init__(self, root):
        self.f = Frame(root, height=700, width=1000, bg='light green')
        self.f.propagate(0)
        self.f.pack()
        self.n = StringVar()
        
        self.width=0
        self.height=100
        
        self.lbl1 = Label(self.f, text='Get your mathematical operations done...', bg='blue', font=('Arial', 14, 'italic'))
        self.lbl1.pack()
        
        self.cb = ttk.Combobox(self.f, width=27, textvariable=self.n)
        self.cb.place(x=300, y=150)
        
        self.cb['values'] = ('Addition', 'Subtraction', 'Multiplication', 'Division', 'LCM', 'HCF', 'Factors of a number', 'Factorial of number', 'Exponents', 'Roots', 'Average', 'Rounding off', 'Absolute Value', 'Area', 'Perimeter', 'Greater or less or equal')
        self.cb.current('0')
        
        self.lbl2 = Label(self.f, text="Select an operation...", bg='light green', font=('Arial', 10))
        self.lbl2.place(x=170, y=150)
        
        self.b1 = Button(self.f, text='Continue', bg='yellow', command=self.perform)
        self.b1.place(x=350, y=200)
        
    def perform(self):
        if self.cb.get() == 'Addition':
            self.f1 = Frame(self.f, height=400, width=1000, bg='orange')
            self.f1.propagate(0)
            self.f1.place(x=0, y=250)
            
            self.lbl3 = Label(self.f1, text='Enter numbers to add', font=('Helvetica', 13, 'italic'))
            self.lbl3.pack()
            
            
            self.b2 = Button(self.f1, text='Add Value', bg='Blue', fg='Pink', font=('Arial', 12, 'bold'), command=self.add_value)
            self.b2.pack(side=BOTTOM)
            
            self.b3 = Button(self.f1, text='Calculate', bg='Blue', fg='Pink', font=('Arial', 12, 'bold'), command=self.show)
            self.b3.pack(side=BOTTOM)
            
    def add_value(self):
        self.e2 = Entry(self.f1, width=5, fg='black', bg='light yellow', font=('Arial', 15))
        self.e2.place(x=self.width, y=self.height)
        
        self.width+=100
        if self.width==1000:
            self.width=0
            self.height+=100
            if self.height == 400:
                messagebox.showinfo("Sorry", "Can't take more values!")
                
    def show(self):
        self.lst = [ ]
        if self.cb.get() == 'Addition':
            if self.e2.get()!='':
                self.val = self.e2.get()
                self.lst.append(int(self.val))
                print(self.lst)
            self.txt_sum = 'Sum of all values is ' + str(sum(self.lst))
            self.show_sum = Label(self.f, text=self.txt_sum, bg='light pink', fg='Dark Blue', font=('Brook Man old style', 12))
            self.show_sum.place(x=700, y=200)
            
root = Tk()
obj = operation(root)
root.mainloop()