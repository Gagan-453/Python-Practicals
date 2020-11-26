Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # BITWISE OPERATORS IN PYTHON
>>> # These operators acts on Binary numbers
>>> #We can use these on integers also. Integers are converted into Binary numbers and the operators acts on these numbers and then again convert  them into Integers.
>>> 
>>> # There are six types of BITWISE OPERATORS
>>> #BITWISE COMPLEMENT OPERATOR(~)
>>> #BITWISE "AND"  OPERATOR(&)
>>> #BITWISE "OR"  OPERATOR( | )
>>> #BITWISE "XOR"  OPERATOR( ^ )
>>> #BITWISE "LEFT SHIFT"  OPERATOR( << )
>>> #BITWISE "RIGHT SHIFT"  OPERATOR( >> )
>>> 
>>> """BITWISE COMPLEMENT OPERATOR(~)"""
'BITWISE COMPLEMENT OPERATOR(~)'
>>> x = 10
>>> ~x # The 0s are converted into 1s and 1s are converted into 0s and
-11
>>> #x = 10 = 00001010
>>> # converted into 11110101 == -11 in integers
>>> 
>>> """BITWISE "AND"  OPERATOR(&)"""
'BITWISE "AND"  OPERATOR(&)'
>>> x = 10
>>> y = 11
>>> # x = 0000 1010
>>> #y = 0000 1011
>>> # 'BITWISE "AND"  OPERATOR(&)' converts ( 0 and  0 into 0), (0 and 1 into 0), (1 and 0 into 0), (1 and 1 into 1)
>>> #EXAMPLE
>>> a = 0
>>> b = 1
>>> a&a
0
>>> a&b
0
>>> b&a
0
>>> b&b
1
>>> x&y # 0000 1010 and 00001011 is converted into 0000 1010 because in x and y, 0 and 0 = 0 (4 times), 1and 1 into 1, 0 and 0 into 0,1and 1 into 1, 0 and 0 into 0
10
>>> """BITWISE "OR"  OPERATOR( | )"""
'BITWISE "OR"  OPERATOR( | )'
>>> x = 10 #0000 1010
>>> y = 11 #00001011
>>> x|y
11
>>> # This operator is opposite to 'BITWISE "AND"  OPERATOR(&)'
>>> # 0000 1010 and 00001011 is converted into 0000 1011 because in x and y, 0 and 0 = 0 (4 times), 1and 1 into 1, 0 and 0 into 0,1and 1 into 1, 0 and 1 into 1
>>> # 'BITWISE "OR"  OPERATOR( | )' converts ( 0 and  0 into 0), (0 and 1 into 1), (1 and 0 into 1), (1 and 1 into 1)
>>> a = 0
>>> b = 1
>>> a|a
0
>>> a|b
1
>>> b|a
1
>>> b|b
1
>>> """BITWISE "XOR"  OPERATOR( | )"""
'BITWISE "XOR"  OPERATOR( | )'
>>> x = 10 #0000 1010
>>> y = 11 #00001011
>>> x^y # # 0000 1010 and 00001011 is converted into 0000 0001 because in x and y, 0 and 0 = 0 (4 times), 1and 1 into 0, 0 and 0 into 0,1and 1 into 0, 0 and 1 into 1
1
>>> # 'BITWISE "XOR"  OPERATOR( ^ )' converts ( 0 and  0 into 0), (0 and 1 into 1), (1 and 0 into 1), (1 and 1 into 0)
>>> a = 0
>>> b = 1
>>> a^a
0
>>> a^b
1
>>> b^a
1
>>> b^b
0

>>> """BITWISE "LEFT SHIFT"  OPERATOR( << )"""
'BITWISE "LEFT SHIFT"  OPERATOR( << )'
>>> # The 'BITWISE "LEFT SHIFT"  OPERATOR( << )' shifts the bits of the number towards left a specified number of positions. It fills the last empty positions as "0"s
>>> x = 10
>>> x = 10 # 0000 1010
>>> x<<2
40
>>> # 40 = 00101000
>>> # The first two '0's are removed and the last two places are filled by two '0's
>>> """BITWISE "RIGHT SHIFT"  OPERATOR( >> )"""
'BITWISE "RIGHT SHIFT"  OPERATOR( >> )'

>>> # The 'BITWISE "RIGHT SHIFT"  OPERATOR( << )' shifts the bits of the number towards right a specified number of positions. It fills the first empty positions as "0"s
>>> x = 10 #0000 1010
>>> x>>2
2
>>> # 2 = 00000010
>>> # The last two digits (1, 0) are removed and the first two places are filled by two '0's
>>> 
>>> #BY:
>>> # GAGAN ADITHYA. Y