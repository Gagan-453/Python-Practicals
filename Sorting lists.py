x = [ ] #Empty list

print('How many elements: ', end = ' ')
n = int(input()) #Taking input (let's say 5)

for i in range(n):
    print('Enter element: ', end = ' ') # Let's say (5, 2, 1, 4, 3)
    x.append(int(input())) #Appending all inputs into the empty list 'x'
    
print('The original list: ', x) #Print the original list

flag = False #When swapping is done flag becomes True
for i in range(n-1): # i is in range 1 to n-1
    for j in range(n-1-i): # if i = 0 for first time, then j = n-1-0, if i = 1, j = n-2, if i = 2, j = n-3
        if x[j] > x[j+1]: # first if x[0] > x[1], then
            #Swapping is done, Then, if x[1] > x[2], then again swapping is done, one element(The Greatest element) would be sorted after swapping one round
            t = x[j]
            x[j] = x[j+1]
            x[j+1] = t
            flag = True
    if flag == False:
        break
else:
    flag = False
    
print('Sorted List: ', x)

#The explanation is saved in GOOGLE DRIVE