Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.		
>>> class Emp:
           def __init__(self, id, name, sal):
                self.id = id
                self.name =  name
                self.sal = sal
           def display(self):
                print("{:d}  {:20s}  {10.2f}" .format(self.id, self.name, self.sal))
