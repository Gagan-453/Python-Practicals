# Program to create a UDP client that receives messages
import socket

# take the server name and port number
host = 'localhost'
port = 7227

# create a client side socket that uses UDP protocol
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# connect it to server with host name and port number
s.bind((host, port))

# receive message string from server, at a time 1024 bytes
msg, addr = s.recvfrom(1024)

try:
    # let the socket blocks after 5 seconds if the server disconnects
    s.settimeout(5) # if the server disconnects, the client will wait for another 5 seconds time and disconnects
    
    # repeat as long as message strings are not empty
    # since the client does not know how many messages the server sends, we can use recvfrom() method inside a while loop to receive all the messages
    while msg:
        print('Received: '+msg.decode())
        msg, addr = s.recvfrom(1024)
except socket.timeout: # the settimeout() method may raise an exception
    print('Time is over and hence terminating....')
    
# disconnect the client
s.close()