n = int(input())
target = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n + 1)
for _ in range(target):
    a, b = map(int,input().split())
    graph[a] += [b]
    graph[b] += [a]
def dfs(v):
    visited[v] = 1
    for nx in graph[v]:
        if visited[nx] == 0:
            dfs(nx)
dfs(1)
print(sum(visited)-1)