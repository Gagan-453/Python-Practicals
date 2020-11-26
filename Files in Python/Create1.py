# Working with text files containing strings

x = open('myfile.txt', 'w')  #Opening the file 'myfile' to write something

print('Enter text(End with @): ') 

while str != '@': #as long as user doesn't write '@', the loop doesn't terminate
    str = input() #Accept input into 'str'
    #Write the string into the file
    if str!='@': 
        x.write(str + '\n')
        
        
x.close() #Close the file

#Program to read the contents
f = open('myfile.txt', 'r') #Open the file

print('The file contents are: ')

str = f.readlines() #readlines() can be used to read all the lines into a list
# 👆The output: ['I am Gagan\n', 'Hi Gagan\n'] #🔴Changes according to the input🔴
# The same line (str = f.readlines()) can be written as "f.read().splitlines()" to avoid '\n'
print(str)

f.close() #Close