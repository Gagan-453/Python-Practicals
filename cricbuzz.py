from tkinter import *

root = Tk()

def onFrameConfigure(event):
        '''Reset the scroll region to encompass the inner frame'''
        t.configure(scrollregion=t.bbox("all"))
        
t = Text(root, width=15, height=20, wrap=NONE)
t.propagate(0)
t.pack(side=TOP, fill=X)

f = Frame(t, width=500, height=500, bg='light green')
f.propagate(0)
f.pack()

s = Scrollbar(t, orient=VERTICAL, command=t.yview)
t.configure(yscrollcommand=s.set)
s.pack(side=RIGHT, fill=Y)



for i in range(50):
    b = Button(t, text='test').pack()


root.mainloop()
