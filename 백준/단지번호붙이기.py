from collections import  deque
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def BFS(x, y):
    q = deque([(x, y)])
    graph[x][y] = 0
    count = 1
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = dr[i] + r
            nc = dc[i] + c
            if nr < 0 or nc < 0 or nr >= n or nc >= n:continue
            if graph[nr][nc] == 1:
                q.append((nr, nc))
                graph[nr][nc] = 0
                count += 1
    return count

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
cnt = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt += [BFS(i, j)]
print(len(cnt))
for i in sorted(cnt):
    print(i)
