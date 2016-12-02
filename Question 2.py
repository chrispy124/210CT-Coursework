def ZeroTrail(n): #declares the function
    fives = 0 

    for num in range ( 2, n+1):
        while ((num > 0) == (True)): #while 
            if num %5 == 0:
                fives +=1
                num = num/5
            else:
                break
    return fives
