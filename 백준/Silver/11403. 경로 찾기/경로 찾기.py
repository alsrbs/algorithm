from collections import deque
import sys

input = sys.stdin.readline


def BFS(s):
    vis = [0] * N
    z = []
    q = deque(a[s])
    while q:
        x = q.popleft()
        if vis[x] == 1:
            continue
        vis[x] = 1
        q += a[x]
        z.append(x)

    for i in z:
        graph[s][i] = 1


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

a = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            a[i].append(j)

for i in range(N):
    BFS(i)

for i in graph:
    print(*i)