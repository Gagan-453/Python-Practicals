# Creating a basic chat  client program in Python
import socket
host = '127.0.0.1'
port = 9999

# create client side socket
s = socket.socket()
s.connect((host, port))

# enter data at client
str = input("Enter data: ")

while str != 'exit':
    # send data from client to server
    s.send(str.encode())
    
    # receive the response data from server
    data = s.recv(1024)
    data = data.decode()
    print("From server: " +data)
    
    # enter data
    str = input("Enter data: ")
    
# close connection
s.close()