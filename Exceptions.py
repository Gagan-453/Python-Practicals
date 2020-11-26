# Errors which can be handled are called 'Exceptions'
# Errors cannot be handled but exceptions can be handled

#to handle exceptions they should be written in a try block
#an except block should be written where it displays the exception details to the user
#The statements in thefinally block are executed irrespective of whether there is an exception or not

# SYNTAX:
#try:
#    statements
#except exceptionname1:
#    handler1
#except exceptionname2: #A try block can be followed by several except blocks
#    handler2
#else:
#    statements
#finally:
#    statements

try:
    2/0
except ZeroDivisionError as ZDE:
    print('Division by zero is not possible')
    print('Please don\'t input zero as input')
else:
    print('Solution is calculated') #if zero is not given as input print 'Solution is calculated
finally:
    print('Problem Solved') # else block and finally block are optional
print('--------------------')
    
# Using the try block with finally block
try:
    x = int(input('Enter a number: '))
    y = 1/x
finally:
    print('No exception')
print('The inverse is: ', y)
print('--------------------')

# The assert statement
# This statement is used to check whether a condition is True or not
# If the condition is False then an AssertionError is raised
try:
    x = int(input('Enter a number between 5 and 10:'))
    assert x>=5 and x<=10 #If these conditions fulfill the input
    print('The number entered: ', x) #Print the number
except AssertionError:
    print('Wrong input Entered: ', x)
print('--------------------')

#Passing message if the input is not correct
try:
    x = int(input('Enter a number between 5 and 10:'))
    assert x>=5 and x<=10, 'Your input is incorrect' #If these are False, print('Your input is incorrect')
    print('The number entered: ', x) #Print the number
except AssertionError as obj: #We can catch the expression as an object that contains some description about the exception
    print(obj)
    
# except:
#      statements
# 👆This catches all types of exceptions
