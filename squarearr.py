def pierw(num):
    sum, n =0, 0
    
    while sum<=num:
        sum += 2*n + 1
        n += 1
    #end
    return n-1
#end

print(pierw(5))