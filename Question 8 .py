def VowelRemove(v): #Creates the function
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O','U') #list of vowels that shouldnt be in the word
    for e in v: #checks for elements (vowels) within the string
      if e in vowels: #if there is an element it 
        v = v.replace(e,"") #changes it to a blank space

    return v #return the result
