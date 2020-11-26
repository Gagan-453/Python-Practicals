#Thread communication using notify() and wait() methods on Condition object
from threading import *
from time import *

#Create Producer class
class Producer:
    def __init__(self):
        self.lst = [ ]
        self.cv = Condition() #This class contains methods which are used in Thread Communication, Ex: notify(), wait()
    def produce(self):
        #Lock the Condition object
        self.cv.acquire()
        
        #Create 1 to 10 items and add to the list
        for i in range(1, 11):
            self.lst.append(i)
            sleep(1)
            print('Item produced...')
            
        #Inform the consumer that production is completed
        self.cv.notify()
        #Release the lock
        self.cv.release()
        
#Create Consumer class
class Consumer:
    def __init__(self, prod):
        self.prod = prod
    def consume(self):
        #Get lock on condition object
        self.prod.cv.acquire()
        
        #Wait only for 0 seconds after the production
        self.prod.cv.wait(timeout=0)
        
        #release the lock
        self.prod.cv.release()
        
        #Display the contents of the list
        print(self.prod.lst)
        
p = Producer() #Producer class object
c = Consumer(p) #Consumer class object passing Producer object

#Create Proucer and Consumer threads
t1 = Thread(target = p.produce)
t2 = Thread(target = c.consume)

#Run the threads
t1.start()
t2.start()