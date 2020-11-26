Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> txt = """My name is Gagan
I am studying class 8 in SSKAL
I am learning Python"""#you can assign a multiline string using three quotes (single or double)
>>> print(txt)
My name is Gagan
I am studying class 8 in SSKAL
I am learning Python
>>> a = "Hello World"
>>> print(a[1])#prints the character at position 1 of var a
e

>>> print(a[2:5])#prints the characters from position 1 to 5 (5 not included)
llo
>>> print(a[-5:-2])#gets the characters from position 5 to 1 starting the count from the end of the string
Wor
>>> print(len(a))#returns the length of the string
11
>>> x = "     Hello World         "
>>> print(x.strip())#removes any whitespace from the beginning or the end
Hello World
>>> print(a.lower())#returns the string in lower case
hello world
>>> print(a.upper())#returns the string in upper case
HELLO WORLD
>>> print(a.replace("H", "J"))#replaces a string with another string
Jello World
>>> print(a.split(" "))#splits the string into substrings
['Hello', 'World']
>>> x = "Gagan" in txt
>>> y = "Gagan" not in txt
>>> print(x)
True
>>> print(y)
False
>>> # this checks a certain phrase or character is present in the following text
>>> m = "Hi"
>>> n = "Friends"
>>> o = m + " " + n #merge variable m with variable n into variable o.  use (" ") to make space between them
>>> print(o)
Hi Friends
>>> # we can use format() method to insert numbers into strings
>>> age = 12
>>> txt = "My name is Gagan, and I am {}"
>>> print(txt)
My name is Gagan, and I am {}
>>> print(txt.format(age))
My name is Gagan, and I am 12
>>> # The format() method takes unlimited number of arguments
>>> p = 25
>>> q = 453
>>> r = 50
>>> myorder = "I want {} mangoes and {} oranges for {}"
>>> print(myorder.format(p, q, r))
I want 25 mangoes and 453 oranges for 50
>>> # you can use index numbers to be sure the arguments are placed in correct placeholders
>>> myorder = "I want {0} mangoes and {2} oranges for {1} rupees"
>>> print(myorder.format(p, q, r))
I want 25 mangoes and 50 oranges for 453 rupees
>>> b = "hello world"
>>> print(b.capitalize())#converts the first character to upper case
Hello world
>>> print(a.casefold())#converts the string into lower case same as lower() function
hello world
>>> print(a.center(20))#used to print in middle with number of space
    Hello World     
