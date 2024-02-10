import sys
from collections import deque

input = sys.stdin.readline

def bfs(v):
    q = deque([v])
    vis[v] = 1

    while q:
        v = q.popleft()
        if v == G:
            return result[G]
        for i in (v + U, v - D):
            if 0 < i <= F and not vis[i]:
                vis[i] = 1
                result[i] = result[v] + 1
                q.append(i)

    if result[G] == 0:
        return 'use the stairs'


F, S, G, U, D = map(int, input().split())
vis = [0] * (F + 1)
result = [0] * (F + 1)
print(bfs(S))
