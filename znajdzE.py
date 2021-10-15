import math
def znajdzka(prec):
    e = 0
    n=0
    while n<prec:
        e+=1/math.factorial(n)
        round(e,3)
        n+=1
    return e

print(znajdzka(112))