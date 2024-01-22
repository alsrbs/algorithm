from collections import deque

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def BFS():

    q = deque([])
    q.append((500, 500))

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = dr[i] + r
            nc = dc[i] + c

            if nr > 1000 or nc > 1000 or nr < 0 or nc < 0:
                continue

            if arr[nr][nc] == 'B':
                return arr[r][c] + 1

            if arr[nr][nc] == 'M' or arr[nr][nc] == '*':
                continue

            if arr[nr][nc] == 0:
                q.append((nr, nc))
                arr[nr][nc] = arr[r][c] + 1


A, B, C = map(int, input().split())
arr = [[0]*10001for _ in range(1001)]

arr[A+500][B+500] = 'B'
for _ in range(C):
    x, y = map(int, input().split())
    arr[x+500][y+500] = 'M'

print(BFS())
