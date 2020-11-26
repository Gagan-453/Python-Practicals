#Element which comes first into the stack will be the first to be removed (First in first out)
# The deletion of elements should be done from the front of the queue and the insertion of elements should be done only at its end. It is not possible to do any operations at the middle of the queue
from que1 import Queue
q = Queue()

choice = 0
while choice<4:
    print('QUEUE OPERATIONS')
    print('1 Add element')
    print('2 Delete element')
    print('3 Search element')
    print('4 Exit')
    choice = int(input('Your choice: '))
    
    #Perform a task depending on user choice
    if choice==1:
        element = float(input('Enter element: '))
        q.add(element)
    elif choice==2:
        element = q.delete()
        if element == -1:
            print("The queue is empty")
        else:
            print("Removed element = ", element)
    elif choice==3:
        element = float(input('Enter element: '))
        pos = q.search(element)
        if pos == -1:
            print('The queue is empty')
        elif pos == -2:
            print('Element not found in the queue')
        else:
            print('Element found at position', pos)
    else:
        break
    print('Queue = ', q.display()) #Display the contents of the queue