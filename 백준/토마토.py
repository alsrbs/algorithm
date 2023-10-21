from collections import deque
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
def BFS():
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = dr[i] + r
            nc = dc[i] + c
            if nr>=M or nc>=N or nr<0 or nc<0:continue
            if graph[nr][nc] == 0:
                graph[nr][nc] = graph[r][c] + 1
                q.append((nr, nc))

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
day = 0
q = deque()
for i in range(M):
    for j in range(N):
        if graph[i][j] == 1:
            q.append((i, j))
BFS()
for i in range(M):
    if 0 in graph[i]:
        print(-1)
        exit()
    day = max(day, max(graph[i]))
print(day-1)