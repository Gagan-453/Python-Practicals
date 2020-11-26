# ME

import socket
host = 'localhost'
port = 2727

s = socket.socket()
s.bind((host, port))

s.listen(1)

c, addr = s.accept()
print('Praveen connected...')

c.send(b"Hi Praveen\n")
c.send(b"This is Gagan\n")
c.send(b"This is Live chat...\n")
c.send(b"Type a message and click on Enter\n")
c.send(b"If you want to exit from chat type 'exit'\n")

while True:
    data = c.recv(1024)
    
    if not data:
        break
    
    print("From Praveen: "+str(data.decode()))
    data1 = input("Type a message: ")
    c.send(data1.encode())

s.close()