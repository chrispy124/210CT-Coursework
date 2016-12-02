def WordRev (Words) : #defines the function
    WordsL = len(Words) #variable is equal too length of 'words'
    if WordsL == 1:
        return Words #if only one word is given then it will only print that word
    else:
        return [Words[-1]]+ WordRev(Words[:-1]) #calls the function to reorder

ListInput = ["this", "is", "awesome"] #list for reverse

print (WordRev (ListInput)) #Print the words swapped round
