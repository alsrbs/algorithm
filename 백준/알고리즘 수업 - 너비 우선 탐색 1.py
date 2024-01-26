from collections import deque
import sys
input = sys.stdin.readline

def bfs(v):
    global count

    q = deque([v])
    visited[v] = 1

    while q:
        x = q.popleft()
        graph[x].sort()

        for i in graph[x]:
            if not visited[i]:
                count += 1
                visited[i] = count
                q.append(i)


n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n + 1)
count = 1

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

bfs(r)

for i in visited[1:]:
    print(i)
