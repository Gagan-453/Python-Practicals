# A program to create basic chat server program in python
import socket

host = '' # means 'localhost'
port = 9999

# create server side socket
s = socket.socket()
s.bind((host, port))

# Maximum number of connections -1
s.listen(1)

# wait till a client connects
c, addr = s.accept()
print('A client connected...')

# server runs continuously
while True:
    # receive data from client
    data = c.recv(1024)
    
    # if client sends empty string, come out
    if not data:
        break
    
    print("From client: "+str(data.decode()))
    
    # Enter response data from server
    data1 = input("Enter response: ")
    
    # send data to client
    c.send(data1.encode())
    
# close connection
c.close()