from collections import deque

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def BFS(i, j):
    q = deque([(i, j)])
    cnt = 0
    cnt += int(maps[i][j])
    maps[i][j] = 'X'

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < w and 0 <= nc < l and maps[nr][nc] != 'X':
                cnt += int(maps[nr][nc])
                maps[nr][nc] = 'X'
                q.append((nr, nc))

    return cnt


maps = ["X591X", "X1X5X", "X231X", "1XXX1"]
maps = [list(row) for row in maps]

result = []
w = len(maps)
l = len(maps[0])


for i in range(w):
    for j in range(l):
        if maps[i][j] != 'X':
            result.append(BFS(i, j))

print(result)
