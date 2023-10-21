from collections import deque
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
def BFS(x, y, h):
    q = deque()
    q.append((x, y))
    vis[x][y] = 1

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = dr[i] + r
            nc = dc[i] + c
            if nr>=n or nc>=n or nr<0 or nc<0:continue
            if vis[nr][nc]:continue
            if graph[nr][nc] <= h:continue
            vis[nr][nc] = True
            q.append((nr, nc))

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
min_num = min(map(min, graph))
max_num = max(map(max, graph))
safe_area = 1

for i in range(min_num, max_num):
    vis = [[False]*n for _ in range(n)]
    cnt = 0
    for j in range(n):
        for k in range(n):
            if vis[j][k] == 0 and graph[j][k] > i:
                cnt += 1;BFS(j, k, i)

    safe_area = max(safe_area, cnt)

print(safe_area)