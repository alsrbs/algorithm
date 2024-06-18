from collections import deque
import sys

input = sys.stdin.readline


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
vis = [[0] * n for _ in range(n)]
q = deque([(0, 0)])

dr = [0, 1]
dc = [1, 0]

while q:
    r, c = q.popleft()

    for i in range(2):
        nr = r + (dr[i]*graph[r][c])
        nc = c + (dc[i]*graph[r][c])

        if 0<=nr<n and 0<=nc<n and not vis[nr][nc]:
            q.append((nr, nc))
            vis[nr][nc] = 1
            if (nr, nc) == (n-1, n-1):
                print('HaruHaru')
                exit()

print('Hing')