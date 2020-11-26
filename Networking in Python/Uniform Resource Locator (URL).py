# A program to retrieve different parts of the URL and display them
import urllib.parse

# take any url
url = 'http://www.dreamtechpress.com:80/engineering/computer-science.html'

# get a tuple with parts of the url
tpl = urllib.parse.urlparse(url)

# display the contents of the tuple
print(tpl)

# display different parts of the url
print('Scheme = ', tpl.scheme) # this gives the protocol name used in the URL
print('Net location = ', tpl.netloc) # gives the website name on the net with port number if present
print('Path = ', tpl.path) # gives the path of the web page
print('Parameters = ', tpl.params) 
print('Port number = ', tpl.port) # gives the port number
print('Total url = ', tpl.geturl()) # Gives total URL