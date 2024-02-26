import sys
from collections import deque

input = sys.stdin.readline


dx = [0, 0, -1, 1, 0, 0]
dy = [-1, 1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def bfs():

    while q:
        z, x, y = q.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h and arr[nz][nx][ny] == 0:
                q.append((nz, nx, ny))
                arr[nz][nx][ny] = arr[z][x][y] + 1


def box_check():
    day = 0
    for i in arr:
        for j in i:
            if 0 in j:
                return -1
            day = max(max(j) - 1, day)

    return day


n, m, h = map(int, input().split())
arr = []
q = deque([])

for i in range(h):
    box = []
    for j in range(m):
        box.append(list(map(int, input().split())))

        for k in range(n):
            if box[j][k] == 1:
                q.append((i, j, k))

    arr.append(box)

bfs()
print(box_check())
