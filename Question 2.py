def ZeroTrail(n): #declares the function
    fives = 0 

    for num in range ( 2, n+1):
        while ((num > 0) == (True)): #while num being bigger than 0 is true
            if num %5 == 0: #if num divided by 5 is equal to 0
                fives +=1
                num = num/5 
            else:
                break #breaks the while loop
    return fives
