# 크루스칼 알고리즘
import sys
import heapq

input = sys.stdin.readline



V, E = map(int, input().split())
parent = [i for i in range(V + 1)]
l = []

def find_parent(x):
    if parent[x] == x:
        return x
    else:
        y = find_parent(parent[x])
        parent[x] = y
        return y

def union_parent(a, b):
    parent_a = find_parent(a)
    parent_b = find_parent(b)

    if parent_a > parent_b:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b

for _ in range(E):
    a, b, c = map(int, input().split())
    heapq.heappush(l, (c, a, b))

result = 0

while l:
    cost, a, b = heapq.heappop(l)

    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        result += cost

print(result)