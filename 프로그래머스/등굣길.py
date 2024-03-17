m = 4
n = 3
puddles = [[2, 2]]

graph = [[1]*m for _ in range(n)]

for i in puddles:
    graph[i[0]-1][i[1]-1] = 0

for i in range(1, n):
    for j in range(1, m):
        if [i+1, j+1] in puddles:continue
        graph[i][j] = graph[i-1][j] + graph[i][j-1]

print(graph[n-1][m-1])