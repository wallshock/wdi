def pierw(liczba,precyzja):
    if liczba < 0:
        print("nie ma takiego pierw")
        quit()
    else:
        a, b, = 1, liczba
        obj = a*b*a
        while (abs(a-b)>precyzja):
            a = (a+b+a)/3
            b = obj/(a*a)
        #end
    return a
#end

num = 216
e = 0.000000000000001

print(pierw(num,e))