from collections import deque
dr = [-2, -2, -1, 1, 2, 2, 1, -1]
dc = [-1, 1, 2, 2, 1, -1, -2, -2]

def bfs(s):
    q = deque([s])
    while True:
        r, c = q.popleft()
        if [r, c] == target:return vis[r][c]
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr>=n or nc>= n or nr<0 or nc<0:continue
            if vis[nr][nc]: continue
            vis[nr][nc] = vis[r][c] + 1
            q.append([nr, nc])

t = int(input())
for _ in range(t):
    n = int(input())
    vis = [[0]*n for i in range(n)]
    s = map(int, input().split())
    target = list(map(int, input().split()))
    print(bfs(s))
