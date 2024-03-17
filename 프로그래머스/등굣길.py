m = 4
n = 3
puddles = [[2, 2]]

puddles = [[q,p] for [p,q] in puddles]
graph = [[0]*(m+1) for _ in range(n+1)]

graph[1][1] = 1

for i in range(1, n+1):
    for j in range(1, m+1):
        if [i, j] == [1, 1]:continue
        if [i, j] in puddles:
            graph[i][j] = 0
        else:
            graph[i][j] = (graph[i-1][j] + graph[i][j-1]) % 1000000007

print(graph[n][m])