#Thread is used to execute a group of statements like a function

import threading #Import thread module
#Program to find currently running thread
print('Let us find the current thread')
print('Currently running thread: ', threading.current_thread().getName()) #Return the name of the current thread
if threading.current_thread() == threading.main_thread(): #if current thread is main thread
    print('The current thread is main thread')
else:
    print('The current thread is not main thread')
print('---------------------------------------------')
from threading import *
def display():
    print('Hello I am running')
for i in range(5):
    t = Thread(target=display) #Create the target and specify the function as its target
    t.start() #run the thread
print('--------------------------')
from threading import *
#Create a function
def display(str):
    print(str)
#Create a thread and run the function for 5 times
for i in range(5):
    t = Thread(target=display, args = ('Hello',)) 
    t.start()
    t.join()
print('----------')

#Program to create a thread by making our class as sub class to Thread class
from threading import *
#Create a class as sub class to Thread class
class Mythread(Thread):
    #Override the run() method of Thread class
    def run(self): #Every Thread will run this method when it is started
        for i in range(1, 6):
            print(i)
t1 = Mythread() #An instance of Myclass
t1.start() #Start running the thread
t1.join() #This will wait till the thread completely executes the run() method

#A program to create a thread that access the instance variable of a class
from threading import *
class Mythread(Thread):
    #Constructor that calls Thread class constructor
    def __init__(self, str):
        Thread.__init__(self)
        self.str = str
    #Override the run() method of Thread class
    def run(self):
        print(self.str)
t1 = Mythread('Hello') #Create an instance of Myclass and pass the string
t1.start() #Start running the thread t1
t1.join() #Wait till the thread completes execution

#Program to create a thread that acts on the object of a class that is not derived from the Thread class
from threading import *
class Mythread:
    #a constructor
    def __init__(self, str):
        self.str = str
    #a method
    def display(self, x, y):
        print(self.str)
        print('The args are: ', x, y)
obj = Mythread('Hello') #An instance for Mythread class and store 'Hello'
t1 = Thread(target=obj.display, args = (1, 2)) #Create a thread to run display method of obj
t1.start() #run the thread
t1.join()

