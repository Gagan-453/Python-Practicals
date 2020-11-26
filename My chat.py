from tkinter import *
import socket
from threading import *

print('Waiting for clients...')

class MyChat:
    def __init__(self, root):
        self.f = Frame(root, height=700, width=1000, bg='yellow')
        self.f.propagate(0)
        self.f.pack()
        
        self.start = Label(self.f, text="Welcome to Gagan's chat...", bg='light green', font=('Times New Roman', 25, 'italic'))
        self.start.place(x=300, y=10)
        
        self.f1 = Frame(self.f, height=500, width=300, bg='light green')
        self.f2 = Frame(self.f, height=500, width=300, bg='dark green')
        self.f1.propagate(0)
        self.f1.pack(side=RIGHT)
        self.f2.propagate(0)
        self.f2.pack(side=RIGHT)
        
        self.host = 'localhost'
        self.port = 2727
        
        self.s = socket.socket()
        self.s.bind((self.host, self.port))
        
        self.s.listen(1)
        
        self.c, self.addr = self.s.accept()
        
        self.name = self.c.recv(1024)
        self.lbl1 = Label(self.f, text= self.name.decode()+ ' connected...', bg='brown')
        self.lbl1.place(x=800, y=600, width=200, height=50)
        self.c.send(b'Gagan')
        
        self.t1 = Text(self.f, width=20, height=10, font=('Calibri', 14), bg='light blue', fg='green')
        self.t1.insert(END, '')
        self.t1.place(x=50, y=400, width=200, height=200)
        self.lbl2 = Label(self.f, text='Type a message here: ')
        self.lbl2.place(x=90, y=380)
        
        self.b1 = Button(self.f, text='SEND--->', font=('Algerian', 20, 'bold'), width=7, height=1, bg='red', fg='pink', activebackground='dark red', command=self.send_msg)
        self.b1.place(x=85, y=600)
        
        self.head1 = Label(self.f, text='You', bg='orange', width=30, height=2)
        self.head2 = Label(self.f, text=self.name.decode(), bg='orange', width=15, height=2)
        self.head1.place(x=740, y=60)
        self.head2.place(x=500, y=60)
             
        
    def send_msg(self):
        
            self.msg = self.t1.get(0.0, END)
            
            self.c.send(self.msg.encode())
            self.sent_label = Label(self.f, text='Message successfully sent', width=20, height=1, bg='black', fg='white')
            self.sent_label.place(x=350, y=600)
            root.after(7000, self.sent_label.destroy)
            self.lm = Label(self.f1, text=(str(self.msg)), bg='yellow', font=('Arial', 15))
            self.lm.pack(side=TOP, fill=X, padx=50, pady=1)
            self.t1.delete(0.0, END)
            
    def recv_msg(self):
        while True:
            self.mr = self.c.recv(1024)
            if not self.mr:
                break
                
            self.rm = Label(self.f2, text=self.mr.decode(), bg='yellow', font=('Arial', 15))
            self.rm.pack(side=TOP, fill=X, padx=0, pady=1)
        
    def send_file(self):
        pass  
    
root = Tk()
root.title("Gagan's Chat")
chat = MyChat(root)

thr = Thread(target=chat.recv_msg)
thr.start()

root.mainloop()