import sys
input = sys.stdin.readline
N, M = map(int, input().split())
edges = []
distance = [sys.maxsize]*(N+1)   # 1~N까지 인덱스 사용

# 에지 데이터 저장
for i in range(M):
    start, end, time = map(int, input().split())
    edges.append((start, end, time))

distance[1] = 0  # 시작 도시
for _ in range(N-1):
    for start, end, time in edges:
        if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
            distance[end] = distance[start] + time

mCycle = False  # 음수 사이클 있는지 검사
for start, end, time in edges:
    if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
        mCycle = True  # 1번이라도 업데이트되면 음수 사이클 존재

if not mCycle:
    for i in range(2, N+1):
        if distance[i] != sys.maxsize:
            print(distance[i])
        else:  # 도착을 못한 경우
            print("-1")

else:  # 음수 사이클이 있는 경우
    print("-1")

