import random #imports the random sequence

def numberRandom(Sequence): #importing the random function
    output = [] #declaring the output

    while len(Sequence) > 0: #while the sequence is greater than 0
        number = random.randrange(len(Sequence))
        output.append(Sequence.pop(number)) #Adding the sequence to output

    return output #output the new random sequence


