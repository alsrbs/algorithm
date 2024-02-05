from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

Baby_Shark = deque()
for i in range(n):
    if 1 not in graph[i]:continue
    for j in range(m):
        if graph[i][j] == 1:
            Baby_Shark.append((i, j))

dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

result = 0

while Baby_Shark:
    r, c = Baby_Shark.popleft()

    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]

        if n <= nr or m <= nc or nr < 0 or nc < 0:continue
        if graph[nr][nc] != 0:continue

        graph[nr][nc] = graph[r][c] + 1
        Baby_Shark.append((nr, nc))
        result = max(result, graph[nr][nc])

print(result - 1)