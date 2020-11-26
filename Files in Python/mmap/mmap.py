# Random Accessing of binary files using mmap(Memory mapped file)
# The data in files can be viewed as strings and can be manipulated using mmap module

import mmap, sys
#Display a menu
print("1 to display all the entries")
print("2 to display phone number")
print("3 to modify an entry")
print("4 exit")
ch = input('Your choice: ')

if ch=='4':
    sys.exit()
    
with open ("phonebook.dat", 'r+b') as f:
    #Memory map the file
    mm = mmap.mmap(f.fileno(), 0) #0 represents the total size of the file should be considered for mapping
    
    #Display the entire file
    if ch=='1':
        print(mm.read().decode()) # read() reads the entire file but readline() reads only the first line
        
    #Display phone number
    if ch == '2':
        name = input('Enter name: ')
        n = mm.find(name.encode()) #Find the position of name
        n1 = n+len(name) #Go to the end of the name
        ph = mm[n1: n1+10] #Display the next 10 bytes(i.e. Phone number)
        print('Phone no: ', ph.decode())
        
    #Modify the phone number
    if ch=='3':
        name = input('Enter name: ')
        n = mm.find(name.encode()) #Find the position of name
        n1 = n+len(name)#Go to the end of name
        ph1 = input('Enter new phone number: ')
        mm[n1: n1+10] = ph1.encode() #The old phone number is 10 bytess after n1
    
    mm.close() #Close the map