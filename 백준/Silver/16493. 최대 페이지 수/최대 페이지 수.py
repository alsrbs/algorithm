n, m = map(int, input().split())
arr = [[0] * 2 for _ in range(m + 1)]
dp = [[0] * (n + 1) for _ in range(m + 1)]

for i in range(1, m + 1):
    arr[i][0], arr[i][1] = map(int, input().split())

for i in range(1, m + 1):
    for j in range(n + 1):
        if j - arr[i][0] >= 0:
            dp[i][j] = max(dp[i - 1][j - arr[i][0]] + arr[i][1], dp[i - 1][j])
        dp[i][j] = max(dp[i - 1][j], dp[i][j])

print(dp[m][n])