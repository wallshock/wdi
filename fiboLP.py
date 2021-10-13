def f(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a
#end

target = int(input("Podaj sume docelową= "))
sum = 0
Lpointer = 1
Rpointer = 1

while(sum!=target):
    if sum < target:
        sum += f(Rpointer)
        Rpointer += 1
    elif sum > target and Lpointer != Rpointer:
        sum -= f(Lpointer)
        Lpointer += 1
    else:
        print("Nie ma")
    #end
#end

for n in range(Lpointer,Rpointer):
    print(f(n))
#end
