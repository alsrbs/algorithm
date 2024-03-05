import sys
from collections import deque

input = sys.stdin.readline


n, m = map(int, input().split())
barn = [[] for _ in range(n+1)]
vis = [0]*(n+1)

for i in range(m):
    a, b = map(int, input().split())
    barn[a].append(b)
    barn[b].append(a)

q = deque([1])
vis[1] = 1

while q:
    node = q.popleft()

    for i in barn[node]:
        if vis[i] == 0:
            vis[i] = vis[node] + 1
            q.append(i)

idx = max(vis)

print(vis.index(idx), idx - 1, vis.count(idx))
