def pierw(liczba,precyzja):
    a, b = 1, liczba
    pole = a*b
    while (abs(a-b)>precyzja):
        a = (a+b)/2
        b = pole/a
    #end
    return a
#end

num = 4
e = 0.000000001

print(pierw(num,e))