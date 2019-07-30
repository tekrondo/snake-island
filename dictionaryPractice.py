names = list()
nameOccurence = dict()
moreNames = True

while moreNames:
    name = input('Enter the name, type done when done: ')
    try:
        name != int(name)
        print('Please input a valid name!')
    except:
        if name == 'done':
            moreNames = False
            print(nameOccurence)
        else:
            names.append(name.title())
            for name in names:
                nameOccurence[name] = names.count(name)
