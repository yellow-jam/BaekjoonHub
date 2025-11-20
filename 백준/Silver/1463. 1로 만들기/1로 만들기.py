import sys
input = sys.stdin.readline
N = int(input())
D = [0]*(N+1)

# 초기화
D[1] = 0

for i in range(2, N+1):
    D[i] = D[i-1] + 1
    if i % 2 == 0:
        D[i] = min(D[i], D[i//2] + 1)
    if i % 3 == 0:
        D[i] = min(D[i], D[i//3] + 1)
        
print(D[N])  # N을 1로 만드는 데 필요한 최소 연산 횟수