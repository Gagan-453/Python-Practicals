from tkinter import *
root = Tk()
f = Frame(root, width=500, height=500, bg='yellow')
f.propagate(0)
f.pack()

def show():
    l = Label(f, text='Hi')
    l.pack(side=BOTTOM)
    
b = Button(f, text='Ntg', width=15, relief=RAISED, bg='light green', command=show, state=DISABLED)
b.pack()

def check():
    a = e.get()
    if a.isspace() == True:
        b.config(state=DISABLED)
    
    elif a == '':
        b.config(state=DISABLED)
        
    else:
        b.config(state=NORMAL)
        
    if e.selection_present():
        t = e.selection_range.get()
        print(t)
    return True
        

e = Entry(f, width=15, validate='key', validatecommand=check)
e.pack()
root.mainloop()

