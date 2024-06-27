import sys

array=[]

K = int(sys.stdin.readline().rstrip())

for i in range(K):
    num = int(sys.stdin.readline().rstrip())
    if (num==0):
        array.pop()
    else:
        array.append(num)

print(sum(array))

