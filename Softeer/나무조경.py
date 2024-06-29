def dfs(x, y, cnt, total):
    global vis, ans
    vis[x][y] = 1

    for i in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx = x + i[0]
        ny = y + i[1]

        if 0<=nx<n and 0<=ny<n and vis[nx][ny] == 0:
            vis[nx][ny] = 1
            new_total = total + arr[x][y] + arr[nx][ny]

            if cnt==3 or (n<3 and cnt==1):
                ans = max(ans, new_total)
                vis[nx][ny] = 0
                return

            for j in range(n):
                for k in range(n):
                    if vis[j][k] == 0:
                        dfs(j, k, cnt+1, new_total)
                        vis[j][k] = 0

            vis[nx][ny] = 0


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
vis = [[0]*n for _ in range(n)]

if n == 2:
    print(sum(arr[0])+sum(arr[1]))

elif n == 3:
    ans = 0
    for i in [arr[0][0], arr[0][2], arr[1][1], arr[2][1], arr[2][2]]:
        total = sum(arr[0]) + sum(arr[1]) + sum(arr[2])
        ans = max(ans, total-i)
    print(ans)

else:
    ans = 0
    for i in range(n):
        for j in range(n):
            dfs(i, j, 0, 0)
            vis[i][j] = 0
    print(ans)