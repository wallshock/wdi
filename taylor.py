import math

def cosinus(x,prec):
    cos = 0
    for i in range(prec):
        sign = ((-1.0)**i)/math.factorial(2.0*i)
        pi = math.pi
        degrees = x*(pi/180.0)
        cos += sign*(degrees**(2.0*i))
    return cos


print(cosinus(60,5))