# Operations on Data Frames

from pandas import *
df = read_csv("c:\\friends.csv")
print(df)

print()
print('----------------------------------')
print()

# Knowing number of rows and columns
# to know the number of rows and columns, we can use shape attribute
print(df.shape)
r, c = df.shape
print(r) #display only no of rows
print(c) #display only no of columns

print()
print('----------------------------------')
print()

# Retrieving rows from dataframe
# The method head() gives the first 5 rows and method tail gives the last 5 rows
print(df.head())
print(df.tail())
print(df.head(2)) # print only first two rows
print(df.tail(2)) # display only last two rows

# Retrieving a range of rows
# We can use slicing
print(df[2:5]) #display 2 to 4 rows (excluding 5)
print(df[::2]) #display alternate rows
print(df[5:0:-1]) #display rows in reverse order

print()
print('----------------------------------')
print()

# Retrieving column names
# To retrieve column names, we can use "columns" attribute
print(df.columns)

print()
print('----------------------------------')
print()

# Retrieving column data
print(df.NAME) #Retrieve data from 'Name' column
# OR
print(df['NAME']) #Retrieve data from 'Name' column

print()
print('----------------------------------')
print()

# Retrieving Data from multiple columns
# To retrieve multiple columns data, we can provide the list of column names as subscript to data frame object as df[ [list of column names] ]
print(df[['NAME', 'CLASS']]) # Retrieve data from 'NAME' and 'CLASS' columns

print()
print('----------------------------------')
print()

# Finding Maximum and Minimum values
# We can use max() and min() methods to find maximum and minimum values
# These methods are applied to columns containing numerical data
print(df['ROLL NO'].max()) # Retrieve the maximum value from 'ROLL  NO' column
print(df['ROLL NO'].min()) # Retrieve the minimum value from 'ROLL  NO' column

print()
print('----------------------------------')
print()

# Displaying Statistical information
# describe() method displays important information like number of values, average, standard deviation, 25% of total value, 50% of the total value
print(df.describe())

print()
print('----------------------------------')
print()

# Performing queries on data
# To retrieve all the rows where CLASS is greater than 7
print(df[df.CLASS>7])

# To retrieve the row where CLASS is maximum
print(df[df.CLASS == df.CLASS.max()])

# To retrieve only id numbers and names where the class is greater than 5
print(df[['NAME', 'ROLL NO']] [df.CLASS>5])

# Knowing the index range
print(df.index)

print()
print('----------------------------------')
print()

# Setting a column as index
# Index column is automatically generated, if we don't want this column and want to set a column from our data as index column, we can use set_index() method
df1 = df.set_index('NAME')
print(df1)

# If we want to modify the origina df and set 'NAME' as index column, we should add "inplace=True"
df.set_index('NAME', inplace=True)
print(df)

# Locate data of any student 
print(df.loc['Gagan'])

print()
print('----------------------------------')
print()

# Resetting the index
# To reset the index from 'NAME' to auto-generated number
df.reset_index(inplace=True)
print(df)