from collections import deque
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
def BFS(x, y, target):
    cnt = 1
    graph[x][y] = 0
    q = deque()
    q.append((x, y))
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr>=n or nc>=m or nr<0 or nc<0:continue
            if target == graph[nr][nc]:
                q.append((nr, nc))
                graph[nr][nc] = 0
                cnt += 1
    return cnt*cnt

m, n = map(int, input().split())
graph = [list(input()) for _ in range(n)]
W_cnt = 0
B_cnt = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'B':
            B_cnt += BFS(i, j, graph[i][j])
        elif graph[i][j] == 'W':
            W_cnt += BFS(i, j, graph[i][j])
print(W_cnt, B_cnt)
