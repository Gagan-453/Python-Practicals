from socket import *
import sys
PORT_NUMBER = 5000
SIZE = 1024

hostName = ''

mySocket = socket( AF_INET6, SOCK_DGRAM )
mySocket.bind( (hostName, PORT_NUMBER) )

print ("Test server listening on port {0}\n".format(PORT_NUMBER))

while True:
    (data,addr) = mySocket.recvfrom(SIZE)
    print(data)
sys.exit()
