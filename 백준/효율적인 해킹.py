import sys
from collections import deque

input = sys.stdin.readline


def bfs(s):
    q = deque([s])
    cnt = 0
    vis = [False]*(n+1)
    vis[s] = 1

    while q:
        x = q.popleft()

        for nx in graph[x]:
            if not vis[nx]:
                vis[nx] = True
                cnt += 1
                q.append(nx)

    return cnt


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

result = []
for i in range(1, n+1):
    result.append(bfs(i))

for i in range(len(result)):
    if max(result) == result[i]:
        print(i+1, end=' ')

