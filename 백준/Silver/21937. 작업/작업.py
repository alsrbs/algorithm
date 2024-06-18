import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6) 

def dfs(v):
    global c
    vis[v] = 1

    for i in graph[v]:
        if not vis[i]:
            c+=1
            dfs(i)


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

x = int(input())
vis = [0]*(n+1)
c = 0

dfs(x)
print(c)