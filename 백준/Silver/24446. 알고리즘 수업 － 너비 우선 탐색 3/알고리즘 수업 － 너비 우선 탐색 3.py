from collections import deque
import sys
input = sys.stdin.readline

def bfs(v):
    q = deque([v])
    visited[v] = 0

    while q:
        x = q.popleft()

        for i in graph[x]:
            if visited[i] == -1:
                visited[i] = visited[x] + 1
                q.append(i)


n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [-1] * (n+1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

bfs(r)

for i in range(1, n+1):
     print(visited[i])
