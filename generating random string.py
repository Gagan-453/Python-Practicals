import random
import string
digs = string.ascii_letters + string.digits + string.punctuation

password = ''.join((random.choice(digs)) for i in range(10))
print(password)