def dfs(a, c):
    if c == n:
        print(*a)
        return

    for i in range(n):
        if vis[i] == 0:
            vis[i] = 1
            dfs(a + [arr[i]], c+1)
            vis[i] = 0


n = int(input())
arr = [i for i in range(1, n+1)]
vis = [0]*n
ans = []
dfs([], 0)

