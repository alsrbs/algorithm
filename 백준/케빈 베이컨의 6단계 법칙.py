import sys
from collections import deque

input = sys.stdin.readline


def bfs(s):
    global result

    q = deque([s])
    vis = [0]*(N+1)

    while q:
        x = q.popleft()

        for j in friend[x]:
            if vis[j] == 0:
                vis[j] = vis[x] + 1
                q.append(j)

    if result[1] > sum(vis)-2:
        result[0] = s
        result[1] = sum(vis)-2


N, M = map(int, input().split())
friend = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())

    friend[a].append(b)
    friend[b].append(a)

result = [0, 99999]
for i in range(1, N+1):
    bfs(i)

print(result[0])