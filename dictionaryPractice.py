names = list()
nameOccurence = dict()
moreNames = True

while moreNames:
    name = input('Enter the name, type done when done: ')
    try:
        name != int(name)
        print('Please input a valid name!\n', 'Or \n')
        numberOfOccurenceInDictionary = input('Look for a name: ')
        # Search for a name in the dictionary and return how many times it appears
        print(f'{numberOfOccurenceInDictionary} appears \
{nameOccurence.get(numberOfOccurenceInDictionary, 0)} \
times in the list')
    except:
        if name == 'done':
            moreNames = False
            print(nameOccurence)
        else:
            names.append(name.title())
            for name in names:
                nameOccurence[name] = names.count(name)
