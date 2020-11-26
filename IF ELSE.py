a = [" Playing"," Eating"," Reading"," Practicing"," Writing"]
w = str(input("What is your name??"))
x = str(input("What are you doing??"))
if x in a:
    z = str(input("Hello "+ w +","+" What are you"+x))
    print("OK, so you are", x, z)
else:
    print("hii", w)
print("Nice to meet you!!")