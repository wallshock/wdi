import math
def argeo(a,b):
    ciaga = a
    ciagb = b
    e = 0.00001 #precyzja

    left = 0
    right = 1
    while abs(left - right) > e:
        left = math.sqrt(ciaga*ciagb)
        right = (ciaga+ciagb)/2
        ciaga = left
        ciagb = right
        
    print(f"{ciaga} ----- {ciagb}")
    

argeo(8,10)


    