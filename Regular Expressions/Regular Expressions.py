#Regular Expressions
print('Hi!\nI am Gagan') #This is a normal string
print(r'Hi!\nI am Gagan') #r' represents that it is a raw string
print('----------------------')

import re #Importing regular expression module
prog = re.compile(r'm\w\w') # 'm' represents that the words starting with 'm' should be matched. '\w' represents any character in A to Z, a to z, 0 to 9
# 'm\w\w' represents that the word must start with 'm' and there can be two chars or nums after 'm'
str = 'cat mat bat rat'
result = prog.search(str) #Search for word which starts with  
print(result.group()) #Dislplay output
# This code can be written as:
result = re.search(r'm\w\w', str) #Instead of compiling the first regular expression and then running the next one, a single step to compile and run all the regular expressions
print(result.group())

#The regular expression after compilation is available in prog object. So we need not compile it again and again when we want to use the same expression on other strings
str1 = 'Operating system format'
result = prog.search(str1)
print(result.group())
print('----------------------')

#The search() method searches for the string according to the regular expression and returns only the first string
import re
str = 'cat mat bat car'
result = re.search(r'c\w\w', str)
if result: #If result is not none
    print(result.group())
# Instead of search(), we can use findall() method. This method returns all resultant strings into a list
import re
str = 'cat bet bat rat'
result = re.findall(r'b\w\w', str)
print(result)
# match() method returns the resultant string only if it is found in the beginning of the string, it gives None if the string is not in the beginning
import re
str = 'man sun mop run'
result = re.match(r'm\w\w', str)
print(result.group())

import re
str = 'sun man mop run'
result = re.match(r'm\w\w', str)
print(result)
print('----------------------')

#Split the given string
# The split() method splits the given string into pieces according to the regular expression and returns the pieces as elements in a list
import re
str = 'This is @#Gagan\'s laptop!!'
r = re.split(r'\W+', str) # 'W' represents everything except alpha numeric (!,@#$%^&*...etc) and '+" after 'W' represents to match 1 or more occurences indicated by 'W'
#The result is that the string will be split into pieces where 1 or more non alpha numeric characters are found
# The work of this regular expression is to split the string at places where there are no alphabets and numbers
print(r)
print('----------------------')

#Replace a string with a new string
#sub() method can be used to replace old value or string to new string or value
import re
str = 'I am Gagan studying in class-9'
res = re.sub(r'class-9', 'class-8', str) #Replace 'class-9' with 'class-8' in str
print(res)
