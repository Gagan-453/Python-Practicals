from tkinter import *
root = Tk()

def onFrameConfigure(event):
        c.configure(scrollregion=c.bbox("all"))

c = Canvas(root, width=500, height=500, bg='orange')
c.pack(side="left", fill="both", expand=True)


f = Frame(c, width=500, height=500, bg='yellow')
f.propagate(0)
f.pack(side=LEFT, fill=BOTH, expand=TRUE)

f1 = Frame(root, width=500, height=500, bg='green')
f1.pack(side=RIGHT, fill=BOTH, expand=TRUE)

vsb = Scrollbar(c, orient="vertical", command=c.yview)
c.configure(yscrollcommand=vsb.set)
vsb.pack(side="right", fill="y")
f.bind("<Configure>", onFrameConfigure)

for i in range(50):
    b = Button(f, text='Just testing..', relief=FLAT)
    b.pack()

root.mainloop()