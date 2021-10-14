def nwd(a,b):
    while b > 0:
        r = a%b
        a = b
        b = r
    return a

def NWD(a,b,c):
    return nwd(a,nwd(b,c))

def nww(a,b):
    return (a*b)//nwd(a,b)

def NWW(a,b,c):
    return nww(a,nww(b,c))


print(NWW(25,85,150))

