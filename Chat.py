import socket
from tkinter import *

root = Tk()
host = 'localhost'
port=2727

s = socket.socket()
s.bind((host, port))

s.listen(1)

c, addr = s.accept()
print(addr)

f = Frame(root, height=700, width=1000)
f.pack()
f.propagate(0)

lbl = Label(f, text=addr)
c.send(b'Gagan')
print(c.recv(1024))

data = input('Enter data: ')
c.send(data.encode())

s.close()


#CLIENT
# s.connect((host, port))
# s.send(b'Gagan')
# 
# str = input("Enter data: ")
# s.send(str.encode())
# s.send(b'Hi')
#     
# while True:
#     print(s.recv(1024).decode())
#     
# s.close()