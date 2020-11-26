#Special Characters in Regular Expressions
# \.^$ [...] [^...] (... )  R | S
import re
str = 'Hello World'
res = re.search(r'^He', str) # '^' symbol is useful to check if a string starting with a sub-string or not
if res:
    print('String starts with "He"')
else:
    print('String does not start with "He"')
    
import re
str = "Hello World"
res = re.search(r"World$", str) # '$' symbol is useful to check if a string ends with a word or not
if res:
    print("String ends with 'World'")
else:
    print("String does not end with 'World'")
    
str = "Hello world"
res = re.search(r"World$", str, re.IGNORECASE) # re.IGNORECASE can be used to ignore the case 
if res:
    print("String ends with 'World'")
else:
    print("String does not end with 'World'")
    
import re
str = 'Rahul got 75 marks, Vijay got 55 marks, whereas Gagan got 98 marks.'
marks = re.findall(r'\d{2}', str) #Find marks
print(marks)
names = re.findall('[A-Z][a-z]*', str) # [ABC] represents that "A or B or C", [A-Z] represents range of charcters from A to Z, [a-z] represents range of chars from a-z
#'[A-Z][a-z]*' , [A-Z] represents that the first letter of the string should be a char from A-Z and [a-z] represents that the remining characters should be of range a-z(Observe '*')
print(names)

import re
str = 'The meeting may be at 8am or 9am or 4pm or 5pm'
res = re.findall(r'\dam|\dpm', str) # '|' represents 'or'
print(res)