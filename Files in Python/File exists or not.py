# Knowing whether a file exists or not
import os, sys #os is operating system module
fname = input('Enter filename: ')

if os.path.isfile(fname): # os module has a sub module 'path'  which contains a method called 'isfile' used to check whether a file exists or not. Gives True if file exists or else False
    f = open(fname, "r")
else:
    print(fname+ " does not exist")
    sys.exit()

print('The file contains: ')
str = f.read()
print(str)
f.close()

#Counting number of lines, words, characters from a file
import os, sys
fname = input('Enter filename: ')

if os.path.isfile(fname):
    f = open(fname, 'r+')
else:
    print(fname+ ' doesn\'t exist')
    sys.exit()
    
cl = cw = cc = 0

for line in f:
    words = line.split() #splits line where ever there are spaces
    cl+=1 #For each line add 1 to cl
    cw+= len(words) #In each line add number of words to cw
    cc += len(line) #In each line add number of characters to cc
    f.write(line)
    
print('No.of lines: ', cl)
print('No.of words: ', cw)
print('No.of characters: ', cc)

f.close() #Close the file