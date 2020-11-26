a = input('Enter something: ')
a = a.lower()
a = a.strip()

g = []
check = ''
for i in range(1, len(a)+1):
    check+=a[-i]

print(check)
if a == check:
    print(a, 'is a palindrome')
else:
    print(a, 'is not a palindrome') 