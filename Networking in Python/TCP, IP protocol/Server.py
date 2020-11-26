# Server provides services to other computers on network
# Client receives services from the server

# A program to create TCP/IP server program that sends messages to client
import socket

# take the server name and port number
host = '' # if we want to run this in individual computer, then we can take host as 'localhost'
port = 6000

# create a socket at server side using TCP/IP protocol
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET represents IP address version 4, SOCK_STREAM indicates that we are using TCP/IP protocol for communication

# bind the socket with server and port number
s.bind((host, port))

# allow maximum 1 connection to the socket
s.listen(1) # specify the maximum number of connections using listen() method

# wait till a client accepts connection
c, addr = s.accept() # 'c' is the connection object that can be used to send messages to the client, 'addr' is the address of the client that has accepted the connection

# display client address
print("Connection from: ", str(addr))

# send messages to the client after encoding into binary string
c.send(b"Hello Client, how are you")
msg = "Bye!"
c.send(msg.encode())

# disconnect the server
c.close()
