Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # PYTHON BOOLEANS
>>> 
>>> # Booleans represent one of two values: TRUE or FALSE
>>> 
>>> # When two values are compared, the expression is evaluated and python returuns the boolean answer
>>> #EXAMPLE
>>> 
>>> print(10>9)
True
>>> print(10==9)
False
>>> print(10<9)
False
>>> 
>>> # When you run a condition in an if statement, Python returns TRUE or FALSE
>>> a, b = 100,200
>>> if b>a:
	print("b is grater than a")
else:
	print("b is less than a")

	
b is grater than a
>>> b,a = 100,200
>>> if b>a:
	print("b is grater than a")
else:
	print("b is less than a")

	
b is less than a
>>> 
>>> #Evaluating Values and Variables
>>> #The bool() function allows you to evaluate any value, and give you TRUE or FALSE in return
>>> print(bool("Hello"))
True
>>> print(bool(27))
True
>>> x,y = "Hello",15
>>> print(bool(x))
True
>>> print(bool(y))
True
>>> 
>>> # Almost any value is evaluated to TRUE if it has some sort of content
>>> # Anything is true, except empty strings
>>> # Any number is true except '0'
>>> # Any list, set, dictionary are TRUE, except empty ones
>>> 
>>> bool("Gagan")
True
>>> bool(27508)
True
>>> bool(["apple", "banana", "cherry"])
True
>>> # Values which are FALSE
>>> # EMPTY VALUES such as   (), [], {}, "", ''
>>> # THE NUMBER  "0"
>>> # THE VALUE  "None"
>>> # THE VALUE "False"
>>> 
>>> bool(False)
False
>>> bool(None)
False
>>> bool(0)
False
>>> bool("")
False
>>> bool('')
False
>>> bool(())
False
>>> bool([])
False
>>> bool({})
False
>>> class myclass():
	def __len__(self):
		return 0

	
>>> myobj = myclass()
>>> print(bool(myobj))
False
>>> def GAGAN():
	return True

>>> print(GAGAN())
True
>>> def Gagan():
	return True

>>> if Gagan():
	print("YES")
else:
	print("NO")

	
YES
>>> 
>>> # Python has many built-in functions that returns a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type
>>> 
>>> # Checking if an object is an integer or not
>>> x = 27
>>> print(isinstance(x,int))
True
>>> y = 100.27
>>> print(isinstance(y,int))
False
>>> 
