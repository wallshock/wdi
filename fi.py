def fib(n):
    a,b =1, 1
    for i in range(n-1):
        a,b = b, a+b
    return a

def proporcja(e):
    return fib(2*e)/fib(2*e-1)

e = 0
while e<1000:
    print(proporcja(e))
    e += 1

