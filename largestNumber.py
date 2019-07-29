# A simple program
# It prompts for numerical input,
# Stores it and asks for more input,
# If none is provided, it prints the largest, smallest numbers of the set.
# If the numbers are equal, it prints it.
# It then prints the sorted and raw values in the set.
# Finally, it prints all the numbers in the set with their index


numberList = []

def askForNumber():
    # This try block ensures that only numberical inputs are accepted,
    # any other input is ignored, basically puting the else in an exception handle
    try:
        number = int(input('What is your number? \n'))
        numberList.append(number)
        additionalNumber()
    except:
        print('Please input a valid number')
        askForNumber()

def additionalNumber():
    moreNumbers = input('Do you want to add more numbers? y/n \n').lower()
    if moreNumbers == 'y':
        askForNumber()
    elif moreNumbers == 'n':
        largestNumber = None
        smallestNumber = None
        for number in numberList:
            if largestNumber is None:
                largestNumber = number
            elif number > largestNumber:
                largestNumber = number
            if smallestNumber is None:
                smallestNumber = number
            elif number < smallestNumber:
                smallestNumber = number
        if smallestNumber == largestNumber:
            print(f'smallest number {smallestNumber} and largest number {largestNumber} are equal')
        else:
            print(f'{smallestNumber} is the smallest number in the set')
            print(f'{largestNumber} is the largest number in the set')
        print(f'Original set is {numberList}')
        print('Sorted set is ', sorted(numberList, reverse=False))
        # getIndex(numberList)
        return
    else:
        print('Please input a valid response. y/n')
        additionalNumber()

# def getIndex(numberList):
#     index = 0
#     sortedNumberList = sorted(numberList, reverse=False)
#     while index < len(sortedNumberList):
#         print([index], sortedNumberList[index])
#         index += 1

askForNumber()