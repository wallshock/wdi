def podzielniki(n):
    lista = []
    for i in range(1,(n//2)+1):
        if n%i == 0: lista.append(i)
    return lista

def friendUwU(doilu):
    n = 1
    while n<doilu:
        if n > sum(podzielniki(n)):
            if sum(podzielniki(sum(podzielniki(n)))) == n:
                print([n,sum(podzielniki(n))])
        n += 1

friendUwU(1000000)

            

            

