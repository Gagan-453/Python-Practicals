#Passing members of one class to another class
class emp: #contains employee details
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary
        
    #This is an instance method
    def display(self):
        print('ID - ', self.id)
        print('Name - ', self.name)
        print('Salary - ', self.salary)
        
class myclass:
    #Method to retrieve employee details and display details
    @staticmethod #used because class variables and instance variables are not disturbed
    def mymethod(e):
        e.salary+=1000 #increment salary of e by 1000
        e.display()
        
ins = emp(12345, 'Gagan', 1000000)

myclass.mymethod(ins)

#Not Related to Passing members of one class to another class
#Program to calculate power value of a number with the help of a static method
class square:
    @staticmethod
    def mymethod(x,n):
        result = x**n
        print('{} to the power of {} is {}' .format(x,n,result))
        
square.mymethod(5,3)
square.mymethod(5,4)
