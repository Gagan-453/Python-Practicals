Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> data = {'Gagan':'Python','Advith':'Java','Harsha':'C++'}
>>> data
{'Gagan': 'Python', 'Advith': 'Java', 'Harsha': 'C++'}
>>> # Printing KEYS
>>> data.keys()
dict_keys(['Gagan', 'Advith', 'Harsha'])
>>> #Printing VALUES
>>> data.values()
dict_values(['Python', 'Java', 'C++'])
>>> # FETCHING A PARTICULAR VALUE FROM THE DICTIONARY
>>> data['Gagan']
'Python'
>>> data['Praveen']
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    data['Praveen']
KeyError: 'Praveen'
>>> 
>>> #get() function can also be used to fetch values
>>> data.get('Advith')
'Java'
>>> data.get('Praveen') #NO ERROR
>>> print(data.get('Praveen'))
None
>>> 
>>> data.get('Gagan','Hello')
'Python'
>>> data.get('Praveen','Hello')
'Hello'
>>> data
{'Gagan': 'Python', 'Advith': 'Java', 'Harsha': 'C++'}
>>> 
>>> # We can also list and Set to create DICTIONARY
>>> keys = ['Gagan','Advith','Shabareesh']
>>> values = ['Python','Java','Ruby']
>>> # Merging these two into a DICTIONARY
>>> data = dict(zip(keys,values))
>>> data
{'Gagan': 'Python', 'Advith': 'Java', 'Shabareesh': 'Ruby'}
>>> #ADDING A NEW VALUE TO DICTIONARY
>>> data['Shivaji'] = 'C'
>>> data
{'Gagan': 'Python', 'Advith': 'Java', 'Shabareesh': 'Ruby', 'Shivaji': 'C'}
>>> # DELETING VALUES FROM DICTIONARY
>>> del data['Shabareesh']
>>> data
{'Gagan': 'Python', 'Advith': 'Java', 'Shivaji': 'C'}
>>> # We can have a DICTIONARY inside a DICTIONARY and a LIST inside a DICTIONARY
>>> prog = {'JS':'Atom','CS':'VS','Python':['Pycharm','Thonny','Django'],'Java':{'JSE':'Netbeans','JEE':'Eclipse'}}
>>> prog
{'JS': 'Atom', 'CS': 'VS', 'Python': ['Pycharm', 'Thonny', 'Django'], 'Java': {'JSE': 'Netbeans', 'JEE': 'Eclipse'}}
>>> prog['JS']
'Atom'
>>> prog['Python']
['Pycharm', 'Thonny', 'Django']
>>> # We can use index numbers to specify the value in the LIST
>>> prog['Python'][1]
'Thonny'
>>> prog['Java']
{'JSE': 'Netbeans', 'JEE': 'Eclipse'}
>>> prog['Java']['JEE']
'Eclipse'
>>> 
>>> # EXTRAS
>>> # CLEARING ALL DATA FROM DICTIONARY(clear)
>>> print(data.clear())
None
>>> data
{}
>>> # REMOVING VALUE
>>> print(prog.pop('JS'))
Atom
>>> prog
{'CS': 'VS', 'Python': ['Pycharm', 'Thonny', 'Django'], 'Java': {'JSE': 'Netbeans', 'JEE': 'Eclipse'}}
>>> # THERE ARE MANY LIKE THIS
>>> 
>>> # PRACTICALS BY:
>>> # Y.GAGAN ADITHYA REDDY
