import sys

wordList = []
N = int(sys.stdin.readline().strip())
for i in range(N):
    wordList.append(sys.stdin.readline().strip())

wordList = list(set(wordList))

wordList.sort()
wordList.sort(key=len)

for i in wordList:
    print(i)
