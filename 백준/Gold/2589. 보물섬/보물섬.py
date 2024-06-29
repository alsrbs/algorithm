from collections import deque
import sys, copy
input = sys.stdin.readline

def bfs(x, y):
    global ans

    vis = [[0]*m for _ in range(n)]
    q = deque([(x, y)])
    vis[x][y] = 1

    while q:
        r, c = q.popleft()

        for i in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nr = r + i[0]
            nc = c + i[1]

            if 0<=nr<n and 0<=nc<m and treasureMap[nr][nc] == 'L' and vis[nr][nc] == 0:
                vis[nr][nc] = vis[r][c] + 1
                q.append((nr, nc))

        if not q:
            ans = max(ans, vis[r][c]-1)



n, m = map(int, input().split())
treasureMap = [list(input()) for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(m):
        if treasureMap[i][j] == 'L':
            bfs(i, j)

print(ans)