# FILE HANDLING


# There are two types of files in Python
# TEXT FILES used to store only text (Ex: 'Gagan')
# BINARY FILES used to store images, audio, video, text

# file handler = open("File name", "Open Mode", "Buffering")
# open function can be used to open a file
# File name represents a name on which data is stored

# Buffer represents a temporary block of memory. 'buffering' is an optional integer used to set the size of the buffer for the file
# In Binary mode, we can pass 0 as buffering integer to inform not to use any buffering
# In text  mode, we can pass 1 for buffering to retrieve data from the file one line at a time

# A file which is opened should be closed using close() method.

# Program to store some characters into a file
f = open('myfile.txt', "w") # If the file already exists it is opened and the previous data would be erased and the present data will be stored into the file. If the file doesn't exist, a new file is created with the name 'myfile'
# To add the text in the file 'myfile' without deleting the previous text, upper line can be written as "  f = open('myfile.txt', "a")  " a = append
str = input('Enter text: ') #Taking input
f.write(str) # A string can be stored into the file using write method
f.close() #Closing the file

# Program to read the file 'myfile'
f = open('myfile.txt', "r") # Open the file for reading data
str = f.read() # Read all the charcters from the file
# The upper line can be written as  " str = f.read(n) ", n represents the number of bytes to be read from the beginning, Ex: 'n' can be written as 5 to read 5 bytes from the file
print(str) #Display them on the screen
f.close() #Close the file

