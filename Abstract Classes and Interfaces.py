# ABSTRACT CLASSES AND METHODS
# An abstract method is a method whose action is redifined in the sub classes as per the requirement of the objects
# An abstract class is a class that generally contains some abstract methods.
# Generally, Abstract methods are written without any body since their body will be defined in the sub classes anyhow.
# The way to create an Abstract class is to derive it from a meta class ABC that belongs to abc(abstract base class)
# A meta class is a class that defines the behaviour of other classes

from abc import ABC, abstractmethod
class Myclass(ABC): #The meta class ABC defines that the class which is derived from it becomes an abstract class
    @abstractmethod
    def calculate(self, x):
        pass
    
class sub1(Myclass):
    def calculate(self, x):
        print('Square Value = ', x*x)
    
import math
class sub2(Myclass):
    def calculate(self, x):
        print('Square Root = ', math.sqrt(x))
        
class sub3(Myclass):
    def calculate(self, x):
        print('Square Value = ', x**3)
        
        
obj1 = sub1()
obj1.calculate(16)

obj2 = sub2()
obj2.calculate(16)

obj3 = sub3()
obj3.calculate(16)

#INTERFACES
# An interface is an abstract class but contains only abstract methods and there are no concrete methods
from abc import *
class Myclass(ABC):
    @abstractmethod
    def connect(self):
        pass
    def disconnect(self):
        pass
    
class Oracle(Myclass):
    def connect(self):
        print('Connecting to Oracle database...')
    def disconnect(self):
        print('Disconnected from Oracle..')
        
class Sybase(Myclass):
    def connect(self):
        print('Connecting to Sybase database...')
    def disconnect(self):
        print('Disconnected from Sybase..')
        
class Database:
    str = input('Enter database name: ')
    classname = globals()[str] # globals()[str] returns the name of the class that is in 'str'
    x = classname()
    
    x.connect()
    x.disconnect()