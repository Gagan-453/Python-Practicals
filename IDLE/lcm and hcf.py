lst = [ ]
a = int(input('How many numbers: '))

for i in range(a):
        print('Enter any number: ', end = ' ')
        lst.append(int(input()))        

print(lst)

y = max(lst)
x = 0
def LCM(m, n):
    if m>n:
        num = m
    elif m<n:
        num = n
    while True:
        if num%m == 0 and num%n == 0:
            print('LCM is', num)
            break
        num+=1
        return LCM
        
o = lst[0]
p = lst[1]
lcm = LCM(o, p)

for i in range(2, len(lst)):
    q= LCM(lcm, lst[i])
            
print(q)

