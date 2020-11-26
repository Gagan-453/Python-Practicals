# A program to download a web page from internet and save it into our computer
import urllib.request

try:
    # store the url of the page into file object
    file = urllib.request.urlopen("https://www.python.org/")
    
    # read data from file and store it into content object
    content = file.read()
except urllib.error.HTTPError: # handle error if web page not found
    print('The web page does not exist')
    exit()
    
# open a file for writing
f = open('myfile.html', 'wb')

# write content into the file
f.write(content)

# close the file
f.close()