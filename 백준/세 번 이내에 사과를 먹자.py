import sys

input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def dfs(x, y, apple, distance):
    global res
    if distance <= 3 and apple >= 2:
        res = 1
        return

    elif distance == 3 and apple < 2:
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < 5 and 0 <= ny < 5:
            tmp = graph[x][y]
            graph[x][y] = -1

            if graph[nx][ny] == 0:
                dfs(nx, ny, apple, distance+1)

            elif graph[nx][ny] == 1:
                dfs(nx, ny, apple+1, distance+1)

            graph[x][y] = tmp

graph = [list(map(int, input().split())) for _ in range(5)]
visited = [[False] * 5 for _ in range(5)]
r, c = map(int, input().split())
res = 0
dfs(r, c, 0, 0)
print(res)


