# FINDING FACTORIAL OF n NUMBERS in Python...

def factorial(n):
    prod = 1
    
    while n>=1:
        prod*=n
        n = n-1
        
    return prod

f = factorial(15)
print("Factorial", '=', f)