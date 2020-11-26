# Knowing IP address
# To know IP address of a website on internet, we can use gethostbyname() function available in socket module

import socket

# take the server name
host = 'www.google.co.in'

try:
    # know the IP adress of the website
    addr = socket.gethostbyname(host)
    print('IP Address:', addr)
except socket.gaierror: # if get address info error occurs
    print('The website does not exist...')