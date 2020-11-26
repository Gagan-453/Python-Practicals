import geocoder
import socket
a = socket.gethostname()
ip = socket.gethostbyname(a)
g = geocoder.ip('106.51.104.145')
print(g.latlng)

