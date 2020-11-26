Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 10
>>> def Gagan():
	a = 27
	print(a)

	
>>> Gagan()
27
>>> print(a)
10
>>> #this was Local and Global variable
>>> #GLOBAL KEYWORD
>>> #used to make a local variable to be used at global scope
>>> def Gagan():
	global a
	a = 27
	print(a)

	
>>> Gagan()
27
>>> print(a)
27
>>> #GLOBALS() KEYWORD
>>> #used to access the global and the local variables in the same function
>>> def Gagan():
	a = 27
	x = globals()['a']
	print(a)
	print(x)

	
>>> Gagan()
27
27
>>> globals()['a'] = 24
>>> print(a)
24
>>> 