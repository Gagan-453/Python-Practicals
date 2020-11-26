x = [' Playing',' Reading',' Practicing', ' Eating',' Writing',' Cleaning',' Washing']
a = str(input("Hello, What's your name??"))
b = str(input("Hi!"+ a + " What are you doing??"))
if b in x:
    print("OK"+ a + " so you are"+ b)
    m = str(input("What are you" + b))
else:
    print("OK, nice")
if b == " Playing":
    print("I also like to play", m)
if b == " Reading":
    print("I also like to read", m)
if b == " Practicing":
    print("I also like to practise", m)
if b == " Eating":
    print("I also like to eat", m)
if b == " Writing":
    print("I am also interested in writing", m)
o = str(input("Are you enjoying your Summer Holidays??"+"(Yes/No)"))
if  o == "Yes" or "yes" or " Yes" or " yes":
    print("I am enjoying my Summer Vaction!!")
else:
    print("I am also not enjoying my Summer Vaction!!")
n = str(input("Are you attending the online classes everyday??"))
a1 = ['No','no',' No',' no']
a2 = ['Yes',' Yes','yes',' yes']
if n in a1:
    print("Very bad!! Attend Online Classes everyday")
if n in a2:
    print("OK, GOOD")
g = str(input("Do you want to calculate some mathematical operations??" + "(Yes or No)"))
v = ['Yes',' Yes','yes',' yes']
if g in v:
    h = str(input("Which operation would you like perform??" + "(Addition, Subtraction, Multiplication, Division)"))
if h == 'Addition' or 'addition' or ' Addition' or ' addition':
    num = int(input("How many numbers do you  want to add??"))
    total_sum = 0
for n in range(num):
    numbers = float(input("Enter any number:"))
    total_sum+= numbers
    print("Sum =", total_sum)
num7 = ['Subtraction' , 'subtraction' , ' Subtraction' , ' subtraction']
if h in num7:
    num1 = float(input("Enter the first number:"))
    num2 = float(input("Enter the second number:"))
    difference = num1-num2 
    print("DIFFERENCE =", difference)