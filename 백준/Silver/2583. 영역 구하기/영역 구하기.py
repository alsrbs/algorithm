import sys
from collections import deque

input = sys.stdin.readline


dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def BFS(x, y):
    q = deque([(x, y)])
    res = 1
    graph[x][y] = 2
    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr >= N or nc >= M or nr < 0 or nc < 0:continue
            if graph[nr][nc] != 1:continue

            q.append((nr, nc))
            graph[nr][nc] += 1
            res += 1

    return res


N, M, K = map(int, input().split())
graph = [[1]*M for _ in range(N)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(min(y1, y2), max(y1, y2)):
        for j in range(min(x1, x2), max(x1, x2)):
            graph[i][j] = 0

cnt = 0
result = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            cnt += 1
            result.append(BFS(i, j))

print(cnt)
print(*sorted(result))