def dfs(a, c):
    global ans

    if c == n:
        cnt = 500
        for i in a:
            cnt += i - k
            if cnt < 500:
                return
            
        ans += 1
        return

    for i in range(n):
        if vis[i] == 0:
            vis[i] = 1
            dfs(a + [arr[i]], c+1)
            vis[i] = 0


n, k = map(int, input().split())
arr = list(map(int, input().split()))
vis = [0]*n
ans = 0
dfs([], 0)

print(ans)