# NESTED LOOPS
# A loop inside a loop is called nested loop
for i in range(3): # i values are from 0 to 2
    for j in range(4): # j values are from 0 to 3
        print('i = ', i, '\t', 'j = ', j) # Display i and j values
# The outer loop repeats for 3 times by changing i values from 0 to 2 and inner loop repeats for 4 times from changing values of j from 0 to 3
# When outer loop is executed once, the inner loop is executed for 4 times here, means when i value is 0, j values will change from 0 to 3
# Once the inner for loop is execution is completed (j reached 3), the python interpreter will go back to outer for loop to repeat the execution for the seecond time.This is executed for 4 times (in this case)

#Using Nested loop to draw a Right - angled triangle
for i in range(1, 10): #to display 10 rows
    for j in range(1, i+1): #if the row number is 'i', then the inner for loop should repeat for 1 to i times (No.of stars = Row number)
        print('*', end = ' ') # the end = ' ' represents that it should not throw the cursor into the next line after displaying each star
    print() # This statement simply throws the cursor into the next line when there is a new row
    
# Program that displays stars in a right-angled triangle using single loop
for i in range(1, 11):
    print('* '*(i)) #Multiply the stars from range 1, 11 (1st time: '* ' multiplied by 1 = *, 2nd time: '* ' multiplied by 2 = * *, 3rd time: .................)

# Using single for loop to draw an equivalateral triangle
n = 40
for i in range(1, 11):
    print(' '*n, end = ' ') #Repeat space for n times in the same line
    print('* '*i) #then display the star and throw the cursor into next line
    n-=1 #Reduce the spaces by 1 in each row
# This can also be  written in an elegant style of Python:
for i in range(1, 11):
    print(' '*(n-i) + '* '*(i))
    
# A python program to display numbers from 1 to 100 in 10 rows and 10 columns in a proper format
for x in range(1, 11):
    for y in range(1, 11):
        print('{:7}'.format(x*y), end = ' ') #Each column size is 7
    print()
