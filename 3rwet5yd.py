from random import randint
x1=randint(0,9)
x10=randint(0,9)
x100 = randint(0, 9)
x1000 = randint(1, 9)
if x10==x1 or x10==x100 or x10==x1000:
    x10=randint(0,9)
if x100 == x1 or x100 == x10 or x100== x1000:
    x100 = randint(0, 9)
if x1000==x1 or x10==x100 or x10==x10:
    x1000=randint(0,9)
number = x1+x10*10+x100*100+x1000*1000

print(number)