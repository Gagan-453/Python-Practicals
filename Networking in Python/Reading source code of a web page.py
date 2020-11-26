# A program that reads the source code of a web page
import urllib.request

# store the url of the page into file object
file = urllib.request.urlopen('https://www.python.org/')

# read the data from file and display it
print(file.read())