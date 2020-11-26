Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Knowing about print() function
>>> # You can use Single quotes or double quotes to print the strings or integer, etc
>>> print("Hello World")
Hello World
>>> print('Hello World')
Hello World
>>> # A string is a collection of characters inside "Double quotes" or 'Single quotes'
>>> 
>>> #You can use 'Single quotes' inside double quotes
>>> #You can use "Double quuotes" inside 'Single quotes'
>>> print("What is 'Gagan' doing?")
What is 'Gagan' doing?
>>> print('What is "Gagan" doing?')
What is "Gagan" doing?
>>> 
>>> # You can't use 'Single Quotes' inside Single Quotes and "Double Quotes" inside Double Quotes
>>> 
KeyboardInterrupt
>>> print('What is 'Gagan' doing?')
SyntaxError: invalid syntax
>>> print("What is "Gagan" doing?")
SyntaxError: invalid syntax
>>> 
>>> print('I'm Gagan')
      
SyntaxError: invalid syntax
>>> print("I'm Gagan")
I'm Gagan
>>> 
>>> # We can use "Double Quotes" inside "Double Quotes" using ESCAPE CHARACTERS
>>> print("What is \"Gagan\" doing?")
What is "Gagan" doing?
>>> print('What is \'Gagan\' doing?')
What is 'Gagan' doing?
>>> 
>>> print('I\'m Gagan')
I'm Gagan
>>> print("Line A")
Line A
>>> print("Line B")
Line B
>>> #You can print these in different lines by using one program (\n)
>>> print("Line A\nLine B")
Line A
Line B
>>> print("Line A\nLine B\nLine C")
Line A
Line B
Line C
>>> # \t
>>> # Used to create space between two strings, integers, etc
>>> 
>>> print("NAME\tGAGAN")
NAME	GAGAN
>>> # \t is used for "TAB"
>>> #\\(BACK SLASH) is used to print the Backslash at the end of the string
>>> 
>>> print("My name is Gagan\")
      
SyntaxError: EOL while scanning string literal
>>> print("My name is Gagan\\")
My name is Gagan\
>>> # We can use \\\\ to print Double BackSlash
>>> print("My name is Gagan\\\\")
My name is Gagan\\
>>> 
>>> # \b (Used for BACKSPACE)
>>> print("Hell\blo") # One "l" will be removed from "Hello"
Helllo
>>> 
>>> # DONE BY:
>>> # Y.GAGAN ADITHYA REDDY
>>> # ROLL NO: 453
>>> # CLASS- 8
>>> # SECTION- A
