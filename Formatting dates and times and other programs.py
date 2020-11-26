#FORMATTING DATES AND TIMES
#strftime() method can be used to format dates and times
import datetime
td = datetime.date.today()
print(td) #Prints date of today
#Format the td convert into string str
str = td.strftime('%d, %B, %Y') # '%d' indicates the day of the month in two digit format , '%B' represents month's full name(Ex: May), '%Y' indicates the four digit year number as 2020
print(str)
print('-------------------------')

#Program to find the  day of the year and the week day name
from datetime import *
#Get today's date
td = date.today()
print(td)
# '%j' returns day of the year as: 001, 001, ...366.
s1 = td.strftime("%j")
print('Today is', s1, 'day of the current year')
# '%A' returns week day name
s2 = td.strftime("%A")
print('It is', s2)
print('-------------------------')

#Program to format the time using strftime() method
from datetime import *
dt = datetime.now()
print(dt)
print('Current time: ', dt.strftime("%H:%M:%S"))

#Program to accept date from keyboard and display the day of the week
from datetime import *
d, m, y = [int (x) for x in input('Enter a date: ').split('/')] #accept date, month, year as input
dt = date(y, m, d) #Store them in date class object 'dt'
print(dt.strftime('Day %w of the week. This is %A')) # %w - day number and %A - Full name of the week day
print('-------------------------')

#Program to find the difference in number of days, weeks and months between two given dates
from datetime import *
#Enter two dates from the keyboard
d1, m1, y1 = [int(x) for x in input("Enter first date: ").split('/')]
d2, m2, y2 = [int(x) for x in input("Enter second date: ").split('/')]
#Create date class object with the input
dt1 = date(y1, m1, d1)
dt2 = date(y2, m2, d2)
#Find difference between two dates
dt = dt1-dt2 #The resultant belongs to timedelta class
print('Days difference = ', dt)
#Find difference in weeks
weeks, days = divmod(dt.days, 7) #divmod() is a built-in function that returns the pair of quotient and reaminder of division, here weeks = Quotient, days = Remainder
print('Weeks difference = ', weeks)
#Find difference in months
months, days = divmod(dt.days, 30)
print('Months difference = ', months)
print('-------------------------')

#Program to find difference between two dates along with times
from datetime import *
#Create two datetime objects that store date and time
d1 = datetime(2000, 6, 25, 8, 00, 25)
d2 = datetime(2020, 5, 27, 7, 55, 15)
#Find the difference
diff = d2-d1
print(diff)
#Divide days by 7 to get weeks and remaining days
weeks, days = divmod(diff.days, 7) #diff.days of timedelta class gives number of days
# Divide seconds by 3600 to get hours
hrs, secs = divmod(diff.seconds, 3600) #diff.seconds timedelta class gives number of seconds
#Divide remaining seconds to get minutes
mins = secs//60 #Get minutes
#take remaining seconds from the remainder of division
secs = secs%60
print('Difference is %d weeks, %d days, %d hours, %d minutes, %d seconds' %(weeks, days, hrs, mins, secs))
