import sys
from collections import deque

input = sys.stdin.readline


def bfs(idx):
    q = deque(graph[idx])

    while q:
        x = q.popleft()
        if vis[x] == 1:continue
        vis[x] = 1
        q += graph[x]


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
vis = [0]*(N+1)


for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


result = 0
for i in range(1, N+1):
    if vis[i] == 0:
        result += 1
        vis[i] = 1
        bfs(i)

print(result)