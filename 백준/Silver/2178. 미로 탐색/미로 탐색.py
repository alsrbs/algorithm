import sys
from collections import deque

input = sys.stdin.readline


N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]

q = deque([(0, 0)])

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

while q:
    r, c = q.popleft()

    for i in range(4):
        nr = dr[i] + r
        nc = dc[i] + c

        if nr >= N or nc >= M or nr < 0 or nc < 0:continue
        if graph[nr][nc] != '1':continue

        graph[nr][nc] = int(graph[r][c]) + 1
        q.append((nr, nc))

print(graph[N-1][M-1])