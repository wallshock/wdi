def bisekcja(funkcja,a,b,e):
    def f(x):
        f = eval(funkcja)
        return f
    #end

    error = abs(a-b)

    while error > e:
        mid = (a+b)/2
        if f(a)*f(b) > 0:
            print("zły przedział")
            print(f(b))
            quit()
        #end

        elif f(mid)*f(b) < 0:
            a = mid
            error = abs(a-b)
        #end

        elif f(mid)*f(a) < 0:
            b = mid
            error = abs(a-b)
        else:
            print("cos poszlo nie tak")
            quit()
        #end
    
    print(f"Miejsce zerowe pomiedzy {a} i {b}, błąd wynosi {error}")

bisekcja("pow(x,x)-2020",0,5,0.001)