import sys
from collections import deque

input = sys.stdin.readline


N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

vis = [0]*(N+1)
q = deque([1])

while q:
    x = q.popleft()

    for i in graph[x]:
        if vis[i] == 0:
            vis[i] = x
            q.append(i)

for i in range(2, N+1):
    print(vis[i])
