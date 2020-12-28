# Printing tables using while loop
i = 1
while i<=5:
    j = 1
    while j<=10:
        print(i, ' * ', j, ' = ', i*j)
        j+=1
    i+=1
    print('\n')

# Printing tables using for loop
i = 1
for i in range(1, 6):
    for j in range(1, 11):
        print(f'{i} * {j} = {i*j}')
    print('')