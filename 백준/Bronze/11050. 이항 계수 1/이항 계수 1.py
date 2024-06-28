a, b = map(int, input().split())

N, K = 1, 1
for i in range(0, b):
    N*=(a-i)
for i in range(1, b+1):
    K*=i

print(int(N/K))