n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
vis = [[False]*m for _ in range(n)]

total = 0
for i in range(n):
    for j in range(m):
        if vis[i][j]:continue
        if arr[i][j] == '-':
            vis[i][j] = True
            c = j
            while True:
                c+=1
                if c>=m or arr[i][c] != '-':
                    total+=1
                    break
                vis[i][c] = True
        elif arr[i][j] == '|':
            vis[i][j] = True
            r = i
            while True:
                r+=1
                if r>=n or arr[r][j] != '|':
                    total += 1
                    break
                vis[r][j] = True
print(total)