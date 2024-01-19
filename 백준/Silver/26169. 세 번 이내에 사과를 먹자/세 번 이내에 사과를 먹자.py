import sys

input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
graph = [list(map(int, input().split())) for _ in range(5)]
visited = [[False] * 5 for _ in range(5)]
r, c = map(int, input().split())

stack = [(r, c, 0, 0)]  # 스택에 시작 상태 추가

while stack:
    y, x, depth, cnt = stack.pop()
    visited[y][x] = True
    if graph[y][x] == 1:
        cnt += 1

    if 2 <= cnt:
        print(1)
        break

    if 3 == depth:
        visited[y][x] = False
        continue

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < 5 and 0 <= nx < 5:
            if not visited[ny][nx] and graph[ny][nx] != -1:
                stack.append((ny, nx, depth + 1, cnt))

else:
    print(0)
