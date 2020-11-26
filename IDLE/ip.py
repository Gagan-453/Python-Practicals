Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from socket import *
>>> has_dualstack_ipv6()
True
>>> has_ipv6()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    has_ipv6()
TypeError: 'bool' object is not callable
>>> has_ipv6
True
>>> getdefaulttimeout()
>>> getfqdn()
'DESKTOP-708A91K'
>>> getservbyname()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    getservbyname()
TypeError: getservbyname() takes at least 1 argument (0 given)
>>> getservbyname('DESTOP-708A91K')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    getservbyname('DESTOP-708A91K')
OSError: service/proto not found
>>> gaierror()
gaierror()
>>> AF_INET6()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    AF_INET6()
TypeError: 'AddressFamily' object is not callable
>>> AF_APPLETALK
<AddressFamily.AF_APPLETALK: 16>
>>> AF_APPLETALK()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    AF_APPLETALK()
TypeError: 'AddressFamily' object is not callable
>>> TCP_MAXSEG()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    TCP_MAXSEG()
TypeError: 'int' object is not callable
>>> AF_INET
<AddressFamily.AF_INET: 2>
>>> IPPROTO_ICMPV6
58
>>> IPPROTO_ICMPV6
58
>>> IPPROTO_AH
51
>>> IPPROTO_EGP
8
>>> IPPROTO_GGP
3
>>> IPPROTO_HOPOPTS
0
>>> IPPROTO_IP
0
>>> IPPROTO_IPv4
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    IPPROTO_IPv4
NameError: name 'IPPROTO_IPv4' is not defined
>>> IPPROTO_IPV4
4
>>> IPPROTO_IPV6
41
>>> getattr()
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    getattr()
TypeError: getattr expected at least 2 arguments, got 0
>>> gethostname()
'DESKTOP-708A91K'
>>> getservbyport(1000)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    getservbyport(1000)
OSError: port/proto not found
>>> getservbyport('216.58.196.67')
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    getservbyport('216.58.196.67')
TypeError: an integer is required (got type str)
>>> gethostbyaddr('216.58.196.67')
('kul01s09-in-f67.1e100.net', ['bom05s11-in-f3.1e100.net'], ['216.58.196.67'])
>>> gethostbyname('DESKTOP-708A91K')
'192.168.29.145'
>>> gethostbyaddr('''192.168.29.145''')
('DESKTOP-708A91K.mshome.net', [], ['192.168.29.145'])
>>> gethostbyaddr('2405:201:c023:6092:doe6:8801:ae56:2bff')
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    gethostbyaddr('2405:201:c023:6092:doe6:8801:ae56:2bff')
socket.gaierror: [Errno 11001] getaddrinfo failed
>>> gethostbyaddr('''106.51.104.145''')
('broadband.actcorp.in', [], ['106.51.104.145'])
>>> gethostbyaddr('''192.168.0.105''')
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    gethostbyaddr('''192.168.0.105''')
socket.herror: [Errno 11004] host not found
>>> gethostbyname('DESKTOP-Q8UUSGD')
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    gethostbyname('DESKTOP-Q8UUSGD')
socket.gaierror: [Errno 11001] getaddrinfo failed
>>> gethostbyname('broadband.actcorp.in')
'202.83.16.167'
>>> gethostbyname('DESKTOP-708A91K.mshome.net')
'192.168.29.145'
>>> gethostbyname('kul01s09-in-f67.1e100.net')
'216.239.32.67'
>>> gethostbyname('bom05s11-in-f3.1e100.net')
'216.58.196.67'
>>> 