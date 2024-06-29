from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]

q = deque([(0, 0)])

while q:
    r, c = q.popleft()

    for i in [(0, 1), (1, 0)]:
        nr = r + i[0]
        nc = c + i[1]

        if 0<=nr<m and 0<=nc<n and graph[nr][nc] == 1:
            graph[nr][nc] += graph[r][c]
            q.append((nr, nc))

if graph[m-1][n-1]+1 == n+m:
    print('Yes')
else:
    print('No')
