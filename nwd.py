def nwd(a,b):
    while b > 0:
        r = a%b
        a = b
        b = r
    return a

def NWD(a,b,c):
    return nwd(a,nwd(b,c))

print(NWD(50,75,150))
