import sys
input = sys.stdin.readline
from queue import PriorityQueue

V, E = map(int, input().split())
K = int(input())
distance = [sys.maxsize]*(V+1)  # 0번 인덱스 사용하지 않음 / sys.maxsize 무한 값으로 초기화
visited = [False] * (V+1)  # 방문 여부 저장 리스트
myList = [[] for _ in range(V+1)]  # 에지 데이터 저장 인접 리스트
q = PriorityQueue()  # 다익스트라 우선순위 큐

for _ in range(E):  # 에지 개수만큼 반복
    u, v, w = map(int, input().split())
    myList[u].append((v, w))  # 무슨 타입으로 들어가는거지

q.put((0, K))  # 우선순위 큐에서, 앞의 값을 기준으로 정렬됨. 거리 배열  # 자동으로 거리가 최소인 노드를 선택하게 됨.
distance[K] = 0

while q.qsize() > 0:
    current = q.get()
    c_v = current[1]  # 현재 노드
    if visited[c_v]:  # 방문한 적 있으면
        continue
    visited[c_v] = True
    for tmp in myList[c_v]:  # c_v을 인덱스로 갖고있는, 이 노드와 연결되어있는 에지를 가져오게 됨
        next = tmp[0]  # v
        value = tmp[1]  # w
        if distance[next] > distance[c_v] + value:
            distance[next] = distance[c_v] + value
            q.put((distance[next], next))   # 업데이트 될 때만 큐에 넣기

for i in range(1, V+1):
    if visited[i]:
        print(distance[i])
    else:
        print("INF")  # 방문한 적 없음 = 시작 노드에서 도달할 수 없음