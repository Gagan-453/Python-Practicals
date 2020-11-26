# A program to create a file client program that sends a file name to the server and receives file contents
import socket

# take server name and port number
host = 'localhost'
port = 9999

# create TCP socket
s = socket.socket()

# connect to server
s.connect((host, port))

# type file name from keyboard
filename = input('Enter filename: ')

# send the file name to the server
s.send(filename.encode())

# receive file content from server
while True:
    content = s.recv(1024)

    f = open('test.mp4', 'ab') # change the mp3 extension if the file has different extension
    f.write(content)
    f.close()
    
    if not content:
        break

print('File downloaded...')
# disconnect the client
s.close()