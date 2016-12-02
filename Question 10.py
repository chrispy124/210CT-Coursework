def SequenceMax(Input):
    temporary = []
    num = 0
    last = []

    for i in range(len(Input)-1):
        if i == 0:
            temporary.append(Input[i])

        else:
            if Input[i] >= Input[i-1]:
                temporary.append(Input[i])

            if Input[i] < Input[i-1]:
                last.append(temporary)

                temporary = []
                temporary.append(Input[i])

    last.append(temporary)

    for i in range(len(last)):
        if i == 0:
            num = len(last[i])
            Input = last[i]
        else:
            if len(final[i]) > num:
                num = len(last[i])
                Input = last[i]
        return str(Input)

Input = [6, 7, 8, 9, 10, 5, 7, 3, 6, 4, 3, 6]

print(SequenceMax(Input))
                
