import sys
from collections import deque

input = sys.stdin.readline

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]


def bfs(x, y):
    q = deque([(x, y)])
    graph[x][y] = '.'

    cnt = 1
    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr >= n or nc >= m or nr < 0 or nc < 0:continue
            if graph[nr][nc] == '#':
                cnt += 1
                graph[nr][nc] = '.'
                q.append((nr, nc))

    return cnt


n, m, k = map(int, input().split())
graph = [['.']*m for _ in range(n)]

food = []
for _ in range(k):
    x, y = map(int, input().split())
    graph[x-1][y-1] = '#'
    food.append((x-1, y-1))

result = 0
for x, y in food:
    if graph[x][y] == '#':
        result = max(bfs(x, y), result)

print(result)