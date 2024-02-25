import sys
from collections import deque

input =sys.stdin.readline


n = int(input())
r1, c1, r2, c2 = map(int, input().split())
board = [[0]*n for _ in range(n)]

dr = [-2, -2, 0, 0, 2, 2]
dc = [-1, 1, -2, 2, -1, 1]

q = deque([(r1, c1)])

while q:
    r, c = q.popleft()

    for i in range(6):
        nr = dr[i] + r
        nc = dc[i] + c

        if nr >= n or nc >= n or nr < 0 or nc < 0:continue
        if board[nr][nc] != 0:continue
        if (nr, nc) == (r2, c2):
            board[nr][nc] += board[r][c] + 1
            break
        board[nr][nc] += board[r][c] + 1
        q.append((nr, nc))


if board[r2][c2]:
    print(board[r2][c2])
else:
    print(-1)