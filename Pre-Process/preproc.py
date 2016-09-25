fp=open("words.txt","r")
allWords=fp.read()
wordList=allWords.split("\n")
outputWordList=[]
for word in wordList:
	rev=word[::-1]
	final=""
	for character in rev:
		if character in ('a','e','i','o','u'):
			character*=2
		final+=character
	outputWordList.append(final)
for inp,target in zip(wordList,outputWordList):
	print inp,target
