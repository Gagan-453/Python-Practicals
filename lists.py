# Python lists
lst = ['Apple', 'Banana', 'Orange', 'Guava'] # A list

lst.append('Pineapple') # Adding element
print(lst)

lst.extend(('Kivy', 'Green Apple')) # Add multiple values
print(lst)

lst.pop() # Remove the last element
lst.pop(1) # Remove 2nd element
print(lst)

lst.remove('Kivy') #Remove  'Kivy' from list
print(lst)

a = lst.index('Apple') # Search for apple in list
print(a)

c = lst.append('Apple')
lst.count('Apple') # Count 'Apple'

lst.sort() # Sort values in ascending order
print(lst)

copy = lst.copy()
print(copy)

r = lst.reverse() # Reverse the list
print(r)

lst.insert(1, 'Grapes') # Add grapes at 2nd position
print(lst)

lst.clear() #clear the list
print(lst)