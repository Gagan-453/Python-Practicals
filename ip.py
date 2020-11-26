sp = float(input("Enter selling price of object: "))
cp = float(input("Enter cost price of object: "))

if sp>cp:
    p = float(sp-cp)
    print(f'You had got profit and the profit is: ',p)
else:
    l = float(cp-sp)
    print(f'You had got loss and the loss is: ',l)