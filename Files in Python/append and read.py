# Program to append data to an existing file and then displaying the entire file

f = open('myfile.txt', "a+") # 'a+' is append and read mode
print('Enter text to append(@ at end)')
while str!='@': #as long as user doesn't write '@', the loop doesn't terminate
    str = input() #Accept input into 'str'
    #Write the string into the file
    if str!='@':
        f.write(str+'\n') # '\n' represents that it should write a new line after each line
        
f.seek(3, 0) # 'f.seek(3,0)', the format is f.seek(offset, fromwhere),  here offset is 3 and fromwhere is 0
# offset represent how many bytes to move, here it starts from 3rd position, if the offset is 0, then it starts counting from beginning
# The fromwhere represents from which position to move, if 'fromwhere' is 0 represents from the begnning of the file, 1 represents from the current position, 2 represents from the ending of the file

print('The file contents are: ')
str = f.read() #Read the file
print(str)
f.close() #Close the file