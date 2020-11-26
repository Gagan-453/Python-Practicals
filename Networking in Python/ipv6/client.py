import sys
from socket import socket, AF_INET6, SOCK_DGRAM

SERVER_IP   = 'fe80::d0e6:8801:ae56:2bff'
PORT_NUMBER = 5000
SIZE = 1024
print ("Test client sending packets to IP {0}, via port {1}\n".format(SERVER_IP, PORT_NUMBER))

mySocket = socket( AF_INET6, SOCK_DGRAM )
myMessage = "Hello!"
myMessage1 = ""
i = 0
while i < 10:
    mySocket.sendto(myMessage.encode('utf-8'),(SERVER_IP,PORT_NUMBER))
    i = i + 1

mySocket.sendto(myMessage1.encode('utf-8'),(SERVER_IP,PORT_NUMBER))

sys.exit()
