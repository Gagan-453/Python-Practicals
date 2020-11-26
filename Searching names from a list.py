# Searching elements in a list
        
lst=['Gagan Adithya', 'Advith', 'Harsha', 'Praveen']

for i in range(len(lst)):
    lst[i] = lst[i].lower() #Converting all the names in the list into lower case letters


print(lst)

x = input("enter element to search:")

x = x.lower() #Converting all the letters into lower case letters from the input
x = x.lstrip() #Removing all the spaces from the input at left
x = x.rstrip() #Removing all the spaces from the input at right
for i in lst:
    if x in i:
        print(i)
        continue
        


# Alternate Method        
lst=['Gagan Adithya', 'advith', 'Harsha', 'Praveen', 'Ranjeet']

x = input("Enter element to search:") #taking input from the user
x = x.strip() #Removing the spaces from beginning or end of the name from the input

for i in range(len(lst)):
    for j in lst:
        if x.lower() in lst[i].lower(): #Converting all letters into lower case letters from the input and all elements in the list and checking if input is in the list
            print(lst[i]) #if input is in list print the name which is in lst
            break # Stopping the loop
