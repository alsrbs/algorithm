from collections import deque
import sys

input = sys.stdin.readline


dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def bfs(x, y):
    dic_count = {'k': 0, 'v': 0, '.': 0}
    dic_count[graph[x][y]] += 1
    graph[x][y] = '#'
    q = deque([(x, y)])

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0<=nr<n and 0<=nc<m:
                if graph[nr][nc] == '#':continue
                dic_count[graph[nr][nc]] += 1
                graph[nr][nc] = '#'
                q.append((nr, nc))

    if dic_count['v'] >= dic_count['k']:
        d_count['v'] += dic_count['v']
    else:
        d_count['k'] += dic_count['k']


n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
d_count = {'k': 0, 'v': 0}
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'v' or graph[i][j] == 'k':
            bfs(i, j)

print(d_count['k'], d_count['v'])