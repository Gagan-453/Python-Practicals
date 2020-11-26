#PICKLE IN PYTHON
# Pickling is a process of converting a class object into a byte stream to store into a file

#Pickling
import Emp, pickle #Emp is a saved file
            
f = open('C:/Users/ADINARAYANAREDDY/Python/Files in Python/Emp.dat', 'wb') #Emp.dat is a binary file, 'wb' refers that write binary
n = int(input('How many employees? ')) #Input

for i in range(n):
    id = int(input('Enter id: '))
    name = input('Enter name: ')
    sal = int(input('Enter Salary: '))
    
e = Emp.Emp(id, name, sal) #Emp class of file Emp
pickle.dump(e, f) #Store the object e into file f

f.close() #Close the file

#Unpickling is a process whereby a byte stream is converted back to into a class object
import Emp, pickle
f = open('Emp.dat', 'rb') # 'rb' refers to read the binary file

while True:
    try:
        obj = pickle.load(f)
        obj.display()
    except EOFError: # Exception raises when it reaches end of the file when there are no objects found    
        print('End of file reached...')
        break #Break the loop
f.close() #Close the file
