Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #2) What is the output of the following statements
#a.  print("Hello 'my dear' world")
#b.  print('Hello 'my dear' world')
#c.  print("Hello "my dear" world")
#d.  print('Hello "my dear" world')
#e.  print('Hello \"my dear" world')
#f.  print('Hello \'my dear\' world')
>>> 
>>> # ANSWERS:
>>> print("Hello 'my dear' world")# NO ERROR
Hello 'my dear' world
>>> print('Hello 'my dear' world')# ERROR
SyntaxError: invalid syntax
>>> # USING ESCAPE CHARACTER
>>> print('Hello \'my dear\' world')# NO ERROR
Hello 'my dear' world
>>> print("Hello "my dear" world")# ERROR
SyntaxError: invalid syntax
>>> # USING ESCAPE CHARACTER
>>> print("Hello \"my dear\" world")# NO ERROR
Hello "my dear" world
>>> print('Hello "my dear" world')# NO ERROR
Hello "my dear" world
>>> print('Hello \"my dear" world')# NO ERROR
Hello "my dear" world
>>> print('Hello \'my dear\' world')# NO ERROR
Hello 'my dear' world
>>> 
>>> #3) What is the output of the following statements
#a.  print("Hello \b'my dear' world")
#b.  print('Hello \t'my dear' world')
#c.  print("Hello \n"my dear" world")
#d.  print('Hello \\"my dear" world')
#e.  print('Hello \\"my dear" world')
#f.  print('Hello \\'my dear\' world')
>>> print("Hello \b'my dear' world")# NO ERROR(BACKSPACE)
Hello 'my dear' world
>>> print('Hello \t'my dear' world')# ERROR
SyntaxError: invalid syntax
>>> # MUST REMOVE THE 'SINGLE QUOTES'
>>> print('Hello \tmy dear world')
Hello 	my dear world
>>> print("Hello \n"my dear" world")# ERROR
SyntaxError: invalid syntax
>>> ## MUST REMOVE THE "DOUBLE QUOTES"
>>> print("Hello \nmy dear world")
Hello 
my dear world
>>> print('Hello \\"my dear" world')# NO ERROR
Hello \"my dear" world
>>> print('Hello \\'my dear\' world')# ERROR
      
SyntaxError: invalid syntax
>>> #MUST KEEP ONLY ONE SLASH BEFORE 'my dear'
>>> print('Hello \'my dear\' world')
Hello 'my dear' world
>>> 
>>> # WORK DONE BY:
>>> # Y.GAGAN ADITHYA REDDY
>>> # ROLL NO:453
>>> # CLASS- 8
>>> # SECTION- A