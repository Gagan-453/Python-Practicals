with open('phonebook.dat', 'wb') as f:
    n = int(input('How many entries? '))
    
    for i in range(n):
        name = input('Enter name: ')
        phone = input('Enter phone number: ')
        name = name.encode()
        phone = phone.encode()
        f.write(name+phone)