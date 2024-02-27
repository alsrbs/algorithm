n = int(input())
dp = [0]*(n+1)
dp[2] = 3
dp[4] = 11
if n <= 2:
    print(dp[2])
elif 2 < n <= 4:
    print(dp[n])
else:

    for i in range(6, n+1):
        dp[i] = (dp[i - 2] * 4 - dp[i - 4]) % 1000000007
    print(dp[n])