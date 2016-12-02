def BSearch(List, Number1, Number2): #3 Arguments for function 
    num1 = 0
    num2 = len(List)-1 
    FoundNum = False

    while num1 <= num2 and not FoundNum:
        middle = (num1 + num2) //2
        if List[middle] > Number1 and List [middle] < Number2:
            FoundNum = True #Returns if number is found

        else: #IF number is not found then use this code
            if Number1< List[middle]:
                num2 = middle - 1
            else:
                num1 = middle + 1 
    return FoundNum


print(BSearch([2,3,5,7,9,13],10,14))
