Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #More about List
>>> #Concatenation in List
>>> mylist = ['Gagan','27']
>>> mylist2 = ['Adithya','7']
>>> mylist+=mylist2
>>> print(mylist)
['Gagan', '27', 'Adithya', '7']
>>> mylist + mylist2
['Gagan', '27', 'Adithya', '7', 'Adithya', '7']
>>> mylist.remove("27")
>>> print(mylist)
['Gagan', 'Adithya', '7']
>>> #Repitition in List
>>> mylist*3
['Gagan', 'Adithya', '7', 'Gagan', 'Adithya', '7', 'Gagan', 'Adithya', '7']
>>> #Slicing in List
>>> mylist[1:5]
['Adithya', '7']
>>> mylist[0:2]
['Gagan', 'Adithya']
>>> #Appending in List
>>> mylist.append("Reddy")
>>> print(mylist)
['Gagan', 'Adithya', '7', 'Reddy']
>>> #Extend in List
>>> mylist3 = ['Gahan','22']
>>> mylist.extend([mylist3])
>>> print(mylist)
['Gagan', 'Adithya', '7', 'Reddy', ['Gahan', '22']]
>>> mylist.insert(1,24)
>>> print(mylist)
['Gagan', 24, 'Adithya', '7', 'Reddy', ['Gahan', '22']]
>>> #More about Dictionary
>>> dic = {'Gagan':'Basketball','Advith':'Football','Harsha':'Hockey'}
>>> #Empty dictionary
>>> #Mentioning nothing in between the curly braces
>>> a = {}
>>> #Dictionary with integer keys
>>> {1:'Apple',2:'Banana',3:'Orange'}
{1: 'Apple', 2: 'Banana', 3: 'Orange'}
>>> #Dictionary with mixed keys
>>> b = {'Name':'Gagan',1:[2,3,4]}
>>> #Pairing in Dictionary
>>> #from sequence having each item as a pair
>>> #len()
>>> len(dic)
3
>>> dic.keys()
dict_keys(['Gagan', 'Advith', 'Harsha'])
>>> dic.values()
dict_values(['Basketball', 'Football', 'Hockey'])
>>> #More about sets
>>> #union
>>> s1 = {'Gagan', 'advith', 'Harsha', 'Praveen'}
>>> s2 = {'advith', 'Gagan', 'Ranjeet', 'Shabareesh'}
>>> s1|s2
{'Praveen', 'Gagan', 'advith', 'Shabareesh', 'Ranjeet', 'Harsha'}
>>> #Intersection in Sets
>>> s1&s2
{'Gagan', 'advith'}
>>> print(s1-s2)
{'Praveen', 'Harsha'}
>>> 
