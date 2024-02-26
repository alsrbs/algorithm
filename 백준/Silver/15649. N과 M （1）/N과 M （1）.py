def dfs(a,b):
    if a == m:
        lst.append(b)
        return
    for i in range(1, n+1):
        if vis[i] == 0:
            vis[i] = 1
            dfs(a+1, b+[i])
            vis[i] = 0

n, m = map(int,input().split())
lst = []
vis = [0]* (n + 1)

dfs(0, [])
for i in lst:
    print(*i)