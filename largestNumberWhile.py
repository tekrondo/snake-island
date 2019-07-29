# This programme takes the largestNumber.py code and shrinks it into while loop.
# It takes the if statements and replaces it with a while loop.

numberList = list()
largestNumber = None
smalestNumber = None
ask = True

while ask:
    numberInput = input('What is your number, type "done" when done: ')
    try:
        numberInput = int(numberInput)
        numberList.append(numberInput)
    except:
        if(numberInput.lower() == 'done'):
            numberList = sorted(numberList, reverse=False)
            smallestNumber = numberList[0]
            largestNumber = numberList[len(numberList)-1]
            print(numberList)
            if(smallestNumber == largestNumber):
                print('Numbers are equal')
            else:
                print(f'{smallestNumber} is the smallestNumber, and {largestNumber} is the largestNumber')
            ask = False
        else:
            print('Please input a valid entry')