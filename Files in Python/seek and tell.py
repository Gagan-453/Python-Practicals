# seek() and tell() Methods

f = open('myfile.txt', "r+b") # 'r+b' is read and write mode
f.write(b'Amazing Python') # b'...' represents binary
  
#             A  m  a  z  i  n  g    P  y  t  h  o  n
# Bytes:    1  2   3  4  5  6  7 8 9 10 11 12 13 14

#Format of seek() method is 'seek(offset, fromwhere)', if "fromwhere" is not defined, it is by default taken as 0
# 'Fromwhere' 0 represents from the beginning of the file, 1 represents from the current position, 2 represents from the last

f.seek(10) #Seek is used to move the file pointer to another position
print(f.tell()) #Tell is used to know the current position of the pointer

f.seek(10) # Same as f.seek(10,0)
print(f.tell()) #Displays 10 because the pointer starts from 10th position

f.seek(-10, 2) #Starts from 4th position from the beginning of the file beacuse -10 represents to count from last and 2 represents to count from the last (Total 14 bytes - 10 bytes from last = 4)
print(f.tell()) #Prints 4


#File open modes for binary files
# If we attach 'b' for text files, they represent modes for binary files

# wb  -  Used to write
# rb  -  Used to read
# ab  -  Used to append
# w+b  -  