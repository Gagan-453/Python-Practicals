from socket import *
host = ''
port = 5678

s = socket(AF_INET, SOCK_STREAM)
s.bind((host, port))

s.listen(1)

c, addr = s.accept()
print(c.recv(1024))

s.close()

# 2409:4070:401d:613:d0e6:8801:ae56:2bff