#The with statement
# The 'with' statement can be used while opening a file
#It will take care of closing a file which is opened by it
with open('sample.txt', 'w') as f:
    f.write('I am Gagan\n')
    f.write('Hi')
    
# Using with statement to open a file
with open('sample.txt', 'r') as f:
    for line in f:
        print(line)
        