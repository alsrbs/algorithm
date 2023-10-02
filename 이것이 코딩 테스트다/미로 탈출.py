from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

q = deque()
q.append((0, 0))

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위를 벗어날 경우
        if nx<0 or nx>=n or ny<0 or ny>=m:continue
        # 방문을 한 경우
        if arr[nx][ny] == 0:continue
        if arr[nx][ny] == 1:
            arr[nx][ny] = arr[x][y] + 1
            q.append((nx, ny))

print(arr[n-1][m-1])

# 5 6
# 1 0 1 0 1 0
# 1 1 1 1 1 1
# 0 0 0 0 0 1
# 1 1 1 1 1 1
# 1 1 1 1 1 1