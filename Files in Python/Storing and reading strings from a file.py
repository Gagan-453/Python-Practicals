#Program to create a binary file and store few records
reclen = 20

with open('Cities.bin', 'wb') as f: #Open 'Cities.bin'
    n = int(input('How many entries? ')) #Input
    
    for i in range(n):
        city = input('Enter city name: ')
        ln = len(city) #Length of each input
        city = city + (reclen-ln)*' ' #After each input add 'reclen(20) - length of input' spaces
        city = city.encode() #Convert the input to store into binary file
        f.write(city) #Write it
        
#Program to randomly access a record from a binary file
reclen = 20 #Take record length as 20 characters
with open('Cities.bin', 'rb') as f: #Open
    n = int(input('Enter record number: ')) #Input
    f.seek(reclen * (n-1)) #Move the file pointer to the end of n-1th record
    str = f.read(reclen) # Get the nth record with 20 chars 
    print('City name: ', str.decode()) #Convert the byte into ordinary string
    
# Program to search for city name in the file and display the record number that contains the city name
import os
reclen = 20 #Take record length as 20 characters

size = os.path.getsize('Cities.bin')
print('Size of file = {} bytes'.format(size)) #Find size of the file

n = int(size/reclen) #Find number of records in the file
print('Number of records = {}'.format(n))

with open('Cities.bin', 'rb') as f: #Open file as 'f'
    name = input('Enter city name: ') #Input
    name = name.encode() #Convert into binary format
    position = 0 #Position represents the position of file pointer
    found = False # found becomes True if city is found in the file
    
    #Repeat for n records in the file
    for i in range(n):
        f.seek(position) #Place the file pointer at position 0 at first
        str = f.read(20) #Read 20 characers from that position
        #If found
        if name in str: 
            print('Found at record number {}' .format(i+1))
            found = True
        position+=reclen #Go to the next record
    
    if not found:
         print('City not found')
         
#Updating the city name in the file
import os
reclen = 20 #Take record length as 20 characters
size = os.path.getsize('Cities.bin') #Find size of the file
n = int(size/reclen) #Find number of records in the file

with open ('cities.bin', 'r+b') as f:
    name = input('Enter city name: ')
    name = name.encode()
    newname = input('Enter new name: ')
    ln = len(newname)
    newname = newname+ (20-ln)*' '
    newname = newname.encode()
    position = 0
    found = False # found becomes True if city is found in the file
    
    #Repeat for n records in the file
    for i in range(n):
        f.seek(position) #Place the file pointer at position 0 at first
        str = f.read(20) #Read 20 characers from that position
        #If found
        if name in str: 
            print('Updated record number {}' .format(i+1))
            found = True 
            f.seek(-20, 1) #Go back 20 bytes from the current position
            f.write(newname) #Update the record
        position+=reclen #Go to the next record
    
    if not found:
         print('City not found')
         
# Deleting a record from the file
import os
reclen = 20 #Take record length as 20 characters
size = os.path.getsize('Cities.bin') #Find size of the file
n = int(size/reclen) #Find number of records in the file

f1 = open('Cities.bin', 'rb') #Open the file for reading
f2 = open('file2.bin', 'wb') #Open file2.bin for writing (This is a temporary file)

city = input('Enter city name to delete: ') #Accept input
ln = len(city) #Length of input
city = city+(reclen-ln)* ' ' #Add spaces so that it will have 20 characters length
city.encode() #Convert city name into binary string

x = ' '
x = x.encode()
#repeat for all n records
for i in range(n):
    str = f1.read(reclen) #Read one record from f1 file
    if str!=city:
        f2.write(x*20)
print('Record deleted...')

f1.close()
f2.close()

os.remove("Cities.bin")
os.rename("file2.bin", "Cities.bin")