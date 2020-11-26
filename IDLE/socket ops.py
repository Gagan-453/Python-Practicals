Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from socket import *
>>> gethostbyaddr('localhost')
('DESKTOP-708A91K', [], ['::1'])
>>> gethostbyaddr('49.37.152.228')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    gethostbyaddr('49.37.152.228')
socket.herror: [Errno 11004] host not found
>>> gethostbyaddr('192.168.29.145')
('DESKTOP-708A91K.mshome.net', [], ['192.168.29.145'])
>>> gethostbyaddr('2001:0:348b:fb58:282e:1c9a:ceda:30c1')
('DESKTOP-708A91K', [], ['2001:0:348b:fb58:282e:1c9a:ceda:30c1'])
>>> gethostbyaddr
<built-in function gethostbyaddr>
>>> 
>>> gethostbyaddr('fe80::282e:1c9a:ceda:30c1%12')
('DESKTOP-708A91K', [], ['fe80::282e:1c9a:ceda:30c1'])
>>> gethostbyaddr('192.168.29.1')
('reliance.reliance', [], ['192.168.29.1'])
>>> gethostbyaddr('2405:201:c023:687f:d00:9baa:431:1b05')
('DESKTOP-708A91K', [], ['2405:201:c023:687f:d00:9baa:431:1b05'])
>>> gethostbyaddr('192.168.29.145')
('DESKTOP-708A91K.mshome.net', [], ['192.168.29.145'])
>>> gethostbyaddr('fe80::d0e6:8801:ae56:2bff%3')
('DESKTOP-708A91K', [], ['fe80::d0e6:8801:ae56:2bff'])
>>> gethostbyname('DESKTOP-708A91K')
'192.168.29.145'
>>> gethostbyaddr('DESKTOP-708A91K')
('DESKTOP-708A91K', [], ['fe80::d0e6:8801:ae56:2bff'])
>>> gethostbyaddr('''49.37.152.228''')
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    gethostbyaddr('''49.37.152.228''')
socket.herror: [Errno 11004] host not found
>>> 