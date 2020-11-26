#Linked lists
#It is very convinient to store data. The operations like inserting elements, removing elements, searching for an element, etc can be done very quickly

ll = [ ] #Create an empty linked list
#Add some string type elements to ll
ll.append("America")
ll.append("Japan")
ll.append("India")

#Display the list
print("The existing list: ", ll)

#Display menu
choice = 0
while choice<5:
    print("LINKED LIST OPERATIONS")
    print('1 Add element')
    print('2 Remove element')
    print('3 Replace element')
    print('4 Search for element')
    print('5 Exit')
    choice = int(input('Your choice: '))
    #Perform a task depending on user choice
    if choice==1:
        element = input("Enter element: ")
        pos = int(input("At what position? "))
        ll.insert(pos, element) #Insert element at pos
    elif choice==2:
        try:
            element = input('Enter element? ')
            ll.remove(element)
        except ValueError:
            print("Element not found")
    elif choice==3:
        element = input('Enter new element: ')
        pos = int(input('At what position? '))
        ll.pop(pos)
        ll.insert(pos, element)
    elif choice==4:
        element = input('Enter element? ')
        try:
            pos = ll.index(element)
            print('Element found at position', pos)
        except ValueError:
            print("Element not found")
    else:
        break
    print("List = ", ll)