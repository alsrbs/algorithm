from collections import deque
import sys

input = sys.stdin.readline


def bfs(y):
    q = deque([(0, y)])
    vis = [[0]*C for _ in range(R)]

    while q:
        r, c = q.popleft()

        for i in range(n):
            nr = r + move[i][0]
            nc = c + move[i][1]

            if r<=nr<R and 0<=nc<C and graph[nr][nc] == 1 and vis[nr][nc] == 0:
                q.append((nr, nc))
                vis[nr][nc] += vis[r][c]+1
                if nr == R-1:
                    result.append(vis[nr][nc])
                    return


R, C = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]
n = int(input())
move = [tuple(map(int, input().split())) for _ in range(n)]
result = []

for i in range(C):
    if graph[0][i] == 1:
        bfs(i)

if result:
    print(min(result))
else:
    print(-1)
