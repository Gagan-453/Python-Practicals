from threading import *
from time import *
class Railway:
    #Constructor that accepts no. of available berths
    def __init__(self, available):
        self.available = available
    #A method that reserves berth
    def reserve(self, wanted):
        print('Available no. of berths = ', self.available)
        #If available>=wanted, allot the berth
        if self.available>=wanted:
            #Find current thread name
            name = current_thread().getName()
            #Display berth is alloted for the person
            print('%d berths is alloted for %s' %(wanted, name))
            #Make time delay so that the ticket is printed
            sleep(1.5)
            #Decrease the no. of available berths
            self.available-=wanted
        else:
            #If available < wanted, then say sorry
            print('Sorry, no berths to allot')
#Create instance to Railway class
obj = Railway(1)
#Create two threads and specify 1 berth is needed
t1 = Thread(target=obj.reserve, args=(1,))
t2 = Thread(target=obj.reserve, args=(1,))
#Give names to the threads
t1.setName('First Person')
t2.setName('Second Person')
#Run the threads
t1.start()
t2.start()
t1.join()
t2.join()
print('-----------------------------')
#THIS GIVES WRONG OUTPUT!! Because both threads run at a time and the value is not updated by the first thread, so the second thread also takes the same number of berths to allot
#This can be solved using "Thread Synchronisation"

#A program to achieve thread synchronisation using locks
from threading import *
from time import *
class Railway:
    #Constructor that accepts no. of available berths
    def __init__(self, available):
        self.available = available
        #Create a lock object
        self.l = Lock() 
    #A method that reserves berth
    def reserve(self, wanted):
        self.l.acquire() #Lock the current object
        print('Available no. of berths = ', self.available)
        #If available>=wanted, allot the berth
        if self.available>=wanted:
            #Find current thread name
            name = current_thread().getName()
            #Display berth is alloted for the person
            print('%d berths is alloted for %s' %(wanted, name))
            #Make time delay so that the ticket is printed
            sleep(1.5)
            #Decrease the no. of available berths
            self.available-=wanted
        else:
            #If available < wanted, then say sorry
            print('Sorry, no berths to allot')
            #Task is competed, release the lock
        self.l.release()
        
#Create instance to Railway class
obj = Railway(1)
#Create two threads and specify 1 berth is needed
t1 = Thread(target=obj.reserve, args=(1,))
t2 = Thread(target=obj.reserve, args=(1,))
#Give names to the threads
t1.setName('First Person')
t2.setName('Second Person')
#Run the threads
t1.start()
t2.start()
t1.join()
t2.join()
#We created a lock object which is avaiable in Thread class and stored the lock into variable 'l' and called that lock after printing the available locks. This lock locks the path when the first thread is running and when it comes out, the lock is released using release() method and the second thread runs.
