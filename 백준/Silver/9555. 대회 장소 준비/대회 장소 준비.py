from collections import deque

dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

def find(a, b):
    x = arr[a][b]
    arr[a][b] = -1
    q = deque([(a, b)])
    cnt = 1
    while q:
        r, c = q.popleft()
        for idx in range(8):
            nr = dr[idx] + r
            nc = dc[idx] + c
            if nr<0 or nc<0 or nr>=n or nc>=m:continue
            if arr[nr][nc] == -1 or arr[nr][nc] != x:continue
            q.append((nr, nc))
            arr[nr][nc] = -1
            cnt += 1
    return cnt, x

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0:
                z, x = find(i, j)
                if z > 1:
                    result += [x]
    print(len(set(result)))