#timedelta class of datetime module is useful to find durations like difference between two dates or finding the date after adding a period to an existing date
#Program to find future date and time from an existing date and time
from datetime import *
d1 = datetime(2016, 4, 29, 16, 45, 0) #Store the date and time in datetime object: d1
period1 = timedelta(days = 10, seconds = 10, minutes = 20, hours = 12) #Define the duration using timedelta object: period1
#Add the duration to d1 and display
print('The new date and time is', d1+period1)
print('-------------------------------------------------------------')
#Program to display the next 10 dates continuously
from datetime import *
d = date.today()
print(d)
for x in range(1, 10): 
    nextdate = d+timedelta(days = x)
    print(nextdate)
print('------------------------')

#Program to accept date of births of two persons and determining the older person
#Enter date of births and store it into date class objects
d1, m1, y1 = [int(x) for x in input('Enter first person\'s date of birth (DD/MM/YYYY): ').split('/')]
b1 = date(y1, m1, d1)
d2, m2, y2 = [int(x) for x in input('Enter second person\'s date of birth (DD/MM/YYYY): ').split('/')]
b2 = date(y2, m2, d2)
#Compare the birth dates
if b1==b2:
    print('Both persons are of equal age')
elif b1 > b2:
    print('The second person is older')
else:
    print('The first person is older')
print('------------------------------------------------------')

#Sorting dates
from datetime import *
group = [] #take an empty list
group.append(date.today()) #Add today's date to list
#Create some more dates
d = date(2019, 6, 29)
group.append(d)
d = date(2017, 7, 15)
group.append(d)
group.append(d+timedelta(days=25)) #Add 25 days to the date and add to list
group.sort() #Sort the list
for d in group:
    print(d)
print('--------------------')

#Stopping Execution temporarily
import time, random
#Generate 10 random numbers
for i in range(10):
    num = random.randrange(100, 200, 5) #Generate in the range 100 to 200
    print(num)
    time.sleep(3.5)#Suspend execution for 3.5 seconds
print('-----')

#Knowing the time taken by a program
from time import *
t1 = perf_counter#Note the starting time of the program
#Do some processing
sum = 1+27829
#Make the processor or PVM sleep for 3 seconds
sleep(3) #This is also measured by perf_counter() but this is not measured if we use perf_time() function
t2 = perf_counter() #Note the ending time of the program
print('Execution time = %f seconds' %t2)