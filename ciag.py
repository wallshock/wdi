def a(x):
    a1 = x
    func = "(x%2)*(3*x+1)+(1-x%2)*x/2"
    step_count = 0
    while x != 1:
        x = eval(func)
        step_count += 1
    #end
    print(f"{a1} osiaga 1 po {step_count} operacjach")
    return step_count
#end
max = []

for i in range(2,10000):
    if not max: max = [i,a(i)]
    if a(i) > max[1]:
        max = [i,a(i)]

print(f"{max[0]} osiaga wartosc 1 po {max[1]} operacjach")



