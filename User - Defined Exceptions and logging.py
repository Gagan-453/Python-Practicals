# User Defined Exceptions
# Checking if every person has more than 2000 rupees as balance amount in his account

class MyException(Exception): # MyException is a sub class for Built-in class Exception
    def __init__(self, arg):
        self.msg = arg
        
def check(dict):
    for k,v in dict.items():
        print('Name = {:15s}  Balance = {:10.2f}' .format(k, v))
        if (v<2000.00): #if the value is less than 2000 rupees
            raise MyException('Balance amount is less in the account of ' + k) #raise an exception        
        
bank = {'Raj' : 5000.00, 'Vani' : 8900.50, 'Ajay' : 1990, 'Naresh' : 15000.00} #Creating a dictionary

try:
    check(bank) # Calling the check function 
except MyException as me:
    print(me)
    
# LOGGING THE EXCEPTIONS
# The logging module stores error and excceptions messages raised by a program into a file called log file
# We can open the file later and read it. This helps the programmer to understand how many errors are there
# This helps in debugging the programs

# Different levels of error messages
# *CRITICAL - Represents a very serious error that needs high attention
# *ERROR - Represents a serious error
# *WARNING - Represents a warning message, some caution is needed
# *INFO - Represents a message with some important information
# *DEBUG - Represents a message with debugging information
# *NOTSET - Represents that the level is not set
import logging
# Store messages into mylog.txt file (This can be done using basicConfig in logging module)
# Store only the messages with level equal to or more than that of ERROR (i.e. ERROR and CRITICAL)
logging.basicConfig(filename = 'mylog.txt', level = logging.NOTSET)
# These messages are stored into the file
logging.error('There is a problem in the program')
logging.critical('There is a problem in the design')
# But these are not stored
logging.warning("The project is going slow")
logging.critical("You are a junior programmer")
logging.debug("Line. no 10 contains SyntaxError")
#The errors are stored in a txt file

# Accepting two numbers from the user and then fiinding the result of their division
# When an exception occurs inside try block, the 'except' block will catch it and the exception message will be stored into the object 'e'.
# This message is then written into the log file 'log.txt(CAN BE CHANGED)'
from logging import * #Importing all methods from logging module

#Storing logging messages into 'log.txt' file
basicConfig(filename = 'log.txt', level = WARNING) #Store only the messages with level equal to or more than that of WARNING (i.e. WARNING, ERROR, CRITICAL)
try:
    a = int(input('Enter a number: '))
    b = int(input('Enter another number: '))
    c = a/b
except Exception as e:
    exception(e)
else:
    print('The result of division: ', c)
# This is stored in mylog.txt file (Along with the upper example)