# Random Accessing of Binary files
#Directly going to any byte in a binary file is called Random Accessing

str = 'Hi'
try:
    with open('data.bin', 'wb') as f: #Open 'data.bin' file
        f.write(str) #Gives error because we can't srore strings into a binary file
        f.write('Hello') # Error can't store strings
except TypeError as e:
    print(e)
    
# To store strings into a binary file the code can be written as:
with open('data.bin', 'wb') as f:
    f.write(str.encode()) #Converting a variable into binary format and writing it in 'data.bin' 
    f.write(b'Hello') #Converting a string into binary format and writing it in 'data.