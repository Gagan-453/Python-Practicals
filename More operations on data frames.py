# Sorting the data from a .csv file
import pandas as pd
df = pd.read_csv("c:\\friends2.csv", parse_dates=['DOB']) # take 'DOB' as datatype field using parse_dates option
print(df)

print()
print('--------------------------------------')
print()

df1 = df.sort_values('DOB') # sort the rows on 'DOB' column into ascending order
print(df1)

print()
print('--------------------------------------')
print()

# To sort the rows in descending order, we can add option 'ascending=False'
df2 = df.sort_values('DOB', ascending=False)
print(df2)

print()
print('--------------------------------------')
print()

# Sort on multiple columns
# Sort 'DOB' is descending order and 'ROLL NO' in ascending order
df3 = df.sort_values(by=['DOB', 'ROLL NO'], ascending=[False, True])
print(df3)

print()
print('--------------------------------------')
print()

# Handling missing data
dm = pd.read_csv("c:\\friends3.csv", parse_dates=['DOB'])
print(dm)
# NaN is the default marker of the missing value

print()
print('--------------------------------------')
print()

# we can use fillna() method to replace the Na or NaN values by a specified value
dm1 = dm.fillna(0) # replace 0s in the place of NaN or Na
print(dm1)

print()
print('--------------------------------------')
print()

# Filling missing blocks with something
dm2 = dm.fillna({'NAME' : 'Charan', 'MARKS' : 0, 'DOB' : '---'}) # Write name as 'Charan', DOB as '---', MARKS as '0'
print(dm2)

print()
print('--------------------------------------')
print()

# If we want to remove rows having Na or NaN values, we can use dropna() method
dm3 = dm.dropna()
print(dm3)