# Downloading an image from internet
# we can use urlretrieve function() for downloading, this function takes the url of the image location and stores it into a file (myimage.jpg in this program)

import urllib.request

# copy the image url
url = 'http://kivy.org/slides/kivypictures-thumb.jpg'

# download the image as myimage.jpg in current directory
download = urllib.request.urlretrieve(url, "myimage.png")