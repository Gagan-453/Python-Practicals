# A program to create a regular expression to retrieve all words starting with 'a' in a given string
import re
# [\w]*' represents 0 or more alphanumeric characters
str = 'an apple a day keeps a doctor away'
result = re.findall(r'a[\w]*', str) #Find words which starts with 'a' or has 'a'
#Print all the elements from the list
for word in result:
    print(word)
#This also represents 'ay' which is in the word 'away'  which is not a word
print('-----')

# The code can be improved to avoid the words which are in the middle of a word in the string
str = 'an apple a day keeps a doctor away'
result = re.findall(r'\ba[\w]*\b', str) #Find words which starts with 'a' or has 'a' and has spaces before and after them
for word in result:
    print(word) #Print all the elements from the list
print("------------------")

#Retrieve all words starting with a numeric digit
import re
str = 'I am Gagan and I am born on 27th in 5th month at 2008'
result = re.findall(r'\d[\w]*', str) #The numeric digit is represented by '\d'
for word in result:
    print(word) #Print the elements from the list
print("------------------")
    
import re
str = 'one two three four five six seven 1 8 10 12345'
result = re.findall(r'\b\w{5}\b', str) # '\b' represents a space, we used this character to get the words surrounded by spaces and 'w{5}' represents a word containing any alphanumeric characters repeated for 5 times
# Any character in curly braces represents repitition for n times
print(result)
# search() method can be used in place of findall() method to return the first occurence only

import re
str = 'one two three four five six seven 1 8 10 12345'
result = re.findall(r'\b\w{4,}\b', str) #Return all the words which have length more than 4 characters
print(result)

import re
str = 'one two three four five six seven 1 8 10 12345'
result = re.findall(r'\b\w{3,5}\b', str) #Return all the words which have length 3 to 5 characters
print(result)

import re
str = 'one two three four five six seven 1 8 10 12345'
result = re.findall(r'\b\d\b', str) #Return all the single digits from the string
print(result)

import re
str = 'one two three four one two three four'
result = re.findall(r'f[\w]*\Z', str) #Return the last word if it starts with 'f'
print(result)

print("------------------")

# A program to extract only name but not number from a string
import re
str = 'Gagan Adithya: 9491657737'
res = re.search(r'\D+', str) # '\D' represents that it should represent non-numeric character and '+' represents that it shoud show all non-numeric characters (More than one repitition)
print(res.group())
print("------------------")

# A program to find all words starting with 'an' or 'ak'
str = 'anil ananth arun arati arundhati abhijit abhinai advith gagan akhil'
res = re.findall(r'\ba[nk][\w]*', str) #\b represents space, r'\ba[nk][\w]*'..a[nk] represents either 'n' or 'k' or both after 'a'
print(res)
print("------------------")

# A program to create regular expression to retrieve date of birth from a string
str = 'Gagan  27-05-2008, Advith 445  21-3-2007, Harsha  8-12-2007'
res = re.findall(r'\d{1,2}-\d{2}-\d{4}', str) #Retrieve numeric digits in the format which has 1 or 2 digits of date, colon, 2 digits of month, colon, 4 digits of year
print(res) #Date of birth of Advith is not printed because it has only 1 digit of month
