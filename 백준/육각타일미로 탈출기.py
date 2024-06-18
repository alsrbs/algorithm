from collections import deque
import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[1]*m for _ in range(n)]
for _ in range(k):
    y, x = map(int, input().split())
    graph[y][x] = 0

q = deque([(0, 0)])

dr = [[-1, -1, 0, 1, 1, 0], [-1, -1, 0, 1, 1, 0]]
dc = [[-1, 0, 1, 0, -1, -1], [0, 1, 1, 1, 0, -1]]

while q:
    r, c = q.popleft()
    for i in range(6):
        nr = r + dr[r%2][i]
        nc = c + dc[r%2][i]

        if 0<=nr<n and 0<=nc<m and graph[nr][nc] == 1:
            graph[nr][nc] += graph[r][c]
            q.append((nr, nc))


if graph[n-1][m-1] == 1:
    print(-1)
else:
    print(graph[n-1][m-1]-1)
