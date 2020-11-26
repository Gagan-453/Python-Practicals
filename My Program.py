from numpy import *
sum = 0
count = 0
lst = [ ]

n = input('Hi! What is your name? ')
print('Hi', n, 'nice to meet you')
wrud = input('What are you doing? ')
if 'ing' in wrud:
    n = wrud.replace('ing', '')
print('I also like to', n, '!!')

m = input('Still...How about performing maths (Yes/No)? ')
m = m.strip()
m = m.lower()

if m == 'yes':
    o = input('Enter operation name (Addition, Subtraction, Multiplication, Division): ')
    o = o.strip()
    o = o.lower()

    if o == 'addition':
        c = int(input('How many numbers do you want to add? '))
        for i in range(c):
            num = int(input('Enter a number: '))
            sum+=num
        print('The sum is: ', sum)
    elif o == 'subtraction':
        s1 = int(input('Enter 1st number: '))
        s2 = int(input('Enter 2nd number: '))
        print('Difference between', s1, 'and', s2, 'is', s1-s2)
    elif o == 'multiplication':
        x = int(input('How many numbers do you want to multiply? '))
        for i in range(x):
            n = int(input('Enter a number: '))
            lst.append(n)
        for i in range(len(lst)):
            arr = array(lst)
        print('Product of all numbers is: ', prod(arr))
    elif o == 'division':
        d1 = int(input('Enter 1st number: '))
        d2 = int(input('Enter 2nd number: '))
        print('Quotient of numbers is: ', d1/d2)
else:
    b = input('OK! Shall I break off? ')
    b = b.lower()
    b = b.strip()
        
    if b == 'no':
        print('Then...what can I do for you? ')
        j = input('Shall I tell a joke (Yes/No)? ')
        j = j.lower()
        j = j.strip()
        if j == 'yes':
            print('The best first: What is white and flies up?\nA retarded snowflake')
            print('--------------------------------------------------------------------------------------')
            print('The best first: Doctor to Mrs. Spew: “Is your daughter always stuttering like that?”\nMrs. Spew shakes her head: “No, only when she wants to say something.”')
            print('Hope they are nice!!')
        else:
            print('OK bye for now')
