Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = "#@!6966998dsvV"
>>> max(a)
'v'
>>> min(a)
'!'
>>> #More about Tuple
>>> tup = ('a', 'b', 'c', 'd')
>>> tup2 = ('e', 'f', 'g', 'h')
>>> tup+=tup2
>>> print(tup)
('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
>>> tup + tup2
('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'e', 'f', 'g', 'h')
>>> tup*2
('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
>>> tup*3
('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
>>> #Indexing in tuple
>>> tup[0]
'a'
>>> tup[1]
'b'
>>> #Slicing in Tuple
>>> tup[1:5]
('b', 'c', 'd', 'e')
>>> tup[1:8]
('b', 'c', 'd', 'e', 'f', 'g', 'h')
