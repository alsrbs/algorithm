import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y, count):
    graph[x][y] = 1
    q = deque([(x, y, count)])

    while q:
        r, c, cnt = q.popleft()

        for i in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr = r + i[0]
            nc = c + i[1]

            if 0<=nr<n and 0<=nc<m and graph[nr][nc] != 1:
                if graph[nr][nc] in [3, 4, 5]:
                    print('TAK')
                    print(cnt+1)
                    return

                graph[nr][nc] = 1
                q.append((nr, nc, cnt + 1))

    print('NIE')


n, m = map(int, input().split())
graph = [list(map(int, list(input().strip()))) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            bfs(i, j, 0)
