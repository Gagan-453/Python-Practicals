import matplotlib.pyplot as plt
import pandas as pd

empdata = {"empid": [1001, 1002, 1003, 1004, 1005, 1006],
           "ename": ['Gagan', 'Advith', 'Harsha', 'Shivaji', 'Shabareesh', 'Praveen'],
           "sal": [1000000000000000000, 3333333, 695430,43289,5432819, 859430],
           "doj": ["27-5-2008", "21-3-2007", "8-12-2007", "29-7-2007", "12-9-2007", "30-1-2008"]}

df = pd.DataFrame(empdata)

x = df['empid']
y = df['sal']

plt.bar(x, y, label='Employee data', color='red')

plt.xlabel('Employee ids')
plt.ylabel('Employee salaries')

plt.title('GOOGLE LLC')

plt.legend()

plt.show()