from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    global ans

    vis = [[0]*m for _ in range(n)]  # 체크 리스트
    q = deque([(x, y)])
    vis[x][y] = 1

    while q:
        r, c = q.popleft()

        for i in [(-1, 0), (1, 0), (0, 1), (0, -1)]:  # 상하좌우 탐색
            nr = r + i[0]
            nc = c + i[1]

            if 0<=nr<n and 0<=nc<m and treasureMap[nr][nc] == 'L' and vis[nr][nc] == 0:  # 갈수있는 경우
                vis[nr][nc] = vis[r][c] + 1
                q.append((nr, nc))

        if not q:
            ans = max(ans, vis[r][c]-1)



n, m = map(int, input().split())
treasureMap = [list(input()) for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(m):
        if treasureMap[i][j] == 'L':  # 육지인 경우 확인
            bfs(i, j)

print(ans)