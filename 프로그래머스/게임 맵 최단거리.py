from collections import deque

maps = [list(map(int, input().split())) for _ in range(5)]

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

q = deque([(0, 0)])

while q:
    r, c = q.popleft()

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr >= 5 or nc >= 5 or 0 > nr or 0 > nc:continue
        if maps[nr][nc] != 1:continue
        maps[nr][nc] = maps[r][c] + 1
        q.append((nr, nc))

print(maps[4][4])
