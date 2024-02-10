import sys
from collections import deque

input = sys.stdin.readline


dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def BFS(x, y):
    q = deque([(x, y)])
    res = 1

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = dr[i] + r
            nc = dc[i] + c

            if nr >= n or nc >= m or nr < 0 or nc < 0:continue
            if nr == x and nc == y:continue
            if graph[nr][nc] != 1:continue
            res += 1
            graph[nr][nc] += 1
            q.append((nr, nc))

    return res


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            cnt += 1
            result = max(BFS(i, j), result)

print(cnt)
print(result)