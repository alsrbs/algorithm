import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y):
    cnt = 1
    graph[x][y] = '0'
    q = deque([(x, y)])

    while q:
        r, c = q.popleft()

        for i in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nr = r + i[0]
            nc = c + i[1]

            if 0<=nr<n and 0<=nc<n and graph[nr][nc] == '1':
                cnt += 1
                graph[nr][nc] = '0'
                q.append((nr, nc))

    return cnt


n = int(input())
graph = [list(input()) for _ in range(n)]

ans = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == '1':
            ans.append(bfs(i, j))

print(len(ans))
for i in sorted(ans):
    print(i)