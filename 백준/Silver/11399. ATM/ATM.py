N = int(input())
A = list(map(int, input().split()))
S = [0]*N

# 삽입정렬

for i in range (1, N):
    insert_point = i   # 0~i 범위의 값을 가짐
    insert_value = A[i]
    for j in range(i-1, -1, -1):
        if A[j] < A[i]:  # 지금 탐색하는 애가 나보다 작으면
            insert_point = j+1  # 그것의 뒤에 삽입
            break
        if j == 0:  # 예외처리: 어떤 값이 맨 앞까지 왔다면
            insert_point = 0  # 그것이 최솟값이므로 맨 앞으로

    for j in range(i, insert_point, -1):  # 삽입하기 전에 그 사이의 값들을 모두 배열의 한칸씩 뒤로 밀어야 함
        A[j] = A[j-1]
    A[insert_point] = insert_value   # 삽입


# 합 배열 만들기
'''
S[0] = A[0]

for i in range(1, N):
    S[i] = S[i-1] + A[i]

sum = 0
for i in range(0, N):
    sum += S[i]
'''

# 축약
S[0] = A[0]
sum = S[0]
for i in range(1, N):
    S[i] = S[i - 1] + A[i]
    sum += S[i]

print(sum)
