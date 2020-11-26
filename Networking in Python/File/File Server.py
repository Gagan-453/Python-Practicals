# A program to create a file server that receives a file name from a client and sends the contents of the file
import socket

# enter server name and port number
host = 'localhost'
port = 9999

# create TCP socket
s = socket.socket() # represents TCP/IP socket

# bind the socket to host and port number
s.bind((host, port))

# maximum 1 connection accepted
s.listen(1)

# wait till client accepts a connection
c, addr = s.accept()
print('A client accepted connection...')

# accept file name from client
fname = c.recv(1024)

# convert file name into a normal string
fname = str(fname.decode())
print("File name received from client: "+fname)

try:
    # open the file at server side
    f = open(fname, 'rb')
    
    # read the content of the file
    content = f.read()
    
    # send file content to client
    c.send(content)
    print('File content sent to client...')
    
    # close the file
    f.close()
except FileNotFoundError:
    c.send(b'File does not exist')

# disconnect server
c.close()