
try:

    firstNumber = int(input('Enter the first number: '))
    secondNumber = int(input('Enter the second number: '))

    if(firstNumber > secondNumber):
        print(f'{firstNumber} is greater than {secondNumber}')
    elif(firstNumber < secondNumber):
        print(f' {firstNumber} is smaller than {secondNumber}' )
    else:
        print(f'{firstNumber} is equal to {secondNumber}')

    # if (type (firstNumber, secondNumber) == int):
    #     print('You are awesome')

except:
    print('Only numbers are allowed, please input a valid number')



