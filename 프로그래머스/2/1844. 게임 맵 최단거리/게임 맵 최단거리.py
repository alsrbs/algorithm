from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]

    q = deque([(0, 0)])

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr >= n or nc >= m or 0 > nr or 0 > nc:continue
            if maps[nr][nc] != 1:continue
            maps[nr][nc] = maps[r][c] + 1
            q.append((nr, nc))

    if maps[n-1][m-1] == 1:
        return -1
    else:
        return maps[n-1][m-1]
        
