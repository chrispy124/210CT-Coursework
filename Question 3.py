import math #Imports the math module

def PerfectSquare(p): #defines the function for perfect square
    if p >= 1: #if p is greater than 1 then it will run the code below
        num = math.sqrt(p) #varable takes the square root of p
        num = int (num)
        print (num) #Prints Number

    else:
        print ("Number Should be 1 or above") #Lets user know if number is below 1
    
