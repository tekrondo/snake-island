wordList = list()
wordDict = dict()
maxCount = dict()

newFile = input('Enter the file name: ')
with open(newFile) as f:
    wordList = f.read().rstrip().split()

# Learnt about dictionar comprehension, rather than looping through a dict(), 
# this is a more pythonic way of doing this.
wordDict = { word : wordList.count(word) for word in wordList }

# Get key with the most appearances
max = max(wordDict, key=wordDict.get)

# Find the value of the key in the dictionary [This should not work but it does]
maxCount[max] = wordDict[max]
print(maxCount)