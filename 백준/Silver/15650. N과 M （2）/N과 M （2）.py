def dfs(a, b, x):
    if a == m:
        lst.append(b)
        return
    for i in range(1,n+1):
        if x < i:
            if vis[i] == 0:
                vis[i] = 1
                x = i
                dfs(a+1, b + [i], x)
                vis[i] = 0

n, m = map(int,input().split())
lst = []
vis = [0] * (n+1)

dfs(0, [], 0)
for i in lst:
    print(*i)