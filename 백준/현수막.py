from collections import deque
import sys

input = sys.stdin.readline


dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

def bfs(x, y):
    q = deque([(x, y)])
    graph[x][y] = '*'

    while q:
        r, c = q.popleft()

        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0<=nr<n and 0<=nc<m and graph[nr][nc] == 1:
                graph[nr][nc] = '*'
                q.append((nr, nc))


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            result += 1
            bfs(i, j)

print(result)