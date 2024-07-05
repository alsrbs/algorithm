import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y):

    vis[x][y] = 1

    q = deque([(x, y)])
    while q:
        r, c = q.popleft()

        for i in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr = r + i[0]
            nc = c + i[1]

            if 0<=nr<n and 0<=nc<m and not vis[nr][nc] and abs(room[r][c] - room[nr][nc]) <= k:
                vis[nr][nc] = 1
                q.append((nr, nc))


n, m, k = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]
vis = [[0]*m for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(m):
        if not vis[i][j]:
            bfs(i, j)
            ans += 1

print(ans)