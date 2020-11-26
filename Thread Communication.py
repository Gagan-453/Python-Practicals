#Thread Communication

#Program where Producer and Consumer threads communicate with each other through a boolean type variable
from threading import *
from time import *
#Create Producer class
class Producer:
    def __init__(self):
        self.lst = [ ]
        self.dataprodover = False
    def produce(self):
        #Create 1 to 10 items and add to the list
        for i in range(1, 11):
            self.lst.append(i)
            sleep(1)
            print('Item produced...')
        #Inform the consumer class that the data production is completed
        self.dataprodover = True

#Create a Consumer class
class Consumer:
    def __init__(self, prod):
        self.prod = prod
    def consume(self):
        #Sleep for 100 ms as long as dataprodover is False
        while self.prod.dataprodover == False:
            sleep(0.1)
            #Display the content when the data production is over
        print(self.prod.lst)

p = Producer() #Producer class object
c = Consumer(p) #Consumer class object and pass Producer object

#Create producer and consumer threads
t1 = Thread(target = p.produce)
t2 = Thread(target = c.consume)

#Run the threads
t1.start()
t2.start()
