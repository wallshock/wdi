def podzielniki(n):
    lista = []
    for i in range(1,(n//2)+1):
        if n%i == 0: lista.append(i)
    return lista

def doskonala(n):
    if sum(podzielniki(n)) == n: return True
    return False

print(doskonala(10))
