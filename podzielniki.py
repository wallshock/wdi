def podzielniki(n):
    lista = []
    for i in range(1,(n//2)+1):
        if n%i == 0: lista.append(i)
    lista.append(n)
    return lista
    
podzielniki(15)