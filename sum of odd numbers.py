x = 0
y = 1
z=0
a = 1

num = int(input("Enter a number: "))

for i in range(num):
    if i%2 != 0:
        x+=y
        y+=2
        z+=1
        if num == x:
            break
else:
    a = 0
    

for i in range(z*2):
    if i%2 != 0 and a!=0:
        print(i, end=', ')
        if num == y:
            break

    