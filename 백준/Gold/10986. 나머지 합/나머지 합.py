import sys
input = sys.stdin.readline
n, m = map(int, input().split())  # n은 수열의 개수, m은 나누어떨어져야 하는 수
A = list(map(int, input().split()))  # 원본 배열
S = [0] * n  # 합 배열
C = [0] * m  # 같은 나머지의 인덱스를 카운트하는 리스트, 나머지의 값은 0부터 m-1까지임.
answer = 0

S[0] = A[0]  # 초기화
for i in range(1, n):
    S[i] = S[i-1] + A[i]

for i in range(n):  # 0번 인덱스부터
    remainder = S[i] % m
    if remainder == 0:
        answer += 1  # 필요함
    C[remainder] += 1

for i in range(m):
    if C[i] > 1:  # 같은 나머지인 구간합이 2개 이상 있으면
        answer += (C[i]*(C[i]-1)  // 2*1)  # 중복조합 식

print(answer)