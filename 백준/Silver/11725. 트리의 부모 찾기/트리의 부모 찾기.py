import sys
sys.setrecursionlimit(10**6)  # 파이썬 재귀 한계 늘리는 설정 (기본 10^3)
input = sys.stdin.readline

N = int(input())
visited = [False]*(N+1)
tree = [[] for _ in range(N+1)]
answer = [0]*(N+1)

for _ in range(1, N):  # 인접 리스트로 저장
    n1, n2 = map(int, input().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

# DFS
def DFS(number):
    visited[number] = True
    for i in tree[number]:  # 노드와 연결된 다른 노드, 자식 노드들에 대해서
        if not visited[i]:  # 미방문 노드이면
            answer[i] = number  # 이번에 방문할 노드(i)는 현재(number)가 부모 노드임
            DFS(i)
DFS(1)  # 1(root)부터 시작

for i in range(2, N+1):
    print(answer[i])


