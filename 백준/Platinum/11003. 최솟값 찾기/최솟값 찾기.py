import sys
from collections import deque

input = sys.stdin.readline

N, L = map(int, input().split())
mydequeue = deque();
now = list(map(int, input().split()))

for i in range(N):
    # 1. 나보다 큰 데이터 삭제
    while mydequeue and mydequeue[-1][0] > now[i]:  # 덱의 제일 끝에 있는(-1) 값(0)
        mydequeue.pop()
    mydequeue.append((now[i], i))  # 값과 인덱스
    # 2. 슬라이딩 윈도우 벗어난 데이터 삭제
    # 윈도우 범위를 벗어나면
    if mydequeue[0][1] <= i-L: # 덱의 맨앞(0)의 인덱스(1)
        mydequeue.popleft()
    print(mydequeue[0][0], end=' ')