# Command Line Arguments
# The arguments are stored in a list with the name 'argv' which is available in sys module

#Program to display command line args
import sys
n = len(sys.argv) # n is the number of arguments
args = sys.argv # args list contains arguments
print('No: of command line args = ', n)
print('The args are: ', args)
print('The args one by one: ')
for a in args:
    print(a)

#Program to add two numbers
import sys
sum = int(sys.argv[1]) + int(sys.argv[2]) #arg[1] represents the first value and arg[2] represents the second value and so on..
print('Sum = ', sum)

# Finding the sum of evens from the input
import sys
args = sys.argv[1: ]
print(args)

sum = 0

for a in args:
    x = int(a)
    if x%2 == 0:
        sum+=x
        
print('Sum of evens = ', sum)



