import sys
from collections import deque

input = sys.stdin.readline


dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]


def bfs(x, y):
    s, w = 0, 0
    q = deque([(x, y)])

    if yard[x][y] == 'v': w += 1
    elif yard[x][y] == 'o': s += 1

    yard[x][y] = '#'

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = dr[i] + r
            nc = dc[i] + c

            if nr >= n or nc >= m or nr < 0 or nc < 0: continue
            if yard[nr][nc] == '#': continue
            if yard[nr][nc] == 'o': s += 1
            if yard[nr][nc] == 'v': w += 1

            yard[nr][nc] = '#'
            q.append((nr, nc))

    if s > w:
        return s, 0
    else:
        return 0, w


n, m = map(int, input().split())
yard = [list(input()) for _ in range(n)]

sheep = 0
wolf = 0

for i in range(n):
    for j in range(m):
        if yard[i][j] != '#':
            s, w = bfs(i, j)
            sheep += s
            wolf += w

print(sheep, wolf)