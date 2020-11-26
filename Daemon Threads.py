# Daemon Threads
#Daemon Threads can be used to perform background tasks
from threading import *
from time import *
from plyer import notification

#Function to display numbers from 1 to 5 every second
def display():
    for i in range(5):
        print('Normal Thread: ', end = ' ')
        print(i+1)
        sleep(1)

# Function to display date and time in every 2 seconds
def display_time():
    while True:
        print('Daemon Thread: ', end = ' ')
        print(ctime())
        sleep(2)
 
 #Create a thread and attach it to display_time()
t = Thread(target = display)
t.start()

#Create a thread and attach it to display_time()
d = Thread(target = display_time) 
d.daemon = True #Make the thread daemon, this can also be done by writing "d.daemon = True"
d.start()# Run the daemon thread