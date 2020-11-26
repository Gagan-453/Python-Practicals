# Program to create TCP/IP client program that receives messages from the server
import socket

# take the server name and port number
host = '192.168.29.1'
port = 6000

# create a client side socket using TCP/IP protocol
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect it to server and port number
s.connect((host, port)) # connect socket to the server and port number using connect method

# receive message string from server, at a time 1024 bytes
msg = s.recv(1024) # we can use recv() method to receive messages from the server, 1024 indicates the buffer size (1024 bytes of data can be received from the server)

# repeat as long as message strings are not empty
while msg:
    print('Received: '+msg.decode())
    msg = s.recv(1024)
    
# disconnect the client
s.close() #  disconnect the client using close() method
