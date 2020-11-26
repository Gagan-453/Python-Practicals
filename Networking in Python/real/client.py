from socket import *
host = '2409:4070:401d:613:c0d7:a851:e282:8812'
port = 9999

s = socket(AF_INET6, SOCK_STREAM)
s.connect((host, port))
s.send(b'HI Hello')
s.close()

# 2409:4070:401d:613:c0d7:a851:e282:8812