n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def dfs(x, y):
    # 범위를 벗어날 경우
    if x <= -1 or x >= n or y <= -1 or y >=m:
        return False
    # 범위 탐색
    if arr[x][y] == 0:
        arr[x][y] = 1
        dfs(x-1, y)
        dfs(x + 1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

res = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            if dfs(i,j) == True:
                res += 1
print(res)
