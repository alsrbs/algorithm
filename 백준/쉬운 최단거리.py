from collections import deque
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
def BFS(x, y):
    graph[x][y] = 0
    vis[x][y] = True
    q = deque()
    q.append((x, y))
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr>=n or nc>=m or nr<0 or nc<0:continue
            if graph[nr][nc] and not vis[nr][nc]:
                q.append((nr, nc))
                graph[nr][nc] = graph[r][c] + 1
                vis[nr][nc] = True

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
vis = [[False]*m for _ in range(n)]
x, y = -1, -1

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            x, y = i, j
            break
    if x >= 0:break

BFS(x, y)
for i in range(n):
    for j in range(m):
        if not vis[i][j] and graph[i][j] == 1:
            graph[i][j] = -1
for i in range(n):
    print(*graph[i])