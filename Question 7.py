def PrimeCheck (n, div = None) :
    if div is None:
        div = n-1
    while div >=2:
        if n % div ==0: 
            return False
        else: return PrimeCheck (n, div-1)

    else:
        return True
