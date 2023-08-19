def false_true(a,b,c):
    result = 0
    
    if a > 0:
            result +=1
    if b> 0:
            result +=1
    if c > 0:
            result +=1
    print(result == 2 )       
    return result == 2        



false_true(2, 4, -3) 

false_true(-4, 6, 8) 

false_true(4, -6, 9) 

false_true(-4, 6, 0)

false_true(-14, -3, -4)