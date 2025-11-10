import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = [[0] * (n+1)]   # 문제 특, 배열 인덱스를 0 대신 1부터 사용!
D = [[0]*(n+1) for _ in range(n+1)]

for i in range(n):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)


for i in range(1, n+1):
    for j in range(1, n+1):  # 배열 인덱스가 1부터 시작
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]
'''

for i in range(n+1):
    D[i][1] = D[i-1][1] + A[i][1]
for j in range(n + 1):
    D[1][j] = D[1][j-1] + A[1][j]

for i in range(2, n+1):
    for j in range(2, n+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]
'''

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)
