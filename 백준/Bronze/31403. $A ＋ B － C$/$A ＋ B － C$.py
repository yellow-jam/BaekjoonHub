import sys
A = int(sys.stdin.readline())
B = sys.stdin.readline()
C = int(sys.stdin.readline())

s = len(B)-1
B = int(B)

print(A+B-C)
print(A*(10**s) + B - C)
