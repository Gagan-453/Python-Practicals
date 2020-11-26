# A program to create a UDP server and send messages to the client
import socket
import time

# take the server name and port number
host = 'localhost'
port = 7227

# create a socket at server side to use UDP protocol
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # SOCK_DGRAM represents UDP protocol

# let server wait for 5 seconds
time.sleep(5)

# Send messages to the client after encoding into binary string
# Since UDP is connection less protocol, server does not know where the  data should be sent, we have to specify the client address in the sendto() function
s.sendto(b"Hello client, how are you?", (host, port))
msg = 'Bye!'
s.sendto(msg.encode(), (host, port))

# disconnect the server
s.close()