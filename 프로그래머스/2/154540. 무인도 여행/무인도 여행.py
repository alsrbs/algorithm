from collections import deque

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def BFS(i, j, maps):
    global w, l, result
    
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

    result.append(cnt)


def solution(maps):
    global w, l, result
    
    maps = [list(row) for row in maps]
    result = []
    w, l = len(maps), len(maps[0])

    for i in range(w):
        for j in range(l):
            if maps[i][j] != 'X':
                BFS(i, j, maps)
    if result:
        return sorted(result)
    else:
        return [-1]