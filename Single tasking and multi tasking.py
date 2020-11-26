#SINGLE TASKING
#A thread can be employed to execute one task at a time. Suppose there are 3 tasks and these are executed by a Thread one by one, then it is called single tasking

#Program to show single tasking using a thread that prepares tea
from threading import *
from time import *
class Mythread:
    def prepare_tea(self):
        self.task1()
        self.task2()
        self.task3()
    def task1(self):
        print('Boil milk and tea powder for 5 minutes...', end = ' ')
        sleep(5)
        print('Done')
    def task2(self):
        print('Add sugar and boil for 3 minutes...', end = ' ')
        sleep(3)
        print('Done')
    def task3(self):
        print('Filter it and serve...', end = ' ')
        print('Done')
obj = Mythread()
t = Thread(target=obj.prepare_tea)
t.start()
t.join()

#MULTI TASKING
# Several threads are executed at a time in multi tasking. Example, to perform two tasks, we can take 2 threads and attach them to 2 tasks, then those tasks are simultaneously executed by the two threads
#Using more than one thread is called 'Multi threading' and multi threading is used in 'Multi tasking'

#A program that performs two tasks using two threads simultaneously
from threading import *
from time import *
class Theatre:
    #Constructor that accepts a string
    def __init__(self, str):
        self.str = str
    #A method that repeats for 5 tickets
    def movie_show(self):
        for i in range(1, 6):
            print(self.str, " : ", i)
            sleep(1) #Sleep for 1 sec
#Create two instances to Theatre class
obj1 = Theatre('Cut ticket')
obj2 = Theatre('Show chair')
# Create two threads to run movie_show()
t1 = Thread(target=obj1.movie_show)
t2 = Thread(target=obj2.movie_show)
#Run the threads
t1.start()
t2.start()
t1.join()
t2.join()

