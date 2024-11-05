from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())  # n 체스판의 크기 m 상대편 말의 수
x, y = map(int, input().split())  # 나이트의 위치

arr = [n*[0] for _ in range(n)]

q = deque([(x-1, y-1)])

dr = [-2, -2, -1, -1, 1, 1, 2, 2]
dc = [-1, 1, -2, 2, -2, 2, -1, 1]

while q:
    r, c = q.popleft()

    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0 or nr >= n or nc < 0 or nc >= n:
            continue

        if arr[nr][nc] != 0 or [x-1, y-1] == [nr, nc]:
            continue

        arr[nr][nc] = arr[r][c] + 1
        q.append((nr, nc))

for i in range(m):
    a, b = map(int, input().split())
    print(arr[a-1][b-1], end=' ')