n = int(input())
dp = [0]*(n+1)
dp[1] = 1

if n < 2:
    print(1)
else:
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[n])