#Thread Communication using a queue
from threading import *
from time import *
from queue import *

#Create Producer class
class Producer:
    def __init__(self):
        self.q = Queue()
    def produce(self):
        #Create 1 to 10 items and add to the queue
        for i in range(1, 11):
            print('Producing item: ', i)
            self.q.put(i)
            sleep(1)
            
#Create a Consumer class
class Consumer:
    def __init__(self, prod):
        self.prod = prod
    def consume(self):
        #Receive 1 to 10 items from the queue
        for i in range(1, 11):
            print('Receiving item: ', self.prod.q.get())
            
p = Producer() #Create proucer object
c = Consumer(p) #Create consumer object and pass producer object

#Create Consumer and Producer Threads
t1 = Thread(target = p.produce)
t2 = Thread(target = c.consume)

#Run the threads
t1.start()
t2.start()
