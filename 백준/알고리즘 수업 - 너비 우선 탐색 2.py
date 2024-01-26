from collections import deque
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
count = 1

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

q = deque([r])
visited[r] = 1

while q:
    x = q.popleft()

    for i in sorted(graph[x], reverse=True):
        if visited[i]:continue
        count += 1
        visited[i] = count
        q.append(i)

for i in range(1, n+1):
    print(visited[i])