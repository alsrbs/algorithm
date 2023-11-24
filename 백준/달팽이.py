N = int(input())
target = int(input())
graph = [[0]*N for i in range(N)]
graph[N//2][N//2] = 1
x, y = 0, 0
target_x, target_y = 0, 0
graph[x][y] = N*N

while True:

    if x + 1 < N and graph[x + 1][y] == 1:
        if target == 1:
            target_x, target_y = x+1, y
        break

    # 밑으로
    while True:
        x += 1
        if x >= N or graph[x][y] != 0:
            x -= 1
            break
        graph[x][y] = graph[x-1][y] - 1
        if graph[x][y] == target:
            target_x, target_y = x, y

    # 오른쪽
    while True:
        y += 1
        if y >= N or graph[x][y] != 0:
            y -= 1
            break
        graph[x][y] = graph[x][y-1] - 1
        if graph[x][y] == target:
            target_x, target_y = x, y

    # 위로
    while True:
        x -= 1
        if x < 0 or graph[x][y] != 0:
            x += 1
            break
        graph[x][y] = graph[x+1][y] - 1
        if graph[x][y] == target:
            target_x, target_y = x, y

    # 왼쪽
    while True:
        y -= 1
        if y < 0 or graph[x][y] != 0:
            y += 1
            break
        graph[x][y] = graph[x][y+1] - 1
        if graph[x][y] == target:
            target_x, target_y = x, y

for i in graph:
    print(*i)
print(target_x + 1, target_y + 1)