# Request for file input
# Read/Stream the contents of the file
# Spit the read lines and push to the list
# Loop through the list, find unique words. For every repeated word, 
# the key is the word and the value is the number of times it appears in the list.
wordDict = dict()
wordsList = list()

newFile = input('Enter the file name: ')
fhand = open(newFile).read()
wordList = fhand.split()

for word in wordList:
    wordDict[word] = wordList.count(word)
print(wordDict)