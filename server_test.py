# Echo server program
import socket
from tkinter import *

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    for i in range(5):
        s.listen(10)
    conn, addr = s.accept()
    s.setblocking(False)
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data: break
            conn.sendall(data)
            

root = Tk()
f = Frame(root, width=500, height=300)
f.pack()
l = Label(f, text='Connected...', width=15, height=2, font=('Arial', 30, 'bold'))
l.pack()


root.mainloop()

