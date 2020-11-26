from tkinter import *
from time import *

root = Tk()
root.title('Flash  Chat')

f = Frame(root, height=700, width=1000, bg='yellow')
f.propagate(0)
f.pack()
lbl1 = Label(f, text='FLASH      CHAT', width=35, height=13, font=('Berlin Sans FB Demi', 40, 'bold'), fg='green', bg='orange')
lbl1.place(x=0, y=0)
root.after(6000, f.destroy)

flash = Label(f, text='⚡', width=0, height=2, font=("Arial", 100, 'bold'), bg='orange', fg='dark blue')
flash.place(x=510, y=250)

c = Canvas(f, bg='orange', width=400, height=275)
img = PhotoImage(file='chat.png')
c_img1 = c.create_image(000, 000, anchor=NW, image=img)
c.place(x=300, y=70)


cover = Label(f, text='', width=8, height=10, bg='orange', fg='orange')
cover.place(x=515, y=350)
f.after(2000, cover.destroy)

messenger = Label(f, text='Messenger', width=10, height=1, bg='orange', fg='dark blue', font=('Brookman old style', 15, 'bold italic'))
messenger.place(x=640, y=440)


class Flash_chat:
    def __init__(self, root):
        self.f1 = Frame(root, height=650, width=1200)
        self.f1.propagate(0)
        self.f1.pack()
        
        self.file = PhotoImage(file='menu.png')
        self.menu_button = Button(self.f1, image=self.file, bg='white', command=self.new_frame)
        self.menu_button.place(x=10, y=10)
        
        self.f1.bind("<Button-1>", self.destroy_frame)
    
    def new_frame(self):
        global f3
        f3 = Frame(self.f1, width=200, height=600, bg='light blue')
        f3.propagate(0)
        f3.place(x=0, y=0)
        
        self.notifications = Button(f3, text='🔔 Notifications',width=28, height=1, fg='green', bg='pink', font=('Arial', 15))
        self.notifications.pack(pady=2)
        
        self.notifications = Button(f3, text='💬 Chat',width=28, height=1, fg='green', bg='pink', font=('Arial', 15))
        self.notifications.pack(pady=2)
        
        self.notifications = Button(f3, text='📢 Public Chat',width=28, height=1, fg='green', bg='pink', font=('Arial', 15))
        self.notifications.pack(pady=2)
        
        self.notifications = Button(f3, text='👥 Friends',width=28, height=1, fg='green', bg='pink', font=('Arial', 15))
        self.notifications.pack(pady=2)
        
        self.notifications = Button(f3, text='Followers',width=28, height=1, fg='green', bg='pink', font=('Arial', 15))
        self.notifications.pack(pady=2)
        
        self.notifications = Button(f3, text='Following',width=28, height=1, fg='green', bg='pink', font=('Arial', 15))
        self.notifications.pack(pady=2)
        
        self.notifications = Button(f3, text='🔎 Search',width=28, height=1, fg='green', bg='pink', font=('Arial', 15))
        self.notifications.pack(pady=2)
        
        self.notifications = Button(f3, text='❓ Help',width=28, height=1, fg='green', bg='pink', font=('Arial', 15))
        self.notifications.pack(pady=2)

    def destroy_frame(self, event):
        try:
            f3.destroy()
        except NameError as f:
            pass

    def donothing(self):
                      pass
                
obj = Flash_chat(root)
root.mainloop() 