def fibo(n):
    a,b = 1, 1
    for i in range(0,n-1):
        a,b = b, a+b
    #end
    return a
#end

target = int(input("Podaj liczbe naturalna= "))
n = 1
while(fibo(n)*fibo(n+1)<=target):
    if fibo(n)*fibo(n+1) == target:
        print(f"{target} to iloczyn liczb {fibo(n)} oraz {fibo(n+1)} ciągu fibonacciego")
        quit()
    else:
        n += 1

print("nie ma takiej pary kolejnych lcizb ciagu fibonacceigo")

    
