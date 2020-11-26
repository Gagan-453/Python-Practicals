# Data Frame
# Data frame is useful in representing data in rows ad columns

# pandas module is useful for data analysis and data manipulation
# xlrd module is useful to retrieve data from excel files

# Reading data from excel files (.xlsx)
import pandas as pd
import xlrd
df = pd.read_excel('c:\\Data.xlsx', 'Sheet1') #to read data from excel files we can use read_excel function of pandas package
print(df)
 
# Just separators
print()
print('--------------------------------------')
print()

# Creating Data Frame from .csv files
# .csv file is a comma-separated values file that is similar to excel file but takes less memory
# To create .csv file, create a file in excel and save it as type CSV.
import pandas as pd
df = pd.read_csv("c:\\friends.csv")
print(df)

print()
print('--------------------------------------')
print()

# Creating data frame using python dictionary
friends = {"Name": ['Harsha', 'Ranjeet', 'Advith', 'Praveen', 'Shabareesh'], "Roll.no": [449, 477, 445, 465, 457], "DOB": ["8-12-2007", "5-10-2005", "21-03-2007", "12-09-2007", "29-07-2007"]}
import pandas as pd
df = pd.DataFrame(friends)
print(df)

print()
print('--------------------------------------')
print()

# Creating data frame from python list of tuples or lists
friends = [('Harsha', 449, "8-12-2007"), ("Ranjeet", 477, "5-10-2005"), ("Shabareesh", 457, "29-07-2007")]
import pandas as pd
df = pd.DataFrame(friends, columns=["Name", "Roll.no", "DOB"]) # Since the list of tuples doesn't have column names, we have to include the column names
print(df)

