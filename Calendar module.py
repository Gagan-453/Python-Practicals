#Working with Calendar module
# Calendar module is useful to create calendar for any month or year

#Program to enter a year number and display whether it is leap or not
from calendar import *
y = int(input('Enter year: '))
if (isleap(y)): # isleap() function can be used to check whether a year is leap or not
    print(y, 'is leap year')
else:
    print(y, 'is not a leap year')
print('-------------------------------------')

#Program to display the calendar for a given month and year
from calendar import *
# Ask for month and year 
yy = int(input('Enter year: '))
mm = int(input('Enter month: '))
#Display the calendar for that month
cal = month(yy, mm) #month() function contains calendar
print(cal)

#Display the calendar for entire year
from calendar import *
year = int(input('Enter year: '))
print(calendar(year, w=2, l=1, c=8, m=3)) #year represents the year number, 'w' represents width between two columns, 'l' represents the blank lines between two rows, 'c' represents column-wise space between two months, 'm' represents the number of months to be displayed in a row
# This can also be written as "print(calendar(year, 2, 1, 8, 3))" or "print(calendar(year))"(The default values taken here are 2, 1, 8, 3)