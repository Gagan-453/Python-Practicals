#Deques are more flexible than queues and stacks
#We can insert and delete elements at front, rear, middle but in queues the insertion will be at one end and deletion will be at another end, in stacks insertion and deletion will take place at one end
from collections import deque  #Import deque
d = deque() #Create an empty deque

choice = 0
while choice<8:
    print("DEQUE OPERATIONS")
    print('1 Add element at front')
    print('2 Remove element at front')
    print('3 Add element at rear')
    print('4 Remove element at rear')
    print('5 Remove element at middle')
    print('6 Search for element')
    print('7 Reverse the deque')
    print('8 Exit')
    choice = int(input('Your choice: '))
    #Perform a task
    if choice==1:
        element = input('Enter element: ')
        d.appendleft(element)# appendleft() can be used to add element at the front
    elif choice==2:
        if len(d) == 0:
            print("Deque is empty")
        else:
            d.popleft()# popleft() can be used to pop an element at front
    elif choice==3:
        element = input('Enter element: ')
        d.append(element) # append() to append element at the rear
    elif choice==4:
        if len(d) == 0:
            print("Deque is empty")
        else:
            d.pop() #pop() to remove element at the rear
    elif choice==5:
        element = input('Enter element: ')
        try:
            d.remove(element)
        except ValueError:
            print("Element not found")
    elif choice==6:
        element = input('Enter element: ')
        c = d.count(element)
        print('The number of times the element found = ', c)
    elif choice==7:
        d.reverse()
        print('Deque reversed')
    else:
        break
    #Display elements using for loop
    print('Deque = ', end = ' ')
    for i in d:
        print(i, ' ', end = ' ')
    print() #move cursor to next line