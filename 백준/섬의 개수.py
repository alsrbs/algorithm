import sys
from collections import deque

input = sys.stdin.readline


dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]


def bfs(x, y):
    q = deque([(x, y)])

    while q:
        r, c = q.popleft()

        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr >= h or nc >= w or nr < 0 or nc < 0:continue
            if graph[nr][nc] != 1:continue

            graph[nr][nc] += 1
            q.append((nr, nc))


while True:
    w, h = map(int, input().split())

    if w == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(h)]

    result = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                result += 1
                graph[i][j] += 1
                bfs(i, j)

    print(result)