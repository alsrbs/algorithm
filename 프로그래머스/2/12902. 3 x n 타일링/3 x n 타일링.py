def solution(n):
    dp = [0]*(n+1)
    dp[2] = 3
    dp[4] = 11
    if n <= 2:
        return dp[n]
    elif 2 < n <= 4:
        return dp[n]
    else:

        for i in range(6, n+1):
            dp[i] = (dp[i-2]*4-dp[i-4])%1000000007
        return dp[n]
