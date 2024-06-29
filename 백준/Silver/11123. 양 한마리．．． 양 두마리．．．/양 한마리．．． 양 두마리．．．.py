from collections import deque
import sys
input =sys.stdin.readline


def bfs(x, y):

    q = deque([(x, y)])
    graph[x][y] = '.'

    while q:
        r, c = q.popleft()

        for i in [(-1, 0), (1, 0), (0, 1), (0, -1)]: # 상하좌우 확인
            nr = r + i[0]
            nc = c + i[1]

            if 0<=nr<h and 0<=nc<w and graph[nr][nc] == '#':    # 양이 있는 경우
                graph[nr][nc] = '.'
                q.append((nr, nc))

for t in range(int(input())):
    h, w = map(int, input().split())
    graph = [list(input()) for _ in range(h)]
    
    ans = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == '#':
                bfs(i, j)
                ans+=1
    
    print(ans)