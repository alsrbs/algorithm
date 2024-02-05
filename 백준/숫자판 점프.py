dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def dfs(r, c, num):
    if len(num) == 6:
        if num not in result:
            result.append(num)
        return

    for i in range(4):
        nr = dr[i] + r
        nc = dc[i] + c

        if 0 <= nr < 5 and 0 <= nc < 5:
            dfs(nr, nc, num + graph[nr][nc])

graph = [list(input().split()) for _ in range(5)]

result = []
for i in range(5):
    for j in range(5):
        dfs(i, j, graph[i][j])

print(len(result))
