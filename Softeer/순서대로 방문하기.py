def dfs(points, c):
    if c == m:
        ans.append(points)
        return
    if points[-1] == checkpoints[c]:
        dfs(points, c+1)
        return

    for i in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr = points[-1][0] + i[0]
        nc = points[-1][1] + i[1]

        if 0<=nr<n and 0<=nc<n and vis[nr][nc] != 1 and (nr, nc) not in points:
            dfs(points + [(nr, nc)], c)


n, m = map(int, input().split())
vis = [list(map(int, input().split())) for _ in range(n)]
checkpoints = []
ans = []
for _ in range(m):
    x, y = map(int, input().split())
    checkpoints.append((x-1, y-1))

dfs([checkpoints[0]], 0)

print(len(ans))
