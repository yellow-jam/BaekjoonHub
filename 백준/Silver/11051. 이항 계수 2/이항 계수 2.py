import sys
input = sys.stdin.readline
N, K = map(int, input().split())
D = [[0 for j in range(N+1)]for i in range(N+1)]

for i in range(0, N+1):
    D[i][1] = i
    D[i][0] = 1
    D[i][i] = 1

for i in range(2, N+1):
    for j in range(1, i):
        D[i][j] = D[i-1][j] + D[i-1][j-1]
        D[i][j] = D[i][j] % 10007  # 문제 조건. 데이터가 커져서 값이 손상되기 전에 (나머지법칙에 따라서) 나눠줘야 됨

print(D[N][K])