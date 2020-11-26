# SORTING LISTS
# SORTING IN ASCENDING ORDER
arr = [5, 2, 8, 1, 9]
temp = 0

print('Elements of original array: ')
print(len(arr))
print("_________")
for i in range(0, len(arr)):
    print(arr[i], end = ' ')
    
for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i]>arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
print(' ')

print("Elements of array sorted in ascending order: ")
for i in range(0, len(arr)):
    print(arr[i], end = ' ')
    
  # SORTING IN DESCENDING ORDER
arr = [5, 2, 8, 1, 9]
temp = 0

print('Elements of original array: ')
print(len(arr))
print("_________")
for i in range(0, len(arr)):
    print(arr[i], end = ' ')
    
for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        if arr[j]>arr[i]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
print(' ')

print("Elements of array sorted in descending order: ")
for i in range(0, len(arr)):
    print(arr[i], end = ' ')
