import sys

array = [0 for i in range(26)]

N = int(sys.stdin.readline().rstrip())

for i in range(N):
    array[ord(sys.stdin.readline()[0])-97]+=1

flag=False
for i in range(26):
    if array[i]>=5:
        print(chr(i+97), end="")
        flag=True
if flag==False:
    print("PREDAJA")