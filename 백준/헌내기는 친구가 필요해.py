import sys
from collections import deque

input = sys.stdin.readline


n, m = map(int, input().split())
graph = []

I = (0, 0)
for i in range(n):
    map_list = list(input())
    graph.append(map_list)
    if 'I' in map_list:
        for j in range(m):
            if map_list[j] == 'I':
                I = (i, j)


dr = [0, 0, 1, -1]
dc = [-1, 1, 0, 0]

q = deque([I])
P_cnt = 0
while q:
    r, c = q.popleft()

    for i in range(4):
        nr = dr[i] + r
        nc = dc[i] + c

        if nr >= n or nc >= m or nr < 0 or nc < 0:continue
        if graph[nr][nc] == 'X' or graph[nr][nc] == 'I':continue
        if graph[nr][nc] == 'P':
            P_cnt += 1
        graph[nr][nc] = 'I'
        q.append((nr, nc))

if P_cnt:
    print(P_cnt)
else:
    print('TT')