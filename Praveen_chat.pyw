from tkinter import *
import socket
from threading import *


class MyChat:
    def __init__(self, root):
        self.f = Frame(root, height=700, width=1000, bg='yellow')
        self.f.propagate(0)
        self.f.pack()
        
        self.conn = self.connect()
        
    def connect(self):    
            self.host = 'localhost'
            self.port = 2727
            
            self.s = socket.socket()
            self.s.connect((self.host, self.port))
            
            self.new = Frame(self.f, height=700, width=1000, bg='light blue')
            self.new.propagate(0)
            self.new.pack()
        
            self.start = Label(self.f, text="Welcome to Gagan's chat...", bg='light green', font=('Times New Roman', 25, 'italic'))
            self.start.place(x=300, y=10)
            
            self.f1 = Frame(self.new, height=500, width=300, bg='light green')
            self.f2 = Frame(self.new, height=500, width=300, bg='dark green')
            self.f1.propagate(0)
            self.f1.pack(side=RIGHT)
            self.f2.propagate(0)
            self.f2.pack(side=RIGHT)
            
            self.name = self.s.recv(1024)
            self.lbl1 = Label(self.new, text= self.name.decode()+ ' connected...', bg='brown')
            self.lbl1.place(x=800, y=600, width=200, height=50)
            
            self.t1 = Text(self.new, width=20, height=10, font=('Calibri', 14), bg='light blue', fg='green')
            self.t1.insert(END, '')
            self.t1.place(x=50, y=400, width=200, height=200)
            self.lbl2 = Label(self.new, text='Type a message here: ')
            self.lbl2.place(x=90, y=380)
            
            self.b1 = Button(self.new, text='SEND--->', font=('Algerian', 20, 'bold'), width=7, height=1, bg='red', fg='pink', activebackground='dark red', command=self.send_msg)
            self.b1.place(x=85, y=600)
             
            self.head1 = Label(self.new, text='You', bg='orange', width=30, height=2)
            self.head2 = Label(self.new, text=self.name.decode(), bg='orange', width=15, height=2)
            self.head1.place(x=740, y=60)
            self.head2.place(x=500, y=60)
    
    def connecting(self):
        self.th = Thread(target=self.connect)
        self.th.start()
             
        
    def send_msg(self):
        
            self.msg = self.t1.get(0.0, END)
            
            self.s.send(self.msg.encode())
            self.sent_label = Label(self.new, text='Message successfully sent', width=20, height=1, bg='black', fg='white')
            self.sent_label.place(x=350, y=600)
            root.after(7000, self.sent_label.destroy)
            self.lm = Label(self.f1, text=(str(self.msg)), bg='yellow', font=('Arial', 15))
            self.lm.pack(side=TOP, fill=X, padx=50, pady=1)
            self.t1.delete(0.0, END)
            
    def recv_msg(self):
        while True:
            self.mr = self.s.recv(1024)
                
            self.rm = Label(self.f2, text=self.mr.decode(), bg='yellow', font=('Arial', 15))
            self.rm.pack(side=TOP, fill=X, padx=0, pady=1)
        
    def send_file(self):
        pass  
    
root = Tk()
root.title("Gagan's Chat")
chat = MyChat(root)

r1 = Thread(target=chat.recv_msg)
r1.start()

root.mainloop()
