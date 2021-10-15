import math

def pifinder(e):
    
    def f(e):
        
        if e == 0: return math.ceil(0.5 + (0.5)*math.sqrt(0.5))
        return round(math.sqrt(0.5) * math.sqrt(0.5+0.5*(math.sqrt(f(e-1)))),2)
    
    return 2/f(e)

print(pifinder(17))
    
    
