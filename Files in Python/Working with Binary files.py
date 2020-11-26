#BINARY FILES
# Binary files handle data in the form of bytes
# Hence, they can be used to read or write text, images, video, audio files

# 'rb' is used to read binary files
# 'wb' is used to write binary files

#Copying an image into a file
f1 = open('Bird.png', 'rb') #Open 'Screenshot (40).png' to read
f2 = open('new.png', 'wb') #Open 'new.png' to write

bytes = f1.read() #Read f1
print(bytes)
f2.write(bytes) #Copy f1 into f2

#Close the files
f1.close()
f2.close()

#If the file is in a different directory
# f1 = open('c:\\Users\\Screenshot (39).png', 'rb') can be used to tell that the Screenshot (39).png is available in 'Users' sub directory in c drive
