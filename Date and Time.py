#The epoch is the point where the time starts
import time
epoch = time.time() #Call time function of time module
print(epoch) #Prints how many seconds are gone since the epoch .i.e.Since the beginning of the current year

#Converting the epoch into date and time
# locatime() function converts the epoch time into time_struct object
import time
t = time.localtime(epoch)
#Retrieve the date from the structure t
d = t.tm_mday
m = t.tm_mon
y = t.tm_year
print('Current date is: %d - %d - %d' %(d, m, y))
#Retrieve the time from the structure t
h = t.tm_hour
m = t.tm_min
s = t.tm_sec
print('Current time is: %d:%d:%d' %(h, m, s))
print('----------------------------------------------')

import time
t = time.ctime(epoch) #ctime() with epoch seconds
print(t)

#Using ctime() without epoch
import time
t = time.ctime() #ctime() without epoch time
print(t) #Current date and time
print('----------------------------------------------')

#Using datetime module to know current date and time
# now() method can be used to access day, month and year using the attributes day, month, year. Similarly, we can use hour, minute, second
from datetime import * #import datetime module
now = datetime.now()
print(now)
print('Date now: {}/{}/{}' .format(now.day, now.month, now.year)) #Retrieve current date using now() method
print('Time now: {} : {} : {}' .format(now.hour, now.minute, now.second)) #Retrieve current time using now() method
print('----------------------------------------------')

#Program to know today's date and time
from datetime import *
tdm = datetime.today() #today() of datetime class gives date and time
print("Today's date and time = ", tdm)
td = date.today() # today() of date class gives date only
print("Today's date = ", td)
print('----------------------------------------------')

#Combining date and time
from datetime import *
d = date(2020, 5, 27) #Create date class object and store some date
t = time(15, 30, 24)
dt = datetime.combine(d, t) #Combine method of 'datetime' class used to combine date and time objects
print(dt)
print('----------------------------------------------')

#Create a datetime object and then change its contents
from datetime import *
dt1 = datetime(year = 2020, month = 10, day = 27, hour = 9, minute = 45) #Create a datetime object
print(dt1)
dt2 = dt1.replace(year = 2008, hour = 17, month = 5)
print(dt2)