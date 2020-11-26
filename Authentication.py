dict = {'gaganreddy2705@gmail.com' : 'I won\'t tell', 'gaganadithyareddy9@gmail.com' : 'ygar27', 'abc2@gmail.com' : '4537g', 'adi27@gmail.com' : 'gar453', 'abc123@gmail.com' : 'cba432', 'yrar0224@gmail.com' : 'mvr@321'}

print('Enter Gmail ID to login:', end = ' ')
n = input()

if n in dict.keys():
    login = input('Enter password: ')
else:
    print('Authentication failed')
 
get_password = dict.get(n)
try:
    if login == get_password:
        print('Congragulations\nLogin Successful')
    else:
        print('Authentication Failed')
        print('Wrong password entered')
except NameError:
    print('Check your Mail ID and try again')