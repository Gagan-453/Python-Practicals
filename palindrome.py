# Checking whether an input is a palindrome
a = input('Enter something: ')
m = a.lower()
m = m.strip()
m = m.replace(' ', '')

check = ''
for i in range(1, len(m)+1):
    check+=m[-i]

if m == check:
    print(a, 'is a palindrome')
else:
    print(a, 'is not a palindrome') 

# OR

a = input('Enter something: ')
a = a.lower()
a = a.strip()

reverse = a[::-1]

if a == reverse:
    print(a, 'is a palindrome')
else:
    print(a, 'is not a palindrome') 