>>> 
>>> fruits = ("banana", "banana", "orange", "banana", "apple")
>>> print(fruits.count("banana"))
3
>>> #counts the number of times a specified value occurs in a string
>>> txt = "My name is Gagan"
>>> print(txt.encode())#this encodes the string, using the specified encoding
b'My name is Gagan'
>>> print(txt.endswith("n"))#checks if the string ends with n
True
>>> print(txt.endswith("Gagan"))
True
>>> print(txt.endswith("is Gagan", 5, 11))#checks if position 5 to 11 ends with phrase "is Gagan"
False
>>> txt = "H\te\tl\tl\to"
>>> print(txt.expandtabs(10))#this method sets the tab size to the specified number of spaces here 10 spaces given
H         e         l         l         o
>>> print(a.find("World"))#finds the first occurence of the specified value
6
>>> print(a.find("e"))
1
>>> print(a.find("o", 5, 10))#fins letter "o" from position 5 to 10
7
>>> txt = "My name is {x}, I'm {age}."
>>> print(txt.format(x = "Gagan" , age = 12))
My name is Gagan, I'm 12.
>>> #this is format method(upper one)
>>> #index method is almost same as find() method
>>> txt = "Hello, Welcome to my world"
>>> print(txt.index("Welcome"))
7
>>> txt = "company453"
>>> text = "company 453"
>>> print(txt.isalnum())#checks if all characters are alphanumeric means A-Z and 1-9
True
>>> print(text.isalnum())#false, because space is not a numeric nor a alphabet
False
>>> txt = "What are you doing"
>>> print(txt.isalpha())# this returns true if all the characters in the string are in the alphabet
False
>>> txt = "gagan"
>>> print(txt.isalpha())
True
>>> txt = "\u0033"#unicode for 3
>>> x = txt.isdecimal()
>>> print(x)
True
>>> #isdecimal() method checks if all the characters in the unicode object are decimals
>>> num = 4536798231
>>> num = "45345345367899"
>>> 
>>> print(num.isdigit())#checks if all the characters in the text are digits
True
>>> print(txt.isdigit())
True
>>> #the isidentifier() method retuns true if the string is a valid identifier, otherwise false
>>> #A string is considered a valid identifier if it only contains alphanumeric letters(a-z) and (0-9), or underscores(_).A valid identifier cannot start with a number, or contain any spaces.
>>> x = "Myfolder"
>>> y = "2chocolates"
>>> z = "I am Gagan"
>>> print(x.isidentifier())
True
>>> print(y.isidentifier())
False
>>> print(z.isidentifier())
False
>>> b = "hello world"
>>> print(a.islower())# this checks if all the characters in the text are in lower case
False
>>> print(b.islower())
True
>>> num = "6430721354"
>>> print(num.isnumeric())#returns true if all the characters are numeric (0-9), otherwise false
True
>>> #exponents are also considered to be numeric values
>>> txt = "Hello! Are you #1?"
>>> print(txt.isprintable())# returns true if all the characers are printable, otherwise false
True
>>> txt = "       "
>>> print(txt.isspace())# returns true if all the characters in a string are whitespaces, otherwise false
True
>>> txt = "Hello, Welcome To My World!"
>>> print(txt.istitle())# this returns true if all words in a text start with a upper case letter, and the rest of the word are lower case letters, otherwise false. Symbols and numbers are ignored
True
>>> txt = "hello world"
>>> print(txt.istitle())
False
>>> text = "HELLO WORLD"
>>> print(txt.isupper())
False
>>> print(text.isupper())
True
>>> #retuns true if all the characters are in upper case, otherwise false
>>> #Numbers, symbols and spaces are not checked
>>> friends = ("Gagan" , "John" , "Vicky")
>>> x = "and".join(friends)
>>> #the join() method takes all items in an iterable and joins them into one string
>>> print(x)# 'and' will be printed in place of commas
GaganandJohnandVicky
>>> x = "banana"
>>> y = x.ljust(20)
>>> print(x, "is my favourite fruit")
banana is my favourite fruit
>>> print(x.ljust(20,"a"))
bananaaaaaaaaaaaaaaa
>>> #this method will left align the string using a specified character as the fill character
>>> txt = "77777777776666666taaaaa....Banana"
>>> print(txt.lstrip("76ta."))# removes 7, 6, t, . from the text(leading characters)
Banana
>>> # This method removes any leading characters (space is the default leading character to remove
>>> txt = "I could eat bananas all day"
>>> x = txt.partition("bananas")
>>> print(x)
('I could eat ', 'bananas', ' all day')
>>> #this method searches for a specified string and splits the string into tuple containing three elements
>>> #the first element contains the part before the specified string
>>> #the second element contains the specified string
>>> #the third element contains the part after the string
>>> txt = "what are you doing and where are you?"
>>> print(txt.rfind("are"))
29
>>> #the rfind() method finds the last occurence of the specified value
>>> #returns as -1 if the value is not found
>>> print(txt.rfind("e", 5, 10))#last occurence of "e" between position 5 to position 10
7
>>> #rindex() method is same as rfind() but rindex() method raises an exception if the value is not found
>>> print(txt.rindex("are"))
29
>>> x = txt.rjust(20, "b")
>>> print(x)
bbbbbbbbbbbbbbbanana
>>> #the rjust() method right aligns the string, using a specified character as the fill character
>>> #rpartition() method is almost same as partition() method but this searches for the last occurence of a specified string, and splits the string into a tuple containing three elements
>>> txt = "I could eat bananas all day, bananas are my favourite fruit"
>>> x = txt.rpartition("bananas")
>>> print(x)
('I could eat bananas all day, ', 'bananas', ' are my favourite fruit')
>>> #the rsplit() method splits a string into a list, starting from the right
>>> txt = "apple, banana, cherry"
>>> x = txt.rsplit(",")
>>> print(x)
['apple', ' banana', ' cherry']
>>> #the rstrip() method removes any trailing characters(characters at the end of the string), space is default trailing character to remove
>>> txt = "banana,,,,,,sssswwwwwwww....."
>>> x = txt.rstrip(",.sw")
>>> print(x)
banana
>>> #the splitliness() method splits a string into a list. The splitting is done at line breaks
>>> txt = "Thank you for the chocolate\nWelcome to my house"
>>> x = txt.splitlines()
>>> print(x)
['Thank you for the chocolate', 'Welcome to my house']
>>> txt = "Hello, welcome to my world"
>>> print(txt.startswith("Hello"))
True
>>> #this method returns true if the string starts with the specified value, otherwise false
>>> print(txt.startswith("wel", 7, 20))#check if position 7 to 20 starts with "wel"
True
>>> txt = "Hello, My Name is GAGAN"
>>> print(txt.swapcase())#this method returns a string where all the upper case letters are lower case and vice versa
hELLO, mY nAME IS gagan
>>> txt = "welcome to my world"
>>> print(txt.title())# This method returns a string where the first character in every word is upper case
Welcome To My World
>>> num = "500"
>>> print(txt.zfill(20))
0welcome to my world
>>> print(num.zfill(20))
00000000000000000500
>>> #the zfill() method adds zeros at the beginning of the string, until it reaches the specified length
>>> 
>>> # THESE ARE ALL PYTHON BUILT-IN FUNCTIONS
>>> 
>>> #DONE  BY
>>> #Y.GAGAN ADITHYA
>>> #ROLL:NO- 453
>>> #CLASS 8 A
