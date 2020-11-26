str = input('Enter a string: ')
str = str.lower()
str = str.strip()

if 'gagan' in str:
    print('"Gagan" is present')
else:
    print('"Gagan" is not present')


for i in range(len(str)):
    if str[i] == 'g' and str[i+1] == 'a' and str[i+2] == 'g' and str[i+3] == 'a' and str[i+4] == 'n':
        print('Gagan')