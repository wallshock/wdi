def podzielniki(n):
    for i in range(2,(n//2)+1):
        if n%i == 0: print(i)
    
podzielniki(1222560)