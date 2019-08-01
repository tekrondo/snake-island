# Request for file input
# Read/Stream the contents of the file
# Spit the read lines and push to the list
# Loop through the list, find unique words. For every repeated word, 
# the key is the word and the value is the number of times it appears in the list.
wordDict = dict()
wordsList = list()
maxDict = dict()


newFile = input('Enter the file name: ')
fhand = open(newFile).read()
wordList = fhand.rstrip().split()

for word in wordList:
    wordDict[word] = wordList.count(word)

# This section finds the word that appears the most in the dictionary 
# and prints it. It gets the key using the max method, then assigns 
# the value by calling the key on the maxDict.

key = max(wordDict)
maxDict[key] = wordDict.get(key)

print(maxDict)