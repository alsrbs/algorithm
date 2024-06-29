from collections import deque
import sys
input = sys.stdin.readline


def bfs(x, y):

    q = deque([(x, y)])
    graph[x][y] = '1'

    while q:
        r, c = q.popleft()

        for i in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr = r + i[0]
            nc = c + i[1]

            if 0 <= nr < n and 0 <= nc < m and graph[nr][nc] == '0':
                q.append((nr, nc))
                graph[nr][nc] = '1'

                if nr == n-1:
                    print('YES')
                    exit()


n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
start_point = []

for i in range(m):
    if graph[0][i] == '0':
        bfs(0, i)

print('NO')