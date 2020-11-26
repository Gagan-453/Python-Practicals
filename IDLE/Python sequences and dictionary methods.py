Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 5.6
>>> b = int(a)
>>> b
5
>>> b = complex(a)
>>> b
(5.6+0j)
>>> #bool function
>>> #true or false
>>> a = 735032
>>> b = 83658653
>>> a>b
False
>>> a<b
True
>>> 453>354
True
>>> int(True)
1
>>> int(False)
0
>>> #List
>>> lst = [25,36,45,12]
>>> type(lst)
<class 'list'>
>>> #Tuple
>>> tup = (24,78,49,17)
>>> type(tup)
<class 'tuple'>
>>> #difference between list and tuple is that the value in list can be changed and the value in tuple cannot be changed
>>> lst[1]
36
>>> tup[1]
78
>>> lst[1] = 99
>>> lst
[25, 99, 45, 12]
>>> tup[0] = 67
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    tup[0] = 67
TypeError: 'tuple' object does not support item assignment
>>> #set
>>> s = {91,27,39,50,27}
>>> s
{27, 50, 91, 39}
>>> #the values in set can be printed in any order and the repeated value will be printed only once
>>> s[1]#gives an error because the value is not permanent in that position
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    s[1]#gives an error because the value is not permanent in that position
TypeError: 'set' object is not subscriptable
>>> #Range
>>> range(0, 100)
range(0, 100)
>>> list(range(100))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> #all even numbers from 1 to 10
>>> list(range(2,11,2))
[2, 4, 6, 8, 10]
>>> #Mapping or dictionary
>>> a = {'Gagan':'Basketball','Advith':'Football','Shivaji':'Volleyball','Harsha':'Hockey'}
>>> a
{'Gagan': 'Basketball', 'Advith': 'Football', 'Shivaji': 'Volleyball', 'Harsha': 'Hockey'}
>>> #you can find values using this method
>>> a.keys()
dict_keys(['Gagan', 'Advith', 'Shivaji', 'Harsha'])
>>> a.values()
dict_values(['Basketball', 'Football', 'Volleyball', 'Hockey'])
>>> a['Gagan']
'Basketball'
>>> a.get('Advith')
'Football'
>>> 
