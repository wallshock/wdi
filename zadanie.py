import math

def pierwsza(n):
    if n % 2 != 0:
        for i in range(3,int(math.sqrt(n))+1,2):
            if n%i == 0: return False
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if n%i == 0: return False
    
    return True

def sumapoteg(n):
    num_str = str(n)
    suma = 0
    for i in num_str:
        suma += int(i)**len(num_str)
    
    return suma
    
def znajdzpierwsze(ilosc_pierwszych):
    ilosc = 0
    liczba = 2
    while ilosc < ilosc_pierwszych:
        if pierwsza(liczba):
            if liczba == sumapoteg(liczba):
                print(liczba)
                ilosc += 1
                liczba += 1
            else:
                liczba += 1
        else:
            liczba += 1

znajdzpierwsze(7)


    
